import pathlib
import socketserver
from http.server import SimpleHTTPRequestHandler

FILES = pathlib.Path(__file__).absolute().parent.joinpath("pages")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, directory=str(FILES), **kwargs)


class IntegrationServer(socketserver.TCPServer):
    """A Simple integration server that serves integration test content."""

    def __init__(self, *args, **kwargs):
        super().__init__(server_address=("", 0), RequestHandlerClass=Handler, *args, **kwargs)

    @property
    def base_url(self) -> str:
        return f"http://{self.server_address[0]}:{self.server_address[1]}"

    def __repr__(self) -> str:
        return f"IntegrationServer(server_address={self.server_address})"
