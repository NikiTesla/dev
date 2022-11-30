package main

import (
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {

	tmpl, _ := template.New("main.html").ParseFiles("main.html")

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		path := r.URL.Path

		c := http.Client{}
		resp, err := c.Get("http://127.0.0.1:8080" + path)
		if err != nil {
			log.Println(err)
			w.Write([]byte("error"))
		}

		defer resp.Body.Close()

		body, _ := ioutil.ReadAll(resp.Body)

		tmpl.Execute(w, string(body))
	})

	http.ListenAndServe(":5005", nil)
}
