from marshmallow import Schema,fields,ValidationError,validates

class KodawariInit:
    def __init__(self,rins_id):
        self.rins_id=rins_id

class KodwariInitSchema(Schema):
    rins_id = fields.Str(required=True,error_messages={"required":"rins_id is req...."})

    @validates('rins_id')
    def validate(self,param):
        if len(param) != 3:
            raise ValidationError("rins_id length is not equal to 10")

