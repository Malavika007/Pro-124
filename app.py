from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        "id":1,
        "Contact":"9988776655",
        "Name":"Tony",
        "done":False,

    },
    {
        "id":2,
        "Contact":"1944776685",
        "Name":"Pepper",
        "done":False,

    }
]

@app.route('/')

def hello_world():
    return 'hello world'

@app.route("/app-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        }, 400)

    Data = {
        'id': data[-1]['id'] + 1,
        'Contact': request.json['Contact'],
        'Name': request.json.get('Name', ""),
        'done': False
    }
    data.append(Data)
    return jsonify({
        "status":"success",
        "message":"Data added "
    })

@app.route("/get-data")
def get_data():
    return jsonify({
        "data":data
    })

if (__name__ == "__main__"):
    app.run(debug=True)