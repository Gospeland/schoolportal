from django.contrib import admin
from . models import Posts, Apply,  Logo,  CustomUser, Form, Exam,  Teachers, HOD,  Staffdata, Studentdata, Student_field, Allcourses, Payment_info, Level, Departments
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('username',  'email', 'first_name', 'last_name', 'is_staff', 'is_student', 'is_teacher', 'mailing_address', 'phone', 'state', 'country')
    search_fields =['username', 'status']

    
    fieldsets = ( 
                 ( None, { 'fields': ('username', 'password') }),
                 ('Personal info', { 'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions') }),
                 ('important dates', {'fields': ('last_login', 'date_joined') }),
                 ('Additional info:', {'fields': ('is_student', 'is_teacher', 'mailing_address',  'phone', 'state', 'country')}),
                 
                 )
    
    add_fieldsets = ( 
                 ( None, { 'fields': ('username', 'password1', 'password2') }),
                 ('Personal info', { 'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions') }),
                 ('important dates', {'fields': ('last_login', 'date_joined') }),
                 ('Additional info:', {'fields': ('is_student', 'is_teacher', 'mailing_address', 'phone', 'state', 'country')}),
                 
                 )
  

class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_date', 'author', 'slug']
    prepopulated_fields = {'slug': ('title',)}   
     
     
class FormAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} 
  
    
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['username', 'fullname']
    prepopulated_fields = {'slug': ('fullname',)}


class HODAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'slug']
    prepopulated_fields = {'slug': ('full_name',)}   
    
    
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['dept_name', 'hod', 'slug']
    prepopulated_fields = {'slug': ('dept_name',)}


class LevelAdmin(admin.ModelAdmin):
    list_display = ['class_name',  'slug']
    prepopulated_fields = {'slug': ('class_name',)}
    

class StaffdataAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'email', 'phone', 'dept']
    prepopulated_fields = {'slug': ('nickname',)}
    
    
class Student_fieldAdmin(admin.ModelAdmin):
    list_display = ['field_title', 'slug']
    prepopulated_fields = {'slug': ('field_title',)}
    
    
class AllcoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'field', 'teacher_in_charge']
    prepopulated_fields = {'slug': ('field',)}
    

class  StudentdataAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'email', 'phone', 'student_class', 'slug']    
    prepopulated_fields = {'slug': ('nickname',)}   

   
class Payment_infoAdmin(admin.ModelAdmin):
    list_display = ['paid', ]


class ExamAdmin(admin.ModelAdmin):
    list_display =['student', 'course', 'scores']
    prepopulated_fields = {'slug': ('student',)}
 
class ApplyAdmin(admin.ModelAdmin):
     list_display = ['firstname', 'lastname', 'phone', 'class_choice']
     prepopulated_fields = {'slug': ('firstname',)}
    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Apply, ApplyAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Staffdata, StaffdataAdmin)
admin.site.register(Studentdata, StudentdataAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Student_field, Student_fieldAdmin)
admin.site.register(Allcourses, AllcoursesAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(HOD, HODAdmin)
admin.site.register(Payment_info, Payment_infoAdmin)
admin.site.register(Logo)
admin.site.register(Posts, PostsAdmin)



