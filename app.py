from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

blogs = [
    {
        "id": 1,
        "title": "a blog 1",
        "description": "some description 1"
    },
    {
        "id": 2,
        "title": "some blog 2",
        "description": "some description 2"
    },
    {
        "id": 3,
        "title": "some blog 3",
        "description": "some description 3"
    }
]


@app.route('/api/v1.0/get-blogs', methods=["GET"])
def getAllBlogs():
    return jsonify({'blogs': blogs})


@app.route('/api/v1.0/blog/<int:id>', methods=["GET"])
def getBlogByID(id):
    blog = [blog for blog in blogs if blog["id"] == id]
    if len(blog) == 0:  # blog not found
        abort(400)
    return jsonify({"blog": blog[0]})


@app.route("/api/v1.0/blog/<string:keyword>")
def getBlogsByKeyword(keyword):
    blog = [blog for blog in blogs if keyword in blog["title"]]
    if len(blog) == 0:  # blog not found
        abort(400)
    return jsonify({"blogs": blog}) # list of blogs


@app.errorhandler(404)
def nodFound(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(debug=True)
