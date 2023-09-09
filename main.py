class person :
    name = "shahd"
    age = 17
    
    def is_adult(self):
        if self.age > 18:
          print("You have too much responsibilities")
        elif self.age <18:
          print("Lucky you")
        else:
           print("baby")
    
frist_person = person()
print(frist_person.name)
print(frist_person.age)
frist_person.is_adult()
  
     
class person1 :
    def __inti__(self , name ,age) :
      self.name = name
      self.age = age
    
    def __str__(self):
        return f"My name is {self.name} and I am {self.age}years old "
    
frist_person1= person1()
print(frist_person.name)
