import json
import re

from flask import Flask, request, render_template, send_from_directory
from functions import loading, found_posts_func

# Import Blueprints
from main.main import main_blueprint
from loader.loader import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Ограничиваем размер файла
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.errorhandler(413)
def page_not_found(e):
    return '<h1>Файл большеват!</h1><p>Найди поменьше, спасибо</p>', 413


# Registering Blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/search_page")
def search_page():
    return found_posts_func()


@app.route("/list")
def page_tag():
    pass


@app.route("/post_uploaded", methods=["POST"])
def page_post_upload():
    return loading('picture', 'content')


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()