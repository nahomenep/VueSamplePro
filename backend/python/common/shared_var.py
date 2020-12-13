from flask import session
from marshmallow import ValidationError

from common.global_var import get_soccer, set_soccer


def test_process():
    app_info = session["appinfo"]
    print("from shared var file", app_info["username"], app_info["appname"],get_soccer())
    #app_info.username = "anny"
    #app_info.appname = "crazy"
    n_app_info=AppInfo("anny1","crazy1")
    session["appinfo"] = n_app_info.tojson()
    set_soccer("marodona")
    raise ValidationError("validationError")


class AppInfo:
    def __init__(self, username, appname):
        self.username = username
        self.appname = appname

    def tojson(self):
        return self.__dict__


    @classmethod
    def set_username(cls, username):
        # cls.username = username
        pass

    @classmethod
    def set_appname(cls, appname):
        # cls.appname = appname
        pass
