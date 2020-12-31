from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/assignment8')
def index_2():

    return render_template('assignment8.html', premision = 'TRUE',movies=['Independents Day','Man in black','Pineapple Express'])

@app.route('/')
def cv_main():
    return render_template('CV.html')



if __name__ == '__main__':
    app.run(debug=True)
