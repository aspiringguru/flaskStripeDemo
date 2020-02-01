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





### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo




## Contributing

Contributions welcome

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

*
