from __future__ import print_function
import tkinter as tk
from tkinter import  messagebox
from flask import Flask, flash, redirect, render_template, request, url_for
from taiga import TaigaAPI
import pdb
import sys
import pymysql
api = TaigaAPI()

api.auth(
    username='anurag.madhur',
    password='madhur@15'
)

root = tk.Tk()
root.withdraw()
pdb.set_trace()
new_project = api.projects
app = Flask(__name__)

db = pymysql.connect(host='localhost',database='users',user='root',password='madhur@9876',autocommit=True)
cur = db.cursor()
@app.route('/')
def index():
    return render_template('index.html')
#@app.route('/projectList', methods=['GET'],['POST'])
#def projectList():


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if (not request.form['username'])  or (not request.form['password']) :
            messagebox.showinfo("Title", "please enter username or password")
            return redirect(url_for('login'))

        cur.execute("Select * from Register where userName = '%s'" % (request.form["username" ]))

        data = cur.fetchone()
       # print(data)
        if not data:
            messagebox.showinfo("Title", "incorrect username")
            return redirect(url_for('login'))

        if not data[2] == request.form["password"]:
            messagebox.showinfo("Title", "incorrect password")
            return redirect(url_for('login'))

        return render_template('home.html')
    else:
        return render_template('login.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
       if request.method =='POST':
            uname = request.form.get("username")

            mail = request.form.get("email_Id")

            pas = request.form.get("password")

            cnpass = request.form.get("confirm_password")
            if pas == cnpass:
                print("=================================")

                cur.execute("INSERT INTO Register VALUES ('%s', '%s', '%s')" % (uname, mail, pas))
                db.commit()

                return render_template('home.html')
            else :
                print("password did not match")


       else:
            return render_template('register.html')

@app.route('/Projects')
def Projects():
    return render_template('projectList.html')
if __name__ == "__main__":
    app.run()
