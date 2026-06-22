from flask import Flask, request, jsonify
from flask_cors import CORS

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

import sqlite3

from auth import encrypt_password, verify_password


app = Flask(__name__)

CORS(app)


app.config["JWT_SECRET_KEY"] = "blog_secret_key"

jwt = JWTManager(app)



# Home Route

@app.route("/")
def home():

    return jsonify(
        {
            "message":"Blog Platform Backend Running"
        }
    )



# -------------------------
# USER REGISTER
# -------------------------

@app.route("/register", methods=["POST"])
def register():

    data=request.json


    username=data["username"]

    email=data["email"]

    password=encrypt_password(
        data["password"]
    )


    connection=sqlite3.connect(
        "blog.db"
    )

    cursor=connection.cursor()


    try:

        cursor.execute(
        """
        INSERT INTO users
        (username,email,password)
        VALUES(?,?,?)
        """,
        (
            username,
            email,
            password
        )
        )


        connection.commit()


        return jsonify(
            {
                "message":"User registered successfully"
            }
        )


    except:

        return jsonify(
            {
                "message":"Email already exists"
            }
        )


    finally:

        connection.close()





# -------------------------
# USER LOGIN
# -------------------------

@app.route("/login", methods=["POST"])
def login():

    data=request.json


    email=data["email"]

    password=data["password"]



    connection=sqlite3.connect(
        "blog.db"
    )

    cursor=connection.cursor()



    cursor.execute(
    """
    SELECT * FROM users
    WHERE email=?
    """,
    (email,)
    )


    user=cursor.fetchone()


    connection.close()



    if user and verify_password(
        password,
        user[3]
    ):


        token=create_access_token(
            identity=user[0]
        )


        return jsonify(
            {
                "token":token
            }
        )


    return jsonify(
        {
            "message":"Invalid credentials"
        }
    )





# -------------------------
# CREATE POST
# -------------------------

@app.route("/posts", methods=["POST"])
@jwt_required()
def create_post():


    user_id=get_jwt_identity()


    data=request.json


    connection=sqlite3.connect(
        "blog.db"
    )

    cursor=connection.cursor()



    cursor.execute(
    """
    INSERT INTO posts
    (user_id,title,content)
    VALUES(?,?,?)
    """,
    (
        user_id,
        data["title"],
        data["content"]
    )
    )


    connection.commit()

    connection.close()


    return jsonify(
        {
            "message":"Post created"
        }
    )





# -------------------------
# GET ALL POSTS
# -------------------------

@app.route("/posts", methods=["GET"])
def get_posts():


    connection=sqlite3.connect(
        "blog.db"
    )

    cursor=connection.cursor()



    cursor.execute(
        "SELECT * FROM posts"
    )


    posts=cursor.fetchall()


    connection.close()


    return jsonify(posts)





# -------------------------
# UPDATE POST
# -------------------------

@app.route("/posts/<int:id>", methods=["PUT"])
@jwt_required()
def update_post(id):


    data=request.json


    connection=sqlite3.connect(
        "blog.db"
    )


    cursor=connection.cursor()



    cursor.execute(
    """
    UPDATE posts
    SET title=?,content=?
    WHERE id=?
    """,
    (
        data["title"],
        data["content"],
        id
    )
    )


    connection.commit()

    connection.close()



    return jsonify(
        {
            "message":"Post updated"
        }
    )






# -------------------------
# DELETE POST
# -------------------------

@app.route("/posts/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_post(id):


    connection=sqlite3.connect(
        "blog.db"
    )


    cursor=connection.cursor()



    cursor.execute(
    """
    DELETE FROM posts
    WHERE id=?
    """,
    (id,)
    )


    connection.commit()

    connection.close()


    return jsonify(
        {
            "message":"Post deleted"
        }
    )






# -------------------------
# ADD COMMENT
# -------------------------

@app.route("/comments", methods=["POST"])
@jwt_required()
def add_comment():


    user_id=get_jwt_identity()


    data=request.json



    connection=sqlite3.connect(
        "blog.db"
    )

    cursor=connection.cursor()



    cursor.execute(
    """
    INSERT INTO comments
    (post_id,user_id,comment)
    VALUES(?,?,?)
    """,
    (
        data["post_id"],
        user_id,
        data["comment"]
    )
    )


    connection.commit()

    connection.close()



    return jsonify(
        {
            "message":"Comment added"
        }
    )





# -------------------------
# GET COMMENTS
# -------------------------

@app.route("/comments/<int:post_id>", methods=["GET"])
def get_comments(post_id):


    connection=sqlite3.connect(
        "blog.db"
    )


    cursor=connection.cursor()



    cursor.execute(
    """
    SELECT * FROM comments
    WHERE post_id=?
    """,
    (post_id,)
    )


    comments=cursor.fetchall()


    connection.close()


    return jsonify(comments)





if __name__=="__main__":

    app.run(debug=True)
