from django.shortcuts import render
from app2.models import User
# Create your views here.

def index(request):
    return render(request,'app2/index.html')

def users(request):

    user_list = User.object.order_by('first_name')
    user_dict = {{'users'} : user_list}

    return render(request,'apptwo/user.html',context = user_dict)
