from flask import Flask, request, jsonify, json, session
import os
import re
import logging
from flask import Flask, request, jsonify, json
from marshmallow import fields, Schema, ValidationError, validates_schema
from marshmallow.validate import Length

from common.global_var import get_soccer, set_soccer
from common.shared_var import test_process, AppInfo
from service.aes_cipher import AESCipher

app = Flask(__name__)
app.secret_key = "any random string"

DATA_KEY_ERROR = 'Input data must have a "data" key.'


@app.errorhandler(ValidationError)
def marshmallow_error_handler(error):
    # print(error.messages) results in expected {'age': ['Missing data for required field.']}
    # return error.messages, 400
    msg = {"msg": "validation error"},
    app_info = session["appinfo"]

    print("api session after validation error ", app_info["username"], app_info["appname"], get_soccer())
    return jsonify(msg), 400


class AppError(Exception):
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# This schema is used to validate the activity form data
class ActivityFormSchema(Schema):
    name = fields.Str(required=True, valdiate=Length(max=100))
    description = fields.Str(required=True, valdiate=Length(max=100))
    image = fields.Str(required=True, valdiate=Length(max=1000))
    badge_prereqs = fields.List(fields.Dict(), required=True)
    module_prereqs = fields.List(fields.Int(), required=True)
    students = fields.Nested("StudentSchema", only=("name", "username", "roles", "image"), many=True)

    # More fields go here...
    class Meta:
        # Fields to show when sending data
        fields = ("name", "description", "image", "badge_prereqs", "module_prereqs", "students")


class StudentSchema(Schema):
    # name = fields.Str(required=True)
    name = fields.Str()
    # username = fields.Email(required=True)
    username = fields.Str()
    roles = fields.Str(required=False)
    image = fields.Str(required=True)
    activities = fields.Nested("ActivitySchema", only=("name", "description", "image"), many=True)

    class Meta:
        # Fields to show when sending data
        fields = ("name", "username", "roles", "image")
        ordered = True


class BandSchema(Schema):
    name = fields.Str()
    data = fields.Str()

    @validates_schema
    def unwrap_envelope(self, data, **kwargs):
        if "data" not in data:
            raise ValidationError(f'{DATA_KEY_ERROR}', 'error')


class BaseSchema(Schema):
    rins_number = fields.Str()
    pp = fields.Str()

    class Meta:
        pass_original = True

    def handle_error(self, exc, data, **kwargs):
        """Log and raise our custom exception when (de)serialization fails."""
        # logging.error(exc.messages)
        # raise AppError("An error occurred with input: {0}".format(data))
        # raise AppError(exc.messages)
        return exc.messages

    @validates_schema
    def validate_param(self, datas, **kwargs):
        print(os.getenv('LANG'))
        # print(os.getenv('HOST'))
        for data in datas:
            if "rins_number" not in data:
                raise ValidationError("rins_number key is requiredaaaa")

    # @pre_load
    def validate_unknown(self, data, **kwargs):
        error = {}
        print(data)
        print(fields)
        if "rins_number" not in data:
            raise ValidationError("rins_number keyss is required")
        # for d in data:
        #     if d not in fields:
        #         raise ValidationError("unknown fields..{}".format(d))


@app.route('/api/')
def hello_world():
    return "Hello World!"


@app.route('/api/cypher', methods=['POST'])
def cypher():
    # start_logging1()
    start_logging1()
    aes = AESCipher("iloveu")
    plain_text = "i am encrypting"
    encrypted_text = aes.encrypt(plain_text)
    decrypted_text = aes.decrypt(encrypted_text)
    print("plain text ", plain_text)
    print("encrypted text ", encrypted_text)
    print("decrypted text ", decrypted_text)
    return "Hello World!"


@app.route('/api/session', methods=['POST'])
def api_session():
    # start_logging1()
    # session['username'] = "mohan"
    app_info = AppInfo("jumper", "world")
    # session['appinfo'] = app_info.tojson()
    session['appinfo'] = app_info.tojson()
    set_soccer("pele pele")
    print("api session start ", app_info.username, app_info.appname, get_soccer())
    test_process()
    return "Hello World!"


def start_logging2():
    # not working ng..
    # logging.basicConfig(filename='output.log')
    extra = {'app_name': 'Super App'}

    logger = logging.getLogger('log-app-name')  # (__name__)
    syslog = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(app_name)s : %(message)s')
    syslog.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(syslog)

    # logger = logging.LoggerAdapter(logger, extra)
    # logger.info('The sky is so blue')
    # # working module..ok
    # FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    # # logging.basicConfig(format=FORMAT)
    # # logging.basicConfig(filename='output.log', format=FORMAT)
    # # logging.getLogger('output.log', format=FORMAT)
    # logger = logging.getLogger('oo_application')
    # fh = logging.FileHandler('spam.log')
    # fh.setFormatter(FORMAT)
    # logger.addHandler(fh)
    # d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    # logger.debug('Protocol problem: %s', 'connection reset', extra=d)
    # logger.error('Protocol problem: %s', 'connection reset', extra=d)


def start_logging1():
    # working module..ok
    FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    # logging.basicConfig(format=FORMAT)
    logging.basicConfig(filename='output.log', format=FORMAT)
    # logging.getLogger('output.log', format=FORMAT)
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    logging.debug('Protocol problem: %s', 'connection reset', extra=d)
    logging.error('Protocol problem: %s', 'connection reset', extra=d)


def start_logging3():
    # not working ng
    FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    # logging.basicConfig(format=FORMAT)
    # logging.basicConfig(filename='output.log', format=FORMAT)
    logger = logging.getLogger('output.log')
    formatter = {'clientip': '192.168.0.1', 'user': 'fbloggs'}

    syslog = logging.StreamHandler()
    # formatter = logging.Formatter('%(asctime)s %(app_name)s : %(message)s')
    syslog.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(syslog)
    logger.debug('Protocol problem: %s', 'connection reset', extra=formatter)
    logger.error('Protocol problem: %s', 'connection reset', extra=formatter)


def start_logging4():
    # create logger with 'spam_application'
    logger = logging.getLogger('spam_application')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('spam.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('creating an instance of auxiliary_module.Auxiliary')
    # a = auxiliary_module.Auxiliary()
    # logger.info('created an instance of auxiliary_module.Auxiliary')
    # logger.info('calling auxiliary_module.Auxiliary.do_something')
    # a.do_something()
    # logger.info('finished auxiliary_module.Auxiliary.do_something')
    # logger.info('calling auxiliary_module.some_function()')
    # auxiliary_module.some_function()
    # logger.info('done with auxiliary_module.some_function()')


# check number
def RepresentsInt(s):
    return re.match(r"[-+]?\d+(\.0*)?$", s) is not None


@app.route('/api/init', methods=['POST'])
def one_param():
    print("init param ")
    print("22.0".isnumeric())
    # print(RepresentsInt("aa.0"))
    param = request.get_json()
    sch = BaseSchema()
    try:
        # pass
        sch.load(param)
        # pprint(sch.load(param))
    except ValidationError as err:
        print("validation error")
        err.messages
        print(err.messages)
        return jsonify(err.messages)
    except AppError as appErr:
        # print(appErr)
        # return appErr
        print("appError")
        print(appErr.__dict__)
        return appErr.__dict__

    return jsonify({"status": "OK"}), 400

    # rins_init=BaseSchema()
    # param=request.get_json()
    # try:
    #     rins_init.load({"rins_number": "The Band"})
    # except ValidationError as err:
    #     return jsonify(err.messages),400

    # return "Hello World!"


@app.route('/api/student', methods=['POST'])
def student_one():
    activity_form_schema = ActivityFormSchema()
    args = request.get_json()
    print(args["students"])
    try:
        dataF = activity_form_schema.load(args)
        return "success"
    except ValidationError as err:
        print(err.messages)
        print(err.valid_data)
        return jsonify(err.messages), 400
    # print(args["badge_prereqs"])
    return "hllll"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
