package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

type Todo struct {
	Name string `json:"name"`
	Done bool   `json:"done"`
}

func main() {
	todos := []Todo{
		{"Learn Go", false},
		{"Learn Python", false},
		{"Learn Java/C#", false},
		{"Learn Physics", false},
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// static file needeed to connect with browser API
		// opening file

		fileContents, err := ioutil.ReadFile("index.html")
		if err != nil {
			log.Println(err)
			w.WriteHeader(http.StatusNotFound)
			return
		}

		w.Write(fileContents)
	})

	http.HandleFunc("/todos", func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("request", r.URL.Path)
		defer r.Body.Close()

		switch r.Method {
		case http.MethodGet:
			productsJson, _ := json.Marshal(todos)
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusOK)
			w.Write(productsJson)

		case http.MethodPost:
			decoder := json.NewDecoder(r.Body)
			todo := Todo{}

			err := decoder.Decode(&todo)
			if err != nil {
				log.Println(err)
				w.WriteHeader(http.StatusBadRequest)
				return
			}
		default:
			w.WriteHeader(http.StatusMethodNotAllowed)
		}
	})

	http.ListenAndServe(":8000", nil)
}
