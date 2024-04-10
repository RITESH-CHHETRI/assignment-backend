
import requests

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    register_url = 'http://localhost:5000/register'
    data = {'username': username, 'password': password}
    response = requests.post(register_url, json=data)
    print(response.json())

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    login_url = 'http://localhost:5000/login'
    auth = (username, password)
    response = requests.post(login_url, auth=auth)
    print(response.json())
    if 'token' in response.json():
        return response.json()['token']
    return None

def refresh_token(token):
    if token:
        refresh_token_url = 'http://localhost:5000/refresh_token'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(refresh_token_url, headers=headers)
        print(response.json())
    else:
        print("Token not available. Please login first.")

while True:
    print("\nOptions:")
    print("0. Show Routes")
    print("1. Register")
    print("2. Login")
    print("3. Refresh Token")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '0':
        response = requests.get('http://localhost:5000/')
        print(response.json())
    elif choice == '1':
        register_user()
    elif choice == '2':
        token = login_user()
    elif choice == '3':
        refresh_token(token)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose again.")
