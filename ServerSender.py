from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = "http://127.0.0.1:5001/webhook-receiver"

@app.route("/send-webhook", methods=["GET","POST"])
def send_webhook():
    webhook_data = {
        "event": "item_deleted",
        "item_id": 123,
        "message": "Se eliminó un elemento del inventario."
    }


    try:
        response = requests.post(WEBHOOK_URL, json=webhook_data)
        return jsonify({"status": "Webhook enviado", "response_code": response.status_code}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
