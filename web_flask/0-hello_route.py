#!/usr/bin/python3
'''starts a script'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''displays a message'''
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')