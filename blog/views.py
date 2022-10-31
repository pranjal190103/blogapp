from django.http import HttpRequest
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from blog.models import Post
from blog.models import Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import  send_mail
from django.conf import settings
import random
from .forms import CommentForm

#html mail required stuff required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def home(request):
    #load all the post from the db(10)
    posts=Post.objects.all()[:11]
    cats=Category.objects.all()
    data={
        'posts':posts,
        'cats':cats
    }
    return render(request,"home.html",data)

def post(request,url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all()
    print(post)
    if request.method=='POST':
        form=CommentForm(request.POST)
        
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post = post
            comment.save()
    else:
         form=CommentForm()       
    return render(request,"posts.html",{'post':post,'form':form,'cats':cats})           

#  return render(request,'posts.html',{"post":post,'cats':cats})

def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat':cat,'posts':posts})


def signup(request):
    if request.method=="POST":
        # username=request.POST.get('username')
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        
        # content=f'''Welcome to Iblog
        # Hii {fname} hope you are doing well!.
        # our whole team welcomes you to our team and
        #  request you to take paricipate in blog website postively.

        #  Thanks and Regards
        #  Whole IBlogs Team.
        # '''
        to=request.POST.get('email')
        content=f''' {fname} 
         '''
            

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        html_content=render_to_string('emailt.html',{'title':'Welcome Mail','content':content})
        text_content=strip_tags(html_content)
        
        email=EmailMultiAlternatives(
            #subject
            "Testing",
            #content
            text_content,

            #from Enmail
            settings.EMAIL_HOST_USER,
            [to]
            #recepients
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        # send_mail(
        #     #subject
        #     'Welcome to IBlog',
        #     #msg,
        #     content,
        #     #from mail
        #     settings.EMAIL_HOST_USER,
        #     #rec mail
        #     [to],

        # )

        myuser.save()
        messages.success(request,"your account is created")
        return  render(request,'login.html')

    return render(request,'signup.html',{})    

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            posts=Post.objects.all()[:11]
            cats=Category.objects.all()
            data={
            'posts':posts,
            'cats':cats,
            'fname':fname,
            }
            # request.path=" "
            # print(request.path)
            # return  HttpResponse("kdggffgffg")
            return render(request,'home.html',data)
        else:
            messages.error(request,"Bad Credentials")
            # return redirect('signup')  

    return render(request,'login.html',{})      


def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return render(request,'login.html')  

def sendanemail(request):
    if request.method=="POST":
        to=request.POST.get("toemail")
        content=request.POST.get('content')
        
        send_mail(
            #subject
            'testing',
            #msg,
            content,
            #from mail
            settings.EMAIL_HOST_USER,
            #rec mail
            [to],

        )
        return render(
            request,
            'email.html',
            {
                'title':'send an email'
            }
        )

    else:
        return render(request,'email.html',{
            'title':'send an email'
        }
        )    

def contactus(request):
    
    num=random.randrange(1121,9899)
    global str_num
    str_num=str(num)
    if request.method=="POST":
     Name=request.POST.get('Name')
     Email=request.POST.get('Email')
     Description=request.POST.get('Description')
     to='pranjalchaubey001@gmail.com'
     
     html_content=render_to_string('contactusemail.html',{'Name':Name,'Email':Email,'Description':Description})
     text_content=strip_tags(html_content)
        
     email=EmailMultiAlternatives(
            #subject
            "QueryRelated Blogs",
            #content
            text_content,

            #from Enmail
            settings.EMAIL_HOST_USER,
            [to]
            #recepients
        )
     email.attach_alternative(html_content,"text/html")
     email.send()




    # if request.method=="POST":
    #     to='pranjalchaubey001@gmail.com'
    #     content='hii'
        
    #     send_mail(
    #         #subject
    #         'testing',
    #         #msg,
    #         content,
    #         #from mail
    #         settings.EMAIL_HOST_USER,
    #         #rec mail
    #         [to],

    #     )
    return render(request,"contactus.html",{"img":str_num}) 



def submit(request):
    print("aaya")
    if request.method == "POST":
     email=request.POST.get("email")
     password=request.POST.get("pass")
     cap=request.POST.get("captha")
     if str(cap)==str_num :
      return HttpResponse("<h4>YOUR FORM HAS BENN SUBMITED SUCCESSFULLY</h4>")
     else:
        return HttpResponse("<h4>Error captha</h4>")
    else:
     return HttpResponse("<h4>SERVER ERROR</h4>") 


     #payment integration
      
