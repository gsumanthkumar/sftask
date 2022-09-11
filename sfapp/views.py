import email
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
# Create your views here.

@csrf_exempt
def register(request):
    if not request.method == "POST":
        return JsonResponse({"status" : 400, "error": "Send a post request with valid parameters only."})

    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]    
    email = request.POST["email"]
    mobile_number = request.POST["mobile_number"]
    password = request.POST["password"]

    emails = list(User.objects.values_list('email', flat=True))
    mobile_numbers = list(User.objects.values_list('mobile_number',flat=True))
    if email in emails:
        return JsonResponse({"status" : 400, "error": "Email is already taken by others!"})
    if mobile_number in mobile_numbers:
        return JsonResponse({"status" : 400, "error": "Mobile Number is already taken by others!"})
    if len(password)>4:
        userdata = User(first_name = firstname, last_name = lastname,email=email,mobile_number=mobile_number)
        userdata.set_password(password)
        userdata.save()
        return JsonResponse({"status" : 200, "data": "User Created Succesfully!"})
    else:
        return JsonResponse({"status" : 400, "error": "Password length must be more than 4 characters"})

@csrf_exempt
def create_customer(request):
    if not request.method == "POST":
        return JsonResponse({"status" : 400, "error": "Send a post request with valid parameters only."})
   
    email = request.POST["email"]
    password = request.POST["password"]
    user = User.objects.get(email=email)
    if user is not None:
        if user.check_password(password):
            c = Customer(user=user)
            c.save()
            return JsonResponse({"status" : 400, "error": "Customer Profile is created for user!"})
        else:
            return JsonResponse({"status" : 400, "error": "Invalid Credentials!"})
    else:
        return JsonResponse({"status" : 400, "error": "Email is not registered!"})