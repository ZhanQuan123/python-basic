import hashlib as hash

auth = input('Enter your Password : ')
encrytion = hash.sha256(auth.encode())

if encrytion.hexdigest()  == ('9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'):
    print('welcome')
else:
    print('no')
