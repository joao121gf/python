import os
os.system('cls' if os.name == 'nt' else 'clear')


messages = []
user_name = input('Type Your Name: ')

while True:
    os.system('cls')
    if len(messages) > 0 :
        for c in messages:
            print(c['name'], "-", c['text'])
    print('_______________')
    text = input('Message: ')
    if text == 'Fim':
        break
    messages.append({
        'name': user_name,
        'text': text
    })
