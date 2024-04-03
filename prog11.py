from flask import Flask, request
import hashlib


def checkpw(username, password):
    user_pass_dict = {"john": "imagine", "paul": "walrus",
                      "george": "thesun", "ringo": "submarine"}
    if username in user_pass_dict:
        if user_pass_dict[username] == password:
            return True
        else:
            return False
    else:
        return False


def checkpwh(username, password):
    user_pass_dict = {"john": hash("imagine"), "paul": hash(
        "walrus"), "george": hash("thesun"), "ringo": hash("submarine")}
    hashed_password = hash(password)
    if username in user_pass_dict:
        if user_pass_dict[username] == hashed_password:
            return True
        else:
            return False
    else:
        return False


list_a = [1, 4, 8, 12]
list_b = [2, 3, 10, 11]
list_c = []

pos_list_a = 0
pos_list_b = 0

num_elem = len(list_a) + len(list_b)

while len(list_c) < num_elem:
    # are there still elements in both the lists?
    if pos_list_a < len(list_a) and pos_list_b < len(list_b):
        if list_a[pos_list_a] < list_b[pos_list_b]:
            list_c.append(list_a[pos_list_a])
            pos_list_a += 1
        else:
            list_c.append(list_b[pos_list_b])
            pos_list_b += 1
    else:
        # add the rest
        if pos_list_a < len(list_a):
            list_c.append(list_a[pos_list_a])
            pos_list_a += 1
        if pos_list_b < len(list_b):
            list_c.append(list_b[pos_list_b])
            pos_list_b += 1

print(list_c)


def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if checkpwh(username, password):
        print("ok")
    else:
        print("failed")


app = Flask(__name__)

user_pass_dict = {"john": hashlib.sha256("imagine".encode()).hexdigest(),
                  "paul": hashlib.sha256("walrus".encode()).hexdigest(),
                  "george": hashlib.sha256("thesun".encode()).hexdigest(),
                  "ringo": hashlib.sha256("submarine".encode()).hexdigest()}


@app.route('/', methods=['GET', 'POST'])
def login_form():
    if request.method == 'POST':
        # Process the form data
        user_name = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if user_name in user_pass_dict and user_pass_dict[user_name] == hashed_password:
            return f'<h1>Welcome, {user_name}!</h1>'
        else:
            return '<h1>Invalid username or password</h1>'

    # Render form
    return '''
        <form method="post">
            User Name:<br>
            <input type="text" name="username" required><br>
            Password:<br>
            <input type="password" name="password" required><br><br>
            <input type="submit" value="Submit">
        </form>
    '''


if __name__ == '__main__':
    app.run(port=5001, debug=True)
    main()
