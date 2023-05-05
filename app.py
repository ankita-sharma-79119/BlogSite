import datetime
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from model.blog_entry import Blog_Entry
from pymongo import MongoClient

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.blog_site

    entries = []

    @app.context_processor
    def add_update_list_method():
        def update_article_list():
            article_count = app.db.entries.count_documents({})
            if article_count != len(entries):
                for en in app.db.entries.find({}):
                    entries.append(Blog_Entry.db_map_entry(en))
            return ""
        return {"update_article_list" : update_article_list}

    @app.route("/", methods=["GET", "POST"])
    def main_page():
        if request.method == "POST":
            entry_title = request.form.get("title")
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today()
            entry = Blog_Entry(entry_title,
                            entry_content, 
                            formatted_date.strftime("%Y-%m-%d"), 
                            formatted_date.strftime("%b %d"),
                            datetime.datetime.now()
                            )
            entries.append(entry)
            app.db.entries.insert_one(entry.db_insert_entry())
        return render_template("index.html", entries=entries)
    
    @app.route("/add", methods=["GET", "POST"])
    def article_page():
        if request.method == "POST":
            entry_title = request.form.get("title")
            entry_author = request.form.get("author")
            entry_image = request.form.get("image")
            entry_image_alt = request.form.get("image_alt")
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today()
            entry = Blog_Entry(entry_title,
                            entry_author, 
                            formatted_date.strftime("%Y-%m-%d"), 
                            formatted_date.strftime("%b %d"),
                            entry_image,
                            entry_image_alt,
                            entry_content
                            )
            entries.append(entry)
            app.db.entries.insert_one(entry.db_insert_entry())
        return render_template("add_article.html", entries=entries)
    
    return app
