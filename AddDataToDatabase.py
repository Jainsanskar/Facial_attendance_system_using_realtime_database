import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://realtimefaceattendance-ca222-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')   # creating database reference

data = {
    "9407":
        {
            "name":"Dr. Devesh Kumar Lal",
            "major":"Big Data",
            "starting_year":2020,
            "total_attendance":31,
            "standing":"G",
            "year":3,
            "last_attendance_time":"2023-04-01 12:40:00"
        }
}

for key,value in data.items():
    ref.child(key).set(value)

