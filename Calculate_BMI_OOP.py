print("****BMI Calculator with Python***"'\n')

class BMICalculator():
    
    def __init__(self,height,weight):
        self._height_meters = height/100
        self._weight = weight

    def get_height(self):
        return self._height_meters*100
    
    def get_weight(self):
        return self._weight
    
    def BMICalculate(self):
        if Height> 0 and Height >0:
            self.BMI = round(self._weight/self._height_meters**2,2)

    def __str__(self):
        return f"your Body Mass Index is {self.BMI}."'\n'

    def compareBMI(self):
        
            if(self.BMI<=16):
                    return "you are severely underweight."
                
            elif(self.BMI<=18.5):
                    return "you are underweight."
                
            elif(self.BMI<=25):
                    return "you are Healthy."
                
            elif(self.BMI<=30):
                    return "you are overweight."
                
            else: return("you are severely overweight.")
            
                       
Height=float(input("Enter your height in centimeters: \n"))
Weight=float(input("Enter your Weight in Kg: \n"))

cal= BMICalculator(Height,Weight)
cal.BMICalculate()
print(cal)
print(cal.compareBMI())



