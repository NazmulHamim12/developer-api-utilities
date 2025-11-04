from flask import Flask, jsonify, request
import uuid
import random
import string
import time
import hashlib

import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Hamim's Developer Utility API",
        "available_endpoints": [
            "/uuid",
            "/timestamp",
            "/random-color",
            "/random-password",
            "/random-string",
            "/hash?text=yourtext&algo=sha256",
            "/validate-email?email=example@gmail.com",
            "/ip-info",
            "/date-info",
            "/random-number?min=1&max=100",
            "/quote"
        ]
    })

@app.route('/uuid')
def generate_uuid():
    return jsonify({
        "uuid": str(uuid.uuid4())
    })


@app.route('/timestamp')
def generate_timestamp():
    return jsonify({
        "timestamp": int(time.time()),
        "readable_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    })


@app.route('/random-color')
def random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return jsonify({
        "color": color
    })


@app.route('/random-password')
def random_password():
    length = int(request.args.get('length', 12))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return jsonify({
        "password": password,
        "length": length
    })


@app.route('/random-string')
def random_string():
    length = int(request.args.get('length', 10))
    characters = string.ascii_lowercase
    rand_str = ''.join(random.choice(characters) for _ in range(length))
    return jsonify({
        "string": rand_str,
        "length": length
    })


@app.route('/hash-string', methods=['POST'])
def hash_string():
    data = request.get_json()
    text = data.get('text')
    algo = request.args.get('algo', 'sha256').lower()

    if not text:
        return jsonify({"error": "Please provide ?text=yourtext"}), 400

    try:
        h = hashlib.new(algo)
        h.update(text.encode())
        return jsonify({
            "input": text,
            "algorithm": algo,
            "hash": h.hexdigest()
        })
    except ValueError:
        return jsonify({"error": "Invalid algorithm. Try md5 or sha256."}), 400


@app.route('/validate-email', methods=['POST'])
def validate_email():
    data = request.get_json()
    email = data.get('email', '')

    
    if len(email) < 6:
        return jsonify({"email": email, "valid": False, "reason": "Too short"})

    
    if '@' not in email:
        return jsonify({"email": email, "valid": False, "reason": "Missing @"})

    
    if not email.endswith(".com") or "gmail.com" not in email:
        return jsonify({"email": email, "valid": False, "reason": "Must be gmail.com"})

    return jsonify({"email": email, "valid": True})


@app.route('/ip-info')
def ip_info():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return jsonify({
        "your_ip": ip
    })


@app.route('/date-info')
def date_info():
    now = datetime.datetime.now()
    return jsonify({
        "date": now.strftime("%Y-%m-%d"),
        "day": now.strftime("%A"),
        "month": now.strftime("%B"),
        "year": now.year,
        "time": now.strftime("%H:%M:%S")
    })


@app.route('/random-number')
def random_number():
    try:
        min_val = int(request.args.get('min', 0))
        max_val = int(request.args.get('max', 100))
        num = random.randint(min_val, max_val)
        return jsonify({
            "number": num,
            "min": min_val,
            "max": max_val
        })
    except ValueError:
        return jsonify({"error": "Invalid input. Use ?min=1&max=100"}), 400


@app.route('/quote')
def random_quote():
    quotes = [
        {"quote": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
        {"quote": "Programs must be written for people to read, and only incidentally for machines to execute.", "author": "Harold Abelson"},
        {"quote": "Code never lies, comments sometimes do.", "author": "Ron Jeffries"},
        {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
        {"quote": "Before software can be reusable it first has to be usable.", "author": "Ralph Johnson"}
    ]
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run()
