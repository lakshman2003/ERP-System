from django.db import models

class department(models.Model):
    department_id = models.CharField(max_length=200, primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.department_id

class student(models.Model):
    student_id = models.CharField(max_length=200, primary_key=True,unique=True,null=False)
    name = models.CharField(max_length=200, null = False)
    department_id = models.ForeignKey(department,on_delete=models.CASCADE)
    email = models.CharField(max_length=200, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    dob = models.DateField(null = False)
    username = models.CharField(max_length=20, null=False, unique = True)
    password = password = models.CharField(max_length=15, null=False)
    def __str__(self):
        return self.student_id

class faculty(models.Model):
    faculty_id = models.CharField(max_length=200, primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=200, null=False)
    department_id = models.ForeignKey(department, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=False, unique=True)
    password = password = models.CharField(max_length=15, null=False)
    def __str__(self):
        return self.faculty_id

class course(models.Model):
    course_id = models.CharField(max_length=200, primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=200, null=False)
    credits = models.IntegerField(null = False)
    faculty_id = models.ForeignKey(faculty, on_delete=models.CASCADE)
    course_dept_id = models.ForeignKey(department, on_delete=models.CASCADE)
    def __str__(self):
        return self.course_id

class enrollment(models.Model):
    enrollment_id = models.CharField(max_length=200, primary_key=True, null=False)
    student_id = models.ForeignKey(student, on_delete=models.CASCADE,null = False)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE,null = False)
    grade = models.TextField(null=False, choices=[(
        "EX", "EX"), ("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("P", "P"), ("F", "F")])
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student_id', 'course_id'], name='unique_student_course'
            )]
        
    def __str__(self):
        return self.enrollment_id

# class student_credential(models.Model):
#     username = models.CharField(max_length=200, primary_key=True, unique=True, null=False)
#     password = models.CharField(max_length=15, null=False)
#     student_id = models.ForeignKey(student, on_delete=models.CASCADE,unique=True)
#     def __str__(self):
#         return self.username
    

# class faculty_credential(models.Model):
#     username = models.CharField(
#         max_length=200, primary_key=True, unique=True, null=False)
#     password = models.CharField(max_length=15, null=False)
#     faculty_id = models.ForeignKey(faculty, on_delete=models.CASCADE,unique=True)

#     def __str__(self):
#         return self.username

