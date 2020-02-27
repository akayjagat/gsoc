import cv2
import numpy as np
import pytesseract
from PIL import Image
from flask import Flask
from flask import Flask, render_template,Response,request ,make_response, session   
import pandas as pd
from werkzeug.utils import secure_filename
app = Flask(__name__,static_folder = "templates")
def processReadTextImage(imagePath):
	img = Image.open(imagePath)
	pytesseract.pytesseract.tesseract_cmd = 'tesseract'
	result = pytesseract.image_to_string(img)
	return result + "<br><br><button style='font-size:20px;font-weight:900;color:black;background-color:lightblue;border:0;padding:20px 10px;'><a href='http://127.0.0.1:5000/'>Home</a></button>"

	@app.route('/readtext.html', methods = ['POST', 'GET'])
def readtext():
	if request.method == 'POST':
		f = request.files['fileToUpload']
		filePath = f.filename
		f.save(secure_filename(filePath))
		extension = filePath.split(".")
		extension = extension[len(extension)-1]
		if "jpeg" in extension or "jpg" in extension or "png" in extension:
			output = processReadTextImage(filePath)
			return output #render_template('/readtext.html',output=output)
		else:
			return "Invalid File uploaded"	
	else:
		return render_template('/index.html')

if __name__ == "__main__":
    app.run(debug=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port) 