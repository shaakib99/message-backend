import socketio
from logger import log, Logger
from connection import conn

sio = conn.sio


class DefaultEvents(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        log(Logger(message=f"{sid} Connected to the server"))

    def on_disconnect(self, sid):
        log(Logger(message=f"{sid} disconnected from the server"))
