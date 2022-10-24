from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if request.method=="POST":
       user_name= request.POST["username"]
       if user_name =="":
         return render(request,"review.html",{
            "has_error": True
             })

       print(user_name)
       return HttpResponseRedirect("/thankyou")

    return render(request,"review.html",{
        "has_error": False
    })

def thankyou(request):
    return render(request,"thankyou.html")