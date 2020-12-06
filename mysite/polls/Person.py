from .db import Database


class Request:
    def __init__(self, label, datetime, timezone, method, url, status_code):
        self.label = label
        self.datetime = datetime
        self.timezone = timezone
        self.method = method
        self.url = url
        self.status_code = status_code


def create_request(request):
    query_string = 'CREATE(' + request.label + ':Request {datetime: "' + request.datetime + '", timezone: "'
    query_string += request.timezone + '", method: "' + request.method + '", url: "' + request.url
    query_string += '", status_code: "' + request.status_code + '"}) RETURN ' + request.label

    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)


class Parameter:
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right


def create_parameter(parameter):
    query_string = 'CREATE(' + parameter.label + ':Parameter {left: "' + parameter.left + ', right: "'
    query_string += parameter.right + '"}) RETURN ' + parameter.label

    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)
