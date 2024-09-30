# Resume Portfolio + Chatbot AI

## How to run the app

### Windows (Powershell)
```ps
python -m venv .venv
.\.venv\Scripts\activate
pip install -r .\requirements.txt
flask --app app run --debug
```

Create a `.env` file and place your Open Router API key there like this:
```
API_KEY="YOUR_API_KEY"
```