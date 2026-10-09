from login import login


def test_login_success():
    assert login("admin", "secret123") is True


def test_login_failure():
    assert login("admin", "wrongpassword") is False
    assert login("wronguser", "secret123") is False
    assert login("wronguser", "wrongpassword") is False
