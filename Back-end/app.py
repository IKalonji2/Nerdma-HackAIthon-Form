from flask import Flask, request, jsonify
from models import db, Applicant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Tables created")

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    new_applicant = Applicant(
        first_name=data['first_name'],
        last_name=data['last_name'],
        phone_number=data['phone_number'],
        email=data['email'],
        company=data['company'],
        experience_level=data['experience_level'],
        track=data['track'],
        team=data['team']
    )
    db.session.add(new_applicant)
    db.session.commit()
    return jsonify({"message": "Application submitted successfully!"}), 201

@app.route('/applications', methods=['GET'])
def get_applications():
    applications = Applicant.query.all()
    results = [
        {
            "first_name": app.first_name,
            "last_name": app.last_name,
            "phone_number": app.phone_number,
            "email": app.email,
            "company": app.company,
            "experience_level": app.experience_level,
            "track": app.track,
            "team": app.team
        } for app in applications
    ]
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
