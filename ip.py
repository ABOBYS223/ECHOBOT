import re

def is_valid_ip(ip):
    ip_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(ip_pattern.match(ip))

# Пример использования
user_input = input("Введите IP-адрес: ")

if is_valid_ip(user_input):
    print("Верный IP-адрес.")
else:
    print("Неверный IP-адрес.")
