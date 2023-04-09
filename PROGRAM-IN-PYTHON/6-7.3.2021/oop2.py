class Student:
    School = "Abhinav"
    def __init__(self,no1,no2,no3):
       self.m1 = no1
       self.m2 = no2
       self.m3 = no3

    def Instance_total(self):
       print("Inside Instance Method")
       return self.m1 + self.m2 + self.m3

    @classmethod
    def Class_DisplaySchool(cls):
       print("School Name :",cls.School)

    @staticmethod
    def Static_Info():
       print("This class cantains the information of school")

def main():
    Student.Class_DisplaySchool()
    obj1 = Student(55,88,77)
    obj2 = Student(51,80,67)
    ret = obj1.Instance_total()
    print("Total obtaned  marks",ret) 
    Student.Static_Info()



if __name__ == "__main__":
    main()