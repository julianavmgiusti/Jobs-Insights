from src.sorting import sort_by


jobs_info = [
    {
        "min_salary": 5000,
        "max_salary": 6000,
        "date_posted": "2022-03-22",
    },
    {
        "min_salary": 2800,
        "max_salary": 5000,
        "date_posted": "2022-04-30",
    },
    {
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "2022-10-17",
    },
]


def test_sort_by_criteria():
    sort_by(jobs_info, "min_salary")
    assert jobs_info[0]["min_salary"] == 1000

    sort_by(jobs_info, "max_salary")
    assert jobs_info[0]["max_salary"] == 6000

    sort_by(jobs_info, "date_posted")
    assert jobs_info[0]["date_posted"] == "2022-10-17"
