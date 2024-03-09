from django.urls import path
from teachapp.views import *

urlpatterns = [
    path('homet', homet,name='homet'),
    path('teacher',teacher, name='teacher'),
]