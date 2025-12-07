from flask import Flask, jsonify
import random
from datetime import date, timedelta
import pandas as pd


app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "hello world"

def generate_sales_data(num_records=10):
    products = ["Apple", "Banana", "Orange", "Milk", "Bread", "Eggs", "Cheese"]
    data = []
    for _ in range(num_records):
        random_date = date(2023, 1, 1) + timedelta(days=random.randint(0, 364))
        product = random.choice(products)
        quantity = random.randint(1, 10)
        price = round(random.uniform(50, 500), 2)
        total = round(quantity * price, 2)
        data.append({
            "Date": random_date.isoformat(),
            "Product": product,
            "Quantity": quantity,
            "Price": price,
            "Total": total
        })
    return pd.DataFrame(data)

@app.route('/api/sales')
def get_sales_data():
    df = generate_sales_data()
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
