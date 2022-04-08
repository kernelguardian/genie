
class Genie:
    def __init__(self):
        self.data_store = [
            {
                "entity": "user:alice",
                "access": "admin",
                "namespace": "doc1"
            }
        ]

        self.access_type = {
            "admin": ["admin", "write", "read", "comment"],
            "write": ["write", "read", "comment"],
            "read": ["read", "comment"],
            "comment": ["comment"],
        }

    def add_rule(self, rule):
        self.data_store.append(rule)

    def remove_rule(self, rule):
        self.data_store.remove(rule)

    def check_access(self, rule):
        user_access = set()
        for policy in self.data_store:
            if policy["entity"] == rule["entity"] and policy['namespace'] == rule['namespace']:
                user_access.update(self.access_type[policy['access']])
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

g.check_access(
    {
        "entity": "user:alice",
        "access": "read",
        "namespace": "doc1"
    }
)

# g.retrieve_collaborators("doc1")
