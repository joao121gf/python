with open('archive.txt', 'w') as archive:
    archive.write('First manipulation of archives')
with open('archive.txt', 'r') as archive:
    message = archive.read()
    print(message)
