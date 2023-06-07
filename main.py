# Copyright 2023 Copy05. All rights reserved

import os
import Tags
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def ReturnHome():
    images = os.listdir('static/cdn')
    imgs = [f"static/cdn/{name}" for name in images]

    return render_template('index.html', images=imgs)

@app.route("/p")
def ReturnImage():
    img = request.args.get('p').lower()
    path = f"/static/cdn/{img}.png"
    tags = Tags.Tags.get(int(img), [])
    copyrightfield = Tags.Copyright.get(int(img), [])

    return render_template('img.html', image=path, Tags=tags, Copyright=copyrightfield[0])

@app.route("/t")
def ReturnTaggedImage():
    tags = request.args.get('tags').lower()
    Tag = {name: tags_list + copyright_list for name, tags_list in Tags.Tags.items() for name2, copyright_list in Tags.Copyright.items() if name == name2}
    filtered_images = [(name, f"/static/cdn/{name}.png") for name, image_tags in Tag.items() if all(tag in image_tags for tag in tags.split(","))]

    return render_template('imglist.html', images=filtered_images, Tag=tags)

@app.errorhandler(404)
def _404Handler(err):
    return err

if __name__ == "__main__":
    app.run()