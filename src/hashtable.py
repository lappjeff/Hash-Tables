# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"Key: {self.key}, Value: {self.value}, Next: {self.next}"

    def __repr__(self):
        return f"Key: {self.key}, Value: {self.value}, Next: {self.next}"

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        max_load_factor = 0.7
        min_load_factor = 0.2

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return self._hash_djb2(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)

        return hash & 0xFFFFFFFF


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        if self.count >= self.capacity:
            self.resize()

        index = self._hash_mod(key)
        node = self.storage[index]
        new_node = LinkedPair(key, value)
        #updates key value if found and key matches
        if node is not None and node.key == key:
            self.storage[index].value = value
        #adds a next item if found
        elif node is not None:
            self.insert_helper(node, new_node)
        #if no other cases match, insert as head
        else:
            self.storage[index] = new_node
            self.count += 1

        print(f"Load Factor: ({self.count / self.capacity:.2f})")

    def insert_helper(self, node, value):
        '''
        Recursive insertion helper for main insert function

        Run through node.next until None found and insert value there
        '''
        if node.next is None:
            node.next = value
        else:
            self.insert_helper(node.next, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        if node is None:
            print("Key Not Found")
            return
        elif node.key == key:
            self.storage[index] = None
        elif node.next.key == key:
            node.next = node.next.next
        else:
            self.remove(node.next.key)

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        node = self.storage[index]
        if node is None:
            print("Key not found")
            return None
        elif node.key == key:
            return node.value
        else:
            self.retrieve(node.next.key)

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        if self.count < self.capacity:
            return

        load_factor = self.count / self.capacity

        if load_factor > self.max_load_factor:
            print("Doubling capacity")
            self.capacity *= 2
            new_storage = [None] * self.capacity

            for i in range(len(self.storage)):
                if self.storage[i]:
                    key_hash = self._hash_mod(self.storage[i].key)
                    new_storage[key_hash] = self.storage[i]



        self.storage = new_storage
