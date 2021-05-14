import sqlite3



def create_stock_db():
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	conn.execute("""CREATE TABLE IF NOT EXISTS stock (
            name text,
            shop_quantity real,
            stored_quantity real,
            price real,
            barcode real
            ) """)
	connection.commit()


def add_prod(name, shop_quantity, stored_quantity, price, barcode):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	with connection:
		conn.execute("SELECT name FROM stock WHERE barcode = :barcode", {'barcode' : barcode})
		check  = conn.fetchone()
	if check is None:
		with connection:
			conn.execute("INSERT INTO stock VALUES (:name, :shop_quantity, :stored_quantity, :price, :barcode)",
				{'name' :name, 'shop_quantity' : shop_quantity, 'stored_quantity' : stored_quantity,
				'price' : price, 'barcode' : barcode})
		return(1)
	else:
		return(0)


#Method = 0, for getting only name and price.
#Method = 1, for getiing all row values
def show_product(input_value, method):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	if input_value.isdigit():
		if method == 1:
			conn.execute("SELECT name,shop_quantity,stored_quantity,barcode FROM stock WHERE barcode = :barcode", {'barcode' : input_value})
		else:	
			conn.execute("SELECT name,price,barcode FROM stock WHERE barcode = :barcode", {'barcode' : input_value})
	else:
		if method == 1:
			conn.execute("SELECT name,shop_quantity,stored_quantity,barcode FROM stock WHERE name LIKE ?",('%'+input_value+'%',))
		else:
		#input_value = '%'+input_value+'%'
			conn.execute("SELECT name,price,barcode FROM stock WHERE name LIKE ?",('%'+input_value+'%',))
	return(conn.fetchall())


def show_products_delete(input_value):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	if input_value.isdigit():
		conn.execute("SELECT name,barcode FROM stock WHERE barcode = :barcode", {'barcode' : input_value})
	else:
		conn.execute("SELECT name,barcode FROM stock WHERE name LIKE ?",('%'+input_value+'%',))
	return(conn.fetchall())



def get_products_from_list(input_value):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	paramlist = '?'
	for i in range(len(input_value)-1):
		paramlist = paramlist + ', ?'
	sql = "SELECT name,shop_quantity,stored_quantity,barcode FROM stock WHERE barcode IN ("+paramlist+")"
	for item in input_value:
		conn.execute(sql, input_value)
	return(conn.fetchall())


def get_full_product(input_value):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	conn.execute("SELECT name,price,shop_quantity,stored_quantity,barcode FROM stock WHERE barcode = :barcode",
				 {'barcode' : input_value})
	return(conn.fetchall())

def update_product(name, price, stored_quantity, shop_quantity, barcode):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	with connection:
		conn.execute("SELECT name FROM stock WHERE barcode = :barcode", {'barcode' : barcode})
		check  = conn.fetchone()
#		print(check)
	if check is None:
		return(0)
	conn.execute("UPDATE stock SET name = ?, price = ?, stored_quantity = ?, shop_quantity = ?  WHERE barcode = ?",
					[name,price,stored_quantity,shop_quantity, barcode])
	connection.commit()
	return(1)

def increase_stock(input_value,barcode):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	#print(input_value,barcode)
	conn.execute("UPDATE stock SET stored_quantity = ? WHERE barcode = ?",
					(input_value, barcode,))
	connection.commit()


def change_stock(input_value,barcode,method):
	#print("Valores change_stock {}, {}, {}".format(input_value,barcode,int(method)))
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
#	result =get_full_product('222')
#	print(result)
	#print("METHOD ES {}".format(method))
	if method == 0:
#		print("METHOD ES = {}".format(int(method)))
#		print("ENTRE EN SHOP")
#		print("input_value es {}".format(input_value))
#		print("Valores en update shop {}, {}".format(input_value,barcode))
		conn.execute("UPDATE stock SET shop_quantity = ? WHERE barcode = ?",
		[input_value, barcode])
	else:
#		print("ENTRE EN STORED")
#		print("input_value es {}".format(input_value))
#		print("Valores en update store {}, {}".format(input_value,barcode))
		conn.execute("UPDATE stock SET stored_quantity = ? WHERE barcode = ?",
					[input_value,barcode])
	connection.commit()
#	result =get_full_product('222')
#	print(result)

def delete_product(input_value):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	with connection:
		conn.execute("SELECT name FROM stock WHERE barcode = :barcode", {'barcode' : input_value})
		check  = conn.fetchone()
		print(check)
	if check is None:
		return(0)
	conn.execute("DELETE FROM stock WHERE barcode = :barcode",{'barcode' : input_value})
	connection.commit()
	return(1)


def get_storage_out_of_stock():
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	conn.execute("SELECT name,shop_quantity,stored_quantity,barcode FROM stock WHERE stored_quantity = 0")
	return(conn.fetchall())


def get_shop_out_of_stock():
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	conn.execute("SELECT name,shop_quantity,stored_quantity,barcode FROM stock WHERE shop_quantity = 0")
	return(conn.fetchall())

#--------------------------------------------------------------------------------------------------------

#SALES HANDLERS

def create_sales_db():
	connection = sqlite3.connect('sales.db')
	conn = connection.cursor()
	conn.execute("""CREATE TABLE IF NOT EXISTS sales (
            name text,
            quantity real,
            barcode real,
            status text,
            record_time DATE DEFAULT CURRENT_DATE
            ) """)
	connection.commit()

def test_db():
	connection = sqlite3.connect('test.db')
	conn = connection.cursor()
	conn.execute(""" CREATE TABLE test(
		book_id INTEGER PRIMARY KEY,
		Book_name TEXT NOT NULL,
		price INTEGER DEFAULT 100
		)""")



def add_sale(name,quantity,barcode,status):
	connection = sqlite3.connect('sales.db')
	conn = connection.cursor()
	with connection:
		conn.execute("INSERT INTO sales (name,quantity,barcode,status)VALUES (?, ?, ?, ?)",
			[name, quantity, barcode, status])


def get_sales(from_time, to_time):
	connection = sqlite3.connect('sales.db')
	conn = connection.cursor()
	with connection:
		conn.execute("SELECT * FROM sales")
		conn.execute("SELECT * FROM sales WHERE record_time BETWEEN date(?) and date(?)",
			[from_time, to_time])
	return(conn.fetchall())

def add_test():
	connection = sqlite3.connect('test.db')
	conn = connection.cursor()
	with connection:
		conn.execute("INSERT INTO test (book_id,Book_name) VALUES(1,'RAMAYANA')")

def get_test():
	connection = sqlite3.connect('test.db')
	conn = connection.cursor()
	with connection:
		conn.execute("SELECT * FROM test")	
	return(conn.fetchall())

