from neo4j import GraphDatabase, basic_auth


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

class Person:
    def __init__(self, uri, name, born):
        self.driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

    def close(self):
        self.driver.close()

    def num_users(self):
        with self.driver.session() as session:
            result = session.read_transaction(self.count_users)
            return result

    @staticmethod
    def count_users(tx):
        result = tx.run("MATCH (a:Person) RETURN count(a)")
        record = result.single()
        return record[0]


def test_neo():
    temp = Person("bolt://localhost:7687", "neo4j", "password")
    temp.num_users()
    temp.close()
