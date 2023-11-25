from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("一定学好django!")


def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")