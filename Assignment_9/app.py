from flask import Flask, render_template, url_for, request, session, redirect

app = Flask(__name__)


@app.route('/')
def main_cv():
    return render_template('CV.html')


@app.route('/Contacts')
def contacts():
    return render_template('Contacts.html')


@app.route('/Assignment9', methods=['GET', 'POST'])
def ass_9():
    if request.method == 'GET':
        res = ''
        list = []
        users = ['Michael Lawson', 'Lindsay Ferguson', 'Tobias Funke', 'Byron Fields', 'George Edwards', 'Rachel Howell']
        emails = {'Michael Lawson': 'michael.lawson@reqres.in',
                  'Lindsay Ferguson': 'lindsay.ferguson@reqres.in',
                  'Tobias Funke': 'tobias.funke@reqres.in',
                  'Byron Fields': 'byron.fields@reqres.in',
                  'George Edwards': 'george.edwards@reqres.in',
                  'Rachel Howell': 'rachel.howell@reqres.in'}
        if 'name' in request.args:
            res = request.args['name']
            answer_U = [i for i in users if res in i]
            for v in answer_U:
                list.append(emails[str(v)])
            return render_template('assignment9.html', name=answer_U, email=list)
    if request.method == 'POST':
        return render_template('assignment9.html', session='TRUE', username = 'name')
    return render_template('assignment9.html')



if __name__ == '__main__':
    app.run()
