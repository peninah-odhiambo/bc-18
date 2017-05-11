class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        #self.array = list.__init__(self, [i for i in range(self.b, (self.a + self.b), self.b) if i]) #returns list
        self.array = list.__init__ (self, [i for i in range (self.b, (self.a + 1)) if i])
        self.length = len(self)

    def search(self,item):
        answer = {}
        count = 0
        answer ['count'] = 0
        first = 0       
        last = self.length + 1
        found = False

        while first < last:                     
            mid = (first + last) // 2
            mid_val = mid
            answer['count'] += 1

            if mid_val == item:
                answer['index'] = mid - 1
                found = True
                return answer

            else:
                if mid_val <= item:
                    first = mid + 1
                elif mid_val > item:
                    last = mid - 1
                found = False
        
        

        if found is False:
            answer['index'] = -1
            return answer


bin = BinarySearch(40,2)

print (bin.search(20))


       