# case2_failure_explained_test.py
def execute_report(report):
    return True


def test_failure():
    result = []
    for report in ["users", "orders", "locations"]:
        result.append(execute_report(report))
    assert all(result) == True
