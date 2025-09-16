from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Category, New, User_model
from .forms import NewForm, Users, NewCategory

from django.shortcuts import render, redirect
from .forms import Users, ProfileForm

# Create your views here.
def home_page(request):
    categories = Category.objects.all()
    new = New.objects.all()

    context = {
        'categories': categories,
        'new': new,
    }

    return render(request, 'home.html', context)

def new_page(request, pk):
    new = New.objects.get(id=pk)
    category = Category.objects.get(id=pk)

    context = {
        'category': category,
        'new': new,
    }

    return render(request, 'new.html', context)

def about_page(request):
    return render(request, 'about.html')

def contacts_page(request):
    return render(request, 'contacts.html')

def categories_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'categories.html', context)

def category_page(request, pk):
    category = Category.objects.get(category_name=pk)

    context = {
        'category': category
    }

    return render(request, 'category.html', context)

def add_new(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_news')
    else:
        form = NewForm()

    context = {
        "form": form
    }

    return render(request, 'add_new.html', context)

def add_category(request):
    if request.method == "POST":
        form = NewCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_categories')
    else:
        form = NewCategory()

    context = {
        "form": form
    }

    return render(request, 'add_category.html', context)

def register_user(request):
    if request.method == 'POST':
        user_form = Users(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()  # создаём User

            # создаём профиль и сохраняем аватарку
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('/')
    else:
        user_form = Users()
        profile_form = ProfileForm()

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, 'register.html', context)



def auth_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, 'authentication.html', context)



@login_required
def profile(request):
    if request.method == "POST":
        field = request.POST.get("field")  # какое поле меняем
        value = request.POST.get("value")  # новое значение

        if field in ["first_name", "last_name", "email", "username"]:
            setattr(request.user, field, value)
            request.user.save()
        return redirect("profile")  # перезагрузка страницы

    return render(request, "profile.html")

from django.shortcuts import render, redirect
from .forms import AvatarForm

@login_required
def change_avatar(request):
    profile = request.user.user_model  # связь OneToOne
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = AvatarForm(instance=profile)

    return render(request, "change_avatar.html", {"form": form})



def logout_view(request):
    logout(request)
    return redirect('/')
