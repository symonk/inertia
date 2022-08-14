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
        yield server


@pytest.fixture
def dummy_page():
    # This is a dummy fixture for now to prove out integration test functionality.  It uses the
    # underlying playwright page but will be built on in the future.  It is non-configurable for now.
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        yield pw.chromium.launch(headless=False).new_page()


@pytest.fixture
def page(webserver, request, dummy_page):
    """A function scoped fixture that can build a browser for testing and navigate to a test
    page.  This is used for integration testing; `webserver` itself should not be used."""
    marker = request.node.get_closest_marker("preload_page")
    if marker is not None:
        dummy_page.goto(f"{webserver.base_url}/{marker.args[0]}")
    return dummy_page
