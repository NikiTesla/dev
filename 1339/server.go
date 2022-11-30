package main

import (
	"fmt"
	"net/http"
	"text/template"
)

type Message struct {
	Name string
	Text string
}

func main() {
	handleRequest()

	http.ListenAndServe(":8080", nil)
}

func handleRequest() {
	http.HandleFunc("/", index)
	// http.HandleFunc("/pidors/")
	// http.HandleFunc("/add_pidor/", add_nefor)
	// http.HandleFunc("/login/", login)
	// http.HandleFunc("/unsetsession/", unsetsession)
	// http.HandleFunc("/signup", signup)
}

func index(w http.ResponseWriter, r *http.Request) {
	tmpl, err := template.ParseFiles("templates/main.html")

	if err != nil {
		fmt.Printf("Error occured: %v", err)
	}

	Messages := []Message{
		{"Nikita", "Hello, world!"},
	}

	tmpl.Execute(w, Messages)
}
