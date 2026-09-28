from app.sql_validator import validate_sql


def test_select_query_is_allowed():
    valid, sql = validate_sql("SELECT * FROM employees;")
    assert valid
    assert sql == "SELECT * FROM employees"


def test_update_query_is_blocked():
    valid, message = validate_sql("UPDATE employees SET salary = 100000 WHERE id = 1;")
    assert not valid
    assert "Only SELECT or WITH queries are allowed." in message


def test_multiple_statements_are_blocked():
    valid, message = validate_sql("SELECT * FROM employees; DELETE FROM employees;")
    assert not valid
    assert "Multiple SQL statements are not allowed." in message
