class Array:
    def __init__(self):
        self.arr =[0]*3 
        self.count = 0
    
    def insert(self,val):
        """ 
            Insert value in the array if the insert exceed the size of the array
            then we grow the array by 50%
        """
        if len(self.arr) == self.count:
            new_arr = [0] * 2 * len(self.arr)
            for i in range(self.count):
                new_arr[i] = self.arr[i]
            self.arr = new_arr

        self.arr[self.count] = val
        self.count += 1
        return
        
    
    def remove_at_index(self,idx):
        """ Removing the item at a given index"""
        for i in range(idx,len(self.arr)-1):
            self.arr[i] = self.arr[i+1]
        self.count -= 1
        return

    
    def print_arr(self):
        """
            Print the array
        """
        print(self.arr)
    
    def largest(self):
        """
        """
        data = sorted(self.arr, reverse=True) 
        return data[0]
    
    def intersection(self,arr):
        """Find common items in 2 arrays

        Args:
            arr (int): user input

        Returns:
            list: common elements
        """
        common = []
        for i in arr: 
            if i in self.arr:
                common.append(i)
        
        return common
    
    def reverse(self):
        """Reversing the array

        Returns:
            list: arr
        """
        return self.arr[::-1]
    
    def insert_at_idx(self,idx,val):
        temp = self.arr[idx]
        self.arr[idx] = val
        for i in range(idx+1,self.count):
            val = temp
            temp = self.arr[i]
            self.arr[i] = val
        
        return




if __name__ == '__main__':
    a = Array()
    a.insert(2)
    a.print_arr()
    a.insert(3)
    a.print_arr()
    a.insert(5)
    a.print_arr()
    a.insert(9)
    a.print_arr()
    a.insert(10)
    a.print_arr()
    a.insert(5)
    a.print_arr()
    a.insert(5)
    a.print_arr()
    a.insert(5)
    a.print_arr()
    a.remove_at_index(3)
    a.print_arr()
    print(a.largest())
    print(a.reverse())
    a.insert_at_idx(2,30)
    a.print_arr()

