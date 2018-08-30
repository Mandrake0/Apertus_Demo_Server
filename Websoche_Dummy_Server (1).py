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

# Websockets Variable
servername = 'localhost'
port = 5678

async def hello(websocket, path):
    client_value = await websocket.recv()
    print(f"< {client_value}")

    sent_approve = "{ok: \"true\"}"

    await websocket.send(sent_approve)



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


if __name__ == '__main__':
    # Start Websocket
    start_server = websockets.serve(hello, servername, port)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    # Start CMD
    # prompt = TestPrompt()
    # prompt.prompt = '> '
    # prompt.cmdloop(cmdloop)

