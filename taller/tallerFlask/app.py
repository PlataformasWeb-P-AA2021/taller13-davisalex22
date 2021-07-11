from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Adminstración Edificios y Departamentos</p><a href='http://127.0.0.1:5000/losEdificios'>Edificios</a><br><a href='http://127.0.0.1:5000/losDepartamentos'>Departamentos</a>"


@app.route("/losEdificios")
def losEdificios():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/edificio/",
            auth=('davisalex22', '123456'))
    edificios = json.loads(r.content)['results']
    num_edificios = json.loads(r.content)['count']
    return render_template("losEdificios.html", edificios=edificios,
    num_edificios=num_edificios)


@app.route("/losDepartamentos")
def losDepartamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/departamento/",
            auth=('davisalex22', '123456'))
    datos = json.loads(r.content)['results']
    num_departamentos = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'propietario':d['propietario'], 'costo':d['costo'], 'numCuartos':d['numCuartos'], 'edificio':d['edificio'],
        'edificio': obtenerEdificio(d['edificio'])})
    return render_template("losDepartamentos.html", datos=datos2,
    num_departamentos= num_departamentos)

# funciones ayuda

def obtenerEdificio(url):
    """
    """
    r = requests.get(url, auth=('davisalex22', '123456'))
    edificios = json.loads(r.content)['nombre'] + " - " + json.loads(r.content)['direccion'] + " - " + json.loads(r.content)['ciudad'] 
    return edificios
