from django.urls import path
from .views import Writer

app_name = 'Employee'
urlpatterns = [
    path('writer/<int:id_>', Writer.as_view(), name='writer'),

]
