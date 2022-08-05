import threading

import pytest

from tests._webserver.server import IntegrationServer


@pytest.fixture(scope="session")
def webserver():
    """A simple webserver that serves content in /pages in a background thread.  This is session scoped
    so can create multiple when xdist is involved."""
    with IntegrationServer() as server:
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        yield


@pytest.fixture
def page_loader(webserver):
    """A function scoped fixture that can build a browser for testing and navigate to a test
    page.  This is used for integration testing; `webserver` itself should not be used."""
    ...
