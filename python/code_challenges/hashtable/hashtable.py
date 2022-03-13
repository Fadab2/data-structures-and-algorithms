
class HashTable():

    def __init__(self, size=1024):
        self.size = size
        self.bucket = size * [None]
        self.all_keys = []

    def set(self, key, value):
        index = self.hash(key)
        data = (key, value)
        if self.bucket[index] is None:
            self.bucket[index] = [data]
        else:
            self.bucket[index].append(data)

    def get(self, key):
        index = self.hash(key)
        if self.bucket[index] is None:
            print("Value does not exist")
        else:
            for value in self.bucket[index]:
                if value[key] == key:
                    return value[value]

    def contains(self, key):
        index = self.hash(key)
        for k in self.bucket[index]:
            if k[0] == key:
                return True
        return False

    def hash(self, key):
        sum = 0
        for ch in key:
            sum += ord(ch)
        primed = sum * 587
        index = primed % (self.size)

        return index

    def keys(self):
        for k in self.bucket:
            if k is not None:
                if len(self.bucket):
                    self.all_keys.append(k[0])
        return self.all_keys


# if __name__ == "__main__":
#     hashed = HashTable()
#     hashed.set('Cat', "Weo Weo")
#     print(hashed.hash('aCt'))
#     print(hashed.hash('international'))
#     print(hashed.contains('aCt'))
#     print(hashed.keys())
