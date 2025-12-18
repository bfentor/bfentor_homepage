from flask import render_template, Flask, redirect, send_file, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/github')
def github():
    return redirect("https://www.github.com/bfentor")
    # return render_template('github.html')


@app.route('/cv')
def cv():
    path = "static/Balazs_Fentor_CV.pdf"
    return send_file(path, as_attachment=False)

    # return render_template('cv.html')

# @app.route('/contact')
# def contact():
#     return render_template('get_in_touch.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)