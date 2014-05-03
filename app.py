#!/usr/bin/env python

from flask import Flask, abort, request, jsonify
from functools import wraps

import rpiblink
import hacklab_status


app = Flask(__name__)

def hacklab_check(f):
    """Respond to commands only if the Hacklab is open"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        status = hacklab_status.get_status()
        if status==1:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/api/blink", methods=['POST'])
@hacklab_check
def blink():
    rpiblink.random_blink()
    return jsonify( { 'done': True } )

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
