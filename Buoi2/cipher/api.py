from flask import Flask, request, jsonify
from cipher import CaesarCipher, VigenereCipher, PlayfairCipher, RailFenceCipher, TranspositionCipher

app = Flask(__name__)

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    text = data.get("text", "")
    shift = int(data.get("shift", 3))
    cipher = CaesarCipher(shift)
    return jsonify({"encrypted_text": cipher.encrypt(text)})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    text = data.get("text", "")
    shift = int(data.get("shift", 3))
    cipher = CaesarCipher(shift)
    return jsonify({"decrypted_text": cipher.decrypt(text)})

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    text = data.get("text", "")
    key = data.get("key", "KEY")
    cipher = VigenereCipher(key)
    return jsonify({"encrypted_text": cipher.encrypt(text)})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    text = data.get("text", "")
    key = data.get("key", "KEY")
    cipher = VigenereCipher(key)
    return jsonify({"decrypted_text": cipher.decrypt(text)})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    text = data.get("text", "")
    key = data.get("key", "KEY")
    cipher = PlayfairCipher(key)
    return jsonify({"encrypted_text": cipher.encrypt(text)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    text = data.get("text", "")
    key = data.get("key", "KEY")
    cipher = PlayfairCipher(key)
    return jsonify({"decrypted_text": cipher.decrypt(text)})

@app.route('/api/rail_fence/encrypt', methods=['POST'])
def rail_fence_encrypt():
    data = request.json
    text = data.get("text", "")
    rails = int(data.get("rails", 3))
    cipher = RailFenceCipher(rails)
    return jsonify({"encrypted_text": cipher.encrypt(text)})

@app.route('/api/rail_fence/decrypt', methods=['POST'])
def rail_fence_decrypt():
    data = request.json
    text = data.get("text", "")
    rails = int(data.get("rails", 3))
    cipher = RailFenceCipher(rails)
    return jsonify({"decrypted_text": cipher.decrypt(text)})

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.json
    text = data.get("text", "")
    key = data.get("key", "SECRET")
    cipher = TranspositionCipher(key)
    return jsonify({"encrypted_text": cipher.encrypt(text)})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.json
    text = data.get("text", "")
    key = data.get("key", "SECRET")
    cipher = TranspositionCipher(key)
    return jsonify({"decrypted_text": cipher.decrypt(text)})

if __name__ == '__main__':
    app.run(debug=True)
