from flask import Flask, request, render_template, redirect, url_for, jsonify
from repository.grosery_main import read_csv_to_dict, write_list_of_dicts_to_csv

app = Flask(__name__)
data = read_csv_to_dict('sample_grocery.csv')

@app.route("/")
def welcome():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

     
        if username and username[0].isupper() and username[1:].islower() and any(c.isalpha() for c in password) and any(c.isdigit() for c in password):
            return redirect(url_for("login_success"))

    return render_template("login.html")

@app.route("/items", methods = ["GET"]) #http://localhost:5000/items
def items():
    return jsonify(data)

@app.route("/items/<SKU>", methods = ["GET"]) #http://localhost:5000/items/A123
def items_SKU(SKU):
    items = items_SKU(SKU)
    if items is None:
        return jsonify({})
    else:
        return jsonify({"SKU":items["SKU"], "Price":items["Price"]})
    
def items_SKU(SKU): 
    for items in data: 
        if items["SKU"] == SKU:
            return items
        return None
    
@app.route("/items", methods=["POST"])  #http://localhost:5000/items ------------------ Abre una segunda terminal y escribe: Invoke-WebRequest -Method Post -Uri "http://localhost:5000/items" -ContentType "application/json" -Body '{"SKU": "5802", "Name": "Luz Karen", "Description": "Alumna", "Price": 1.00, "Quantity": 10, "Expiration Date": "2024-03-18"}'
def add_item():
    new_item = request.json
    data.append(new_item)
    write_list_of_dicts_to_csv('sample_grocery.csv', data)
    return jsonify(new_item), 201

@app.route("/items/<SKU>", methods=["DELETE"]) #http://localhost:5000/items ----------------------- Abre una segunda terminal y escribe  Invoke-WebRequest -Method Delete -Uri "http://localhost:5000/items/A123"
def delete_item(SKU):
    global data
    data = [item for item in data if item["SKU"] != SKU]
    write_list_of_dicts_to_csv('sample_grocery.csv', data)
    return '', 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
