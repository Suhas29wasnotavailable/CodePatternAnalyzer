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

## How accurate is it?

Measured with stratified 5-fold cross-validation (`python evaluate.py`): in each fold the n-gram
vocabulary and the MLP are fitted on 40 files and scored on the 10 they have not seen.

| | |
|:--|:--|
| **Accuracy on unseen files** | **76.0%** ± 8.0% across folds |
| Chance (always guess the commonest author) | 20.0% |

```
confusion (rows: true author, columns: predicted)
                         0   1   2   3   4
            Kamuyu104 0  10   0   0   0   0
           Seanforfun 1   6   4   0   0   0
TheAlgorithmsTeam-git 2   0   0   9   1   0
                haoel 3   0   1   0   8   1
      youngyangyang04 4   1   2   0   0   7
```

The weak spot is specific: **6 of Seanforfun's 10 files are attributed to Kamuyu104**, while
Kamuyu104's own files are never missed. The model has learned something that both authors share,
and with 10 files each it cannot tell them apart. That is the first thing a larger corpus should
fix.

## Known limitations

Worth being upfront about, since they shape how far the results can be trusted:

- **The served model is not the evaluated one.** The API fits on all 50 files; the accuracy
  above comes from refitting on four fifths at a time, which is the standard estimate of how the
  full model generalises, not a measurement of it.
- **Small corpus.** 10 files per author is enough to demonstrate the method, not enough to
  make the classifier robust to unfamiliar code.
- **Python only.** The AST features depend on `ast.parse`.

## Roadmap

- [x] Train/test split and reported cross-validated accuracy
- [x] Confusion matrix over the 5 authors
- [ ] Widen the corpus — more authors, more files each
- [x] Replace the stubbed AI-detection field with a real model, or drop it (dropped)
- [ ] Persist the fitted model instead of retraining on every cold start
