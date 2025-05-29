from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ----------------------------
# Render view routes (HTML pages)
# ----------------------------
cipher_routes = [
    ('/', 'index'),
    ('/caesar', 'caesar'),
    ('/vigenere', 'vingenere'),  # Note: using "vingenere". Change to "vigenere" if needed.
    ('/playfair', 'playfair'),
    ('/rail_fence', 'rail_fence'),
    ('/transposition', 'transposition')
]

def create_view(template_name):
    def view():
        return render_template(f'{template_name}.html')
    return view

for route, template in cipher_routes:
    app.add_url_rule(
        route,
        endpoint=template,
        view_func=create_view(template)
    )

# ----------------------------
# API Endpoints for Caesar Cipher
# ----------------------------
@app.route('/api/caesar/encrypt', methods=['POST'])
def api_caesar_encrypt():
    data = request.get_json()
    text = data.get('text', '')
    try:
        shift = int(data.get('shift', 0))
    except ValueError:
        shift = 0

    encrypted_text = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def api_caesar_decrypt():
    data = request.get_json()
    text = data.get('text', '')
    try:
        shift = int(data.get('shift', 0))
    except ValueError:
        shift = 0

    decrypted_text = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift + 26) % 26 + base)
        else:
            decrypted_text += char
    return jsonify({'decrypted_text': decrypted_text})

# ----------------------------
# API Endpoints for Vigenère Cipher (spelled "vingenere" here)
# ----------------------------
@app.route('/api/vingenere/encrypt', methods=['POST'])
def api_vingenere_encrypt():
    data = request.get_json()
    text = data.get('text', '')
    key = data.get('key', '')
    if not key:
        return jsonify({'encrypted_text': text})
    key = key.upper()
    encrypted_text = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            encrypted_text += char
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vingenere/decrypt', methods=['POST'])
def api_vingenere_decrypt():
    data = request.get_json()
    text = data.get('text', '')
    key = data.get('key', '')
    if not key:
        return jsonify({'decrypted_text': text})
    key = key.upper()
    decrypted_text = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_text += chr((ord(char) - base - shift + 26) % 26 + base)
            key_index += 1
        else:
            decrypted_text += char
    return jsonify({'decrypted_text': decrypted_text})

# ----------------------------
# API Endpoints for Playfair Cipher
# ----------------------------
@app.route('/api/playfair/encrypt', methods=['POST'])
def api_playfair_encrypt():
    data = request.get_json()
    text = data.get('text', '').upper().replace("J", "I")
    key = data.get('key', '').upper().replace("J", "I")
    # Generate the key square.
    def generate_key_square(key_str):
        key_str = "".join(dict.fromkeys(key_str))  # Remove duplicates.
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"     # 'J' is omitted.
        for letter in alphabet:
            if letter not in key_str:
                key_str += letter
        square = [list(key_str[i*5:(i+1)*5]) for i in range(5)]
        return square

    square = generate_key_square(key)

    def find_position(letter, square):
        for i, row in enumerate(square):
            for j, ch in enumerate(row):
                if ch == letter:
                    return i, j
        return None, None

    # Preprocess text: keep only letters.
    filtered_text = "".join(filter(str.isalpha, text))
    # Form digrams. Insert 'X' between identical letters.
    digrams = []
    i = 0
    while i < len(filtered_text):
        a = filtered_text[i]
        if i + 1 < len(filtered_text):
            b = filtered_text[i+1]
            if a == b:
                digrams.append(a + "X")
                i += 1
            else:
                digrams.append(a + b)
                i += 2
        else:
            digrams.append(a + "X")
            i += 1

    encrypted_text = ""
    for pair in digrams:
        a, b = pair[0], pair[1]
        row1, col1 = find_position(a, square)
        row2, col2 = find_position(b, square)
        if row1 == row2:
            # Same row: shift right.
            encrypted_text += square[row1][(col1+1) % 5] + square[row2][(col2+1) % 5]
        elif col1 == col2:
            # Same column: shift down.
            encrypted_text += square[(row1+1)%5][col1] + square[(row2+1)%5][col2]
        else:
            # Rectangle rule.
            encrypted_text += square[row1][col2] + square[row2][col1]
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def api_playfair_decrypt():
    data = request.get_json()
    text = data.get('text', '').upper().replace("J", "I")
    key = data.get('key', '').upper().replace("J", "I")
    def generate_key_square(key_str):
        key_str = "".join(dict.fromkeys(key_str))
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in key_str:
                key_str += letter
        square = [list(key_str[i*5:(i+1)*5]) for i in range(5)]
        return square

    square = generate_key_square(key)

    def find_position(letter, square):
        for i, row in enumerate(square):
            for j, ch in enumerate(row):
                if ch == letter:
                    return i, j
        return None, None

    decrypted_text = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        row1, col1 = find_position(a, square)
        row2, col2 = find_position(b, square)
        if row1 == row2:
            decrypted_text += square[row1][(col1-1) % 5] + square[row2][(col2-1) % 5]
        elif col1 == col2:
            decrypted_text += square[(row1-1)%5][col1] + square[(row2-1)%5][col2]
        else:
            decrypted_text += square[row1][col2] + square[row2][col1]
        i += 2
    return jsonify({'decrypted_text': decrypted_text})

# ----------------------------
# API Endpoints for Rail Fence Cipher
# ----------------------------
@app.route('/api/rail_fence/encrypt', methods=['POST'])
def api_rail_fence_encrypt():
    data = request.get_json()
    text = data.get('text', '')
    try:
        rails = int(data.get('rails', 2))
    except ValueError:
        rails = 2

    if rails <= 1:
        return jsonify({'encrypted_text': text})
    
    fence = ['' for _ in range(rails)]
    rail = 0
    direction = 1
    for char in text:
        fence[rail] += char
        rail += direction
        if rail == rails:
            rail = rails - 2
            direction = -1
        elif rail < 0:
            rail = 1
            direction = 1

    encrypted_text = ''.join(fence)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/rail_fence/decrypt', methods=['POST'])
def api_rail_fence_decrypt():
    data = request.get_json()
    text = data.get('text', '')
    try:
        rails = int(data.get('rails', 2))
    except ValueError:
        rails = 2

    if rails <= 1:
        return jsonify({'decrypted_text': text})
    
    n = len(text)
    rail_pattern = []
    rail = 0
    direction = 1
    for i in range(n):
        rail_pattern.append(rail)
        rail += direction
        if rail == rails:
            rail = rails - 2
            direction = -1
        elif rail < 0:
            rail = 1
            direction = 1

    rail_counts = [rail_pattern.count(r) for r in range(rails)]
    rails_text = []
    index = 0
    for count in rail_counts:
        rails_text.append(text[index:index+count])
        index += count

    indices = [0] * rails
    decrypted_text = ''
    for r in rail_pattern:
        decrypted_text += rails_text[r][indices[r]]
        indices[r] += 1

    return jsonify({'decrypted_text': decrypted_text})

# ----------------------------
# API Endpoints for Transposition Cipher (Columnar Transposition)
# ----------------------------
@app.route('/api/transposition/encrypt', methods=['POST'])
def api_transposition_encrypt():
    data = request.get_json()
    text = data.get('text', '')
    key = data.get('key', '')
    try:
        num_cols = int(key)
    except ValueError:
        num_cols = len(key) if key else 2

    num_rows = (len(text) + num_cols - 1) // num_cols
    padded_text = text.ljust(num_rows * num_cols)
    matrix = [padded_text[i*num_cols:(i+1)*num_cols] for i in range(num_rows)]
    encrypted_text = ''
    for col in range(num_cols):
        for row in range(num_rows):
            encrypted_text += matrix[row][col]
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def api_transposition_decrypt():
    data = request.get_json()
    text = data.get('text', '')
    key = data.get('key', '')
    try:
        num_cols = int(key)
    except ValueError:
        num_cols = len(key) if key else 2

    num_rows = (len(text) + num_cols - 1) // num_cols
    matrix = [[''] * num_cols for _ in range(num_rows)]
    index = 0
    for col in range(num_cols):
        for row in range(num_rows):
            if index < len(text):
                matrix[row][col] = text[index]
                index += 1
    decrypted_text = ''.join(''.join(row) for row in matrix)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
