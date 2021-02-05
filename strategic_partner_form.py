from flask import Flask, request, jsonify

from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

# Initialize Firestore Database
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
sp_ref = db.collection('strategicpartners')

class SP(object):
    def __init__(self, name, perm_add,present_add,date,DOB,bld_grp,mob_no,email,ref,comp_name,comp_add,designation,kyc,nominee_name,nominee_relation,Autohub_Advisor):
        self.name = name
        self.perm_add = perm_add
        self.present_add = present_add
        self.date = date
        self.DOB = DOB
        self.bld_grp = bld_grp
        self.mob_no = mob_no
        self.email = email
        self.ref = ref
        self.comp_name = comp_name
        self.comp_add = comp_add
        self.designation = designation
        self.kyc = kyc
        self.nominee_name = nominee_name
        self.nominee_relation = nominee_relation
        self.Autohub_Advisor = Autohub_Advisor

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            'name': self.name,
            'perm_add': self.perm_add,
            'present_add': self.present_add,
            'date': self.date,
            'DOB': self.DOB,
            'bld_grp': self.bld_grp,
            'mob_no': self.mob_no,
            'email': self.email,
            'ref': self.ref,
            'comp_name': self.comp_name,
            'comp_add': self.comp_add,
            'designation': self.designation,
            'kyc': self.kyc,
            'nominee_name': self.nominee_name,
            'nominee_relation': self.nominee_relation,
            'Autohub_Advisor': self.Autohub_Advisor
        }

        return dest

@app.route('/spform',methods=['POST'])
def spform():
    if request.is_json:
        content = request.get_json()
        name = content['name']
        perm_add = content['perm_add']
        present_add = content['present_add']
        date = content['date']
        DOB = content['DOB']
        bld_grp = content['bld_grp']
        mob_no = content['mob_no']
        email = content['email']
        ref = content['name']
        comp_name = content['comp_name']
        comp_add = content['comp_add']
        designation = content['designation']
        kyc = content['kyc']
        nominee_name = content['nominee_name']
        nominee_relation = content['nominee_relation']
        Autohub_Advisor = content['Autohub_Advisor']

        sp = SP(name=name, perm_add=perm_add,present_add=present_add,date=date,DOB=DOB,bld_grp=bld_grp,
        mob_no=mob_no,email=email,ref=ref,comp_name=comp_name,comp_add=comp_add,designation=designation,
        kyc=kyc,nominee_name=nominee_name,nominee_relation=nominee_relation,Autohub_Advisor=Autohub_Advisor)
        db.collection('strategicpartners').add(sp.to_dict())

        # db.collection('strategicpartners').get()
        # .then(snapshot => console.log(snapshot.size))


        return 'Data Saved'

@app.route('/getdata',methods=['GET'])
def get_data():
    docs = db.collection('strategicpartners').stream()
    my_dict = { el.id: el.to_dict() for el in docs }
    return my_dict
    

if __name__ == '__main__':
    app.run()



