"""from flask import request
@app.route('/')
def index():
 user_agent = request.headers.get('User-Agent')
 return '<p>Your browser is {}</p>'.format(user_agent)"""


from flask import Flask
from flask import request
from flask import make_response

#Step 1
app = Flask(__name__)

"""@app.route('/')
def index():
 return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, {}!</h1>'.format(name)
"""
"""@app.route('/')
def badR():
 return '<h1>Bad Request</h1>', 400"""

"""@app.route('/')
def index():
 user_agent = request.headers.get('User-Agent')
 return '<p>Your browser is {}</p>'.format(user_agent)
"""
"""@app.route('/res/')
def index():
 response = make_response('<h1>This document carries a cookie!</h1>')
 response.set_cookie('answer', '42')
 return response"""

"""from flask import redirect
@app.route('/')
def index():
 return redirect('http://www.kaggle.com')

from flask import abort
@app.route('/user/<id>')
def get_user(id):
 user = load_user(id)
 if not user:
    abort(404)
 return '<h1>Hello, {}</h1>'.format(user)

def load_user(n):
    return n"""


#render template ------------------------

from flask import Flask, render_template
from datetime import datetime
# ...
"""@app.route('/')
def index():
 return render_template('index.html',
 current_time=datetime.utcnow())"""
@app.route('/user/<name>')
def user(name):
 return render_template('user.html', name=name)

from flask_bootstrap import Bootstrap
# ...
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500

from flask_moment import Moment
moment = Moment(app)


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
class NameForm(FlaskForm):
 name = StringField('What is your name?', validators=[DataRequired()])
 submit = SubmitField('Submit')

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
    

"""@app.route('/', methods=['GET', 'POST'])
def index():
 app = Flask(__name__)
 app.config['SECRET_KEY'] = SECRET_KEY
 name = None
 form = NameForm()
 if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
 return render_template('index.html', form=form, name=name)"""

from flask import Flask, render_template, session, redirect, url_for
from flask import flash
"""@app.route('/', methods=['GET', 'POST'])
def index():
 form = NameForm()
 if form.validate_on_submit():
  session['name'] = form.name.data
  return redirect(url_for('index'))
 return render_template('index.html', form=form, name=session.get('name'))"""

@app.route('/', methods=['GET', 'POST'])
def index():
 form = NameForm()
 if form.validate_on_submit():
  old_name = session.get('name')
  if old_name is not None and old_name != form.name.data:
   flash('Looks like you have changed your name!')
  session['name'] = form.name.data
  return redirect(url_for('index'))
 return render_template('index.html',
form = form, name = session.get('name'))
