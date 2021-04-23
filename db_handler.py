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



def show_product(input_value):
	connection = sqlite3.connect('stock.db')
	conn = connection.cursor()
	if input_value.isdigit():
		conn.execute("SELECT name,price FROM stock WHERE barcode = :barcode", {'barcode' : input_value})
	else:
		conn.execute("SELECT name,price FROM stock WHERE name = :input_value",
							 {'input_value' : input_value})
	return(conn.fetchall())






#create_db()
#add_prod('Medias',10,20,500,8000)
#add_prod('Calzones',10,50,300,9000)
#add_prod('Medias Azules',10,20,500,8000)
#result =show_product('8000')
#print(result)
#def show_product(input):
#	if input