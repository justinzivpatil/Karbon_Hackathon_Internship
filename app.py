from flask import Flask, render_template, request, redirect, url_for
import json
from model import probe_model_5l_profit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            # Load the uploaded JSON file
            data = json.load(file)
            # Process the data using the model
            result = probe_model_5l_profit(data["data"])
            # Pass the result to the result page
            return redirect(url_for("result", result=json.dumps(result)))
    return render_template("upload.html")

@app.route("/result")
def result():
    result = request.args.get("result")
    result = json.loads(result)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
