import mysql.connector as con
import json

class mylist(list):
        def __str__(self):
            return json.dumps(self)

def connect():
    try:
        cnx = con.connect(username="root", password='mypass', host="db", port="3306", db="db")
    except:
        return("error")

    return cnx

def read_database():
    cnx = connect()
    if cnx == "error":
        return("Connection Error")

    cursor = cnx.cursor(buffered=True)

    query = ("SELECT secret FROM data")

    try:
        cursor.execute(query)
    except:
        return("could not run query")

    ret = mylist()
    for word in cursor.fetchall():
        ret.append(word[0])
    cursor.close()
    cnx.close()
    return(str(ret))


def write_database(data):
    cnx = connect()
    ret = None
    if cnx == "error":
        return("Connection Error")

    cursor = cnx.cursor(buffered=True)
    value = (data['data'],)

    query = ("INSERT INTO data (secret) VALUES ('%s')" % (value))
    print(query)

    try:
        for result in cursor.execute(query, multi=True):
            ret = "Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount)
    except Exception as e:
        return(str(e), "query:", query)
    cnx.commit()
    cursor.close()
    cnx.close()

    return(ret)

def drop_column():
    cnx = connect()
    if cnx == "error":
        return("Connection Error")

    cursor = cnx.cursor(buffered=True)

    query = ("DELETE FROM data WHERE 1=1")

    try:
        cursor.execute(query)
        cnx.commit()
    except Exception as e:
        return(str(e))
    cursor.close()
    cnx.close()

    return("executed query")
