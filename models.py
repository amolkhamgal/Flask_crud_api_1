from sqlalchemy import Column,String,Integer,Text
from database import Base


class Students(Base):
    __tablename__="students_table"
    id=Column(Integer,primary_key=True)
    name=Column(String(20))
    email=Column(String(40),unique=True)
    dept=Column(String(20))
    city=Column(String(20))
    marks=Column(Integer)
    gender=Column(String(20))
    
    
    def to_json(self):
        return {"id":self.id,"name":self.name,"email":self.email,"dept":self.dept,"city":self.city,"marks":self.marks,"gender":self.gender}
        
    
        