from flask import Flask,request,jsonify,render_template
import numpy as np
import json
import pickle
import config
from flask_mysqldb import MySQL

app = Flask(__name__)

####### MYSQL CONFIGURATION STEP########

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'AjayAjay1504'
app.config['MYSQL_DB'] = 'breast_cancer'
mysql = MySQL(app)



@app.route("/")
def home():
    return render_template('index.html') 

@app.route("/check_cancer",methods=["GET","POST"])
def cancer():

    with open(config.MODEL_PATH,'rb') as f:
        cancer_model = pickle.load(f)

    with open(config.DATA_PATH,'r') as f:
        cancer_data = json.load(f)

    input = request.form
     
    test_array = np.zeros(len(cancer_data['columns']))

    test_array[0] = eval(input['mean_radius'])
    a = test_array[0]
    test_array[1] = eval(input['mean_texture'])
    b = test_array[1]
    test_array[2] = eval(input["mean_perimeter"])
    c = test_array[2]
    test_array[3] = eval(input["mean_area"])
    d = test_array[3]
    test_array[4] = eval(input["mean_smoothness"])
    e = test_array[4]
    test_array[5] = eval(input["mean_compactness"])
    f = test_array[5]
    test_array[6] = eval(input["mean_concavity"])
    g = test_array[6]
    test_array[7] = eval(input["mean_concave_points"])
    h = test_array[7]
    test_array[8] = eval(input["mean_symmetry"])
    i = test_array[8]
    test_array[9] = eval(input["mean_fractal_dimension"])
    j = test_array[9]
    test_array[10] = eval(input["radius_error"])
    k = test_array[10]
    test_array[11] = eval(input["texture_error"])
    l = test_array[11]
    test_array[12] = eval(input["perimeter_error"])
    m = test_array[12]
    test_array[13] = eval(input["area_error"])
    n = test_array[13]
    test_array[14] = eval(input["smoothness_error"])
    o = test_array[14]
    test_array[15] = eval(input["compactness_error"])
    p = test_array[15]
    test_array[16] = eval(input["concavity_error"])
    q = test_array[16]
    test_array[17] = eval(input["concave_points_error"])
    r = test_array[17]
    test_array[18] = eval(input["symmetry_error"])
    s = test_array[18]
    test_array[19] = eval(input["fractal_dimension_error"])
    t = test_array[19]
    test_array[20] = eval(input["worst_radius"])
    u = test_array[20]
    test_array[21] = eval(input["worst_texture"])
    v = test_array[21]
    test_array[22] = eval(input["worst_perimeter"])
    w = test_array[22]
    test_array[23] = eval(input["worst_area"])
    x = test_array[23]
    test_array[24] = eval(input["worst_smoothness"])
    y = test_array[24]
    test_array[25] = eval(input["worst_compactness"])
    z = test_array[25]
    test_array[26] = eval(input["worst_concavity"])
    aa = test_array[26]
    test_array[27] = eval(input["worst_concave_points"])
    ab = test_array[27]
    test_array[28] = eval(input["worst_symmetry"])
    ac = test_array[28]
    test_array[29] = eval(input["worst_fractal_dimension"])
    ad = test_array[29]

    output = cancer_model.predict([test_array])

    cursor = mysql.connection.cursor()
    query =  'CREATE TABLE IF NOT EXISTS B_CANCER (mean_radius VARCHAR(20),mean_texture VARCHAR(20),mean_perimeter VARCHAR(20),mean_area VARCHAR(20),mean_smoothness VARCHAR(20),mean_compactness VARCHAR(20),mean_concavity VARCHAR(20),mean_concave_points VARCHAR(20),mean_symmetry VARCHAR(20),mean_fractal_dimension VARCHAR(20),radius_error VARCHAR(20),texture_error VARCHAR(20),perimeter_error VARCHAR(20),area_error VARCHAR(20),smoothness_error VARCHAR(20),compactness_error VARCHAR(20),concavity_error VARCHAR(20),concave_points_error VARCHAR(20),symmetry_error VARCHAR(20),fractal_dimension_error VARCHAR(20),worst_radius VARCHAR(20),worst_texture VARCHAR(20),worst_perimeter VARCHAR(20),worst_area VARCHAR(20),worst_smoothness VARCHAR(20),worst_compactness VARCHAR(20),worst_concavity VARCHAR(20),worst_concave_points VARCHAR(20),worst_symmetry VARCHAR(20),worst_fractal_dimension VARCHAR(20),output VARCHAR(20))'
    cursor.execute(query)
    cursor.execute('INSERT INTO B_CANCER (mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension,output) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,output))
    
    mysql.connection.commit()
    cursor.close()

    return render_template("index1.html",output=output)



if __name__ == "__main__":
    app.run(port=config.PORT_NO,debug=False)