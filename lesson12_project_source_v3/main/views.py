from flask import Flask, render_template, Blueprint, request
import json
import functions

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates_main")

@main_blueprint.route("/")
def main_page():
    return render_template("index.html")

@main_blueprint.route("/search/")
def search_page():
    search_query= request.args.get("s", '')
    posts = functions.get_posts_by_word(search_query)
    page = render_template("post_list.html", query = search_query, posts = posts)
    return page