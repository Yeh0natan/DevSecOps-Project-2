import requests

# 1
class MyUser:
    def __init__(self, id, email, username, name):
        self.id = id
        self.email = email
        self.username = username
        self.name = name

    def __str__(self):
        return f" id={self.id}, email={self.email}, username={self.username}, name={self.name}"

u1 = MyUser(11, "u1@gmail.com", "u1", "user1")
print(u1)


# 2
def find_user_by_name(name):
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    users = res.json()

    for user in users:
        if user['name'] == name:
            return MyUser(user["id"], user["email"], user["username"], user["name"])
        elif name in user['name']:
            return MyUser(user["name"],user["id"], user["email"], user["username"])

    return "User not found."


user_name = input("Enter user name: ")
user = find_user_by_name(user_name)
print(user)
