# Project Title

Flask Stripe demo

## Getting Started

Setup virtual environment


## Development Notes

cd /mnt/g/2020_working/coding/flask_stripe_demo

conda deactivate
which python3
python3 --version
python3 -m venv env
source env/bin/activate
(env)$ which python3
(env)$ python3 --version
(env)$ pip install flask
(env)$ pip freeze


add basic json hello world
https://github.com/aspiringguru/flaskStripeDemo/tree/471897185404c2d5c0c0cb92cc997f911642c785

- for reference. do not use production mode.
- $export FLASK_ENV=production   
$export FLASK_ENV=development
$printenv | grep FLASK

pip install stripe

login stripe, get keys
https://dashboard.stripe.com/test/apikeys

export STRIPE_PUBLISHABLE_KEY=<YOUR_STRIPE_PUBLISHABLE_KEY>
export STRIPE_SECRET_KEY=<YOUR_STRIPE_SECRET_KEY>

add python code to retrieve stripe keys and create stripe object
https://github.com/aspiringguru/flaskStripeDemo/tree/0f1d88fc16973402f3db09bb70f2018d6f31843f


https://stripe.com/au/payments/checkout
add templates/charge.html & @app.route('/charge', methods=['POST']) to app.py
http://127.0.0.1:5000
use the test card details
https://stripe.com/docs/testing#cards
visit stripe dashboard to see results.
https://dashboard.stripe.com/test/payments

"wip, added simple charge form and process charge to credit card."
https://github.com/aspiringguru/flaskStripeDemo/tree/69c3d9827bd5c831bd77864216a2dc27fcc0ffa1


"wip, added error page for strip api errors."
https://github.com/aspiringguru/flaskStripeDemo/tree/a6c93bce63e5de01d18e15a5ed961211f72cac69

"wip, added styling & customize logo."
https://github.com/aspiringguru/flaskStripeDemo/tree/d5d29ab912b8603844fe3f6dc3d0a93894faf2e6

https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

nb error messages during stripe checkout.
A cookie associated with a cross-site resource at http://checkout.stripe.com/ was set without the `SameSite`
error: {type: "invalid_request", message: "Unable to perform color detection."}

"wip, added customisation, post purchase feedback and retrieved data"
https://github.com/aspiringguru/flaskStripeDemo/tree/506a2cc4ac6ffab379b8955452de9715d459e552


Add forms - test method in app_forms.py
pip install flask-wtf

pip freeze
certifi==2019.11.28
chardet==3.0.4
Click==7.0
Flask==1.1.1
Flask-WTF==0.14.2
idna==2.8
itsdangerous==1.1.0
Jinja2==2.11.1
MarkupSafe==1.1.1
pkg-resources==0.0.0
requests==2.22.0
stripe==2.42.0
urllib3==1.25.8
Werkzeug==0.16.1
WTForms==2.2.1




## Contributing

Contributions welcome

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

*
code based on this tutorial.
https://github.com/testdrivenio/flask-stripe-checkout
