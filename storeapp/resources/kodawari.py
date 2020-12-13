from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, fresh_jwt_required
from models.item import ItemModel
from schemas.item import ItemSchema
from models.tkukaku import TKukakuModel
from schemas.tkukaku import TKukakuSchema
from schemas.kodwari_init_param import KodawariInit,KodwariInitSchema
from marshmallow import ValidationError
from sqlalchemy import sql

NAME_ALREADY_EXISTS = "An item with name '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the item."
ITEM_NOT_FOUND = "Item not found."
ITEM_DELETED = "Item deleted."

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)

kodawari_init_sch= KodwariInitSchema()
tkukaku_schema=TKukakuSchema()

class Kodawari(Resource):
    #@classmethod
    #def get(cls, rins_id: str):
        #print("i am get kodawari")
        ##check the input data
        #if len(rins_id) < 3:
        #    return {"message":"enter the id of length 2"},401
        ##kodawari = KukakuModel.find_by_id(rins_id)
        #return rins_id
        ##item = ItemModel.find_by_name(rins_id)
        ##if item:
        ##    return item_schema.dump(item), 200

        ##return {"message": ITEM_NOT_FOUND}, 404

    @classmethod
    #@fresh_jwt_required
    def post(cls):
        #insert dummy data
        tkukaku =  TKukakuModel()
        tkukaku.kukakuId="11"
        tkukaku.bukkenId="22"
        tkukaku.typeId="33"
        tkukaku.updateDate=sql.func.now()
        tkukaku.rinsId="100"
        #tkukaku.save_to_db();

        print("validating json..")

        #json format check
        #try:
        #    input_data=kodawari_init_sch.load(request.get_json())
        #except ValidationError as err:
        #    print(err.messages)
        #    return {"message" : err.messages} , 601
        kodawari=kodawari_init_sch.load(request.get_json()) #check the input json data
        kodawari_inputObj=KodawariInit(**kodawari)
        mainInfo=TKukakuModel.find_by_rinsid(kodawari_inputObj.rins_id)
        # if mainInfo:
        #    return tkukaku_schema.dump(mainInfo), 200

        # return {"message": ITEM_NOT_FOUND}, 404

        ###join tkodawari and mkodawari table


        #print(kodawari_inputObj.rins_id)

        #now select from tkukaku table
        #tkukaku = TKukakuModel.find_by_rinsid(rin)
        return request.get_json()

        #return {"message":"kodawari_init_sch.load(request.get_json())"}

        #if ItemModel.find_by_name(name):
        #    return {"message": NAME_ALREADY_EXISTS.format(name)}, 400

        #item_json = request.get_json()
        #item_json["name"] = name

        #item = item_schema.load(item_json)

        #try:
        #    item.save_to_db()
        #except:
        #    return {"message": ERROR_INSERTING}, 500

        #return item_schema.dump(item), 201

    @classmethod
    #@jwt_required
    def delete(cls, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": ITEM_DELETED}, 200

        return {"message": ITEM_NOT_FOUND}, 404

    @classmethod
    def put(cls, name: str):
        item_json = request.get_json()
        item = ItemModel.find_by_name(name)

        if item:
            item.price = item_json["price"]
        else:
            item_json["name"] = name
            item = item_schema.load(item_json)

        item.save_to_db()

        return item_schema.dump(item), 200


class ItemList(Resource):
    @classmethod
    def get(cls):
        return {"items": item_list_schema.dump(ItemModel.find_all())}, 200
