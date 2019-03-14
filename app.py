from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index') 
def index():
    return render_template('index.html')

@app.route('/products') 
def products():
    return render_template('products.html')

@app.route('/registered') 
def registered():
    return render_template('registered.html')

@app.route('/login') 
def login():
    return render_template('login.html')


@app.route('/contact') 
def contact():
    return render_template('contact.html')

@app.route('/about') 
def about():
    return render_template('about.html')

@app.route('/categories') 
def categories():
    return render_template('categories.html')

@app.route('/makeups') 
def makeups():
    return render_template('makeups.html')

@app.route('/skincare') 
def skincare():
    return render_template('skincare.html')

@app.route('/bodyscents') 
def bodyscents():
    return render_template('bodyscents.html')

@app.route('/offers') 
def offers():
    return render_template('offers.html')

@app.route('/single') 
def single():
    return render_template('single.html')

@app.route('/java') 
def java():
    return render_template('java.java')

@app.route('/javascript') 
def javascript():
    return render_template('javascript.html')




if __name__ == '__main__':
    app.run(debug=True)
    