import timeit

mysetup = '''
class Genie:
    def __init__(self):
        self.data_store = [
            {"entity": "user:alice", "access": "write", "namespace": "doc1"}]

    def populate_data_store(self, limit):
        self.gen_store = []

        for i in range(0, limit):
            data = {"entity": "user:james", "access": "read", "namespace": "doc" + str(i)}
            self.gen_store.append(data)
        self.data_store += self.gen_store

    def add_rule(self, rule):
        self.data_store.append(rule)

    def remove_rule(self, rule):
        self.data_store.remove(rule)

    def check_access(self, rule):
        user_access = set()
        for policy in self.data_store:
            if policy["entity"] == rule["entity"] and policy['namespace'] == rule['namespace']:
                user_access.add(policy['access'])
        print(user_access)
        if rule['access'] in user_access:
            print("User is permitted to access this namespace")
        else:
            print("User is not permitted to access this namespace")

    def retrieve_collaborators(self, namespace):
        access_list = set()
        for policy in self.data_store:
            if policy['namespace'] == namespace:
                access_list.add(policy['entity'])
        print(access_list)


g = Genie()
g.check_access({"entity": "user:james", "access": "admin", "namespace": "doc1"})
g.populate_data_store(100000)
'''
mycode = '''g.retrieve_collaborators("doc1")'''

print(timeit.timeit(setup=mysetup,
                    stmt=mycode,
                    number=1))
