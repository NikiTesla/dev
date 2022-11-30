package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	_ "github.com/mattn/go-sqlite3"
)

//type DataBase interface {
//	get() string
//	push() error
//	connect() sql.DB
//	getAll() ([]string, error)
//	create(string, string) error
//}

func pushToDB(dbType string, dbName string, name string, age int) error {
	db := connectDB(dbType, dbName)
	_, err := db.Exec("INSERT INTO 'test' VALUES (?, ?)", name, age)

	if err != nil {
		fmt.Printf("error occured, can't get data: %v\n", err)
		panic(err)
	}
	fmt.Println("Pushed line")

	return nil
}

func getAllFromDB(dbType string, dbName string) (*[][]string, error) {
	db := connectDB(dbType, dbName)
	rows, err := db.Query("SELECT * FROM 'test'")

	if err != nil {
		fmt.Printf("error occured, can't get data: %v\n", err)
		return nil, err
	}

	var data [][]string
	for rows.Next() {
		line := []string{"", ""}
		rows.Scan(&line[0], &line[1])

		data = append(data, line)
	}

	return &data, nil
}

func connectDB(dbType string, dbName string) *sql.DB {
	db, err := sql.Open(dbType, dbName+".db")
	fmt.Println("Database connected")

	if err != nil {
		fmt.Println("Can't connect database")
	}

	return db
}

func createDB(dbType string, dbName string) error {
	db, err := sql.Open(dbType, dbName+".db")
	fmt.Printf("creating file %v\n", dbName)
	panicOnError(err)

	_, err = db.Exec("CREATE TABLE IF NOT EXISTS 'test' (name TEXT, count INT);")

	if err != nil {
		fmt.Println("ERROR")
		panic(err)
	}

	return err

}

func workWithData(dbType string, dbName string) {
	createDB(dbType, dbName)
	pushToDB(dbType, dbName, "nikita", 20)
	pushToDB(dbType, dbName, "matvey", 6)
	pushToDB(dbType, dbName, "sergay", 20)

	lines, _ := getAllFromDB(dbType, dbName)

	fmt.Println(*lines)

}

func panicOnError(err error) {
	if err != nil {
		fmt.Printf("Error occured, %v", err)
		panic(err)
	}
}
