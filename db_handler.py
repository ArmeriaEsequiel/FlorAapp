import sqlite3



def create_db():
	connection = sqlite3.connect('stock.db')
	conn = conn.cursor()
	conn.execute("""CREATE TABLE stock (
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
		print(check)
	if check is None:
		with connection:
			conn.execute("INSERT INTO stock VALUES (:name, :shop_quantity, :stored_quantity, :price, :barcode)",
				{'name' :name, 'shop_quantity' : shop_quantity, 'stored_quantity' : stored_quantity,
				'price' : price, 'barcode' : barcode})
		return('El producto se guardo correctamente')
	else:
		return('Ya existe el producto')


#Method = 0, for getting only name and price.
#Method = 1, for getiing all row values
def show_product(input_value, method):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	if input_value.isdigit():
		if method == 1:
			conn.execute("SELECT name,shop_quantity,stored_quantity,barcode FROM stock WHERE barcode = :barcode", {'barcode' : input_value})
		else:	
			conn.execute("SELECT name,price FROM stock WHERE barcode = :barcode", {'barcode' : input_value})
	else:
		if method == 1:
			conn.execute("SELECT name,shop_quantity,stored_quantity,barcode FROM stock WHERE name LIKE ?",('%'+input_value+'%',))
		else:
		#input_value = '%'+input_value+'%'
			conn.execute("SELECT name,price FROM stock WHERE name LIKE ?",('%'+input_value+'%',))
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
	print(price)
	conn.execute("UPDATE stock SET name = ?, price = ?, stored_quantity = ?, shop_quantity = ?  WHERE barcode = ?",
					[name,price,stored_quantity,shop_quantity, barcode])
	connection.commit()

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
	#print("METHOD ES {}".format(method))
	if method == 1:
		#print("Valores en update shop {}, {}".format(input_value,barcode))
		conn.execute("UPDATE stock SET shop_quantity = ? WHERE barcode = ?",
		[input_value, barcode])
	else:
		#print("Valores en update store {}, {}".format(input_value,barcode))
		conn.execute("UPDATE stock SET stored_quantity = ? WHERE barcode = ?",
					[input_value,barcode])
	connection.commit()
	#result =show_product('9000', 1)
	#print(result)


#create_db()
#add_prod('Medias',10,20,500,8000)
#add_prod('Calzones',10,50,300,9000)
#add_prod('Medias Rojas',10,20,500,7001)
##add_prod('Medias Veres',10,20,500,7002)
#add_prod('Medias Rosas',10,20,500,7003)
#add_prod('Medias Grises',10,20,500,7004)
#add_prod('Medias Negras',10,20,500,7005)
#add_prod('Medias ASd',10,20,500,7006)
#add_prod('Medias ddd',10,20,500,7007)
#add_prod('Medias aaa',10,20,500,7008)
#add_prod('Medias sss',10,20,500,7009)
#add_prod('Medias gggggggggggggggggggggggg',10,20,500,7016)
##add_prod('Medias hhh',10,20,500,7020)
#add_prod('Medias jjj',10,20,500,7027)




#result =show_product('9000', 1)
#print(result)
#def show_product(input):
#	if input