import sqlite3
from decimal import Decimal


def dict_factory(cursor, row):      # A function found online to convert a tuple (returned by SQL) to a dict
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class dbCtrl:
    def __init__(self):
        global db, cur # set db and cur to be global
        db = sqlite3.connect("stocksystem.db") # connect to the database
        db.row_factory = dict_factory # lay out the results as a dict
        cur = db.cursor() # create the cursor

    def createItem(self, tag, name, category, price, qty, extra):
        row = cur.execute("SELECT ID FROM stock WHERE ID = '{0}'".format(tag)).fetchone() # check if an item with the Id already exists
        if row is None: # if no item with that ID exists
            cur.execute("INSERT INTO stock (ID, Name, Category, Price, Quantity, extrainfo, priceMult) VALUES ('{0}', '{1}', '{2}', {3}, {4}, '{5}', 1)".format(tag, name, category, price, qty, extra))
            # add a new item with all of the specified attributes
        else:   # if that ID DOES already exist
            cur.execute("UPDATE Stock SET Category='{1}', Name='{2}', Quantity={3}, Price={4}, extrainfo='{5}' WHERE Id = {0}".format(tag, category, name, qty, price, extra))
            # update the item with that set of attributes
        db.commit()

    def editItem(self, tag, item, new_val):
        cur.execute("UPDATE stock SET '{0}' = '{1}' WHERE ID = '{2}'".format(tag, item, new_val))
        db.commit()

    def searchList(self, keyphrase, list):
        return list.execute("SELECT * FROM stock WHERE Name LIKE '%{0}%'".format(keyphrase))

    def sortList(self, attr, order, list):
        return list.execute("SELECT * FROM stock ORDER BY '{0}' {1}".format(attr, order))

    def filterQuery(self, search="", minPrice=0.0, maxPrice=None, minQty=0, maxQty=None, orderAttr="", order=""):
        if Decimal(minPrice).as_tuple().exponent < -2 or minPrice != float(minPrice):
        # check if minPrice is a float with 2 or fewer decimal places, if not make it 0 - validate this attribute
            minPrice = 0.0
        if minQty != int(minQty): # ensure minQty is an integer, otherwise make it 0 - attribute validation
            minQty = 0
        query = """SELECT * FROM stock
        WHERE Name LIKE '%{0}%'
        AND Price >= {1}    
        AND Quantity >= {2}""".format(search, minPrice, minQty) # set up the base SQL query with these attributes
        if maxPrice is not None and maxPrice == float(maxPrice) and Decimal(maxPrice).as_tuple().exponent >= -2:
            query = query + """ AND Price <= {0}""".format(maxPrice)
            # validate maxPrice in the same way as minPrice and add it into the query if valid and specified by user
        if maxQty is not None and maxQty == int(maxQty):
            query = query + """ AND Quantity <= {0}""".format(maxQty)
            # validate maxQty in the same way as minQty and add it into the query if valid and specified by user
        if orderAttr != "" and (order == "ASC" or order == "DESC"):
            query = query + """ ORDER BY {0} {1};""".format(orderAttr, order)
            # if there is anything in orderAttr and order is one of these two values, then add a corresponding order clause to the query
        return cur.execute(query) # return the cursor object after executing the query

    def deleteItem(self, productid):
        cur.execute("DELETE FROM stock WHERE ID = '{0}'".format(productid))  # Delete the passed in ID
        db.commit()  # Commit to the database
