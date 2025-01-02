from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    data = {'name': 'Nile', 'age': 25, 'salary': 90000}
    return render_template('index.html', data=data)


@app.route('/about')
def about():
    products = ['Laptop', 'Mobile', 'Tablet', 'Camera', 'Headphone']
    return render_template('about.html', products=products)


@app.route('/admin')
def profile():
    username = 'Nile'
    return render_template('admin.html', username=username)


@app.route('/contact')
def contact():
    fname = request.args.get('fname')
    details = request.args.get('details')
    return render_template('thankyou.html', data={'fname': fname, 'details': details})


if __name__ == '__main__':
    app.run(debug=True)
