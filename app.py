from flask import render_template, redirect, request, url_for
from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='api_enotech'

mysql.init_app(app)

def callBD(query,value = 0):
    conexion = mysql.connect()
    cursor = conexion.cursor()
    if value == 0:
        cursor.execute(query)
    else:
        cursor.execute(query,value)
    conexion.commit()
    return cursor.fetchall()

@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('/nosotros.html')

@app.route('/contacto')
def contacto():
    return render_template('/contacto.html')

@app.route('/productos')
def productos():
    return render_template('/productos.html')


@app.route('/getAll')
def getAll():
    sql ="select a.idWine,a.winery,a.wine,b.country,a.image from `Api_Enotech`.`wines` as a inner join `Api_Enotech`.`Locations` as b on a.id_Location = b.idLocation "     
    datos = callBD(sql)

    return render_template('/getAll.html',wines = datos)



@app.route('/create')
def create():
    sql = "select `idLocation`,`country` from `Api_Enotech`.`Locations`"
    datos = callBD(sql)

    return render_template('/create.html',locations = datos)



# TODO: REALIZAR EL GUARDADO DE LAS IMAGENES
@app.route('/addWine',methods=["POST"])
def addWine():
    _winery = request.form["winery"]
    _wine = request.form["wine"]
    _location = request.form["location"]
    # _image = request.form["image"]
    _image = request.files["txtFoto"]
    datos = (_winery,_wine,_location,_image)

    sql = "insert into `Api_Enotech`.`wines` (`winery`,`wine`,`id_Location`,`image`) values (%s,%s,%s,%s)" 
    callBD(sql,datos)

    return redirect(url_for('getAll'))

@app.route('/edit/<int:id>')
def edit(id):

    sql ="select a.idWine,a.winery,a.wine,b.country,a.image from `Api_Enotech`.`wines` as a inner join `Api_Enotech`.`Locations` as b on a.id_Location = b.idLocation where `idWine` = %s"     
    query = "select `idLocation`,`country` from `Api_Enotech`.`Locations`"
    
    wine = callBD(sql,id)
    locations = callBD(query)

    return render_template('/edit.html',datos = wine, locations = locations)

@app.route('/update',methods=["POST"])
def update():
    __id = request.form["id"]
    _winery = request.form["winery"]
    _wine = request.form["wine"]
    _location = request.form["location"]
    _image = "null"

    update =[_winery,_wine,_location,_image,__id]
    query = "update `Api_Enotech`.`wines` set `winery`=%s,`wine`=%s,`id_Location`=%s,`image`=%s where `idWine`=%s"
    callBD(query,update)

    return redirect('/getAll')

@app.route('/delete/<int:id>')
def delete(id):
    query = "delete from `Api_Enotech`.`wines` where `idWine` = %s"
    callBD(query,id)
    
    return redirect('/getAll')


if __name__ == '__main__':
    app.run(debug=True,port=8500)