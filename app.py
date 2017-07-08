import os
import uuid
import logging
import json
import helpers
import boto3
from flask import Flask, request, session, g, redirect, url_for, abort
from flask import render_template, flash, jsonify

app = Flask(__name__)

# pylint: disable=C0103,E1101
secrets_dict = helpers.parse_json_config(
    os.path.join(app.root_path, 'veganolia_config.json'))

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY=secrets_dict['secret_key'],
    USERNAME=secrets_dict['username'],
    PASSWORD=secrets_dict['password']
))

@app.route('/')
def index():
    return render_template('index.html', entries=items)

if __name__ == '__main__':
    # The following code only gets executed when the app is run locally
    # on the host. NOT inside of docker.
    app.debug = True
    app.run()
