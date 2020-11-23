from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
    <h1>This is a web page from flask!!</h1>
    </html>
    """

@app.route('/random')
def get_random():
    number = random.randrange(100)
    name = "Joe"
    dict_data = {'color':'red','shape':'triangle'}
    l_data = ["one",'two','three']
    return render_template('random_template.html',number = number, n = name,
                           d = dict_data, l = l_data)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
