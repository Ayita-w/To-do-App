from flask import Flask, render_template , request ,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///Todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


class Todo(db.Model):
    SNo=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.SNo} - {self.title}"      

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title=(request.form['title'])
        desc=(request.form['desc'])
        todo=Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    allTodo=Todo.query.all()
    return render_template('index.html',allTodo=allTodo)
    # return "<p>Hello World!</p>"

@app.route("/Show")
def About():
    allTodo=Todo.query.all()
    print(allTodo)
    return "<p>This is About Page </p> " # for multiple pages we can create like this 

@app.route("/update/<int:SNo>",methods=['GET','POST'])
def update(SNo):
    if request.method=='POST':
          title=(request.form['title'])
          desc=(request.form['desc'])
          todo=Todo.query.filter_by(SNo=SNo).first()
          todo.title=title
          todo.desc=desc
          db.session.add(todo)
          db.session.commit()
          return redirect("/")
    todo=Todo.query.filter_by(SNo=SNo).first()
          
          
    return render_template('update.html',todo=todo,SNo=SNo)

     # for multiple pages we can create like this 

@app.route("/delete/<int:SNo>")
def delete(SNo):
    todo=Todo.query.filter_by(SNo=SNo).first()
    db.session.delete(todo)
    db.session.commit()
    
    return redirect("/") # for multiple pages we can create like this 
 

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) # can change the port  port:4000
    
#static directory me mojud koi b file as it is open krne k kam aati koi b file ho.
   # tempelates basically for source file like view page source. # jinja 2 is an templetic engine.
   