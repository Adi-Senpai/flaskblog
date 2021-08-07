from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
import os
from flask_mail import Mail
from werkzeug.utils import secure_filename
import math
with open('config.json','r') as c:
    params=json.load(c)["params"]
local_server=True
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER']=params['upload_location']
app.config.update()
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]


db = SQLAlchemy(app)

class Contact(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phno = db.Column(db.String(12), unique=True, nullable=False)
    mes = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow,nullable=True)

class Posts(db.Model):
    
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow,nullable=True)



@app.route("/")
def home():
    post=Posts.query.filter_by().all()
    last=math.ceil(len(post)/1)
    
    page=request.args.get("page")


    if not str(page).isnumeric():
        page=1
    page=int(page)
    post=post[(page-1)*1: (page-1)*1+1]
    if page==1:
        prev="#"
        next="/?page="+str(page+1)
    elif page==last:
        next="#"
        prev="/?page="+str(page-1)
    else:
        prev="/?page="+str(page-1)
        next="/?page="+str(page+1)
    
    return render_template("index.html",params=params,post=post,prev=prev,next=next)
@app.route("/about")
def about():
    return render_template("about.html",params=params)
    
@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    if 'user' in session and session["user"]==params["username"]:
        post=Posts.query.all()
        return render_template("dashboard.html",params=params,post=post)
    
    
    if request.method=="POST":
        if params["username"]==request.form['email'] and params["passwd"]==request.form["passwd"]:
            session["user"]=params["username"]
            post=Posts.query.all()
            return render_template("dashboard.html",params=params,post=post)
    
    return render_template("login.html",params=params)
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect("/dashboard")
@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phno=request.form['phone']
        mes=request.form['message']
        name=request.form['name']
        entry=Contact(name=name,phno=phno,mes=mes,email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html",params=params)
@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post=Posts.query.filter_by(slug=post_slug).first()

    return render_template("post.html",params=params,post=post)
@app.route("/edit/<string:sno>",methods=['GET','POST'])
def edit(sno):
    if 'user' in session and session["user"]==params["username"]:
        if request.method=="POST":
            box_title=request.form['title']
            box_slug=request.form['slug']
            box_content=request.form['content']
            date = datetime.now()
            if sno=='0':
                post=Posts(title=box_title,slug=box_slug,content=box_content,date=date)
                db.session.add(post)
                db.session.commit()
        
            else:
                post=Posts.query.filter_by(sno=sno).first()
                post.title=box_title
                post.slug=box_slug
                post.content=box_content
                db.session.commit()
                return redirect('/edit/'+sno)
        post=Posts.query.filter_by(sno=sno).first()
        return render_template("edit.html",params=params,post=post)
@app.route("/delete/<string:sno>",methods=['GET','POST'])
def delete(sno):
    if 'user' in session and session["user"]==params["username"]:
        post=Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect("/dashboard")


@app.route("/uploader",methods=['GET','POST'])
def uploader():
    if 'user' in session and session["user"]==params["username"]:
        if request.method=="POST":
            f=request.files["file1"]
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            return"upload successful"





app.run(debug=True,port="100")