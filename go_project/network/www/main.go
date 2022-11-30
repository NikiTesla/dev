package main

import (
	"database/sql"
	"fmt"
	"net/http"
	"text/template"

	"github.com/gorilla/mux"
	_ "github.com/mattn/go-sqlite3"
)

type Neffor struct {
	Id          uint16
	Name, About string
}

func main() {
	handleFunc()

	http.ListenAndServe(":8080", nil)
}

func handleFunc() {
	rtr := mux.NewRouter()
	rtr.HandleFunc("/", index).Methods("GET")
	rtr.HandleFunc("/create", add_neffor).Methods("GET")
	rtr.HandleFunc("/save_article", save_neffor).Methods("POST")
	rtr.HandleFunc("/delete_neffor/{id:[0-9]+}", delete_neffor).Methods("GET", "POST")

	http.Handle("/", rtr)
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static/"))))
}

func index(w http.ResponseWriter, r *http.Request) {
	tmpl, err := template.ParseFiles("templates/index.html", "templates/header.html", "templates/footer.html")
	var neffors []Neffor

	if err != nil {
		fmt.Fprint(w, err.Error())
	}

	db, err := sql.Open("sqlite3", "instance/test.db")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	res, err := db.Query("SELECT * FROM `Neffor`")
	if err != nil {
		panic(err)
	}

	for res.Next() {
		var neffor Neffor
		res.Scan(&neffor.Id, &neffor.Name, &neffor.About)
		neffors = append(neffors, neffor)
	}

	tmpl.ExecuteTemplate(w, "index", neffors)
}

func add_neffor(w http.ResponseWriter, r *http.Request) {
	tmpl, err := template.ParseFiles("templates/create.html", "templates/header.html", "templates/footer.html")

	if err != nil {
		fmt.Fprint(w, "Error occured", err)
	}

	tmpl.ExecuteTemplate(w, "create", nil)
}

func save_neffor(w http.ResponseWriter, r *http.Request) {
	name := r.FormValue("name")
	about := r.FormValue("about")

	if name == "" || about == "" {
		fmt.Fprintf(w, "correct data not presented")
	} else {

		db, err := sql.Open("sqlite3", "instance/test.db")

		if err != nil {
			fmt.Fprint(w, "Error occured", err)
		}
		defer db.Close()

		_, err = db.Exec("INSERT INTO `Neffor` (`name`, `about`) VALUES(?, ?)", name, about)

		if err != nil {
			fmt.Fprint(w, "Error occured", err)
		}

		http.Redirect(w, r, "/", http.StatusSeeOther)
	}
}

func delete_neffor(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	// w.WriteHeader(http.StatusOK)

	go func() {
		db, err := sql.Open("sqlite3", "instance/test.db")
		if err != nil {
			fmt.Printf("Error occured %v\n", err)
		}

		defer db.Close()

		_, err = db.Exec("DELETE FROM `Neffor` WHERE `id` = ?", vars["id"])
		if err != nil {
			fmt.Printf("Error occured, %v\n", err)
		}
	}()

	http.Redirect(w, r, "/", http.StatusSeeOther)
}
