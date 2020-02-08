import os
import zlib
import time
import pymysql
from flask import *  
from os.path import dirname, abspath
from werkzeug.utils import secure_filename



app = Flask(__name__)  
 
@app.route('/')  
def uploafffd():  
	return render_template("file_upload_form.html")  
 

@app.route('/login')  
def uploadfd():  
	return render_template("login.html")  
 
@app.route('/signup')  
def upload():
	return render_template("sign_up.html")  




@app.route('/success', methods = ['POST','GET'])  
def success():
	f = request.files['file']
	
	timestr = time.strftime("%Y%m%d-%H%M%S")
	f.filename = str('durgpremi')+timestr+".jpg"

	path_sourc = dirname(abspath(__file__))
	path_sourc += '/images'


	filename = secure_filename(f.filename)
	print('filename==>>',filename)

	f.save(os.path.join(path_sourc, filename))


	im = path_sourc+ '/' +filename

	host = "localhost"
	user = "akshaypawar" 
	password = "Appa9596@" 
	db = "durgpremi"
	con = pymysql.Connection(host = host,user = user,password = password,database = db) 
	cur = con.cursor() 
	q="INSERT INTO durgpremiIMG(name, userid, caption) values(%s,%s,%s)"
	cur.execute(q,(im,'userid','caption'))
	con.commit()
	con.close()
	return render_template("success.html")

if __name__ == '__main__':  
	app.run( host = '0.0.0.0', port = 5000, threaded = True, debug = True ) 





 

