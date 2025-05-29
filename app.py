from flask import Flask, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
