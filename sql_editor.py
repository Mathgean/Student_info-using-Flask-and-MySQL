from flask import Flask, url_for, render_template, redirect, request, flash
from flask_mysqldb import MySQL

web = Flask(__name__)

web.config["MYSQL_HOST"] = "localhost"
web.config["MYSQL_USER"] = "root"
web.config["MYSQL_PASSWORD"] = "MAgi!1729"
web.config["MYSQL_DB"] = "first"
web.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(web)


@web.route('/')
def home():
    con = mysql.connection.cursor()
    sql = "select * from student;"
    con.execute(sql)
    res = con.fetchall()
    return render_template("home.html", datas=res)


@web.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    con = mysql.connection.cursor()
    sql = "Delete from student where Reg_no = %s;"
    con.execute(sql, [id])
    mysql.connection.commit()
    con.close()
    flash("Data deleted")
    return redirect(url_for('home'))


@web.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        con = mysql.connection.cursor()
        sql = "insert into student (Name,Age,City) values (%s,%s,%s);"
        con.execute(sql, [name, age, city])
        mysql.connection.commit()
        con.close()
        flash("Data added")
        return redirect(url_for('home'))
    return render_template('add.html')



@web.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        con = mysql.connection.cursor()
        sql = "update student set Name = %s,Age = %s, City = %s where Reg_no = %s;"
        con.execute(sql, [name, age, city, id])
        mysql.connection.commit()
        con.close()
        flash("Data updated")
        return redirect(url_for('home'))
    con = mysql.connection.cursor()
    sql = "select * from student where Reg_no = %s;"
    con.execute(sql, [id])
    res = con.fetchone()
    return render_template('update.html', data=res)


if __name__ == "__main__":
    web.secret_key="s2k9d2"
    web.run(debug=True)
