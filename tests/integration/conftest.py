import pytest


@pytest.fixture(autouse=True)
def webserver():
    """An auto use fixture that starts the web server for each session automatically."""
