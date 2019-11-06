# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:49:49 2019

@author: admin
"""

import asyncio

HOST = 'localhost'
PORT = int(input("Введите порт для соединения:"))
if not 0 <= PORT <= 65535:
    PORT = 9090

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    print('Received {0}'.format(message))
    writer.write(data)
    await writer.drain()
    print("Close the socket")
    writer.close()


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, HOST, PORT, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
input()