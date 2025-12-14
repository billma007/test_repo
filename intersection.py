"""Simple set intersection utility with sample test cases.

The Intersection function computes setA ∩ setB for hashable elements. Sample
cases are exercised when running this file directly.
"""
from typing import AbstractSet, Any, Set


def intersection(setA: AbstractSet[Any], setB: AbstractSet[Any]) -> Set[Any]:
    """Return the intersection of two sets.

    Accepts any abstract set of hashable elements (set, frozenset, etc.).
    Returns a mutable set containing elements present in both inputs.
    """
    return setA.intersection(setB)


def _format_set(values: AbstractSet[Any]) -> str:
    """Stable string representation that handles mixed element types."""
    return "{" + ", ".join(sorted((repr(item) for item in values), key=str)) + "}"


def run_examples() -> None:
    empty = frozenset()

    test_cases = [
        ({1, 2, 3, 4}, {1, 2}, {1, 2}),
        ({1, 2, 3, 4}, {3, 4, 5, 6}, {3, 4}),
        ({1, 2, empty, frozenset({3})}, {empty, frozenset({3}), "a", "b"}, {empty, frozenset({3})}),
        ({1, 2, 3, 4}, {"a", "b", "c"}, set()),
        (set(), {3, 4, 5, 6}, set()),
        ({1, 2, 3, 4}, set(), set()),
    ]

    for idx, (set_a, set_b, expected) in enumerate(test_cases, start=1):
        result = intersection(set_a, set_b)
        assert result == expected, f"Case {idx} failed: expected {expected}, got {result}"
        print(f"Case {idx}: {_format_set(set_a)} & {_format_set(set_b)} = {_format_set(result)}")


if __name__ == "__main__":
    run_examples()
