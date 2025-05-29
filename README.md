# Simple Chatbot Backend

This is a basic Flask-based chatbot backend with rule-based responses.

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the app:
```
python app.py
```

3. Test using curl or Postman:
```
POST http://localhost:5000/chat
Body: { "message": "hello" }
```

## Example Response
```json
{
  "response": "Hi there! How can I help you today?"
}
```
