# test_repo

## Overview
Python utility to compute set intersections, including cases with nested sets. The entry point `intersection.py` includes a callable `intersection` function and sample cases covering empty sets, overlapping integers, and nested frozensets.

## Running the examples
```bash
cd /Users/billma007/project/test_repo
python intersection.py
```

Expected printed results:
```
Case 1: {1, 2, 3, 4} & {1, 2} = {1, 2}
Case 2: {1, 2, 3, 4} & {3, 4, 5, 6} = {3, 4}
Case 3: {1, 2, frozenset(), frozenset({3})} & {frozenset(), frozenset({3}), 'a', 'b'} = {frozenset(), frozenset({3})}
Case 4: {1, 2, 3, 4} & {'a', 'b', 'c'} = {}
Case 5: {} & {3, 4, 5, 6} = {}
Case 6: {1, 2, 3, 4} & {} = {}
```

## Notes
- Nested sets are represented with `frozenset` so they remain hashable.
- The helper `_format_set` keeps output stable for mixed element types.