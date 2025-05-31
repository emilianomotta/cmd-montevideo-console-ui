from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = 'Emi-token-123'  # Debe coincidir con el token en Meta

@app.route('/webhook', methods=['GET'])
def verify():
    # Verificación webhook GET
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode == 'subscribe' and token == VERIFY_TOKEN:
        print('WEBHOOK VERIFICADO')
        return challenge, 200
    else:
        return 'Error de verificación', 403

@app.route('/webhook', methods=['POST'])
def webhook():
    # Recibe mensajes y eventos
    data = request.get_json()
    print('Evento recibido:', data)
    # Aquí podés agregar lógica para responder mensajes
    return 'EVENTO RECIBIDO', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
