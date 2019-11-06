# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:50:45 2019

@author: admin
"""
import asyncio
HOST = 'localhost'
PORT = int(input("Введите порт для соединения:"))
if not 0 <= PORT <= 65535:
    PORT = 9090

async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    message="Здравствуйте,сервер"
    print('Send:{0}'.format(message))
    writer.write(message.encode())
    await writer.drain()
    
    data = await reader.read(100)
    print('Received:{0}'.format(data.decode()))

    print('Close the socket')
    
    writer.close()
    #await writer.wait_closed()

# asyncio.run(tcp_echo_client(HOST, PORT))
loop = asyncio.get_event_loop()
task = loop.create_task(tcp_echo_client(HOST, PORT))
loop.run_until_complete(task)
input()