import mysql.connector

#mathud to connect and insert a list to a mySQL DB

def InsertListToDB(BookList):
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'intsightbooks',
        'raise_on_warnings': True,
        'use_pure': False,
    }

    cnx = mysql.connector.connect(**config)
    for Books in BookList:
        for Book in Books:
            query = cnx.cursor(buffered=True)
            query.execute("insert into books (name,author,date,price,stars,reviews) VALUES ('" + Book.name.replace("'", "") + "','" + Book.author.replace("'", "") + "','" + Book.date + "','" + Book.price + "','" + Book.numberOfStars + "','" + Book.numberOfReviews + "')")
            cnx.commit()
            query.close()
    return