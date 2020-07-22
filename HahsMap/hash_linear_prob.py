#!/usr/bin/env python

class MyTable:
    
    def __init__(self, size):
        self.max_size = size
        self.keys = [None] * size
        self.values = [None] * size
        self._deleted = "deleted"
        
    def hash_code(self, key):
        hashed = 0
        for char in key:
            hashed += ord(char)

        return (hashed % self.max_size)
    
    def __setitem__(self, key, value):
        idx = self.hash_code(key)
        start = idx       
        while(True):
            if (self.keys[idx] is None): 
                self._set(idx, key, value)
                return
            if (self.keys[idx] == key):
                self.values[idx] = value
                return 
            idx = (idx + 1) % self.max_size
            if (idx == start):
                break

        self._set(idx, key, value)

    def __getitem__(self, key):
        start = self.hash_code(key)
        idx = start
        while (self.keys[idx] is not None):
            if (self.keys[idx] == key):
                return self.values[idx]
            
            idx = (idx + 1) % self.max_size
            if (idx == start):
                break

        return "Key not in table."    

    
    # lazy deletion
    def __delitem__(self, key):
        idx = self.hash_code(key)
        start = idx
        while (self.keys[idx] is not None):
            if (self.keys[idx] == key):
                self._set(idx, self._deleted, self._deleted)
                return 

            idx = (idx + 1) % self.max_size
            if (idx == start):
                break
   
    def _set(self, index, key, value):
        self.keys[index] = key
        self.values[index] = value
        
        
if __name__ == "__main__":
    m = MyTable(5)

    # The following keys all hash to the same index.
    m["a"] = "apple"
    m["f"] = "butter"
    m["k"] = "yummy"

    print("Current keys in m: ", m.keys)
    
    # "p" also hashes to the same place.
    # Your class should detect that it's not in the table
    # without scanning through the entire keys list.
    print("\n")
    print("m[`p`]:", m["p"])
   
    # We can access key "k"
    print("\n")
    print("m[`k`]:", m["k"])
    
    # Even if we remove "f"
    del m["f"]
    print("m[`k`]:", m["k"])
    print("Current keys in m:", m.keys)

    # Even after removing "f", we can overwrite "k"
    m["k"] = "newstuff"
    print("\n")
    print("Current keys in m:", m.keys)
    print("Current values in m:", m.values)

    del m["k"]
    print("\n")
    print("Current keys in m:", m.keys)
    print("Current values in m:", m.values)

    m["k"] = "stuff"
    print("\n")
    print("Current keys in m:", m.keys)
    print("Current values in m:", m.values)

    m["a"] = "orange"
    print("\n")
    print("Current keys in m:", m.keys)
    print("Current values in m:", m.values)

    m["e"] = "banana"
    print("\n")
    print("Current keys in m:", m.keys)
    print("Current values in m:", m.values)

    m["g"] = "kiwi"
    print("\n")
    print("Current keys in m:", m.keys)
    print("Current values in m:", m.values)

    del m["g"]
    print("\n")
    print("Current keys in m:", m.keys)
    print("Current values in m:", m.values)

    del m["g"]
    print("\n")
    print("Current keys in m:", m.keys)
    print("Current values in m:", m.values)

    print("\n")
    print("End!")

