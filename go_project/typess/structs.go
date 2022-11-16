package main

import (
	"fmt"
)

func main() {
	p1 := Point{1, 1, 1, "red"}
	p2 := Point{3, 3, 3, "black"}

	fmt.Println(p1.color)
	fmt.Println(p2.radius_vector())

	my_int := MyInt(3)
	fmt.Println(my_int.squared())

	var my_vect Vector
	my_vect.x = 1
	my_vect.y = 2
	my_vect.z = 3

	fmt.Println(my_vect.length)
	fmt.Println(my_vect.radius_vector())

	MakerNoize(p1)
}
