import pymysql
from dotenv import dotenv_values


host = dotenv_values(".env")["HOST"]
user = dotenv_values(".env")["USER"]
password = dotenv_values(".env")["PASSWORD"]
db_name = dotenv_values(".env")["DB_NAME"]

try:
	connection = pymysql.connect(
		host=host,
		port=3306,
		user=user,
		password=password,
		db=db_name,
		cursorclass=pymysql.cursors.DictCursor
	)
	print("Connected to database")

	try:
		with connection.cursor() as cursor:
			create_table = "CREATE TABLE IF NOT EXISTS `ideas` (" \
			               "id INT NOT NULL AUTO_INCREMENT," \
							"author VARCHAR(255) NOT NULL," \
							"email VARCHAR(255) NOT NULL," \
							"phone VARCHAR(255) NOT NULL," \
							"category VARCHAR(255) NOT NULL," \
							"title VARCHAR(255) NOT NULL," \
							"intro VARCHAR(255) NOT NULL," \
							"description TEXT NOT NULL," \
							"date_ TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
							"published BOOLEAN NOT NULL DEFAULT FALSE," \
							"archived BOOLEAN NOT NULL DEFAULT FALSE," \
							"PRIMARY KEY (id)"
			cursor.execute(create_table)
			connection.commit()
			print("Table created")
	finally:
		connection.close()

except Exception as ex:
	print("Could not connect to database")
	print(ex)
