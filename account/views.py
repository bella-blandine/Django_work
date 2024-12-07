from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.hashers import check_password



def home(request):
    return render(request, 'accounts/home.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()  # Save the user
#             role = form.cleaned_data['role']
#             messages.success(request, "Account created successfully. Please log in.")
#             return redirect('login')  # Redirect to login page
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Save the User instance
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()  # Save the User instance to the database
            
            # Check if a Profile already exists for this User
            profile, created = Profile.objects.get_or_create(
                user=user,  # Link the Profile to the User
                defaults={  # Provide default values only if a Profile does not exist
                    'username': user.username,
                    'password': user.password,  # This should not store raw passwords, but it is your requirement
                    'role': form.cleaned_data['role']
                }
            )
            if not created:
                # If the Profile already exists, update its role to the one from the form
                profile.role = form.cleaned_data['role']
                profile.save()

            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})



# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)  # Log the user in
            
#             # Check the role and redirect to the appropriate home page
#             if hasattr(user, 'profile') and user.profile.role == 'performer':
#                 return redirect('performer_home')  # Adjust to the correct URL for performer home
#             elif hasattr(user, 'profile') and user.profile.role == 'judge':
#                 return redirect('judge_home')  # Adjust to the correct URL for judge home
#             else:
#                 return redirect('home')  # Default fallback if no profile or role
            
#         else:
#             messages.error(request, 'Invalid username or password')
    
#     return render(request, 'accounts/login.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Fetch the user from the User model
            user = User.objects.get(username=username)
            
            # Compare the input password with the stored hashed password
            if check_password(password, user.password):
                # Fetch the associated profile
                try:
                    profile = user.profile  # Accessing the profile through the OneToOne relationship
                    messages.error(request, f"{profile.role}")
                    if profile.role == 'performer':
                        return redirect('/performer')  # Redirect to performer home page
                    elif profile.role == 'judge':
                        return redirect('/judge')  # Redirect to judge home page
                except Profile.DoesNotExist:
                    # Handle the case where the user has no profile
                    messages.error(request, 'No profile found for this user.')
                    return redirect('home')  # Fallback if profile doesn't exist
            else:
                # If the password does not match
                messages.error(request, 'Invalid username or password.')
        except User.DoesNotExist:
            # If the username does not exist
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')