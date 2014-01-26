#!/usr/bin/env python

from flask import Flask, request, jsonify
import rpiblink

app = Flask(__name__)

@app.route("/api/blink",methods = ['GET'])
def blink():
    rpiblink.random_blink()
    return jsonify( { 'done': True } )

if __name__ == '__main__':
    app.run(host="0.0.0.0")

