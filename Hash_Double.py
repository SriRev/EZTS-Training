class HashTable:
    def __init_(self, size):
        self.size = size
        self.table = [None] * self.size

    def insert(self, data):
        index1 = data % self.size
        index2 = 8 - (data % 8)
        i = 0
        while self.table[(index1 + i * index2) % self.size] is not None:
            i += 1
            if i >= self.size:
                # If we have checked all slots and found no empty one
                raise Exception("HashTable is full")

        index = (index1 + i * index2) % self.size
        self.table[index] = data

m=[20,34,45,70,56,81,104,37,36,39]
x=HashTable(11)
for p in m:
    x.insert(p)
print(x.table)