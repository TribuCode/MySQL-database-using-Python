# Libraries that we need to import
from setup import cursor, db
import time 

# DB_NAME = 'TRIBUCODE'

# Function which add a follower to the table
def add_follower(user,last_name):
    sql = ("INSERT INTO Followers(user,last_name) VALUES (%s,%s)")
    cursor.execute(sql, (user,last_name,))
    db.commit()

# Function which show a follower according to his id
def get_onefollower(id):
    sql = ("SELECT * FROM Followers WHERE id= %s")
    cursor.execute(sql, (id,))
    data = cursor.fetchone()
    print(data)
    

# Function which shows all the followers
def get_followers():
    sql = ("SELECT * FROM Followers ORDER BY date ASC") #DESC if you want to order by descendent order
    cursor.execute(sql)
    data = cursor.fetchall()

    for record in  data:
        print(record)

# Function which updates a follower using his id and user(name)
def update_follower(id,user):
    sql = ("UPDATE Followers SET user= %s WHERE id = %s")
    cursor.execute(sql, (user,id))
    db.commit()
    print("Updated")


# Function which deletes a follower using his id
def delete_follower(id):
    sql = ("DELETE FROM  Followers WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print("Deleted")


# Function which deletes a table.
def delete_table(table='followers'):
    cursor.execute("DROP TABLE {}".format(table))


# Function which deletes a database.
def delete_database(DB_NAME):
    cursor.execute("DROP DATABASE {}".format(DB_NAME))



#All commands used to check the program.


#delete_table(table = 'followers')
#delete_database(DB_NAME='tribucode')
# get_onefollower(2)
#get_followers()

#update_follower(2,"Juan")

#delete_follower(2)
#get_followers()


# add_follower('Lucia','Gomez')
# add_follower('Ramon','Garcia')
# add_follower('German','Gomez')
# time.sleep(1)
# add_follower('Pedro','Garcia')



#Thanks for downloading. You can find all my videos on my channel of Youtube Tribucode
# TRIBUCODE