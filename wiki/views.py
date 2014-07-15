#!/usr/bin/env python
# encoding: utf-8

from . import wiki_b
from models import Wiki
from flask import request, redirect, render_template
from flask.ext.login import current_user, login_required


@wiki_b.route("/wiki/<string:wiki_url>", methods=["GET", "POST"])
def echo_wiki(wiki_url):
    flag = not current_user.is_anonymous() or "None"
    try:
        item = Wiki.objects(title=wiki_url).order_by('-updated_at')[0]
    except:
        return redirect("/edit/"+wiki_url)

    if request.method == "POST":
        return render_template('/wiki/edit_page.html',
                               flag=flag,
                               title=item.title,
                               content=item.content,
                               author=item.author)

    elif request.method == "GET":
        return render_template('/wiki/wiki_page.html',
                               flag=flag,
                               title=item.title,
                               content=item.content,
                               author=item.author,
                               created_at=item.created_at)



@wiki_b.route("/edit/<string:wiki_url>", methods=["GET", "POST"])
@login_required
def edit_wiki(wiki_url):
    title = wiki_url
    author = current_user.username or 'Anonymous'
    if request.method == "POST":
        content = request.form["content"]
        wiki = Wiki(title=title,
                    author=author,
                    content=content)
        wiki.save()
        return redirect("/wiki"+title)
    return render_template("/wiki/edit_page.html",
                           title=title,
                           author=author)

@wiki_b.route("/")
def index():
    return redirect("/wiki/home")
