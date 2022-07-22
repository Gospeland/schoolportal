from dataclasses import fields
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, FormView, ListView, View, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login
from profiles.models import CustomUser, Apply, Exam, Logo, Student_field, Staffdata as StaffdataModel, Studentdata, Allcourses, Teachers
from studentportal.models import TrialUser
from .forms import  Applyform, Examform, Register, Staffproform, Studentproform
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin



class AdmissionStat(LoginRequiredMixin, ListView):
    model = Apply
    template_name ='admissionstat.html'
    context_object_name ='applicantlist'
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['applicants'] = context['applicantlist'].filter(nickname=self.request.user)
        context['logo'] = Logo.objects.all()

        return context
    

class Applicantlist(LoginRequiredMixin, ListView):
    model = Apply
    template_name ='allapplicants.html'
    context_object_name ='applicantlist'
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()

        return context
    
class ApplicantlistDetail(LoginRequiredMixin, DetailView):
    model = Apply
    template_name ='allapplicantsdetail.html'
    context_object_name ='applicantsdetail'
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()

        return context    
    
    
class Register(LoginRequiredMixin,  FormView):
    form_class = Register
    template_name = 'portalregister.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('portal')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(
            form.cleaned_data["password"]
        )
        user=form.save(commit=True)
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'portallogin.html'
    fields = '__all__'
    redirect_authenticated_user = True


class CustomLogout(LogoutView):
    pass


class Createstudentdata(LoginRequiredMixin,  CreateView):
    model = Studentdata
    fields = ['firstname', 'lastname', 'email', 'phone', 'state', 'study_field', 'student_class', 'class_form', 'student_image']
    #form_class = Studentproform
    template_name = 'createstudentdata.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('studentprofile')

    def form_valid(self, form):
        form.instance.nickname = self.request.user
       # self.request.user =form.save(commit=True)  //Use this when using form_class and forms.py
        return super(Createstudentdata, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.model.objects.filter(nickname=self.request.user).exists():
            return redirect('studentprofile')
        else:
            return super(Createstudentdata, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()

        return context


class Updatestudentdata(LoginRequiredMixin,  UpdateView):
    model = Studentdata
    form_class = Studentproform
    template_name = 'createstudentdata.html'

    def form_valid(self, form):
        form.instance.nickname = self.request.user
        return super(Updatestudentdata, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()

        return context

    def get_success_url(self):
        return reverse_lazy('studentprofile')


class Portal(  ListView):
    model = Student_field
    template_name = 'portal.html'
    context_object_name = 'studentfields'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()

        return context


class Staffdata(LoginRequiredMixin, ListView):
    model = StaffdataModel
    form_class = Staffproform
    template_name = 'staffdata.html'
    context_object_name = 'staffdata1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staffdata'] = context['staffdata1'].filter(nickname=self.request.user)
        context['mycourses'] = Allcourses.objects.filter(tic_username=self.request.user)
        context['logo'] = Logo.objects.all()

        return context
    
class ApplicationForm(LoginRequiredMixin, FormView):
    model = Apply
    form_class = Applyform
    template_name = 'application.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('admissionstat') 
    
    def form_valid(self, form):
        form.instance.nickname = self.request.user
        return super(ApplicationForm, self).form_valid(form)

   
    def get(self, *args, **kwargs):          
        if self.model.objects.filter(nickname=self.request.user).exists():
            return redirect('admissionstat')
        else:
            return super(ApplicationForm, self).get(*args, **kwargs)   
 
    def form_valid(self, form):
        form.instance.nickname = self.request.user
        self.request.user = form.save()
        if self.request.user is not None:
            self.request.user = form.save(commit=False)
        return super(ApplicationForm, self).form_valid(form)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()
        
        return context
      

class Createstaffdata(LoginRequiredMixin,  FormView):
    model = StaffdataModel
    form_class = Staffproform
    template_name = 'createstaffdata.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('staffprofile') 


    def get(self, *args, **kwargs):          
        if self.model.objects.filter(nickname=self.request.user).exists():
            return redirect('staffprofile')
        else:
            return super(Createstaffdata, self).get(*args, **kwargs)   
 
    def form_valid(self, form):
        form.instance.nickname = self.request.user
        self.request.user = form.save(commit=True)
        return super(Createstaffdata, self).form_valid(form)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()
        
        return context
    


    

class Updatestaffdata(LoginRequiredMixin,  UpdateView):
    model = StaffdataModel
    form_class = Staffproform
    template_name = 'createstaffdata.html'
    context_object_name ='staffdata'

    def form_valid(self, form):
        form.instance.nickname = self.request.user
        return super(Updatestaffdata, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()

        return context

    def get_success_url(self):
        return reverse_lazy('staffprofile')


class Studentdata(LoginRequiredMixin,  ListView):
    model = Studentdata
    template_name = 'studentdata.html'
    context_object_name = 'studentdata'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['studentdata1'] = context['studentdata'].filter(nickname=self.request.user)
        context['logo'] = Logo.objects.all()
        context['userdata'] = CustomUser.objects.filter(username= self.request.user)#for showing real student data from user details
        context['studentexams'] = Exam.objects.filter(student_username =self.request.user)

        return context




class Staffdashboard(LoginRequiredMixin,  View):
    def get(self, request):
        return render(request, 'staffdashboard.html')

    '''def get(self, request):
        if request.user.is_teacher or request.user.is_superuser:
            return render(request, 'staffdashboard.html')
        return render('register')'''


class Studentdashboard(View):
    def get(self, request):
        return render(request, 'studentdashboard.html')



    

        
class Examresultteacher(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'examscores.html'
    context_object_name ='examscores'
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['examscores'] = context['examscores'].filter(teacher_username=self.request.user)
        context['logo'] = Logo.objects.all()


        return context    
    
class CreateExam(LoginRequiredMixin, FormView):
    model = Exam
    form_class = Examform
    template_name = 'newscores.html'
    
    def get_success_url(self):
        return reverse_lazy('newexamscores') 
    
    def form_valid(self, form):
        form.instance.teacher_username = self.request.user   
        return super(CreateExam, self).form_valid(form)
   
    def form_valid(self, form):
        self.request.user = form.save()
        if self.request.user is not None:
            self.request.user = form.save(commit=False)
        return super(CreateExam, self).form_valid(form)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()
        
        return context       
    
    
class Viewscores(LoginRequiredMixin,  ListView): 
    model = Exam
    template_name = 'viewscores.html' 
    
    def get_context_data(self, **kwargs):   
            context = super().get_context_data(**kwargs)
            context['logo'] = Logo.objects.all()
            context['studentexams'] = Exam.objects.filter(student_username =self.request.user)
            
            return context          
        
