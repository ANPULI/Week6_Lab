class Student:
    def __init__(self, name = "", class_of = 0, major = ""):
        self.name = name
        self.class_of = class_of
        self.major = major
        
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name            
    
    def set_class_of(self, class_of):
        self.class_of = class_of
    
    def get_class_of(self):
        return self.class_of
    
    def set_major(self, major):
        self.major = major
    
    def get_major(self):
        return self.major
        
s = Student(name = "James")
"""
test your case below, call the methods you created to get desired information
"""
print(s.get_name())
s.set_class_of(2020)
print(s.get_class_of())
s.set_major("Maths")
print(s.get_major())
