#!/usr/bin/env python
# encoding: utf-8

from . import wiki_b
from models import Wiki
from flask import request, redirect, render_template
from flask.ext.login import current_user


@wiki_b.route("/wiki/<string:wiki_url>", methods=["GET", "POST"])
def wiki(wiki_url):
    flag = not current_user.is_anonymous() or "None"
    print flag
    if request.method == "POST":
        title = wiki_url
        author = current_user.username or 'Anonymous'
        content = request.form["content"]
        wiki = Wiki(title=title,
                    author=author,
                    content=content)
        wiki.save()
        redirect("/wiki/"+title)
    try:
        item = Wiki.objects(title=wiki_url).order_by('-updated_at')[0]
    except:
        return render_template("/wiki/newpage.html",
                               wiki_url=wiki_url,
                               author=author)
    if wiki_url == str(item.title):
        return render_template('/wiki/wikipage.html',
                               flag=flag,
                               title=item.title,
                               content=item.content,
                               author=item.author,
                               created_at=item.created_at)


@wiki_b.route("/")
def index():
    return redirect("/wiki/home")
