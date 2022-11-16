package main

import (
	"fmt"
	"os"
)

// struct example
type Example_struct struct {
	flag    bool
	counter int16
	pi      float32
}

// place to create many constant variables
const (
	flagUserEnabled = 1 << iota
	flagUserVerified
	flagUserPremium

	size = 3
)

func main() {
	// fast initialization of variables
	some_text := "some_text\n\tworld!"
	println(some_text)

	defer CatchErr()

	// printing in console
	some_text = "integer:"
	println("enabled:", flagUserEnabled)
	println("verified", flagUserVerified)
	println("premium", flagUserPremium)

	// arrays
	var l [size]int
	l[1] = 3
	fmt.Println("Array:", l, "length:", len(l))

	// slices
	var matrix []int
	matrix = append(matrix, 1)
	fmt.Println("capacity: ", matrix, cap(matrix))
	matrix = append(matrix, 2)
	fmt.Println("capacity: ", matrix, cap(matrix))

	s2 := []int{10, 20, 30}
	s3 := []int{40, 50}
	s2 = append(s2, s3...)
	fmt.Println(s2)

	slice1 := make([]float64, 0, 15)
	fmt.Println(slice1, len(slice1), cap(slice1))

	// maps
	// var mm map[string]string = map[string]string{}
	// mm := map[string]string{}
	var mm = make(map[string]string)
	mm["test"] = "nottest"
	mm["lol"] = "lol"
	mm["foo"] = "arp"
	mm["hell"] = "hell"
	mm["flag"] = "OK"
	fmt.Println(mm["test"])

	val, res := mm["testt"]
	fmt.Println(val, res)

	// if-else constructions
	a := 1
	if a == 1 {
		fmt.Println("a equals 1")
	}
	// with key
	if val, res := mm["test"]; res {
		println(val)
	}

	// cycles
	for i := 0; i < 10; i++ {
		println(i, i+1, i+2)
	}
MyLoop:
	for k, v := range mm {
		switch {
		case v == "OK":
			break MyLoop
		default:
			println(k, v)
		}
	}

	for _, i := range s2 {
		println(i)
	}

	// switch
	switch mm["test"] {
	case "test", "testt":
		println("switched to test")
	case "nottest":
		if mm["flag"] == "OK" {
			println(mm["flag"])
			break
		}
		fallthrough
	default:
		println("default")
	}
	var pan string

	fmt.Println("Yes? ")
	fmt.Fscan(os.Stdin, &pan)

	if pan == "yes" {
		// panic raise
		panic("Hey, it's panic")
	}

	printElements(1, 2, 3, 2, 1)

	str := Example_struct{
		flag:    true,
		counter: 2,
		pi:      3.1415,
	}
	fmt.Println(str)

	GetName()
}

func printElements(sl ...int) {
	for _, i := range sl {
		fmt.Println(i)
	}
}

func CatchErr() {
	fmt.Println("Error catched")
}