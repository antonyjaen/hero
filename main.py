from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import json_util
import os

app = Flask(__name__)

app.config["UPLOAD_FOLDER"]= os.path.abspath("D:/Angular/segunda/app/src/assets/img/")

app.config['MONGO_URI']="mongodb://u8vbscnqv0fgcvq1bgme:SCJpwwaoB5sExywCQBOg@bciadiyiykotz6l-mongodb.services.clever-cloud.com:27017/bciadiyiykotz6l"
mongo = PyMongo(app)
CORS(app)


@app.route('/habitAdd',methods=["GET","POST"])
def HabitacionesAdd():
    res=request.args.get('data')
    num=eval(res)['numero']
    pis=eval(res)['piso']
    des=eval(res)['descripcion']
    car=eval(res)['caracteristicas']
    pre=eval(res)['precio']
    est=eval(res)['estado']
    tip=eval(res)['tipo']
    img=eval(res)['img']
    try:
        mongo.db.rooms.insert({"numero":num,"piso":pis,"descripcion":des,"caracteristicas":car,"precio":pre,"estado":est,"tipo":tip,"img":img})
        return("Agregado")
    except :
        return("Datos Incorrectos")


@app.route('/workerAdd',methods=["POST"])
def workerAdd():
    res=request.data
    res=eval(res)['data']
    nombre=res['nombre']
    apellidoP=res['apellidoP']
    apellidoM=res['apellidoM']
    tipo=res['tipo']
    documento=res['documento']
    direccion=res['direccion']
    telefono=res['telefono']
    mail=res['mail']
    acceso=res['acceso']
    usuario=res['usuario']
    password=res['password']
    estado=res['estado']
    try:
        mongo.db.workers.insert({
        "documento":documento,
        "nombre":nombre,
        "apellidoP":apellidoP,
        "apellidoM":apellidoM,
        "tipo":tipo,
        "direccion":direccion,
        "telefono":telefono,
        "mail":mail,"acceso":acceso,
        "usuario":usuario,
        "password":password,
        "estado":estado
        })
        return("Agregado")
    except :
        return("Datos Incorrectos")



@app.route('/worker',methods=["GET"])
def worker():
    users = mongo.db.workers.find()
    res = json_util.dumps(users)
    return res


@app.route('/habit',methods=["GET"])
def Habitaciones():
    users = mongo.db.rooms.find()
    res = json_util.dumps(users)
    return res

@app.route('/habit/<id>',methods=["POST"])
def findHabitaciones(id):
    resu = mongo.db.rooms.find_one({"numero":id})
    res = json_util.dumps(resu)
    return res 

#try, needs improve
@app.route('/worker/<id>',methods=["POST"])
def findWorker(id):
    resu = mongo.db.workers.find_one({"documento":id})
    res = json_util.dumps(resu)
    return res 

@app.route('/habitEdit',methods=["POST"])
def habitEdit():
    res=request.data
    iden=eval(res)['idi']
    res=eval(res)['data']
    num=res['numero']
    pis=res['piso']
    des=res['descripcion']
    car=res['caracteristicas']
    pre=res['precio']
    est=res['estado']
    tip=res['tipo']
    try:
        img = res["img"]
    except :
        img = ""
    try:
        mongo.db.rooms.update({'numero':iden},{"numero":num,"piso":pis,"descripcion":des,"caracteristicas":car,"precio":pre,"estado":est,"tipo":tip,"img":img})
        return("Agregado")
    except :
        return("Datos Incorrectos")


@app.route('/habitDel/<id>',methods=["DELETE"])
def habitDel(id):
    try:
        val = {"numero":id}
        r = mongo.db.rooms.delete_one(val)
        return("Eliminado")
    except :
        return('Error')

@app.route('/log',methods=["POST"])
def Login():
    try:
        res=request.data
        pas=eval(res)['pas']
        us=eval(res)['user']
        resu = mongo.db.workers.find_one({"usuario":us,"password":pas})
        if(resu):
            res = json_util.dumps(resu)
            return res 
        else:
            return "no"
    except :
        return "no"
    

if __name__ == '__main__':
    app.run(port =3000, debug= False)