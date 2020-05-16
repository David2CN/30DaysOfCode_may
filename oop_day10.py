class Student:
    """
    Students have age weight and height.
    """
    def __init__(self, age, weight, height):
        """Class constructor, a Student has three parameters, age, weight and height
        """
        self.age = age
        self.weight = weight
        self.height = height
        assert type(self.age) == int and type(self.weight) == float and type(self.height) == float and weight > height, "Error, invalid arguments!"
    
    def info(self):
        """
        returns Student age and BMI(weight / height**2)
        """
        return (self.age, (round(self.weight / (self.height ** 2), 2)))
    
    
def average(students):
    """
    This function takes in Student objects and returns the average of their ages, weights and heights.
    """
    x = len(students)
    if x == 0:
        return ()
    total_age, total_weight, total_height = 0,0,0
    for student in students:
        total_age += (student.age + 10)
        total_weight += (student.weight * 1.05 ** 10)
        total_height += (student.height * 1.02 ** 10)  
    return round((total_age) / x, 2), round((total_weight) / x, 2), round((total_height) / x, 2)