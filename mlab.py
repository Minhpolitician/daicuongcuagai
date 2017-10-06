
import mongoengine
#mongodb://<dbuser>:<dbpassword>@ds163711.mlab.com:63711/cuagaidaicuong

host = "ds163711.mlab.com"
port = 63711
db_name = "cuagaidaicuong"
user_name = "Cobra_king"
password = "AndromedaM31"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
