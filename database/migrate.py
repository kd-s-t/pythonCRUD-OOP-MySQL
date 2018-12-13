import database as db

db = db.Database("python_crud_oop")
db.setLocalhost("localhost")
db.setUsername("root")
db.setPassword("")
db.createDatabase()

db.setTableName("customers")
db.createTable()
