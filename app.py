from flask import Flask, render_template
from dotenv import load_dotenv
import pymysql
import os

load_dotenv()

app = Flask(__name__)


def get_connection():
    conn = pymysql.connect(
        host=os.getenv("db_host"),
        db=os.getenv("db_name"),
        user=os.getenv("db_user"),
        password=os.getenv("db_password"),
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return conn


@app.route("/")
def display_all_courses():
    title = "トレノケート クラウドコース一覧"
    connection = get_connection()

    sql = "SELECT * FROM contents"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            courses = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

    return render_template("index.html", title=title, courses=courses)
