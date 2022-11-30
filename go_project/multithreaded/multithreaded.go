package main

import (
	"fmt"
	"time"
)

func main() {

	ch := make(chan int, 10)
	go get_five(ch)

	time.Sleep(1 * time.Second)
	go get_anotherfive(ch)

	time.Sleep(1 * time.Second)
	go print_five(ch)
	time.Sleep(1 * time.Second)

	fmt.Println("end")
}

func print_five(ch chan int) {
	for i := 0; i < 10; i++ {
		fmt.Println("print", <-ch)
	}
}

func get_anotherfive(ch chan int) {
	for i := 0; i < 5; i++ {
		ch <- i

		fmt.Println("get", i)
	}
}

func get_five(ch chan int) {
	for i := 5; i < 10; i++ {
		ch <- i
		fmt.Println("get", i)
	}
}
