import hashlib
obj = hashlib.md5()
obj = hashlib.sha256()

obj.update("hello".encode("utf-8"))

print(obj.hexdigest())