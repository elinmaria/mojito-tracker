from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

cred = credentials.Certificate("firebase-secret.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mojito-maestro-default-rtdb.europe-west1.firebasedatabase.app/'  # ← update this line!
})

@app.route('/')
def index():
    names = [
        "EMMA BERCKMANS", "HELENA HORNSBY", "AISA KAJOUK", "MIREIA MIRALLES",
        "SOPHIE PASCHKE", "NOEMIE CHEVRIER", "MADDY ANDERSON",
        "MEGAN JONES", "LINDA ALAMI", "ELIN JOHANSSON"
    ]
    return render_template('index.html', names=names)

@app.route('/get-scores')
def get_scores():
    ref = db.reference('players')
    return jsonify(ref.get())

@app.route('/update-score', methods=['POST'])
def update_score():
    data = request.json
    player = data['player']
    ref = db.reference(f'players/{player}')
    ref.set(data['new_score'])
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
