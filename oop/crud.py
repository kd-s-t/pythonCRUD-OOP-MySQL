import mysql.connector

class CRUD:

	def __init__(self):
		self.__localhost     = "localhost"
		self.__username      = "root"
		self.__password      = ""
		self.__database_name = "python_crud_oop" 
		self.__table_name 	 = "customers" 
		self.createConnection()

	def create(self):
		print('Enter your name:')
		name = input()
		print('Enter your address:')
		address = input()

		cursor = self.__db.cursor()

		val = (name, address)
		cursor.execute("INSERT INTO "+self.__table_name+" (name, address) VALUES (%s, %s)", val)

		self.__db.commit()

		print(cursor.rowcount, "record inserted.")

	def read(self):
		cursor = self.__db.cursor()

		cursor.execute("SELECT * FROM "+self.__table_name+"")

		myresult = cursor.fetchall()

		for x in myresult:
		  print(x)

	def update(self):
		print('Search by id:')
		id = input()

		print('Edit name:')
		name = input()

		if name is "":
			print("Leaving name empty will update the value to empty as well.")

		print('Edit address:')
		address = input()

		if address is "":
			print("Leaving address empty will update the value to empty as well.")

		cursor = self.__db.cursor()

		cursor.execute ("UPDATE "+self.__table_name+" SET name=%s, address=%s WHERE id=%s ", (name, address, id))

		self.__db.commit()

		print(cursor.rowcount, "record update.")

	def delete(self):
		print('Search by id to delete:')
		id = input()
		
		cursor = self.__db.cursor()

		cursor.execute ("DELETE FROM "+self.__table_name+" WHERE id = %s", (id,))

		self.__db.commit()

		print(cursor.rowcount, "record deleted.")

	def createConnection(self):
		db = mysql.connector.connect(
		  host     = self.__localhost,
		  user     = self.__username,
		  passwd   = self.__password,
		  database = self.__database_name
		)

		self.__db = db

