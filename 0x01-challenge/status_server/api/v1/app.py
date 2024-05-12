#!/usr/bin/python3
"""
Web server
"""
from flask import Flask, jsonify, make_response

app = Falsk(__name__)


@app.route('/api/v1/status'))
def status():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
