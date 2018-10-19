from flask import Flask, request, redirect, render_template, send_file
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        try:
            given = request.form['someText']
            # someText = open("/c/Users/aerot/coding/saveFileTest/templates/sometext.txt", "w")
            someText = open("someText.txt", "w+")
            someText.write(given)
            someText.close()
            return redirect("/downloads")
        except Exception as e:
            return str(e)
            # return redirect("/return-files/")

        # except Exception as e:
        #     return str(e)
@app.route("/downloads")
def download():
    try:
        return send_file("someText.txt", as_attachment=True, attachment_filename='sometext.txt')
    except Exception as e:
            return str(e)
# @app.route('/return-files/')
# def return_files_tut():
# 	try:
# 		return send_file('/c/Users/aerot/coding/saveFileTest/templates/sometext.txt', attachment_filename='sometext.txt')
# 	except Exception as e:
# 		return str(e)

if __name__ == "__main__":
    app.run()