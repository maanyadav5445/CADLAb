users = {}
messages = []

def register():
    user = input()
    pwd = input()
    users[user] = pwd

def login():
    user = input()
    pwd = input()
    if user in users and users[user] == pwd:
        return user
    return None

def send_message(sender):
    receiver = input()
    msg = input()
    messages.append((sender, receiver, msg))

def read_messages(user):
    for s, r, m in messages:
        if r == user:
            print(s, m)

current_user = None

while True:
    choice = input()
    if choice == "1":
        register()
    elif choice == "2":
        current_user = login()
    elif choice == "3":
        if current_user:
            send_message(current_user)
    elif choice == "4":
        if current_user:
            read_messages(current_user)
    elif choice == "5":
        break