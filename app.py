# save this as app.py
from flask import Flask
from flask import request 
from flask import render_template
from flask import jsonify 
import json 

app = Flask(__name__)

@app.route("/")
def defaut():
    return render_template("template.html")

@app.route("/actualites", methods=['GET', 'POST'])
def commentaire():
    if request.method == 'POST':
        nom = request.form['nom']
        commentaire = request.form['commentaire']

        comm = {
                'nom': nom,
                'commentaire': commentaire
        }
    
        json_data = json.dumps(comm)
        
        # Écriture des données dans un fichier JSON
        with open('static/donnees.json', 'w') as f:
            f.write(json_data)

        return actualites()
    else:
        return actualites()



def actualites():
    f = open('static/concert.json')
    data = json.load(f)
    print(data)
    f.close()

    f1 = open('static/donnees.json')
    comm=json.load(f1)
    print(comm)
    f.close()
    return render_template("actualites.html", data=data ,comm=comm)


@app.route("/concert")
def concert():
    return render_template("concert.html")


@app.route("/actualites_jazz")
def actualites_jazz():
    return render_template("actualites_jazz.html")


@app.route("/actualites_rock")
def actualites_rock():
    return render_template("actualites_rock.html")


@app.route("/actualites_electro")
def actualites_electro():
    return render_template("actualites_electro.html")