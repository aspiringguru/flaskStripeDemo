import os
import stripe
from flask import Flask, jsonify, render_template, request

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

@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])


@app.route('/charge', methods=['POST'])
def charge():
    # amount in cents
    amount = 500
    customer = stripe.Customer.create(
        email='sample@customer.com',
        source=request.form['stripeToken']
    )
    stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )
    return render_template('charge.html', amount=amount)


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000)
