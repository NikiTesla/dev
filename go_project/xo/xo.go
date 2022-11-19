package main

import (
	"fmt"
	"os"
)

func main() {
	board := [][]string{
		{"_", "_", "_"},
		{"_", "_", "_"},
		{"_", "_", "_"},
	}

	for i := 0; i < 9; i++ {
		put(&board, i)
		draw_board(&board)
	}

}

func put(b *[][]string, i int) {
	var x, y int
	fmt.Print("x: ")
	fmt.Fscan(os.Stdin, &x)
	fmt.Print("y: ")
	fmt.Fscan(os.Stdin, &y)

	if i%2 == 0 {
		(*b)[x-1][y-1] = "X"
	} else {
		(*b)[x-1][y-1] = "O"
	}
}

func draw_board(b *[][]string) {
	for i := 0; i < 3; i++ {
		fmt.Println((*b)[i])
	}
}
