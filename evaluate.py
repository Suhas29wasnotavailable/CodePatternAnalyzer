"""Measure how well the authorship model generalises to files it has not seen.

The API trains on all 50 files, so it has no accuracy number of its own. This script runs
stratified 5-fold cross-validation with the same features and classifier as main.py: in each fold
the n-gram vocabulary and the MLP are fitted on four fifths of the files and scored on the rest.
Fitting the vectorizer per fold matters; fitting it once on everything would leak the held-out
files' n-grams into training and flatter the score.

    python evaluate.py
"""

from collections import Counter

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import StratifiedKFold
from sklearn.neural_network import MLPClassifier

# Importing main also trains the API's model once; only its helpers are used here.
from main import extract_structural_features, load_dataset

FOLDS = 5
SEED = 42


def fit_and_predict(train_texts, train_labels, test_texts):
    vectorizer = CountVectorizer(analyzer="char", ngram_range=(2, 4), max_features=200)
    train_ngrams = vectorizer.fit_transform(train_texts).toarray()
    test_ngrams = vectorizer.transform(test_texts).toarray()

    def features(texts, ngrams):
        structural = np.array([extract_structural_features(code)[0] for code in texts])
        return np.hstack((structural, ngrams))

    model = MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=500, random_state=SEED)
    model.fit(features(train_texts, train_ngrams), train_labels)
    return model.predict(features(test_texts, test_ngrams))


def main():
    texts, labels = load_dataset()
    texts, labels = np.array(texts, dtype=object), np.array(labels)
    authors = sorted(set(labels))

    folds = StratifiedKFold(n_splits=FOLDS, shuffle=True, random_state=SEED)
    scores = []
    predicted = np.empty_like(labels)
    for train, test in folds.split(texts, labels):
        predicted[test] = fit_and_predict(list(texts[train]), labels[train], list(texts[test]))
        scores.append(accuracy_score(labels[test], predicted[test]))

    majority = Counter(labels).most_common(1)[0][1] / len(labels)
    print(f"{len(texts)} files, {len(authors)} authors, {FOLDS}-fold stratified cross-validation")
    print(f"accuracy: {np.mean(scores):.1%} ± {np.std(scores):.1%} across folds")
    print(f"chance (always guess the commonest author): {majority:.1%}")
    print()
    print("confusion (rows: true author, columns: predicted)")
    matrix = confusion_matrix(labels, predicted, labels=authors)
    width = max(len(a) for a in authors)
    print(" " * (width + 2) + " ".join(f"{i:>3}" for i in range(len(authors))))
    for i, (author, row) in enumerate(zip(authors, matrix, strict=True)):
        print(f"{author:>{width}} {i:>1} " + " ".join(f"{n:>3}" for n in row))


if __name__ == "__main__":
    main()
