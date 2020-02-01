import os
import stripe
from flask import Flask, jsonify

app = Flask(__name__)

stripe_keys = {
  'secret_key': os.environ['STRIPE_SECRET_KEY'],
  'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}
print("stripe_keys:",stripe_keys)

stripe.api_key = stripe_keys['secret_key']

@app.route('/hello')
def hello_world():
    return jsonify('hello, world!')


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000)
