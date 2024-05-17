# save this as app.py
from flask import Flask
from flask import request 
from flask import render_template
from flask import jsonify 
import json 
from flask import session 
from flask import url_for, redirect 


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]'

@app.route("/")
def index():
    return login()

@app.route("/login", methods=['GET', 'POST'])
def login():
    """ Permet de se connecter """
    if request.method == 'POST':
        session['username'] = request.form['username']
        return render_template("actualites.html")
    return '''
    <form action="/login" method="post">
        <p><input requiered placeholder=username type=text name=username>
        <p><input requiered placeholder=password type=text name=password>
        <p><input type=submit value=Connexion>
    </form>

    '''
@app.route("/logout", methods=['GET', 'POST'])
def logout():
    """ Permet de se déconnecter (enlève le nom d'utilisateur de la session)""" 
    session.pop('username', None)
    return render_template("actualites.html")


@app.route("/ajout_actu", methods=['GET', 'POST'])
def ajout_actu():
    if request.method == 'POST':
        nom = request.form['nom']
        date = request.form['date']
        description = request.form['description']

        ajoutactu =  {
                'nom': nom,
                'date': date,
                'description' : description
        }
            
        json_data = json.dumps(ajoutactu)
        
     # Écriture des données dans un fichier JSON
        with open('static/actu.json', 'w') as f:
            f.write(json_data)

        return actualites()
    else:
        return render_template("ajout_actu.html")



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

    f1 = open('static/donnees.json')
    comm=json.load(f1)
    print(comm)
    f1.close()

    f2 = open('static/actu.json')
    ajoutactu = json.load(f2)
    print(ajoutactu)
    f2.close()
    return render_template("actualites.html", comm=comm, ajoutactu=ajoutactu )


@app.route("/ajout_concert", methods=['GET', 'POST'])
def ajout_concert():
    if request.method == 'POST':
        date = request.form['date']
        lieu = request.form['lieu']
        nom = request.form['nom']


        ajoutconcert =  {
                'date': date,
                'lieu': lieu,
                'nom' : nom
        }
        dataconcert = lire_concert()
        
        dataconcert.append(ajoutconcert)
        
        json_data = json.dumps(dataconcert)

     # Écriture des données dans un fichier JSON
        with open('static/concert.json', 'w') as f:
            f.write(json_data)

        return concert()
    else:
        return render_template("ajout_concert.html")

def lire_concert():
    try:
        with open('concert.json', 'r') as f:
            contenu = f.read().strip()
            if contenu:
                dataconcert = json.loads(contenu)
            else:
                dataconcert= []
    except FileNotFoundError:
        dataconcert=[]
    return dataconcert

@app.route("/concert")
def concert():
    f = open('static/concert.json')
    data = json.load(f)
    print(data)
    f.close()

    return render_template("concert.html", data=data)



@app.route("/actualites_jazz")
def actualites_jazz():
    return render_template("actualites_jazz.html")


@app.route("/actualites_rock")
def actualites_rock():
    return render_template("actualites_rock.html")


@app.route("/actualites_electro")
def actualites_electro():
    return render_template("actualites_electro.html")





    