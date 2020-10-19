# Import Packages
from flask import Flask, jsonify, request, Blueprint
from bs4 import BeautifulSoup
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import requests
from webscrapping import get_ips
import logging as logger

# Log Config
logger.basicConfig(
    filename="log.log",
    level="DEBUG",
    filemode="w",
    format="%(asctime)s:%(levelname)s:%(message)s",
)

# Init App
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

# Define database
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50), nullable=False, unique=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


# Define Marshmallow Schema
class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "ip")


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class PostsResource(Resource):
    def get(self):
        logger.debug("Get Method")
        return jsonify(posts_schema.dump(Post.query.all()))

    def post(self):
        data = request.get_json
        post = Post(ip=data["ip"])

        db.session.add(post)
        db.session.commit()

        # 		logger.debug(f'{post_schema.dump(post)}')
        logger.debug("Post Method")
        return post_schema.dump(post)

        def put(self):
            data = request.get_json()
            post = Post.query.filter()

            if "ip" in data:
                post.ip = data["ip"]

            db.session.update(post)
            db.session.commit()
            logger.debug("Put Method")
            return post_schema.dump(post)

        def delete(self):
            data = request.get_json()
            post = Post(ip=data["ip"])
            post = Post.query.filter(ip="id")

            if "ip" in data:
                post.id = data["ip"]

            db.session.delete(post)
            db.session.commit()
            logger.debug("Delete Method")
            return post_schema.dump(post)


class PostResource(Resource):
    def get(self):
        ips = get_ips()
        return ips

        # result = requests.get("https://www.dan.me.uk/torlist/")
        # src = result.content
        # soup = BeautifulSoup(src, "lxml")
        # print(soup.p.text)

        # logger.debug("Get Method")
        # return jsonify(post_schema.dump(Post.query.get_or_404(id)))
        # return jsonify(post_schema.dump(Post.query.get_or_404(id)))
        m  # essage = f"Hello{ip}"
        # return {"message": message}
        # print(message)


api.add_resource(PostsResource, "/api")
api.add_resource(PostResource, "/torlist")

if __name__ == "__main__":
    logger.debug("Starting the application")
    app.run(host="0.0.0.0", port=5001, debug=True, use_reloader=True)
