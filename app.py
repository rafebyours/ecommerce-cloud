from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Konfigurasi koneksi ke RDS
db = pymysql.connect(
    host='ecommerce-db.cm50wm8ac224.us-east-1.rds.amazonaws.com',
    user='admin',
    password='SurajaKids',
    database='ecommercedb'
)

@app.route('/products', methods=['GET'])
def get_products():
    cursor = db.cursor()
    cursor.execute("SELECT name, price, image_url FROM products")
    data = cursor.fetchall()
    result = []
    for row in data:
        result.append({
            'name': row[0],
            'price': row[1],
            'image_url': row[2]
        })
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)