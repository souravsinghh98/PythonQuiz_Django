from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#email verification
from OnlineQuiz.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.
def home(request):
    show_all = Question.objects.all()
    
    context = {'show_all':show_all}
    return render(request,'QuizApp/home.html',context)

@login_required(login_url='login')
def add(request):
    form = AddQues()
    if request.method=='POST':
        form = AddQues(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Question added successfully!!')
            return redirect('home')
    context = {'form':form}
    return render(request,'QuizApp/addQues.html',context)    

@login_required(login_url='login')
def test(request):
    all = Question.objects.all()
    context = {'all':all}
    return render(request,'QuizApp/test.html',context)



@login_required(login_url='login')
def result(request):
    answers = Question.objects.all()
    
    count=0 
    entered_answer = []
    count_correct_answer = 0
    if request.method=='POST':
        for i,field in enumerate(answers):
            correct_answer = field.correct
            count_correct_answer += 1
            var = request.POST.get(str(field.id))
            entered_answer.append(var)
            print(entered_answer)
            if entered_answer[i] == correct_answer:
                count += 1   
        if request.user.is_active:
            e=Leader.objects.get(user=request.user)
            e.score=count
            print(e.score)
            print(count)
            e.save()  
        
    leaders = Leader.objects.order_by('-score')    
    total_attempt = len(entered_answer)
    for i in entered_answer:
        if i == None:
            total_attempt -= 1              
    context = {'count':count,'total_attempt':total_attempt,'count_correct':count_correct_answer,'leaders':leaders}            
    return render(request,'QuizApp/result.html',context)  


def UserRegistration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        form = CreateUserForm()
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                
                Leader.objects.create(
                    user = user
                )
                
                
                uname = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                ########## mail system #########
                
                subject = 'Welcome to OnlineQuiz'
                message = 'Hi'+uname+'Thanks for using our service.'
                recepient = email
                print(recepient)
                send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently = False)
                
                messages.success(request,'User created successfuly')
                return redirect('login')
            else:
                pass
        context = {'form':form}
        return render(request,'QuizApp/registration.html',context)


def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        
        if request.method=='POST':
            uname = request.POST.get('uname')
            pwd = request.POST.get('pwd')
            user = authenticate(request,username=uname,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Invalid username or password')    
        return render(request,'QuizApp/login.html')
        
                      

def UserLogout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    profile_pic = Leader.objects.get(user=request.user)
    user = request.user
    form = UpdateUser(instance=user)
    if request.method=='POST':
        form = UpdateUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request,'Updated successfully')
    context = {'profile':profile_pic,'form':form}
    return render(request,'QuizApp/profile.html',context)

@login_required(login_url='login')
def profile_pic(request):
    curr_profile = Leader.objects.get(user=request.user)
    form = UpdateProfilePic(instance=curr_profile)
    if request.method=='POST':
        form = UpdateProfilePic(request.POST, request.FILES, instance=curr_profile)
        if form.is_valid():
            form.save()
            messages.info(request,'Profile pic changed')
            return redirect('profile')
    context = {'form':form,'profile':curr_profile}
    return render(request,'QuizApp/change_pic.html',context)    

@login_required(login_url='login')
def leader_profile(request,pk):
    leaders = Leader.objects.get(id=pk)
    context = {'leaders':leaders}
    return render(request,'QuizApp/leader.html',context)
       


   


