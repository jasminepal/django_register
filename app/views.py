from django.shortcuts import render

# view for register page
def RegisterPage(request):
    return render(request, "app/register.html")