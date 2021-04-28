import sqlite3



def create_db():
	conn = sqlite3.connect('stock.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE stock (
            name text,
            shop_quantity real,
            stored_quantity real,
            price real,
            barcode real
            ) """)
	conn.commit()



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


def increase_stock(input_value,product_list):
	pass



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
#add_prod('Medias ggg',10,20,500,7010)
##add_prod('Medias hhh',10,20,500,7020)
#add_prod('Medias jjj',10,20,500,7027)




#result =show_product('8000')
#print(result)
#def show_product(input):
#	if input