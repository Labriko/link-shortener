from flask import Flask, render_template, redirect, request
app = Flask(__name__)

import string
import random
def link_generator(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

from data import saved_links

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/new_link", methods=["POST"])
def new_link():
    link = request.form['input_link']
    short_link = link_generator()
    saved_links[short_link] = link
    return render_template('link.html', link=short_link)

@app.route('/<link_id>')
def red(link_id):
    return redirect(saved_links[link_id])


if __name__ == '__main__':
    app.run(debug=True)
