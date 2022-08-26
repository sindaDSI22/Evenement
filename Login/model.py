from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base import Session, Base

class Role(Base):
    __tablename__ = "role"
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    role = Column(String(255), nullable=True)

    def __init__(self, id=None, role=None):
        self.id = id
        self.role = role

class roleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_relationships = False
        load_instance = True

class User(Base):
    __tablename__ = "user"
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    login = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
    # role_id = Column(Integer, ForeignKey('role.id'), nullable=True)
    # role = relationship("Role", foreign_keys=[role_id], backref="role_id")
    role_id = Column(Integer, nullable=True)

    def __init__(self, id=None, login=None,password=None,role_id=None):
        self.id = id
        self.login= login
        self.password= password
        self.role_id = role_id

    def get(self):
        evt = Session.query(User).filter(User.login == self.login).all()
        return login.dump(evt)

    def checkLogin(self):
        # import pdb;pdb.set_trace();
        login = Session.query(User).filter(User.login == self.login,User.password == self.password).first()
        if login:
            return True
        else:
            return False
class loginSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

login = loginSchema(many=True)