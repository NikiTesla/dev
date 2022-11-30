package main

import (
	"fmt"
	"math"
)

func (p Point) Say() {
	fmt.Println("x:", p.x)
}

func (p Vector) Say() {
	fmt.Println("radius:", p.length)
}

func (p Point) Cry() {
	fmt.Println("x:", p.x)
	fmt.Println("x:", p.x)
	fmt.Println("x:", p.x)
}

func (p Vector) Cry() {
	fmt.Println("radius:", p.length)
	fmt.Println("radius:", p.length)
	fmt.Println("radius:", p.length)
}

type MyInt int

func (p MyInt) squared() MyInt {
	return p * p
}

type Point struct {
	x, y, z float64
	color   string
}

type Vector struct {
	Point
	length float64
	Speaker
}

func (p Point) radius_vector() float64 {
	return math.Sqrt(p.x*p.x + p.y*p.y + p.z*p.z)
}

type Speaker interface {
	Say()
	Cry()
}
func MakerNoize(s Speaker) {
	s.Cry()
	s.Say()
}