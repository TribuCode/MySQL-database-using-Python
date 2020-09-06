# Libraries that we need to import.
import mysql.connector
from mysql.connector import errorcode
from setup import cursor

# Name of the Database
DB_NAME = 'TRIBUCODE'

# Init the tables empty
TABLES = {}

#Creation of the Tables with his features
TABLES['Followers'] = (
    "CREATE TABLE `Followers`(" 
    " `id` int(15) NOT NULL AUTO_INCREMENT,"
    "`user` varchar(250) NOT NULL,  "
    " `last_name` varchar(250) NOT NULL, "
    " `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"   
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

# Function which create the database schema
def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))

# Function which create the table inside the database schema
def create_tables():
    cursor.execute("USE {}".format(DB_NAME))
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({}) ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exists")
            else:
                print(error.msg)
        
# Calling the functions to execute them
create_database()
create_tables()



#Thanks for downloading. You can find all my videos on my channel of Youtube Tribucode
# TRIBUCODE #