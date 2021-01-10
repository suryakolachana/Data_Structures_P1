from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity = capacity
        self.storage_limit = 0
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if type(key) != int:
            return -1

        if key in self.cache:
            self.set(key,self.cache[key])
            return self.cache[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity < 1:
            return

        if type(value) != int:
            return

        if value in self.cache:
            self.cache.pop(value)
            self.storage_limit -= 1
        
        if self.storage_limit < self.capacity:
            self.cache[key] = value
            self.storage_limit += 1
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value

def main():
    # TEST CASE 1:
    print("TEST CASE 1:")
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)


    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))       # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)           
    our_cache.set(6, 6)

    print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    # TEST CASE 2:
    print("TEST CASE 2:")
    sec_cache = LRU_Cache()

    sec_cache.set(10,10)
    sec_cache.set(20,20)
    sec_cache.set(30,30)
    sec_cache.set(None,None) # won't be added to the cache
    sec_cache.set('','')     # won't be added to the cache
    sec_cache.set(' ',' ')   # won't be added to the cache

    print(sec_cache.get(10)) # return 10
    print(sec_cache.get(20)) # return 20
    print(sec_cache.get(10)) # return 30

    sec_cache.set(40,40)
    sec_cache.set(50,50)

    print(sec_cache.get(30)) # return 30

    sec_cache.set(60,60)

    print(sec_cache.get(20))  # returns -1

    # TEST CASE 3:
    print("TEST CASE 3:")

    third_cache = LRU_Cache(10) # High capacity size 

    third_cache.set(1,1)
    third_cache.set(20,20)
    third_cache.set(300,300)
    third_cache.set(3.14159,3.14159) # will not be added as it is not an integer
    third_cache.set(10001101,10001101)
    third_cache.set(7878787878787887898980898980909090,7878787878787887898980898980909090)

    print(third_cache.get(300))   # Returns 300
    print(third_cache.get(7878787878787887898980898980909090))  # returns 7878787878787887898980898980909090

    print(third_cache.get(3.14159))  # Returns -1 
    
    # TEST CASE 4: 
    print("TEST CASE 4:")

    fourth_cache = LRU_Cache(0) 

    fourth_cache.set(1,1)
    fourth_cache.set(2,2)
    fourth_cache.set(3,3)

    print(fourth_cache.get(1))   # Returns -1
    print(fourth_cache.get(2))   # Returns -1

    # TEST CASE 5:
    print("TEST CASE 5:")

    fourth_cache = LRU_Cache(-1) 

    fourth_cache.set(0,0)
    fourth_cache.set(1,1)
    fourth_cache.set(3,3)

    print(fourth_cache.get(0))   # Returns -1
    print(fourth_cache.get(1))   # Returns -1
    
    
    # TEST CASE 6:
    print("TEST CASE 6:")

    our_cache = LRU_Cache(3)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache.get(4))  # Expected Value = 4
    print(our_cache.get(1))  # Expected Value = -1
    our_cache.set(2, 4)
    print(our_cache.get(2))  # Expected Value = 4 Your Output=2

if __name__ == "__main__":
    main()