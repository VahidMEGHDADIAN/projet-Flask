from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row  # To fetch results as dictionaries
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM customer LIMIT 50').fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/all-data')
def all_data():
    conn = get_db_connection()
    query = '''
    SELECT *
    FROM customer
    JOIN customer_order ON customer.id = customer_order.customer_id
    JOIN order_detail ON customer_order.id = order_detail.order_id
    JOIN product ON order_detail.product_id = product.id
    LIMIT 50;
    '''
    data = conn.execute(query).fetchall()
    conn.close()
    return render_template('all_data.html', data=data)

