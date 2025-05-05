from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from space.models import Post
from users.models import Student


# Create your views here.
@login_required(login_url='student-login')
def home_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def student_login_view(request):
    message = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            message = messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form': form, 'message': message})

def create_post_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')

        try:
            student = Student.objects.get(id=request.user.id)
        except Student.DoesNotExist:
            return HttpResponse("Faqat studentlar post yarata oladi", status=403)

        post = Post.objects.create(title=title, image=image, user=student)
        post.save()
        return redirect('home')
    return render(request, 'create-post.html')