import os
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Initialize total donations
total_donations = 0

# Load donations from a file if it exists
def load_donations():
    global total_donations
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            total_donations = data.get('total_donations', 0)
    except FileNotFoundError:
        total_donations = 0

# Save donations to a file
def save_donations():
    with open('data.json', 'w') as file:
        json.dump({'total_donations': total_donations}, file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    global total_donations
    if request.method == 'POST':
        amount = request.form.get('amount', type=int)
        if amount and 0 < amount <= 500:  # Max donation is 500
            total_donations += amount
            save_donations()
            return jsonify({'total_donations': total_donations})
        else:
            return jsonify({'error': 'Invalid donation amount'}), 400
    return render_template('donate.html')

@app.route('/total')
def total():
    return jsonify({'total_donations': total_donations})

if __name__ == '__main__':
    load_donations()  # Load donations at startup
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=port)  # Listen on all interfaces and the specified port
