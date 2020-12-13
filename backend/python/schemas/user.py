from marshmallow import Schema
# Product Schema
class UserSchema(Schema):
    class Meta:
        fields = ('id', 'firstname', 'lastname', 'email')
