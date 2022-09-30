from django.http import HttpResponse
from django.shortcuts import render
from timer.models import exam,section

# Create your views here.
def myHome (request) :
    examList = exam.objects.all()
    context = {"exams": examList}
    return render(request,'home.html', context)
    #return  HttpResponse("hello world")

def myTable (request,id) :
#select * from timer_section where test_id=1 order by  "order"
    examSection = section.objects.filter(test_id=id).order_by('order')
    context = {"sections":examSection}
    print(examSection.query)
    return render(request,'sections.html', context)

def myTimer (request,testId,order) :
#select * from timer_section where test_id=1 order by  "order"
    examSection = section.objects.filter(test_id=testId,order=order)
    context = {"section":examSection}
    print(examSection.query)
    return render(request,'timing.html', context)

def myTimer1 (request,sectionId) :
#select * from timer_section where test_id=1 order by  "order"
    examSection = section.objects.filter(id=sectionId)
    context = {"section":examSection}
    print(examSection.query)
    return render(request,'timing.html', context)
    
    