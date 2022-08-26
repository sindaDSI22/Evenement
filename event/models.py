from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mysqlx import Column
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, Integer, String, Date

from base import Base, Session

class Evenement(Base):
    __tablename__ = "event"
    id = Column('id', Integer, primary_key=True,autoincrement=True, nullable=False)
    titre = Column(String(255), nullable=True)
    type = Column(String(255), nullable=True)
    DT = Column(Date, nullable=True)
    description = Column(String(255), nullable=True)
    photo = Column(String(255), nullable=True)

    def __init__(self, id=None, titre=None,type=None, DT =None, description=None,
                 photo = None):
        self.id = id
        self.titre = titre
        self.type = type
        self.DT = DT
        self.description = description
        self.photo = photo

    def get(self):
        evt = Session.query(Evenement).all()
        return event.dump(evt)

    def getbyid(self):
        evt = Session.query(Evenement).filter(Evenement.id == self.id).all()
        return event.dump(evt)

    def updateEvent(self,idE):
        evt = Session.query(Evenement).filter(Evenement.id == idE).first()
        evt.titre = self.titre
        evt.type = self.type
        evt.DT = self.DT
        evt.desccription = self.description
        evt.photo= self.photo
        Session.commit()

        if evt:
            return event.dump([evt])
        else:
            return None

class evenementSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Evenement
        include_relationships = False
        load_instance = True

event = evenementSchema(many=True)