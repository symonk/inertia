import pathlib
from http.server import SimpleHTTPRequestHandler
from http.server import ThreadingHTTPServer


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs) -> None:
        # Todo: Absolute path to the parent pages dir.
        super().__init__(*args, directory=str(pathlib.Path()), **kwargs)


class IntegrationTestWebServer(ThreadingHTTPServer):
    """A simple http server that serves the /pages directory for use in tests.
    Each test `session` receives its own web server instance on an ephemeral port
    to allow execution of parallel testing.
    """

    ...
