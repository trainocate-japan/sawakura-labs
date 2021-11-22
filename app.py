from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import pymysql
import os

load_dotenv()
INITIAL_DB_HOST = 'initial-db'

app = Flask(__name__)


def get_connection(dbhost):
    conn = pymysql.connect(
        host=dbhost,
        db=os.getenv("db_name"),
        user=os.getenv("db_user"),
        password=os.getenv("db_password"),
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return conn


# コース一覧表示画面
@app.route("/")
def display_all_courses():
    dbhost = os.getenv('db_host')

    # 初回起動ならデータベースホストの設定画面へ
    if dbhost == INITIAL_DB_HOST:
        return render_template("dbhost_set.html")

    title = "トレノケート クラウドコース一覧"
    sql = "SELECT * FROM contents"

    try:
        connection = get_connection(dbhost)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            courses = cursor.fetchall()
    # テーブルが見つからなければデータベースホストの設定画面へ
    except pymysql.err.ProgrammingError as e:
        return render_template("dbhost_set.html")
    except pymysql.err.OperationalError as e:
        return render_template("dbhost_set.html")
    finally:
        cursor.close()
        connection.close()

    return render_template("index.html", title=title, courses=courses)


# データベースホスト設定画面
@app.route('/', methods=['POST'])
def set_db_host():
    dbhost = request.form.get("dbhost")
    os.environ['db_host'] = dbhost

    connection = get_connection(dbhost)
    create_table = "create table IF not exists contents (id INT(20) AUTO_INCREMENT PRIMARY KEY, course_code VARCHAR(16) NOT NULL, course_name VARCHAR(120) NOT NULL) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"
    with connection.cursor() as cursor:
        cursor.execute(create_table)
    contents = "INSERT INTO contents (id, course_code, course_name) VALUES (%s, %s, %s);"
    with connection.cursor() as cursor:
        cursor.execute(contents, (0, 'NFC0313G', 'クラウドコンピューティング概要'))
        cursor.execute(contents, (0, 'NFC0314G', 'ビジネスパーソンのためのクラウド入門'))
        cursor.execute(contents, (0, 'NFC0267G', 'クラウドアーキテクト・ファーストステップ'))
        cursor.execute(contents, (0, 'NFC0295G', '実践クラウドデザインパターン'))
        cursor.execute(contents, (0, 'NFC0477G', 'さわってわかるクラウド入門'))
    connection.commit()

    cursor.close()
    connection.close()
    return redirect(url_for('display_all_courses'))


if __name__ == '__main__':
    app.run(port=80, host="0.0.0.0", debug=False)
