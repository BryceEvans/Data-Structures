class Heap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)
        self.size += 1

    def delete(self):
        if len(self.storage) == 1:
            self.size -= 1
            return self.storage.pop()
        else:
            if len(self.storage) == 0:
                return None
            else:
                temp = self.storage[0]
                self.storage[0] = self.storage.pop()
                self._sift_down(0)
                self.size -= 1
                return temp

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        # 1. Check to see if the index is greater than zero
        # 2. Grab the parent index
        # 3. Check if current value is greater than or less than parent value
            # a. if current is greater than
            # b. Swap
        # 4. If current is lesser than parent
            # a. leave it alone - break

        # while index > 0:
        #     parent = (index - 1) // 2
        #     if self.storage[index] > self.storage[parent]:
        #         self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        #         index = parent # updating your new index
        #     else:
        #         break
        parent_index = (index - 1) // 2
        current_index = index
        while parent_index >= 0:
            if self.storage[parent_index] < self.storage[current_index]:
                self.storage[parent_index], self.storage[current_index] = self.storage[current_index], self.storage[parent_index]
            else:
                break
            current_index = parent_index
            parent_index = (parent_index - 1) // 2


    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
            if index * 2 + 2 > len(self.storage) - 1:
                max = index *2 + 1
            elif self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
                max = index * 2 + 1
            else:
                max = index * 2 + 2
            if self.storage[max] > self.storage[index]:
                self.storage[max], self.storage[index] = self.storage[index], self.storage[max]
            index = max
