class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not self.set.count(val):
            self.set.append(val)
            return 1
        return 0
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        valid = self.set.count(val)
        if valid:
            self.set.remove(val)
        return valid

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        len_set = len(self.set)
        if len_set < 1:
            return False
        else:
            if len(self.set)<2:
                return self.set[0]
            import random
            r = random.randrange(0, len(self.set))
            
            return self.set[r]    
#############################################################################################
class RandomizedSet2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.set:
            return 0
        else:
            self.set.append(val)
            return 1        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set:
            self.set.remove(val)
            return 1
        return 0

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        len_set = len(self.set)
        if len_set < 1:
            return 0
        else:
            if len(self.set)<2:
                return self.set[0]
                       
            return random.choice(self.set)
