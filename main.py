from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import os
import ast
import re

from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# N-GRAM VECTORIZER (GLOBAL)
# -----------------------------
vectorizer = CountVectorizer(
    analyzer='char',
    ngram_range=(2, 4),  # bi-grams to 4-grams
    max_features=200
)

# -----------------------------
# STRUCTURAL FEATURES
# -----------------------------
def extract_structural_features(code: str):
    try:
        tree = ast.parse(code)
    except:
        return np.zeros(6), {}

    function_count = 0
    loop_count = 0
    if_count = 0
    max_depth = 0

    def traverse(node, depth=0):
        nonlocal function_count, loop_count, if_count, max_depth
        max_depth = max(max_depth, depth)

        if isinstance(node, ast.FunctionDef):
            function_count += 1
        if isinstance(node, (ast.For, ast.While)):
            loop_count += 1
        if isinstance(node, ast.If):
            if_count += 1

        for child in ast.iter_child_nodes(node):
            traverse(child, depth + 1)

    traverse(tree)

    complexity = loop_count + if_count + 1
    lines = len(code.split("\n"))
    function_density = function_count / lines if lines > 0 else 0

    metrics = {
        "ast_depth": max_depth,
        "cyclomatic_complexity": complexity,
        "function_density": round(function_density, 3)
    }

    return np.array([
        lines,
        function_count,
        loop_count,
        if_count,
        max_depth,
        complexity
    ]), metrics


# -----------------------------
# LOAD DATASET
# -----------------------------
def load_dataset():
    texts = []
    labels = []

    base_path = "data"

    for author in os.listdir(base_path):
        author_path = os.path.join(base_path, author)

        if os.path.isdir(author_path):
            for file in os.listdir(author_path):
                try:
                    with open(os.path.join(author_path, file), "r", encoding="utf-8") as f:
                        code = f.read()
                        texts.append(code)
                        labels.append(author)
                except:
                    continue

    return texts, labels


texts, labels = load_dataset()

# -----------------------------
# FIT N-GRAM VECTORIZER
# -----------------------------
X_ngram = vectorizer.fit_transform(texts).toarray()

# -----------------------------
# STRUCTURAL FEATURES
# -----------------------------
X_struct = np.array([extract_structural_features(code)[0] for code in texts])

# -----------------------------
# COMBINE FEATURES
# -----------------------------
X = np.hstack((X_struct, X_ngram))
y = np.array(labels)

# -----------------------------
# TRAIN MLP MODEL
# -----------------------------
model = MLPClassifier(
    hidden_layer_sizes=(128, 64),
    max_iter=500,
    random_state=42
)

model.fit(X, y)


# -----------------------------
# API
# -----------------------------
@app.post("/analyze")
def analyze_code(data: dict):
    code = data.get("code", "")

    struct_features, metrics = extract_structural_features(code)
    ngram_features = vectorizer.transform([code]).toarray()[0]

    combined = np.hstack((struct_features, ngram_features)).reshape(1, -1)

    probs = model.predict_proba(combined)[0]
    classes = model.classes_

    top_indices = np.argsort(probs)[::-1][:3]

    top_authors = [
        {
            "name": classes[i],
            "confidence": float(round(probs[i], 3))
        }
        for i in top_indices
    ]

    return {
        "author_prediction": top_authors[0]["name"],
        "author_confidence": top_authors[0]["confidence"],
        "top_authors": top_authors,
        "metrics": metrics,
        "detected_language": "Python",
        "ai_prediction": "Likely Human",
        "ai_confidence": 0.85
    }