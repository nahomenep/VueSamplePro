from typing import List
from db import db
from sqlalchemy import sql

class TKodawariModel(db.Model):
    __tablename__ = "tkodawari"

    kukakuId = db.Column(db.String(10), nullable=False)
    bukkenId = db.Column(db.String(10), nullable=False)
    sdistance = db.Column(db.Integer(10), nullable=False)
    sname=db.Column(db.String(20))
    value1=db.Column(db.String(10))
    value2 = db.Column(db.String(10))


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
