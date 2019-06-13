from django.shortcuts import render

# Create your views here.
def homeview(request):
    return render(request,"app5/home.html")

def movieview(request):
    return render(request,"app5/movies.html")

def sportview(request):
    return render(request,"app5/sport.html")

def politicsview(request):
    return render(request,"app5/politics.html")

'''

def homesview(request):
    name="arpit sachan"
    brnach="IT"
    age=35
    return render(request,"app5/homes.html")
'''
def cookieview(request):
    count=int(request.COOKIES.get('count',0))
    newcount=count+1
    response=render(request,'app5/demo.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response

def nameview(request):
    return render(request,"app5/name.html")

def ageview(request):
    name=request.GET['name']
    response=render(request,'app5/age.html')
    response.set_cookie('name',name)
    return response

def gfview(request):
    age=request.GET['age']
    response=render(request,'app5/gf.html')
    response.set_cookie('age',age)
    return response

def resultview(request):
    gf=request.GET['gf']
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    return render(request,'app5/result.html',{'name':name,'age':age,'gf':gf})
