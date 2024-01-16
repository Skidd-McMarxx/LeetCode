import random
class RandomizedSet:

    def __init__(self):
       self.randmap = {}
       self.randlist = []

    def insert(self, val: int) -> bool:
        if val not in self.randmap:
            self.randmap[val] = len(self.randlist)
            self.randlist.append(val)
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.randmap:
            val_index = self.randmap[val]
            last_index = self.randlist[-1]
            self.randlist[val_index] = last_index
            self.randlist.pop()
            self.randmap[last_index] = val_index
            del self.randmap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.randlist)