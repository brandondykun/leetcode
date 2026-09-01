# Python Solutions

Each problem lives in its own folder under `python/`:

```
226_Invert_Binary_Tree/
  README.md      # problem statement
  start.py       # empty Solution stub
  solution.py    # implementation
  test.py        # tests
utils/           # shared helpers (trees, lists, pytest ids)
```

## Setup

From this `python/` directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e utils
```

That installs `leetcode_utils` (binary tree and linked list helpers) and `pytest`.

## Running tests

### pytest (preferred)

Newer problems use pytest. Pass the test file explicitly — pytest does not collect `test.py` by default (it looks for `test_*.py` and `*_test.py`).

From the problem folder:

```bash
pytest test.py
```

From `python/`:

```bash
pytest 226_Invert_Binary_Tree/test.py
```

Useful flags:

```bash
pytest test.py -v          # show each case name
pytest test.py -k "Test 3" # run one case
```

### Script-style tests

Older problems print pass/fail instead of using pytest. From the problem folder:

```bash
python test.py
```
