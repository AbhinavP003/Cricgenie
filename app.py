from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query_text = data.get('query', '')
    # Echo the query text as the answer
    return jsonify({"response": query_text})

if __name__ == '__main__':
    app.run(debug=True)
