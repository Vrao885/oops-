class point:
    def __init__(self, x, y, z ):
        self.x= x 
        self.y= y 
        self.z= z
    def sqsum(self):
        return self.x**2+self.y**2+self.z**2
# creating a instance of a point class 
pt = point(1, 3, 5 )
# calling the method to calculate square sum and printing it
result= pt.sqsum()
print(result)
