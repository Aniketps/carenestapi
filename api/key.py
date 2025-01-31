from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/test", methods=["GET"])
def test():
    return jsonify({
        "response" : "Success"
    })

@app.route("/key", methods=["GET"])
def key():
    return jsonify({
        "response" : "Finished"
    })
    
if __name__ == "__main__":
    app.run()