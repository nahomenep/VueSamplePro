from ma import ma
from models.tkukaku import TKukakuModel

class TKukakuSchema(ma.ModelSchema):
    class Meta:
        model = TKukakuModel
       # load_only = ("store",)
      #  dump_only = ("id",)
       # include_fk = True
