import sqlite3
import os
from decimal import Decimal


class dbCtrl:
    def __init__(self):
        global db
        db = sqlite3.connect("stocksystem.db")
        global cur
        cur = db.cursor()

    def createItem(self, tag, name, category, price, qty, img, extra, bogof, pricemult):
        cur.execute("INSERT INTO stock (ID, Name, Category, Price, Quantity, imgpath, extrainfo, BOGOF, priceMult) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(tag, name, category, price, qty, img, extra, bogof, pricemult))
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
            minPrice = 0.0
        if minQty != int(minQty):
            minQty = 0
        query = """SELECT * FROM stock
        WHERE Name LIKE '%{0}%'
        AND Price >= {1}
        AND Quantity >= {2}""".format(search, minPrice, minQty)
        if maxPrice is not None and maxPrice == float(maxPrice) and Decimal(maxPrice).as_tuple().exponent >= -2:
            query = query + """ AND Price <= {0}""".format(maxPrice)
        if maxQty is not None and maxQty == int(maxQty):
            query = query + """ AND Quantity <= {0}""".format(maxQty)
        if orderAttr != "" and (order == "ASC" or order == "DESC"):
            query = query + """ ORDER BY {0} {1};""".format(orderAttr, order)
        print(query)
        return cur.execute(query)


banana = dbCtrl()
banana.filterQuery() # Test case
print(cur.fetchall())
