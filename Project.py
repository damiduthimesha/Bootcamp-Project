import hashlib

print("Enter your value :")
value = input()

#using hexdigest()
print(hashlib.md5(value.encode('utf-8')).hexdigest())
print(hashlib.md5("000005fab4534d05key9a055eb014e4e5d52write".encode('utf-8')).hexdigest())

#using digest()
print(hashlib.md5(value.encode('utf-8')).digest())
print(hashlib.md5("000005fab4534d05key9a055eb014e4e5d52write".encode('utf-8')).digest())

