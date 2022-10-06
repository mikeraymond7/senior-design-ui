import os
from flask import Flask, request, jsonify, render_template
from firebase_admin import credentials, firestore, initialize_app, storage

app = Flask(__name__)

cred = credentials.Certificate('../../key.json')
initialize_app(cred, {'storageBucket': 'groovy-groove-363915.appspot.com'})
db = firestore.client()
users_ref = db.collection('users')
stats_ref = db.collection('stats')
lifts_ref = db.collection('lifts')

@app.route('/uploader')
def upload_file():
	return render_template('./upload.html')


# File successfully uploads
# Need to fully confirm with Download
# Make it so that files can be uploaded by bytes
@app.route('/uploadFile', methods=['POST'])
def uploadFile():
	f = request.files['file']
	#f.save(f.filename)
	try:
		fileName = f.filename
		#fileName = "../../test.txt"
		bucket = storage.bucket()
		blob = bucket.blob(fileName)
		print(blob)
		blob.upload_from_filename(fileName)
		blob.make_public()
		print("File URL: " + blob.public_url)
		return jsonify({"success": True}), 201
	except Exception as e:
		return f"An Error Occured while uploading file: {e}."

