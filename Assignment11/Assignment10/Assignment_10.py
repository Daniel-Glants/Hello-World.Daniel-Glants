from flask import Flask, Blueprint, render_template, url_for, request, session, redirect,jsonify
import mysql.connector


Assignment_10 = Blueprint('Assignment_10', __name__,
                          static_folder='static',
                          static_url_path='/Assignment_10',
                          template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='rootdaniel',
                                         database='web')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@Assignment_10.route('/delete_user', methods=['GET', 'POST'])
def delete():
    if request.method == "GET":
        user_id = request.args['id']
        query = "DELETE FROM users WHERE ID='%s';" % user_id
        interact_db(query, 'commit')
        return redirect('/Assignment_10')
    return render_template('Assignment_10.html')


@Assignment_10.route('/add_user', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        ID = request.form['id']
        query = "INSERT INTO users(ID, First_name, Last_name, Email) VALUES ('%s','%s','%s','%s')" %(ID, first_name, last_name, email)
        interact_db(query, query_type='commit')
    return redirect('/Assignment_10')

@Assignment_10.route('/update_user', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        ID = request.form['id']
        query = "update users set First_Name= '%s', Last_Name='%s' , Email='%s' where ID=%s" % (first_name, last_name, email, ID)
        interact_db(query, query_type='commit')
    return redirect('/Assignment_10')

@Assignment_10.route('/Assignment_10', methods=['GET', 'POST'])
def index():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('Assignment_10.html', users=query_result)


@Assignment_10.route('/assignment11/users')
def assignment11():
    if request.method == 'GET':
        query = "SELECT * FROM users;"
        query_result = interact_db(query=query, query_type='fetch')
        return jsonify({
                'success':'True',
                'data': query_result
            })
    else:
        return f'The method is: {request.method}'

@Assignment_10.route('/assignment11/users/selected', defaults={'some_user_id':3})
@Assignment_10.route('/assignment11/users/selected/<int:some_user_id>')
def get_use(some_user_id):
    if request.method == 'GET':
        query = "SELECT * FROM users WHERE id='%s';" % some_user_id
        query_result = interact_db(query=query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({
                'success':'False',
                'data':[]
            })
        else:
            return jsonify({
                'success':'True',
                'data': query_result
            })
    else:
        return f'The method is: {request.method}'


if __name__ == '__main__':
    Assignment_10.run()
