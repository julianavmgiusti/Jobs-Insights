from src.brazilian_jobs import read_brazilian_file
path = "tests/mocks/brazilians_jobs.csv"


titles_mock = {
    "title": "Analista de Software",
    "salary": "4000",
    "type": "full time"
    }


def test_brazilian_jobs():
    translation = read_brazilian_file(path)
    assert titles_mock in translation
