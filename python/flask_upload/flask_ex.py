from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return "file uploaded"
      #return render_template('upload.html')
      		
if __name__ == '__main__':
   app.run(host='192.168.43.170', debug = True,port=5000)
