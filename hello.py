from flask import Flask, render_template, request, redirect, url_for, session
from function import valid_login
from pprint import pprint

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.get("/")
def index():
    return render_template('index.html')

@app.get('/register')
def register():
     return render_template('auth/register.html')


@app.post('/inscription')
def inscription():
    pprint(request.form)
    return "test"


#Créer une route signifie créer un chemin dans l'URL par exemple : hhtp://domain.com/login, il s'agit de créer une
#route avec laquelle on va chercher la page. Il y a 5 méthodes : GET (récupérer)/ POST(créer une route)
# / PUT / PATCH (mettre à jour)/ DELETE (supprimer)
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None

    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('profile'))
        else:
            error = 'Invalid username/password'

    return render_template('auth/login.html', error=error)


@app.get('/profile') #On créer une route avec GET pour récupérer les informations de la page profile
def profile():
    if 'username' in session:
        return render_template('profile.html', name=session['username'])
    else:
        return redirect(url_for('login'))


@app.get('/about') #il faut lier la route que l'on vient de créer avec une fonction
def about():        #On défini la fonction
    return render_template('about.html')

@app.get('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None) #session.pop est une fonction qui supprime la valeur contenu dans username

    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()





#Ajouter le bouton logout sur la page registrer.