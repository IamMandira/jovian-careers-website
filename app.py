from flask import Flask,render_template,jsonify
app=Flask(__name__)
JOBS=[
    {
    'id':'1',
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary': 'Rs.100000/-'
    },
    {
    'id':'2',
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary': 'Rs.120000/-'
    },
    {
    'id':'3',
    'title':'Full stack developer',
    'location':'Hyderabad, India',
    'salary': 'Rs.90000/-'
    },
    {
    'id':'4',
    'title':'Backend developer',
    'location':'Remote',
    'salary': 'Rs.105000/-'
    }
   
]
@app.route('/')
def hello():
    return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route('/api/jobs')
def listjobs():
    return jsonify(JOBS)
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)