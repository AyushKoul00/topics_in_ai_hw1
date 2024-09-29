import mysql.connector

def insertQuery(name, email, message):
    mydb = mysql.connector.connect(
        host="localhost",
        user="aditya",
        password="pass",
        database="resume"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO query (name, email, message) VALUES (%s, %s, %s)"
    val = (name, email, message)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

