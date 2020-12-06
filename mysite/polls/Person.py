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


# driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", ""))
# session = driver.session()
#
# result = session.run("MATCH(a:Person) WHERE a.name = $name")
# print(result.data())
# result = session.run()
#
# def count_users(tx):
#     result = tx.run("MATCH (a:User) RETURN count(a)")
#     record = result.single()
#     return record[0]
#
# num_users = session.read_transaction(count_users)

# class Person:
#     def __init__(self, uri, name, born):
#         self.driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

#     def close(self):
#         self.driver.close()

#     def num_users(self):
#         with self.driver.session() as session:
#             result = session.read_transaction(self.count_users)
#             return result

#     @staticmethod
#     def count_users(tx):
#         result = tx.run("MATCH (a:Person) RETURN count(a)")
#         record = result.single()
#         return record[0]


# def test_neo():
#     temp = Person("bolt://localhost:7687", "neo4j", "password")
#     temp.num_users()
#     temp.close()

#uri = "bolt://localhost:7687"
#driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))



#     def close(self):
#         self.driver.close()

#     def create_in_db(self):
#         with self.driver.session() as session:
#             return session.write_transaction(create_request, self)

#     @staticmethod
#     def create_request(tx, self):
#         request = tx.run("CREATE($request_name:Request "
#             "{datetime: $datetime, timezone: $timezone, method: $method, url: $url, status_code: $status_code}) "
#             "RETURN $request_name", request_name=self.name, datetime=self.datetime, timezone=self.timezone,
#             method=self.method, url=self.url, status_code=self.status_code)
#         return request.single()[0]

# class Parameter:
#     def __init__(self, left, right):
#         self.driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
    
#     def close(self):
#         self.driver.close()
    
#     def create_in_db(self):
#         with self.driver.session() as session:
#             return session.write_transaction(create_parameter, self)
    
#     @staticmethod
#     def create_parameters(tx, self):
#         param = tx.run("CREATE($param_name:Parameter {left: $left, right: $right}) RETURN $param_name",
#             param_name=self.name, left=self)
