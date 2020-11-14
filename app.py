from flask import Flask ,render_template,request,redirect,jsonify
import json
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sevenhills.db'

db=SQLAlchemy(app)

class login(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),nullable=False,unique=True)
	password=db.Column(db.String(20),nullable=False)
	email=db.Column(db.String(33),unique=True,nullable=False)
#	def __repr__(self):
#		return '<username%r,id%r>'%self.username,%self.id
#	def __str__(self):
		#return "%r %r"%(self.id,self.username)


class Invoice(db.Model):
    id_invo=db.Column(db.Integer,primary_key=True)
    user=db.Column(db.String(20),nullable=False)
    invonum=db.Column(db.Integer,nullable=False)
    product=db.Column(db.String(50), nullable=False  )
    price=db.Column(db.Integer,nullable=False)
    qty=db.Column(db.Integer,nullable=False)
    total=db.Column(db.Integer,nullable=False)
    provider=db.Column(db.String(50),nullable=False)
    provider_rep=db.Column(db.String(50),nullable=False)
    provider_info=db.Column(db.String(100),nullable=False)
    customer_name=db.Column(db.String(20),nullable=False )
    customer_address=db.Column(db.String(50),nullable=False )
    date=db.Column(db.String(20),nullable=False )
    
    
    
	

per=""
invoice_no=0

@app.route("/")
def Login():
	return render_template("register.html")
	
	
@app.route("/signup",methods=["POST","GET"])
def signup():
		return render_template("login.html")


@app.route("/addtodb",methods=["post"])
def addtodb():
		if request.form["registor"]=="registor":
		   uname=request.form["username"]
		   pas=request.form["password"]
		   rpassword=request.form["rpassword"]
		   Email=request.form["mail"]
		   print(uname)
		   print(pas)
		   if pas==rpassword:
		   	row=login(username=uname,password=pas,email=Email)
		   	try:
		   		db.session.add(row)
		   		
		   		db.session.commit()
		   		
		   		return redirect("/signup")
		   	except:
		   		return "username is taken try diffrent one or the email is already registored"
		   else:
		   	return "username and password do not match"
		
		   	
		   	
@app.route("/signin",methods=["POST","GET"])
def signin():
		 if request.method=='POST':
		 	 
			 iu=request.form['username']
			 ip=request.form['password']
			 a=login.query.filter_by(username=iu,password=ip).all()
			 global invoice_no
			 if not a:
		 		return 'account not exits'
			 else:
			     global per
			     per=iu
			     allrows=Invoice.query.filter(Invoice.user==per).all()
			     if len(allrows)==0:
			         invoice_no=1
			     else:
			         invoice_no=(allrows[-1].invonum)+1
			     return render_template("invoice.html",data=invoice_no,user=per)
		 
		   			
@app.route("/changepassword",methods=["POST","GET"])
def changepassword():
		   	if request.method=="POST":
		   		
		   		iu=request.form['username']
		   		ip=request.form['password']
		   		a=login.query.filter_by(username=iu).all()
		   		if not a:
		   		    return 'user dosenot exit'
		   		else:
		   		    login.query.filter_by(username=iu).update(dict(password=ip))
		   		    db.session.commit()
		   		    return render_template("login.html",mess='hello your password is updated please login')
		   	
		   	elif request.method=="GET":
		   		return render_template("changepss.html")	   		
		   	


@app.route("/store",methods=["POST","GET"])
def store():
    print("above json")
    dic=json.loads(request.args.get("dic"))
    print(dic['date'])
    global invoice_no,per
    results=Invoice.query.filter(Invoice.user==dic["user"]).filter(Invoice.invonum==invoice_no).all()
    if len(results)!=0:
        db.session.query(Invoice).filter(Invoice.user==per).filter(Invoice.invonum==invoice_no).delete()
        db.session.commit()
    
    for i in range(len(dic['qt'])):

        pro=dic['pro'][i]
        pri=dic["pri"][i]
        qt=dic["qt"][i]
        tot=dic["tot"][i]
        date=dic["date"]
        provider=dic["provider"]
        provider_rep=dic["provider_rep"]
        provider_info=dic["provider_info"]
        customer_name=dic["customer_name"]
        customer_address=dic["customer_address"]
        
        per=dic["user"]
        invoice_no=dic["invoice_no"]
        
        
    
        
        dbrow=Invoice(user=per,invonum=invoice_no,product=pro,price=pri,qty=qt,total=tot,provider=provider,provider_rep=provider_rep,provider_info=provider_info,customer_name=customer_name,customer_address=customer_address,date=date)
        db.session.add(dbrow)
        db.session.commit()
            
    
    
    
    return render_template("/invoice.html",user=int(invoice_no)+1)




@app.route("/show_invoice",methods=["Post","GET"])

def show_invoice():
    print(request.args.get("flag"))
    per=request.args.get("user")
    print(per)
    if request.args.get("flag")=='1':
        print("inside if")
        
        #created invo_no to store invoice no coming from show_invoice.html
        invo_no=int(request.args.get("num"))
        per=(request.args.get("user"))
        results=Invoice.query.filter(Invoice.user==per).filter(Invoice.invonum==invo_no).all()
    
        product=[]
        price=[]
        quntity=[]
        total=[]
        date=results[0].date
        provider=results[0].provider
        provider_rep=results[0].provider_rep
        provider_info=results[0].provider_info
        customer_name=results[0].customer_name
        customer_address=results[0].customer_address
        for result in results:
            product.append(result.product)
            price.append(result.price)
            quntity.append(result.qty)
            total.append(result.total)
        dic={ "pro":product,"pri":price, "qty":quntity,"tot":total,"date":date,"provider":provider,"provider_rep":provider_rep,"provider_info":provider_info,"customer_name":customer_name,"customer_address":customer_address}
        print("below for loop and dictonary")
        print(dic)
        return jsonify(dic)
    else:
        return render_template("showinvoice.html",data=per)
        
        
if  __name__ == "__main__":
	app.run(debug=True)	