import mysql.connector

# Configuration of the database. 
config = {
    'user': 'root',
    'password': '1234' ,
    'host': 'localhost',
    'database':'TRIBUCODE'

}

# calling main functions
db = mysql.connector.connect(**config)
cursor = db.cursor()


#Thanks for downloading. You can find all my videos on my channel of Youtube Tribucode
# TRIBUCODE #