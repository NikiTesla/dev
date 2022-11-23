package main

import (
	"database/sql"
	"fmt"
	"net/http"
	"text/template"

	_ "github.com/mattn/go-sqlite3"
)

type Message struct {
	Name string
	Text string
}

type User struct {
	Name string `json:"name"`
	Age  uint16 `json:"age"`
}

func main() {
	handleRequest()
	setDB()
	workWithDB()

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

func workWithDB() {
	db, err := sql.Open("sqlite3", "instance/test.db")

	if err != nil {
		fmt.Println("Error occured: ", err)
	}

	fmt.Println("Connected database")

	if err != nil {
		fmt.Println("Error occured", err)
	}
	_, err = db.Exec("INSERT INTO `users` (`name`, `age`) VALUES('Nikita', 20);")
	if err != nil {
		fmt.Println("Error occured", err)
	}
	db.Exec("INSERT INTO `users` (`name`, `age`) VALUES('Sergay', 20);")
	db.Exec("INSERT INTO `users` (`name`, `age`) VALUES('Stepan', 26);")

	rows, err := db.Query("SELECT `name`, `age` FROM `users`;")

	if err != nil {
		fmt.Printf("Error occured: %v", err)
	}
	defer rows.Close()

	for rows.Next() {
		var name string
		var age int
		err = rows.Scan(&name, &age)

		if err != nil {
			fmt.Println("Can't get data", err)
		}

		fmt.Printf("Name: %v\n Age: %v\n\n", name, age)
	}
}

func setDB() {
	db, err := sql.Open("sqlite3", "instance/test.db")

	if err != nil {
		panic(nil)
	}
	db.Exec("DROP TABLE users")
	db.Exec("CREATE TABLE `users` (`name` VARCHAR(255), `age` INT)")

}
