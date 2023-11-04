from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path('', views.search, name='search'),
    path('add_word', views.add_word, name='add_word'),
    path('update_word/<int:id>/', views.update_word, name='update_word')

]
