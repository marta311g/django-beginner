from .neo4j_db import Database

class Request:
    def __init__(self, datetime, timezone, method, url, status_code):
        self.datetime = datetime
        self.timezone = timezone
        self.method = method
        self.url = url
        self.status_code = status_code

    def create_dictionary(self):
        myDict = {
            "datetime": self.datetime,
            "timezone": self.timezone,
            "method": self.method,
            "url": self.url,
            "status_code": self.status_code
        }
        return myDict
    
    def get_node_name(self):
        return "Request"


class Parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def create_dictionary(self):
        myDict = {
            "name": self.name,
            "value": self.value
        }
        return myDict
    
    def get_node_name(self):
        return "Parameter"


class Ip:
    def __init__(self, address, ip_type):
        self.address = address
        self.ip_type = ip_type
    
    def create_dictionary(self):
        myDict = {
            "address": self.address,
            "ip_type": self.ip_type
        }
        return myDict
    
    def get_node_name(self):
        return "Ip"


class Isp:
    def __init__(self, isp_name):
        self.isp_name = isp_name
    
    def create_dictionary(self):
        myDict = {
            "isp_name": self.isp_name
        }
        return myDict
    
    def get_node_name(self):
        return "Isp"


class As:
    def __init__(self, as_name):
        self.as_name = as_name
    
    def create_dictionary(self):
        myDict = {
            "as_name": self.as_name
        }
        return myDict
    
    def get_node_name(self):
        return "As"


class City:
    def __init__(self, city_name, postal_code):
        self.city_name = city_name
        self.postal_code = postal_code
    
    def create_dictionary(self):
        myDict = {
            "city_name": self.city_name,
            "postal_code": self.postal_code
        }
        return myDict
    
    def get_node_name(self):
        return "City"


class Region:
    def __init__(self, region_name):
        self.region_name = region_name
    
    def create_dictionary(self):
        myDict = {
            "region_name": self.region_name
        }
        return myDict
    
    def get_node_name(self):
        return "Region"


class Country:
    def __init__(self, country_name, country_code):
        self.country_name = country_name
        self.country_code = country_code
    
    def create_dictionary(self):
        myDict = {
            "country_name": self.country_name,
            "country_code": self.country_code
        }
        return myDict
    
    def get_node_name(self):
        return "Country"


#stvara cvor 'class_name' sa atributima 'parameters'
#class_name je string, a attributes je dictionary
def create_node(class_name, attributes):
    i = 0
    query_string = 'CREATE(label' + ':' + class_name + '{'
    for attribute in attributes:
        if i == 1:
            query_string += attribute + ': "' + attributes[attribute] + '"'
        elif i > 1:
            query_string += ', ' + attribute + ': "' + attributes[attribute] + '"'
        i += 1
    query_string += '}) RETURN label'

    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)

#first_node and second_node are dictionaries, relationship_name is a string
def create_relationship(first_node_name, first_node, second_node_name, second_node, relationship_name):
    i = 0
    j = 0
    query_string = 'MATCH(a:' + first_node_name + '),(b:' + second_node_name + ') WHERE '
    for attribute in first_node:
        if i == 0:
            query_string += 'a.' + attribute + ' = "' + first_node[attribute] + '"'
        else:
            query_string += ' AND a.' + attribute + ' = "' + first_node[attribute] + '"'
        i += 1
    for attribute in second_node:
        if j == 0:
            if i > 0:
                query_string += ' AND '
            query_string += 'b.' + attribute + ' = "' + second_node[attribute] + '"'
        else:
            query_string += ' AND b.' + attribute + ' = "' + second_node[attribute] + '"'
        j += 1
    query_string += ' CREATE(a)-[r:' + relationship_name + ']->(b) RETURN r'

    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)

#klasa je ime čvora, parametri je dictionary sa where parametrima
def get_nodes(class_name, attributes):
    i = 0
    query_string = 'MATCH(label:' + class_name + '{'
    for attribute in attributes:
        if i == 0:
            query_string += attribute + ': "' + attributes[attribute] + '"'
        else:
            query_string += ', ' + attribute + ': "' + attributes[attribute] + '"'
        i += 1
    query_string += '}) RETURN label'

    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)
#example
#mydict = {
#    "datetime": "30/Aug/2020:03:24:31",
#        "method": "GET"
#}
#print(get_nodes('Request', mydict))

def get_requests_for_ip(ip_address):
    query_string = 'MATCH(a:Ip {address: "' + ip_address + '"})-[:HAS_SENT]->(b:Request) RETURN b'
    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)