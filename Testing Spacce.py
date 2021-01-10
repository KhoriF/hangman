'''def even(nums):
    count = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            count += 1
    return count

print(even([34324,324,2432,3242,111,3333]))'''

'''def max69(num):
    realnum = str(num)
    for i in realnum:
        if i == '9':
            continue
        else:
            realnum = realnum.replace(i,'9',1)
            break 
    return int(realnum)


print(max69('666666'))'''


'''def test_function():
    print("This is a test function")

test_function()'''




'''def quadratic (a,b,c):
    root = ((b**2)-(4*a*c))**(1/2)

    denominator = 2*a

    pos_num = (-b + root)/denominator
    
    neg_num = (-b - root)/denominator

    print(pos_num, "and", neg_num)


quadratic(1,2,3)'''






'''def duplicate_count(text):
    doubles = {i for i in text if text.count(i.lower()) > 1}
    print(len(doubles))
    return doubles

class Point:
    def __init__(self, x , y):
        self.x = x 
        self.y = y

    def distance_bt_pts(self, other):
        return (((self.x - other.x)**2)+((self.y-other.y)**2)**(1/2))

    def dist_from_origin(self):
        return Point(0,0).distance_bt_pts(Point(self.x,self.y))
    
    def __lt__(self, other):
        return (Point(self.x,self.y).dist_from_origin() < Point(other.x,other.y).dist_from_origin()) 

    def __gt__(self, other):
        return (Point(self.x,self.y).dist_from_origin() > Point(other.x,other.y).dist_from_origin())   

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == self.x)

def f2(n):  
    old = 0   
    new = 1
    for i in range(n): 
        old = new 
        new = old + new 
    return old

print(f2(6))

if __name__ == '__main__':
    testPoint = Point(2,1)
    testPoint2 = Point(1,2)
    assert(testPoint < testPoint2)
    #assert(testPoint.y == 2)
    #print(testPoint < testPoint2)'''

def reverse(x):
    pos = abs(x) 
    lst = []
    zero = False
    string = str(pos)
    n = len(string)
    if string[-1] == '0': 
        zero = True 
    if n == 1:
        return x 
    else: 
        for i in range(len(string)): 
            lst.append(string[i])
        if zero == True: 
            while zero: 
                lst.pop() 
                if lst[-1] != '0':
                    zero = False
        newlst = []
        for i in range(len(lst)-1, -1, -1):
            newlst.append(lst[i])
        if x < 0:
            return int("".join(newlst)) * -1
        else:
            return int("".join(newlst))












            
