from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

#database credentials (XAMPP)
#hostname "localhost"
app.config['MYSQL_HOST'] = 'localhost'
#username "root"
app.config['MYSQL_USER'] = 'root'
#passwod "root"
app.config['MYSQL_PASSWORD'] = ''
#database
app.config['MYSQL_DB'] = 'vinalynn'

#initialize all these credentials(XAMPP)
mysql = MySQL(app)

#call routes from the lask
from app import routes