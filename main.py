import hashlib

password = "pas123"
hashed_password = hashlib.sha256(password.encode()).hexdigest()
if 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f' == hashed_password:
    print('yes')
else:
    print(hashed_password)
    print('no')

print(hashed_password)