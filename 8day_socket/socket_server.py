#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-0705
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : socket server
# @Disc    : support python 2.x and 3.x



import SocketServer


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        while True:
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            if not self.data:
                print(self.client_address,"断开了")
                break
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    #server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler) #多线程支持

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()