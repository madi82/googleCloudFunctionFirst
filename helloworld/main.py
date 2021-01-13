import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("../firestoreServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def hello_world(request):
    request_args = request.args
    request_json = request.get_json(silent=True)
    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']

        doc = db.collection('places').document('rome')
        res = doc.get().to_dict()
        print(res)

        snapshots = list(db.collection('places').get())
        for snapshot in snapshots:
            print(snapshot.to_dict())

        resAdd = db.collection('places').document('italy').set({
            'lat': 47, 'long': 687,
            'weather': 'lol',
            'landmarks': [
                'guadí park',
                'gaudí',
                'everything'
            ]
        })
        print(resAdd)
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        name = 'World'
        lastname = ''
    return f'Hello {name} {lastname}'