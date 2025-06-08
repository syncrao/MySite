from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        print(f"username: {username_or_email}, password: {password}")

        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            return render(request, './auth/login.html', {'error': 'Invalid credentials'})

    return render(request, './auth/login.html')



def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('date_of_birth')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, './auth/register.html', {'error': "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, './auth/register.html', {'error': "Username already taken"})

        if User.objects.filter(email=email).exists():
            return render(request, './auth/register.html', {'error': "Email already registered"})

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=dob,
            password=password1
        )

        return redirect('login')  

    return render(request, './auth/register.html')

def logout_view(request):
    logout(request)
    return redirect('index')