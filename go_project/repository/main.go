package main

func main() {
	dbName, dbType := "test", "sqlite3"
	//fmt.Print("Enter your database (dbType then dbName): ")
	//fmt.Fscan(os.Stdin, &dbType)
	//fmt.Fscan(os.Stdin, &dbName)
	workWithData(dbType, dbName)
}
