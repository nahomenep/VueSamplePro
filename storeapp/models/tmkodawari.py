from typing import List
from db import db
from sqlalchemy import sql

class TMKodawariModel(db.Model):
    __tablename__ = "tmkodawari"

    kukakuId = db.Column(db.String(10), primary_key=True)
    bukkenId = db.Column(db.String(10), primary_key=True)
    other1 = db.Column(db.Integer(10), nullable=False)
    other2=db.Column(db.String(20))
    remarks1=db.Column(db.String(10))
    remarks2 = db.Column(db.String(10))


    @classmethod
    def find_by_rinsid(cls, rinsId: str):
        print("find by id {}",format(rinsId))
        return cls.query.filter_by(rinsId=rinsId).first()
    #def find_by_rinsid(cls, rinsId: str) -> "TKukakuModel":
    #    return cls.query.filter_by(rinsId=rinsId).first()

    @classmethod
    def find_all(cls) -> List["ItemModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
