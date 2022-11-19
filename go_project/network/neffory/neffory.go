package main

import (
	"fmt"
	"html/template"
	"io/ioutil"
	"log"
	"math/rand"
	"net/http"
	"time"
)

type Page struct {
	Title string
	Body  []byte
}

var letterRunes = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
var sessions = map[string]string{}

func init() {
	rand.Seed(time.Now().UnixNano())
}

func main() {
	fmt.Println("Hello, world!")
	// defer clearCookie()

	http.HandleFunc("/", index)
	http.HandleFunc("/login", login)
	http.HandleFunc("/get_cookie", getCookie)
	http.HandleFunc("/clear_cookie", clearCookie)

	log.Fatal(http.ListenAndServe(":8080", nil))
}

func RandStringRunes(n int) string {
	b := make([]rune, n)
	for i := range b {
		b[i] = letterRunes[rand.Intn(len(letterRunes))]
	}
	return string(b)
}

func getCookie(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	inputLogin := r.Form["login"][0]
	password := r.Form["password"][0]
	expiration := time.Now().Add(365 * 24 * time.Hour)

	sessionID := RandStringRunes(32)
	sessions[sessionID] = inputLogin
	fmt.Println("Password: ", password)

	cookie := http.Cookie{Name: "session_id", Value: sessionID, Expires: expiration}

	http.SetCookie(w, &cookie)
	http.Redirect(w, r, "/login", http.StatusFound)
}

func login(w http.ResponseWriter, r *http.Request) {
	sessionID, err := r.Cookie("session_id")

	if err == http.ErrNoCookie {
		viewTemplate(w, r, "login")
		return
	} else if err != nil {
		fmt.Println("ERROR:", err)
		panic(err)
	}

	username, ok := sessions[sessionID.Value]

	if !ok {
		fmt.Fprint(w, "session not found")
	} else {
		fmt.Fprint(w, "Welcome "+username)

	}
}

func index(w http.ResponseWriter, r *http.Request) {
	viewTemplate(w, r, "index")
}

func viewTemplate(w http.ResponseWriter, r *http.Request, title string) {
	p, err := loadPage(title)

	if err != nil {
		fmt.Println("err", err)
		w.Write([]byte("error"))
	}

	t, err := template.ParseFiles("templates/" + title + ".html")
	if err != nil {
		log.Println(err)
	}

	t.Execute(w, p)
}

func clearCookie(w http.ResponseWriter, r *http.Request) {
	cookie := http.Cookie{Name: "session_id", Value: "http.ErrNoCookie", MaxAge: -1}

	http.SetCookie(w, &cookie)
	http.Redirect(w, r, "/login", http.StatusFound)
}

func loadPage(title string) (*Page, error) {
	filename := "templates/" + title + ".html"
	body, err := ioutil.ReadFile(filename)

	if err != nil {
		return nil, err
	}
	return &Page{Title: title, Body: body}, nil
}
