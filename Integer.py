class Integer:
    def __init__(self,value:int):
        self.value = value
    
    @classmethod
    def from_float(cls,value):
        if not isinstance(value,float):
            return f'value is not a float'
    
    @classmethod
    def from_roman(cls,value:str):
        roman = {'I':1,'V':5,'X':10,'L':50}
        total = 0
        prev_value = 0
        for char in reversed(value):
            value = roman[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return cls(total)

    @classmethod
    def from_string(cls,value:str):
        if not isinstance(value,str):
            return "wrong type"
        try:
            int(value)
        except:
            return "wrong type"
            
            
    def add(self,integer) :    
        if not isinstance(integer,Integer):
            return "Number should be an interger"
        return self.value + integer.value


first_num = Integer(10) 
second_num = Integer.from_roman("IV") 
 
print(Integer.from_float("2.6")) 
print(Integer.from_string(2.6)) 
print(first_num.add(second_num)) 
