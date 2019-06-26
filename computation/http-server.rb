#!/usr/bin/env ruby

require 'socket'

def main
  	socket = Socket.new(:INET, :STREAM)
	socket.setsockopt(Socket::SOL_SOCKET, Socket::SO_REUSEADDR, true)
	socket.bind(Addrinfo.tcp("127.0.0.1", 9000))
	socket.listen(0)
	conn_sock, addr_info = socket.accept
end
# initially ./http-server.rb&; sleep 0; curl 'http://localhost:9000/'
main
