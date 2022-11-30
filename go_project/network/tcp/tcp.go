package main

import (
	"bufio"
	"fmt"
	"net"
)

func main() {
	listener, err := net.Listen("tcp", ":8080")

	if err != nil {
		fmt.Println("Can not connect", err)
	}

	for {
		conn, err := listener.Accept()

		if err != nil {
			fmt.Println("Can not connect!", err)
			conn.Close()
			continue
		}

		fmt.Println("Connected")

		bufReader := bufio.NewReader(conn)
		fmt.Println("Start reading")

		go func(c net.Conn) {
			defer conn.Close()

			for {
				rbyte, err := bufReader.ReadByte()

				if err != nil {
					fmt.Println("Cannot read", err)
					break
				}

				fmt.Print(string(rbyte))
			}
		}(conn)
	}
}
