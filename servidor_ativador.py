from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de dispositivos autorizados (poderia ser armazenado em um banco de dados)
dispositivos_autorizados = {}

@app.route("/autorizar", methods=["POST"])
def autorizar():
    dados = request.json
    mac = dados.get("mac")
    if not mac:
        return jsonify({"status": "erro", "mensagem": "MAC não enviado"}), 400

    # Adiciona o MAC na lista autorizada
    dispositivos_autorizados[mac] = True
    return jsonify({"status": "sucesso", "mensagem": f"MAC {mac} autorizado"}), 200

@app.route("/verificar", methods=["POST"])
def verificar():
    dados = request.json
    mac = dados.get("mac")
    autorizado = dispositivos_autorizados.get(mac, False)
    return jsonify({"autorizado": autorizado}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
