from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def ReturnImage():
    img = request.args.get('p')
    path = f"/static/cdn/{img}.png"

    return render_template('index.html', image=path)

@app.errorhandler(404)
def _404Handler(err):
    return err

if __name__ == "__main__":
    app.run()