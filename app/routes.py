from app import app,mysql

from flask import render_template
from flask import jsonify

#create firt route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def showProducts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM product")
    product_data = cursor.fetchall()
    print(product_data)
    cursor.close()
    return render_template ('products.html', products = product_data)

@app.route('/orders')
def showOrders():
    return render_template('orders.html')

#this routes is to test only connection
# @app.route('/testconnect')
# def testdb():
#     try:
#         cursor = mysql.connection.cursor()
#         cursor.close()
#         print("Database credentials are all correct")
#         return jsonify({'message':'Database credentials all Goods'})
        
#     except Exception as e:
#         print("Some database credentials are incorrect",str(e))
#         return jsonify({'message':'Merong mga errors sa database'})
