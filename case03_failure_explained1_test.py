# case03_failure_explained1_test.py
def execute_report(report):
    if report == 'users':
        return False
    return True


def test_failure():
    result = []
    for report in ["users", "orders", "locations"]:
        result.append(execute_report(report))
    assert all(result) == True
