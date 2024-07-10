from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import *

# Create your views here.

def careerlist(request):
    qulificationmodel = qulificationRfeild.objects.all() 
    print(qulificationmodel,'dxfcgvhbjnkml')
    return render(request, 'career/Careerguidance.html', {'qulificationmodel': qulificationmodel})

def courselist(request,id):
    print(id,'id')
    Branchmodel = Branch.objects.filter(qualification=id).all() 
    return render(request, 'career/course.html',{'Branchmodel':Branchmodel})

def coursedetails(request,Subject):
    print(Subject,'Subject')
    detailsmodel=CourseDetails.objects.filter(course=Subject).all()
    return render(request, 'career/coursedetail.html',{'detailsmodel':detailsmodel})