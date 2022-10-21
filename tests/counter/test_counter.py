from src.counter import count_ocurrences
path = "src/jobs.csv"


def test_counter():
    assert count_ocurrences(path, 'python') == 1639
    assert count_ocurrences(path, 'javascript') == 122
