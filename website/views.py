from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
     return render_template('home.html')

@views.route('/about')
def about():
     return render_template('about.html')

@views.route('/education')
def education():
     return render_template('education.html')     

@views.route('/skills')
def skills():
     return render_template('skills.html')   

@views.route('/projects')
def projects():
     return render_template('projects.html')

@views.route('/contact')
def contact():
     return render_template('contacts.html')
