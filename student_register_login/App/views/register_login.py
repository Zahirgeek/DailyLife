from flask import Blueprint, request, render_template, redirect, url_for, flash

from App.ext import db
from App.models import Student

blue = Blueprint("blue", __name__,url_prefix="/student")

@blue.route("/register/", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("student_register.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        student = Student()
        student.s_name = username
        student.s_password = password

        db.session.add(student)
        db.session.commit()

        return redirect(url_for("blue.login"))

@blue.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("student_login.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        student = Student.query.filter(Student.s_name.__eq__(username)).first()

        if student and student.check_passwd(password):
            return "Login success"

        flash("用户名或密码错误")
        return redirect(url_for("blue.login"))