
#flask imports
from flask import Flask, render_template, request, redirect, url_for, flash
import secrets

#set up flask app
app = Flask(__name__)

#set up secret key
app.secret_key = secrets.token_urlsafe(32)

#index route
@app.route('/')
def index():
    return render_template('index.html')

#designers route
@app.route('/designers')
def designers():
    return render_template('designers.html')

#projects route
@app.route('/projects')
def projects():
    return render_template('projects.html')

#marketplace route
@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

#submit project information route
@app.route('/submit_project', methods = ['POST'])
def submit_project():
    #get project info from form
    project_name = request.form.get('project_name')
    project_style = request.form.get('project_style')
    project_budget = request.form.get('project_budget')
    project_location = request.form.get('project_location')

    #store project information
    session['project_name'] = project_name
    session['project_style'] = project_style
    session['project_budget'] = project_budget
    session['project_location'] = project_location

    #match clients with designers
    designers = get_designers(project_style, project_location)

    #redirect to list of designers
    return redirect(url_for('designers'))

#get designers
def get_designers(style, location):
    #query database for designers
    designers = []
    #add designers to list
    #return list of designers
    return designers

#run the app
if __name__ == '__main__':
    app.run(debug=True)
