import datetime
from flask import Flask, render_template, request
from model.blog_entry import Blog_Entry
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://m001-student:m001-student@cluster0.0rlwa8b.mongodb.net/test")
    app.db = client.blog_site

    entries = []

    @app.route("/", methods=["GET", "POST"])
    def main_page():
        if len(entries) == 0:
            for en in app.db.entries.find({}):
                entries.append(Blog_Entry.db_map_entry(en))

        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today()
            entry = Blog_Entry(entry_content[:30],
                            entry_content, 
                            formatted_date.strftime("%Y-%m-%d"), 
                            formatted_date.strftime("%b %d")
                            )
            entries.append(entry)
            app.db.entries.insert_one(entry.db_insert_entry())
        return render_template("index.html", entries=entries)
    
    return app
