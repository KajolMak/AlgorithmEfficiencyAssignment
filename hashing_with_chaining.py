import random

class HashTable:
    def __init__(self, size=10):
        """
        Initialize the hash table with a given size and an empty list for each slot (chaining).
        """
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_elements = 0

    def hash_function(self, key):
        """
        A simple universal hash function for demonstration.
        Minimizes collisions by using prime multipliers.
        """
        prime = 31  # Prime multiplier for hash function
        return (sum(ord(char) * prime ** idx for idx, char in enumerate(str(key))) % self.size)

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.
        """
        index = self.hash_function(key)
        # Check if the key already exists in the chain; if so, update the value
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        # Otherwise, append the new key-value pair to the chain
        self.table[index].append([key, value])
        self.num_elements += 1
        # Resize if load factor exceeds 0.7
        if self.load_factor() > 0.7:
            self.resize()

    def search(self, key):
        """
        Searches for a value associated with a key in the hash table.
        Returns the value if found, ot        """
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table if the key exists.
        """
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                self.num_elements -= 1
                return True
        return False

    def load_factor(self):
        """
        Calculates the load factor, defined as the ratio of
import random

class HashTable:
    def __init__(self, size=10):
        """
        Initialize the hash table with a given size and an empty list for each slot (chaining).
        """
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_elements = 0

    def hash_function(self, key):
        """
        A simple universal hash function for demonstration.
        Minimizes collisions by using prime multipliers.
        """
        prime = 31  # Prime multiplier for hash function
        return (sum(ord(char) * prime ** idx for idx, char in enumerate(str(key))) % self.size)

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.
        """
        index = self.hash_function(key)
        # Check if the key already exists in the chain; if so, update the value
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        # Otherwise, append the new key-value pair to the chain
        self.table[index].append([key, value])
        self.num_elements += 1
        # Resize if load factor exceeds 0.7
        if self.load_factor() > 0.7:
            self.resize()

    def search(self, key):
        """
        Searches for a value associated with a key in the hash table.
        Returns the value if found, otherwise None.
        """
        index = self.hash_function(key)
 import random

class HashTable:
    def __init__(self, size=10):
        """
        Initialize the hash table with a given size and an empty list for each slot (chaining).
        """
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_elements = 0

    def hash_function(self, key):
        """
        A simple universal hash function for demonstration.
        Minimizes collisions by using prime multipliers.
        """
        prime = 31  # Prime multiplier for hash function
        return (sum(ord(char) * prime ** idx for idx, char in enumerate(str(key))) % self.size)

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.
        """
        index = self.hash_function(key)
        # Check if the key already exists in the chain; if so, update the value
        for item in self.table[index]:
            if item[0] == key:

                item[1] = value
                return
        # Otherwise, append the new key-value pair to the chain
        self.table[index].append([key, value])
        self.num_elements += 1
        # Resize if load factor exceeds 0.7
        if self.load_factor() > 0.7:
            self.resize()

    def search(self, key):
        """
        Searches for a value associated with a key in the hash table.
        Returns the value if found, otherwise None.
        """
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table if the key exists.
        """
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                self.num_elements -= 1
                return True
        return False

    def load_factor(self):
        """
        Calculates the load factor, defined as the ratio of elements to the size of the table.
        """
        return self.num_elements / self.size

    def resize(self):
        """
        Resizes the hash table when the load factor exceeds a threshold (0.7).
        """
        old_table = self.table
        self.size *= 2  # Double the table size
        self.table = [[] for _ in range(self.size)]
        self.num_elements = 0  # Reset and reinsert items

        # Rehash all items into the new table
        for chain in old_table:
            for key, value in chain:
                self.insert(key, value)

# Example usage
if __name__ == "__main__":
    ht = HashTable()
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    ht.insert("city", "New York")
    print("Search for 'name':", ht.search("name"))  # Should print "Alice"
    print("Search for 'age':", ht.search("age"))    # Should print 25
    ht.delete("city")
    print("Search for 'city':", ht.search("city"))  # Should print None (deleted)
# Load Factor and Dynamic Resizing:
# - Load factor is calculated as (number of elements) / (size of hash table).
# - When the load factor exceeds a threshold (e.g., 0.7), the table size is doubled
#   to maintain efficient operations and minimize collisions.
# - Resizing involves rehashing all elements into a new, larger table.
# - Maintaining a low load factor (below 1) ensures that the average time complexity
#   for insert, search, and delete remains O(1) on average.

       
