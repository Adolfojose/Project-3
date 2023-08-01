from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexPopulation.html')

@app.route('/data')
def get_data():
    try:
        response = requests.get('https://restcountries.com/v3.1/all')
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
