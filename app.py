from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE_PATH = 'data.json'

# Function to read the total amount raised from a JSON file
def read_total_amount():
    if os.path.exists(DATA_FILE_PATH):
        with open(DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
            return data.get("totalAmount", 0)
    return 0

# Function to write the total amount raised to a JSON file
def write_total_amount(amount):
    with open(DATA_FILE_PATH, 'w') as file:
        json.dump({"totalAmount": amount}, file)

# Initialize the total amount raised
total_amount = read_total_amount()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/api/donation', methods=['GET'])
def get_donation():
    return jsonify({"totalAmount": total_amount})

@app.route('/api/donation', methods=['POST'])
def add_donation():
    global total_amount
    data = request.get_json()
    amount = data.get("amount", 0)

    if isinstance(amount, (int, float)) and amount > 0:
        total_amount += amount
        write_total_amount(total_amount)
        return jsonify({"totalAmount": total_amount}), 200
    else:
        return jsonify({"error": "Invalid donation amount"}), 400

if __name__ == '__main__':
    app.run(port=5000)
