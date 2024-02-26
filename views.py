from flask import Flask, render_template, request

def load_database():
    file = open("account.txt")
    account = file.read.split(":")
    file.close()
    database = {}

    for line in account:
        username, password = line.read.split(":")
        database[username] = password

    return database

def create_new_user(username, password):
    file = open("account.txt")
    
    variable = str(username + " : " + password + "\n")  
    
    file.write("{username}:{password}\n")

app = Flask(__name__)
result = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/accueil", methods=['POST'])
def accueil():
    global result
    result = request.form
    return render_template("accueil.html", name = result['name'])

@app.route("/commande", methods=['POST'])
def commande():
    global result
    return render_template("commande.html", name = result['name'])

@app.route("/paiement", methods=["POST"])
def paiement():
    global result
    return render_template("paiement.html", name = result['name'])

app.run(debug=True)