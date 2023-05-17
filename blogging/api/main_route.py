import datetime
import os
from bson import ObjectId
from flask import (
    render_template, 
    request, 
    Blueprint,
    current_app
)

from blogging.model.blog_entry import Blog_Entry
from blogging.utils.mongo_util import update_article_list_filtered

main_route = Blueprint("main_route", __name__, static_folder='static', template_folder='templates')

entries = []
LinkedIn = os.getenv("LINKEDIN_URI")
github = os.getenv("GITHUB_URI")
medium = os.getenv("MEDIUM_URI")

@main_route.context_processor
def add_update_list_method():
    def update_article_list():
        article_count = current_app.db.entries.count_documents({})
        if article_count != len(entries):
            entries.clear()
            for en in current_app.db.entries.find({}):
                entries.append(Blog_Entry.db_map_entry(en))
        return ""
    return {"update_article_list" : update_article_list}

@main_route.route("/", methods=["GET", "POST"])
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
        current_app.db.entries.insert_one(entry.db_insert_entry())
    return render_template("homepage.html", entries=entries, 
                            LinkedIn = LinkedIn, 
                            github=github, 
                            medium=medium)

@main_route.route("/add", methods=["GET", "POST"])
def add_article_page():
    if request.method == "POST":
        entry_title = request.form.get("title")
        entry_author = request.form.get("author")
        entry_image = request.form.get("image_link")
        entry_image_alt = request.form.get("image_alt")
        entry_content = request.form.get("content")
        formatted_date = datetime.date.today()
        str_formatted_date = formatted_date.strftime("%Y-%m-%d")

        entry = Blog_Entry(entry_title,
                        entry_author, 
                        datetime.datetime.strptime(str_formatted_date, "%Y-%m-%d"), 
                        formatted_date.strftime("%b %d"),
                        entry_image,
                        entry_image_alt,
                        entry_content
                        )
        entries.append(entry)
        current_app.db.entries.insert_one(entry.db_insert_entry())
    return render_template("add_article.html", entries=entries, 
                        LinkedIn=LinkedIn, github=github, 
                        medium=medium)

@main_route.route("/about", methods=["GET"])
def aboutme():
    return render_template("about.html", 
                        LinkedIn=LinkedIn, 
                        github=github, 
                        medium=medium)


@main_route.route("/blog", methods=["GET", "POST"])
def blog():
    filtered_entry = entries
    start_date="2023-01-01"
    end_date="2023-01-01"
    if request.method == "POST":
        start_date = request.form.get('filter_start')
        end_date = request.form.get('filter_end')
        filtered_entry = update_article_list_filtered(datetime.datetime.strptime(start_date, "%Y-%m-%d"), 
                                                    datetime.datetime.strptime(end_date, "%Y-%m-%d"))

    return render_template("blog.html", entries=filtered_entry,
                        LinkedIn=LinkedIn, 
                        github=github, 
                        medium=medium,
                        start_date=start_date,
                        end_date=end_date)

@main_route.route("/view/<string:id>")
def view_article(id):
    entry = list(current_app.db.entries.find({'_id': ObjectId(id)}))
    return render_template("view_article.html",
                           entry = Blog_Entry.db_map_entry(entry[0]),
                           LinkedIn=LinkedIn, 
                           github=github, 
                           medium=medium)