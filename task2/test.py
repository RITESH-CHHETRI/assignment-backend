import requests
import json

base_url = 'http://localhost:5000'

def register_user(username, password):
    url = f'{base_url}/register'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print('User registered successfully')
    else:
        print('Failed to register user:', response.json())

def login_user(username, password):
    url = f'{base_url}/login'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        token = response.json()['token']
        return token
    else:
        print('Login failed:', response.json())
        return None

def perform_operation(token, operation, num1, num2):
    url = f'{base_url}/{operation}'
    headers = {'Authorization': token}
    data = {'num1': num1, 'num2': num2}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()['result']
        print(f'{num1} {operation} {num2} = {result}')
    else:
        print('Operation failed:', response.json())

def get_calculations(token):
    url = f'{base_url}/calculations'
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        calculations = response.json()['calculations']
        for calc in calculations:
            print(f"ID: {calc['id']}, Operation: {calc['operation']}, Numbers: {calc['num1']}, {calc['num2']}, Result: {calc['result']}")
    else:
        print('Failed to get calculations:', response.json())

if __name__ == '__main__':
    choice = input('Enter 1 to register, 2 to login: ')
    if choice == '1':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        register_user(username, password)
    elif choice == '2':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        token = login_user(username, password)
        if token:
            while True:
                print('Choose an operation:')
                print('1. Add')
                print('2. Subtract')
                print('3. Multiply')
                print('4. Divide')
                print('5. View History')
                print('6. Exit')

                option = input('Enter your choice: ')
                if option == '1':
                    num1 = float(input('Enter the first number: '))
                    num2 = float(input('Enter the second number: '))
                    perform_operation(token, 'add', num1, num2)
                elif option == '2':
                    num1 = float(input('Enter the first number: '))
                    num2 = float(input('Enter the second number: '))
                    perform_operation(token, 'subtract', num1, num2)
                elif option == '3':
                    num1 = float(input('Enter the first number: '))
                    num2 = float(input('Enter the second number: '))
                    perform_operation(token, 'multiply', num1, num2)
                elif option == '4':
                    num1 = float(input('Enter the first number: '))
                    num2 = float(input('Enter the second number: '))
                    perform_operation(token, 'divide', num1, num2)
                elif option == '5':
                    get_calculations(token)
                elif option == '6':
                    break
                else:
                    print('Invalid choice')
    else:
        print('Invalid choice')
