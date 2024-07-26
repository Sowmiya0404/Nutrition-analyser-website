from flask import Flask, render_template, request,session
import os
from werkzeug.utils import secure_filename
import numpy as np
from keras.models import load_model
from keras.utils import load_img,img_to_array
import sqlite3
import keras
import tensorflow

UPLOAD_FOLDER=os.path.join('static','uploads')
ALLOWED_EXTENSIONS = {'jpg','png','jpeg'}

app = Flask('_name_', template_folder="templates")
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.secret_key = "nutrition"

UPLOAD_FOLDER=os.path.join('static','uploads')
ALLOWED_EXTENSIONS = {'jpg','png','jpeg'}

app = Flask('_name_', template_folder="templates")
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.secret_key = "veg"

UPLOAD_FOLDER=os.path.join('static','uploads')
ALLOWED_EXTENSIONS = {'jpg','png','jpeg'}

app = Flask('_name_', template_folder="templates")
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.secret_key = "food"

@app.route('/')  # route to display the home page
def dashboard():
    return render_template('dashboard.html')  # rendering the home page

@app.route('/calculation')
def calculation():
  return render_template('calculation.html')

@app.route('/hospital')
def hospital():
  return render_template('hospital.html')

@app.route('/salem')
def salem():
  return render_template('salem.html')

@app.route('/scardiologist')
def scardiologist():
    return render_template('scardiologist.html')

@app.route('/sneurologist')
def sneurologist():
    return render_template('sneurologist.html')

@app.route('/sskincare')
def sskincare():
    return render_template('sskincare.html')

@app.route('/sdiabetes')
def sdiabetes():
    return render_template('sdiabetes.html')

@app.route('/schildspecialist')
def schildspecialist():
    return render_template('schildspecialist.html')

@app.route('/erode')
def erode():
  return render_template('erode.html')

@app.route('/ecardiologist')
def ecardiologist():
    return render_template('ecardiologist.html')

@app.route('/eneurologist')
def eneurologist():
    return render_template('eneurologist.html')

@app.route('/eskincare')
def eskincare():
    return render_template('eskincare.html')

@app.route('/ediabetes')
def ediabetes():
    return render_template('ediabetes.html')

@app.route('/echildspecialist')
def echildspecialist():
    return render_template('echildspecialist.html')

@app.route('/tiruppur')
def tiruppur():
  return render_template('tiruppur.html')

@app.route('/tcardiologist')
def tcardiologist():
    return render_template('tcardiologist.html')

@app.route('/tneurologist')
def tneurologist():
    return render_template('tneurologist.html')

@app.route('/tskincare')
def tskincare():
    return render_template('tskincare.html')

@app.route('/tdiabetes')
def tdiabetes():
    return render_template('tdiabetes.html')

@app.route('/tchildspecialist')
def tchildspecialist():
    return render_template('tchildspecialist.html')

@app.route('/karur')
def karur():
  return render_template('karur.html')

@app.route('/kcardiologist')
def kcardiologist():
    return render_template('kcardiologist.html')

@app.route('/kneurologist')
def kneurologist():
    return render_template('kneurologist.html')

@app.route('/kskincare')
def kskincare():
    return render_template('kskincare.html')

@app.route('/kdiabetes')
def kdiabetes():
    return render_template('kdiabetes.html')

@app.route('/kchildspecialist')
def kchildspecialist():
    return render_template('kchildspecialist.html')

@app.route('/namakkal')
def namakkal():
  return render_template('namakkal.html')

@app.route('/ncardiologist')
def ncardiologist():
    return render_template('ncardiologist.html')

@app.route('/nneurologist')
def nneurologist():
    return render_template('nneurologist.html')

@app.route('/nskincare')
def nskincare():
    return render_template('nskincare.html')

@app.route('/ndiabetes')
def ndiabetes():
    return render_template('ndiabetes.html')

@app.route('/nchildspecialist')
def nchildspecialist():
    return render_template('nchildspecialist.html')

@app.route('/identify')
def identify():
  return render_template('identify.html')

@app.route('/fruit')
def fruit():
  return render_template('fruit.html')

@app.route('/imageprediction')
def imageprediction():
    return render_template('imageprediction.html')

@app.route('/addimageprediction', methods=['POST']
)  # routes to the index imageprediction
def addimageprediction():
    if request.method=="POST":
        img  = request.files["image"]
        img_filename = secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'],img_filename))
        session['uploaded_img_filepath'] = os.path.join(app.config['UPLOAD_FOLDER'],img_filename)
        img_filepath = session.get('uploaded_img_filepath',None)
        image_pred = launch(img_filepath)
        print(img_filepath)
        return render_template("imageprediction.html",value=img_filepath,pred=image_pred[0],content=image_pred,flag=True)
    else:
        return render_template("fruit.html",data="image not send or error")

def launch(img_filepath):
    model = tensorflow.keras.models.load_model('nutrition.h5', compile=False)
    img = load_img(img_filepath, target_size=(64, 64))  # load and reshaping the image
    x = img_to_array(img)  # converting image to an array
    x = np.expand_dims(x, axis=0)  # changing the dimensions of the imag
    predict_x = model.predict(x)
    classes_x = np.argmax(predict_x)
    index = ['Apple', 'Banana', 'Orange', 'Pineapple', 'Watermelon']
    values = nutrition(index[classes_x])
    return [index[classes_x], values]
  
def nutrition(x):
    conn = sqlite3.connect('nutro.db')
    cursor = conn.execute(f'''SELECT * FROM nutro WHERE FRUIT=="{x}"''')
    rec = cursor.fetchall()[0]
    return rec

@app.route('/vegetable')
def vegetable():
  return render_template('vegetable.html',data="working")

@app.route('/ vegimageprediction')
def vegimageprediction():
    return render_template('vegimageprediction.html')

@app.route('/addvegimageprediction', methods=['POST']
)  # routes to the index vegimageprediction
def addvegimageprediction():
    if request.method=="POST":
        img  = request.files["image"]
        img_filename = secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'],img_filename))
        session['uploaded_img_path'] = os.path.join(app.config['UPLOAD_FOLDER'],img_filename)
        img_path = session.get('uploaded_img_path',None)
        image_pred = veglauch(img_path)
        print(img_path)
        return render_template("vegimageprediction.html",value=img_path,pred=image_pred[0],content=image_pred,flag=True)
    else:
        return render_template("vegetable.html",data="image not send or error")

def veglauch(img_path):
    model = tensorflow.keras.models.load_model('veg.h5', compile=False)
    img = load_img(img_path, target_size=(64, 64))  # load and reshaping the image
    y = img_to_array(img)  # converting image to an array
    y = np.expand_dims(y, axis=0)  # changing the dimensions of the imag
    predict_y = model.predict(y)
    classes_y = np.argmax(predict_y)
    index = ['BROCCOLI', 'CARROT', 'CAULIFLOWER','ONION','POTATO']
    values = veg(index[classes_y])
    return [index[classes_y], values]
  
def veg(y):
    conn = sqlite3.connect('veg.db')
    cursor = conn.execute(f'''SELECT * FROM veg WHERE VEGETABLE=="{y}"''')
    rec = cursor.fetchall()[0]
    return rec


@app.route('/food')
def food():
  return render_template('food.html',data="working")

@app.route('/ foodimageprediction')
def foodimageprediction():
    return render_template('foodimageprediction.html')

@app.route('/addfoodimageprediction', methods=['POST']
)  # routes to the index vegimageprediction
def addfoodimageprediction():
    if request.method=="POST":
        img  = request.files["image"]
        img_filename = secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'],img_filename))
        session['uploaded_img_file'] = os.path.join(app.config['UPLOAD_FOLDER'],img_filename)
        img_file = session.get('uploaded_img_file',None)
        image_pred = foodlaunch(img_file)
        print(img_file)
        return render_template("foodimageprediction.html",value=img_file,pred=image_pred[0],content=image_pred,flag=True)
    else:
        return render_template("food.html",data="image not send or error")

def foodlaunch(img_file):
    model = tensorflow.keras.models.load_model('food.h5', compile=False)
    img = load_img(img_file, target_size=(64, 64))  # load and reshaping the image
    z = img_to_array(img)  # converting image to an array
    z = np.expand_dims(z, axis=0)  # changing the dimensions of the imag
    predict_z = model.predict(z)
    classes_z = np.argmax(predict_z)
    index = ['BURGER', 'CHAPATI', 'DOSA','IDLI','PIZZA']
    values = food(index[classes_z])
    return [index[classes_z], values]
  
def food(z):
    conn = sqlite3.connect('food.db')
    cursor = conn.execute(f'''SELECT * FROM food WHERE FOOD=="{z}"''')
    rec = cursor.fetchall()[0]
    return rec


if __name__ == "__main__":
    app.run(debug=False)