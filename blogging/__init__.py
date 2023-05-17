import os
from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient

from blogging.api.main_route import main_route

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.blog_site

    app.register_blueprint(main_route)

    return app
