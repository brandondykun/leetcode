def generate_test_ids(cases: list[tuple]) -> list[str]:
    return [f"Test {i}" for i in range(1, len(cases) + 1)]
