import pyrebase

firebaseConfig = {
    "apiKey": "",
  "authDomain": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "databaseURL": ""
    }
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

def upload(img,res):
    path_on_cloud = res+".jpg"
    path_local = "logs/frame"+res+".jpg"
    storage.child(path_on_cloud).put(path_local)
