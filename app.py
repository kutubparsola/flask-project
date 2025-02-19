from flask import Flask, render_template
app = Flask(__name__)

JOBS=[{
    "role":"data analyst",
    "place": "bengluru",
    "salary": "12,00,000"
},
{ "role":"data scientist",
    "place": "remote",
},      
{ "role":"pentester",
    "place": "delhi",
    "salary": "12,00,000"
},      
{ "role":"front-end developer",
    "place": "jaipur",
    "salary": "12,00,000"
}      
]   
@app.route("/")
def technozz():
    return render_template("jobs.html",jobs=JOBS)

if __name__=="__main__":
    app.run(debug=True,port=8000)