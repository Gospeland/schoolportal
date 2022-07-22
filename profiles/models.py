from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from matplotlib.backend_bases import MouseEvent

TITLE_CHOICE = (
    (1,  'Mr.'), 
    (2,  'Mrs.'), 
    (3,  'Engr.'), 
    (4,  'Prof.'), 
    (5,  'Ms.')
)

STATUS_CHOICE = (
    (1,  'student'), 
    (2,  'teacher')
)


class CustomUser(AbstractUser):
    phone = models.IntegerField(null=True,  unique=True)
    country = models.CharField(max_length=200,  blank=True)
    state = models.CharField(max_length=200,  blank=True)
    is_student = models.BooleanField(default=0)
    is_teacher = models.BooleanField(default=0)
    # status = models.IntegerField(choices=STATUS_CHOICE, default=0,  null=True )
    mailing_address = models.CharField(max_length=200,  blank=True)


class HOD(models.Model):
    title = models.IntegerField(choices=TITLE_CHOICE,  default=0)
    full_name = models.CharField(max_length=200,  null=True)
    slug = models.SlugField(max_length=200,  null=True)

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Head of Department'
        verbose_name_plural = 'Head of Departments'

    def __str__(self):
        return self.full_name


class Departments(models.Model):
    dept_name = models.CharField(max_length=200,  null=True)
    hod = models.ForeignKey(HOD,  on_delete=models.CASCADE)
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['dept_name']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.dept_name


class Staffdata(models.Model):
    nickname = models.ForeignKey(CustomUser,  on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200,  null=True,  blank=True)
    lastname = models.CharField(max_length=200,  null=True,  blank=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    staff_image = models.ImageField(upload_to='media/', null=True)
    state = models.CharField(max_length=200,  )
    dept = models.ForeignKey(Departments,  on_delete=models.CASCADE)
    date_employed = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['nickname']
        verbose_name = 'staffdatum'
        verbose_name_plural = 'staffdata'

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def save(self,  *args,  **kwargs):
        self.slug = slugify(self.nickname)
        super(Staffdata,  self).save(*args,  **kwargs)


class Form(models.Model):
    name = models.CharField(max_length=200,  null=True)
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'

    def __str__(self):
        return self.name


class Level(models.Model):
    class_name = models.CharField(max_length=200,  null=True)
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['class_name']
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.class_name


class Logo(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name



class Student_field(models.Model):
    field_title = models.CharField(max_length=200,  null=True,  blank=True)
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['field_title']
        verbose_name = 'Student Field'
        verbose_name_plural = 'Student Fields'

    def __str__(self):
        return self.field_title

    def save(self,  *args,  **kwargs):
        self.slug = slugify(self.field_title)
        super(Student_field,  self).save(*args,  **kwargs)


class Teachers(models.Model):
    fullname = models.CharField(max_length=200,  null=True,  blank=True)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    staff_name =models.ForeignKey(Staffdata, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)
    
    
    def __str__(self):
        return '{} {}'.format(self.staff_name.firstname, self.staff_name.lastname)

    
class Allcourses(models.Model):
    title = models.CharField(max_length=200,  null=True,  blank=True)
    field = models.ForeignKey(Student_field,  on_delete=models.CASCADE,  null=True)
    teacher_in_charge = models.ForeignKey(Teachers,  on_delete=models.CASCADE,  null=True)
    tic_username = models.ForeignKey(CustomUser, on_delete=models.CASCADE,  null=True)
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title



class Studentdata(models.Model):
    nickname = models.ForeignKey(CustomUser,  on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=200,  null=True,  blank=True)
    lastname = models.CharField(max_length=200,  null=True,  blank=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    state = models.CharField(max_length=200,  )
    date_enrolled = models.DateTimeField(auto_now_add=True)
    study_field = models.ForeignKey(Student_field,  on_delete=models.CASCADE, null=True)
    student_class = models.ForeignKey(Level,  on_delete=models.CASCADE)
    class_form = models.ForeignKey(Form,  on_delete=models.CASCADE,  null=True)
    student_image = models.ImageField(upload_to='media/',  null=True)
    slug = models.SlugField(max_length=100, null=True)

    class Meta:
        ordering = ['slug']
        verbose_name = 'student datum'
        verbose_name_plural = 'students data'

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.firstname)
        super(Studentdata, self).save(*args, **kwargs)
        


class Payment_info(models.Model):
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['paid']

    def __str__(self):
        return self.paid


class RegisterCourses(models.Model):
    my_username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course_name = models.ManyToManyField(Allcourses)
    
        
        
class Exam(models.Model):
    course = models.ForeignKey(Allcourses,   on_delete=models.CASCADE)
    student =models.ForeignKey(Studentdata, on_delete=models.CASCADE)
    student_username=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    teacher_username=models.ForeignKey(CustomUser, on_delete=models.CASCADE,  null = True, related_name='exam_teacher')
    scores = models.IntegerField()
    slug =models.SlugField(max_length=100)
    
    def __str__(self):
        return 'Exam score of {} {}'.format(self.student.firstname, self.student.lastname)

    def save(self,  *args,  **kwargs):
        self.slug = slugify(self.student)
        super(Exam,  self).save(*args,  **kwargs)

class Apply(models.Model):
    nickname = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    middlename = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.DateTimeField()
    nationality = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    class_choice = models.ForeignKey(Level, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, null=True)

    class Meta:
        ordering = ['firstname']
        verbose_name = 'Admission Application'
        verbose_name_plural = 'Admission Applications'
        
    def __str__(self):
        return 'Admission application of {} {} {} for class of {}'.format(self.firstname, self.middlename, self.lastname, self.firstname, self.class_choice.class_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.firstname)
        super(Apply, self).save(*args, **kwargs)
        
class Posts(models.Model):
    title = models.CharField(max_length=100, null=True)
    slug =models.SlugField(max_length=100)
    author =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/')
    
    class Meta:
        ordering = ['post_date']
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)
        