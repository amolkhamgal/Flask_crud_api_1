from flask import Flask,jsonify,request,Response
from models import Students
from database import Base,engine,sessionLocal

Base.metadata.create_all(bind=engine)

app=Flask(__name__)

db=sessionLocal()

@app.route("/")
def home():
    return jsonify({"message":"Welcome to CRUD Application!"})


@app.route("/students",methods=["GET"])
def get_all_students():
    stds=db.query(Students).all()
    return jsonify([std.to_json()  for std in stds])

@app.route("/students/<int:std_id>",methods=["GET"])
def get_student_by_id(std_id):
    std=db.query(Students).filter_by(id=std_id).first()
    if not std:
        return jsonify({"message":f"Student of id {std_id} is not found"}),404
    return jsonify(std.to_json())

@app.route("/students",methods=["POST"])
def create_students():
    std=request.get_json()
    create_std=Students(name=std['name'],email=std['email'],dept=std['dept'],city=std['city'],marks=std['marks'],gender=std['gender'])
    db.add(create_std)
    db.commit()
    return jsonify("Created students Successfully",create_std.to_json()) ,201

@app.route("/students/<int:std_id>",methods=["PUT"])
def update_students(std_id):
    data=request.get_json()
    std=db.query(Students).filter_by(id=std_id).first()
    if std:
        std.name=data.get('name',std.name)
        std.email=data.get('email',std.email)
        std.dept=data.get('dept',std.dept)
        std.city=data.get('city',std.city)
        std.marks=data.get('marks',std.marks)
        std.gender=data.get('gender',std.gender)
        db.commit()
        return jsonify(std.to_json())
    return jsonify({"message":f"Student of id {std_id} is not found"}),404

    
@app.route("/students/<int:std_id>",methods=["DELETE"])
def delete_students(std_id):
    std=db.query(Students).filter_by(id=std_id).first()
    if std:
        db.delete(std)
        db.commit()
        return jsonify ({"message":f"Data of id {std_id} is deleted successfully"})
    return jsonify({"message":f"Student of id {std_id} is not found"}),404
    



if __name__=="__main__":
    app.run(debug=True)