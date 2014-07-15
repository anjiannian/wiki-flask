#!/usr/bin/env python
# encoding: utf-8

from . import auth_b
from auth.models import User
from flask.ext.login import login_user, logout_user
from util import valid_username, valid_password, valid_email
from flask import flash, request, redirect, url_for, render_template


@auth_b.route("/login", methods=["GET", "POST"])
def login():
    c_user = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        is_correct = False
        try:
            c_user = User.objects.get(username=username)
            is_correct = c_user.verify_password(password)
            if is_correct:
                login_user(c_user)
                return redirect("/wiki/home")
        except:
            print(u"Username does not match the password")
    return render_template("/auth/login.html")


@auth_b.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth_b.login"))


@auth_b.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        verify = request.form["verify"]
        email = request.form["email"]

        if valid_username(username) and valid_password(password)\
                and valid_email(email) and password == verify:
                user = User(username=username, email=email)
                user.password = password
                for exist in User.objects(username=username):
                    if user.username == exist.username:
                        flash(u"Username or Email already exist!!")
                        return redirect("/login")
                for exist in User.objects(email=email):
                    if user.email == exist.email:
                        flash(u"Username or Email already exist!!")
                        return redirect("/login")
                user.save()
                login_user(user)
                return redirect("/wiki/home")
        else:
            flash(u"Invalid Username or Password or Email!!")
            return redirect("/signup")

    return render_template("/auth/signup.html")
