import requests

base_url = 'http://localhost:5000'

def upload_file(file_path):
    url = f'{base_url}/upload'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    print(response.text)

def download_file(filename):
    url = f'{base_url}/download/{filename}'
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f'Downloaded {filename} successfully')
    else:
        print(f'Failed to download {filename}')

while True:
    print("1. Upload File")
    print("2. Download File")
    print("3. Show Routes")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        upload_file_path = input('Enter the file path to upload: ')
        upload_file(upload_file_path)
    elif choice == '2':
        download_file_name = input('Enter the filename to download: ')
        download_file(download_file_name)
    elif choice == '3':
        response = requests.get(f'{base_url}/')
        print(response.json())
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")
