#список всех почт
emails = {
    'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
    'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
    'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
    'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
    'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
    'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']
}
#cортировка по доменам и юзерам
sorted_emails = {domain: sorted([f"{user}@{domain}" for user in users]) for domain, users in emails.items()}
#сортировка групп на домены и по алфавиту
for domain, addresses in sorted(sorted_emails.items()):
    print(f"{domain}:")
    for address in addresses:
        print(f"  {address}")
