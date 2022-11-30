package main

import (
	"net/http"
	"text/template"
)

func main() {
	http.HandleFunc("/", index)

	http.ListenAndServe("0.0.0.0:5050", nil)
}

func index(w http.ResponseWriter, r *http.Request) {
	tmpl, err := template.ParseFiles("templates/index.html")

	if err != nil {
		panic(err)
	}

	tmpl.Execute(w, nil)
}
