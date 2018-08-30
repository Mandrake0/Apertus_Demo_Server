#!/usr/bin/env python
"""
This is a Dummy Websocket Server for testing the Apertus Axiom GUI.

Creator: Francis Tyrone Pimenta
version: 0.1
"""
# Import Commandline Promt
from cmd import Cmd
# Import required Websocket Libs
import asyncio
import websockets
from threading import Thread
import datetime
import random







# Websockets Variable
servername = 'localhost'
port_getreturn = 5678
port_feed = 5679

async def async_loop(websocket, path):
    client_value = await websocket.recv()
    print(f"< {client_value}")

    sent_approve = "{ok: \"true\"}"

    await websocket.send(sent_approve)

async def async_feed(websocket, path):
    while True:
        # now = datetime.datetime.utcnow().isoformat() + 'Z'
        v = "{ok:" + now + "}"
        await websocket.send(v)
        await asyncio.sleep(random.random() * 10)


class TestPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print("Hello, %s" % name)

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


cmdloop = """
    Apertus Dummy Server 
    ====================
    help    | Show all Commands
    quit    | Close Server
    """

def run_loop(loop):
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(async_loop, servername, port_getreturn)
    loop.run_until_complete(start_server)
    loop.run_forever()


def run_feed(loop):
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(async_feed, servername, port_feed)
    loop.run_until_complete(start_server)
    loop.run_forever()


if __name__ == '__main__':
    # Starting the loop Messaging
    new_loop = asyncio.new_event_loop()
    t = Thread(target=run_loop, args=(new_loop,))
    t.start()

    # Starting Feed
    feed_loop = asyncio.new_event_loop()
    t = Thread(target=run_feed, args=(feed_loop,))
    t.start()

    print("run")

    # Start CMD
    # prompt = TestPrompt()
    # prompt.prompt = '> '
    # prompt.cmdloop(cmdloop)

