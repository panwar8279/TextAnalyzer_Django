# i have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # params={'name':'pratigya','place':'Saharanpur'}
    # return render(request,'index.html',params)
    return render(request,'index.html')
    # return HttpResponse("Hello world")
    # return HttpResponse("<h1> Hello")
def analyze(request):
    djtext =request.GET.get('text','default')
    removepunc =request.GET.get('removepunc','off')
    punctuations='''!(),-[]{};:'"/.?@#$%^&*~'''
    analyzed=""
    if removepunc=="on":
      for char in djtext:
         if char not in punctuations:
          analyzed=analyzed+char
          params={'purpose':'Removed punctuatons','analyzed_Text':analyzed}
      return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")



def about(request):
    return HttpResponse("about hello")
def capfirst(request):
    return HttpResponse("captalize first <a href='/'> Back</a>")
def removepunc(request):
    print(request.GET.get('text','default'))
    return HttpResponse("remove punc")



