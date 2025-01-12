from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook-receiver", methods=["POST"])
def webhook_receiver():

    data = request.get_json()
    print(f"Webhook recibido: {data}")

    
    return jsonify({"status": "Webhook recibido correctamente"}), 200

if __name__ == "__main__":
    app.run(port=5001, debug=True, host="0.0.0.0")
