class firstClass:
    val1 = 0
    val2 = 0
    val3 = 0
    val4 = 0
    val5 = 0

    def __init__(self,a,b,c,d,e):
        print(' this is constructor')
        self.val1 = a
        self.val2 = b
        self.val3 = c
        self.val4 = d
        self.val5 = e


    def addValue(self):                           
        print(f'addition = {self.val1 + self.val2+self.val3+self.val4+self.val5}')

    def subValue(self):
        print(f'subtraction = {self.val1 - self.val2-self.val3-self.val4-self.val5}')

    def mulValue(self):
        print(f'multiplication = {self.val1 * self.val2*self.val3*self.val4*self.val5}')

    def divValue(self):
        print(f'division = {self.val1 / self.val2/self.val3/self.val4/self.val5}')

    def minvalue(self):
        print(f'minimum = {min(self.val1,self.val2,self.val3,self.val4,self.val5)}')

    def maxvalue(self):
        print(f'maximum = {max(self.val1,self.val2,self.val3,self.val4,self.val5)}')

    def medianValue(self):
        values = [self.val1, self.val2, self.val3, self.val4, self.val5]
        values.sort()
        med_value = values[2]
        print(f'Median = {med_value}')

    def modeValue(self):
        values = [self.val1, self.val2, self.val3, self.val4, self.val5]
        mode_value = max(set(values), key=values.count)
        print(f'Mode = {mode_value}')

    def modValue(self):
        print(f'Modulus = {self.val1 % self.val2 % self.val3 % self.val4 % self.val5}')

    def percentile_75_50_25(self):
        print(f'75_percetile = {(75*(self.val1 + self.val2 + self.val3 + self.val4 + self.val5))/100}') 
        print(f'50_percetile = {(50*(self.val1 + self.val2 + self.val3 + self.val4 + self.val5))/100}') 
        print(f'25_percetile = {(25*(self.val1 + self.val2 + self.val3 + self.val4 + self.val5))/100}')



f1 = firstClass(2,3,4,6,8)
print('f1.val1 = ',f1.val1)
print('f1.val2 = ',f1.val2)
print('f1.val3 = ',f1.val3)
print('f1.val4 = ',f1.val4)
print('f1.val5 = ',f1.val5)

f1.addValue()

f1.subValue()
f1.mulValue()
f1.divValue()
f1.minvalue()
f1.maxvalue()
f1.medianValue()
f1.modeValue()
f1.modValue()
f1.percentile_75_50_25()