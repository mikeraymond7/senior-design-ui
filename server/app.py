import os
from flask import Flask, request, jsonify, render_template
from firebase_admin import credentials, firestore, initialize_app, storage

app = Flask(__name__)

cred = credentials.Certificate('../../key.json')
initialize_app(cred, {'storageBucket': 'groovy-groove-363915.appspot.com'})
db = firestore.client()

@app.route('/uploader')
def upload_file():
	return render_template('./upload.html')


# File successfully uploads
# Make it so that files can be uploaded by bytes
@app.route('/uploadFile', methods=['POST'])
def uploadFile():
	if request.method == 'POST':
		f = request.files['file']
		f.save(f.filename)
		try:
			fileName = f.filename
			#fileName = "../../test.txt"
			bucket = storage.bucket()
			blob = bucket.blob(fileName)
			print(blob)
			blob.upload_from_filename(fileName)
			blob.make_public()
			print("File URL: " + blob.public_url)
			os.remove(fileName)
			return jsonify({"success": True}), 200
		except Exception as e:
			# change error to return to error page
			return f"An Error Occured while uploading file: {e}."

@app.route('/downloadFile', methods=['POST'])
def downloadFile():
	#f = request.files['fileName']
	bucket = storage.bucket()
	blob = bucket.blob("test.txt")
	blow.download_to_filename("downloaded.txt")
	return jsonify({"success" : True}), 200











