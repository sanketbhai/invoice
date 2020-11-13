from flask import Flask ,render_template,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///trail.db'

db=SQLAlchemy(app)

class login(db.Model):
	
	username=db.Column(db.String(20),nullable=False,unique=True,primary_key=True)
	password=db.Column(db.String(20),nullable=False)
	invoice=db.relationship("Invoice",backref='person')



class Invoice(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    invonum=db.Column(db.Integer,nullable=False)
    
    price=db.Column(db.Integer,nullable=False)
    
    user=db.Column(db.String(20),db.ForeignKey(login.username))
	

@app.route("/")
def Login():
	return "hello"


if  __name__ == "__main__":
	app.run()	