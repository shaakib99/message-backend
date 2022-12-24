import socketio
from aiohttp import web
import sys
from logger import log, Logger
from dataclasses import dataclass, field
from events.root import events

PORT = 8080
HOST = "localhost"


@dataclass(order=False)
class Connection:
    sio: socketio.AsyncServer = field(default_factory=socketio.AsyncServer)
    app: web.Application = field(default_factory=web.Application)

    def __post_init__(self) -> None:
        self.sio.attach(self.app)


conn = Connection()

if __name__ == "__main__":

    file_name, server_command, *args = sys.argv

    match server_command.lower():
        case "start":
            for e in events:
                conn.sio.register_namespace(e)

            log(Logger(message=f"Server started at http://{HOST}:{PORT} port"))
            web.run_app(app=conn.app, host=HOST, port=PORT)
        case _:
            assert "", f"{server_command} was not recognized"
