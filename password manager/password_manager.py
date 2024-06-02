from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


m_pwd = input("What is the master password? ")
key = load_key() + m_pwd.encode()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user + ", Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
# "w" clears the file and makes it new, "r" only lets you read it, "a" append, lets u add or create it


while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add), Q to quit: ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()

    elif mode == "q":
        break
    else:
        print("Invalid mode.")
        continue
