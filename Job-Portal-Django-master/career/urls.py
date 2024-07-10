from django.urls import path
from career import views

app_name = "career"


urlpatterns = [

    path('careerlist/', views.careerlist, name='careerlist'),
    path('courselist/<str:id>', views.courselist, name='courselist'),
    path('coursedetails/<str:Subject>', views.coursedetails, name='coursedetails'),
    
   
   


]
 