import requests

base_url = 'http://localhost:5000/tasks' 

def create_task():
    title = input('Enter task title: ')
    description = input('Enter task description (optional): ')
    done = input('Is the task done? (y/n): ').lower() == 'y'

    data = {
        'title': title,
        'description': description,
        'done': done
    }
    response = requests.post(base_url, json=data)
    print('Create Task Response:', response.json())

def get_tasks():
    response = requests.get(base_url)
    print('Get Tasks Response:', response.json())

def get_task_by_id():
    task_id = input('Enter task ID to retrieve: ')
    response = requests.get(f'{base_url}/{task_id}')
    print('Get Task Response:', response.json())

def update_task():
    task_id = input('Enter task ID to update: ')
    title = input('Enter updated task title (press Enter to keep current title): ')
    description = input('Enter updated task description (press Enter to keep current description): ')
    done = input('Is the task done? (y/n, press Enter to keep current status): ')
    done = done.lower() == 'y' if done else None

    data = {}
    if title.strip():
        data['title'] = title
    if description.strip():
        data['description'] = description
    if done is not None:
        data['done'] = done

    response = requests.put(f'{base_url}/{task_id}', json=data)
    print('Update Task Response:', response.json())

def delete_task():
    task_id = input('Enter task ID to delete: ')
    response = requests.delete(f'{base_url}/{task_id}')
    print('Delete Task Response:', response.json())

while True:
    print("\nSelect an option:")
    print("0. Show Routes")
    print("1. Create Task")
    print("2. Get All Tasks")
    print("3. Get Task by ID")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == '0':
        response = requests.get('http://localhost:5000/')
        print('Show Routes Response:', response.json())
    elif choice == '1':
        create_task()
    elif choice == '2':
        get_tasks()
    elif choice == '3':
        get_task_by_id()
    elif choice == '4':
        update_task()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
