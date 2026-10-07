# CodePatternAnalyzer

Identify who wrote a piece of Python from style alone.

Two programmers solving the same problem leave different fingerprints — how deeply they
nest, how often they reach for a helper function, how they space and punctuate. This tool
learns those fingerprints and guesses the author of an unseen file.

**[Try the live demo →](https://code-pattern-analyzer.vercel.app)**

---

## How it works

Each file is turned into a **206-dimension feature vector**, combining two views of the code:

**Structural (6 features)** — parsed from the Python AST, so they describe shape rather than text:

| Feature | What it captures |
|:--|:--|
| Line count | Overall verbosity |
| Function count | How much the author decomposes |
| Loop count | Iteration style |
| Conditional count | Branching habits |
| Max AST depth | How deeply the author nests |
| Cyclomatic complexity | `loops + conditionals + 1` |

**Lexical (200 features)** — character n-grams of length 2–4 via `CountVectorizer`, capping at
the 200 most frequent. These pick up habits below the level of syntax: spacing around
operators, naming conventions, comment style.

The two vectors are concatenated and fed to a scikit-learn `MLPClassifier` with two hidden
layers (128 → 64), trained for up to 500 iterations.

```
code ──┬── AST parse ──────────► 6 structural features ──┐
       │                                                 ├──► MLP (128→64) ──► author + confidence
       └── char n-grams (2–4) ─► 200 lexical features ───┘
```

## The dataset

50 Python files — **5 GitHub authors × 10 files each**, collected from public repositories
and kept in `data/<author>/`. The corpus is third-party code used purely as training data.

## API

A single FastAPI endpoint. The model trains once at startup and stays in memory.

```bash
POST /analyze
Content-Type: application/json

{ "code": "def solve(n):\n    return [i for i in range(n) if n % i == 0]\n" }
```

```jsonc
{
  "author_prediction": "haoel",
  "author_confidence": 0.731,
  "top_authors": [          // top 3, descending
    { "name": "haoel",           "confidence": 0.731 },
    { "name": "Seanforfun",      "confidence": 0.164 },
    { "name": "youngyangyang04", "confidence": 0.061 }
  ],
  "metrics": {
    "ast_depth": 4,
    "cyclomatic_complexity": 3,
    "function_density": 0.25
  }
}
```

## Running it locally

```bash
git clone https://github.com/Suhas29wasnotavailable/CodePatternAnalyzer
cd CodePatternAnalyzer

pip install fastapi uvicorn scikit-learn numpy
uvicorn main:app --reload
```

The API comes up on `http://127.0.0.1:8000`, with interactive docs at `/docs`.

The browser UI lives in its own repository —
**[CodePatternAnalyzer-demo](https://github.com/Suhas29wasnotavailable/CodePatternAnalyzer-demo)** —
so this repo stays focused on the model and the API.

## Known limitations

Worth being upfront about, since they shape how far the results can be trusted:

- **No held-out test split.** The model currently fits on all 50 files, so it has no honest
  accuracy number attached. A stratified train/test split with cross-validation is the next
  thing to add.
- **Small corpus.** 10 files per author is enough to demonstrate the method, not enough to
  make the classifier robust to unfamiliar code.
- **The `ai_prediction` field is a placeholder.** It returns a fixed value today and is not
  a real human-vs-AI detector.
- **Python only.** The AST features depend on `ast.parse`.

## Roadmap

- [ ] Train/test split and reported cross-validated accuracy
- [ ] Confusion matrix over the 5 authors
- [ ] Widen the corpus — more authors, more files each
- [ ] Replace the stubbed AI-detection field with a real model, or drop it
- [ ] Persist the fitted model instead of retraining on every cold start
