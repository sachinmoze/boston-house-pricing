from django.urls import path
from . import views


urlpatterns=[
    path("",views.home,name="home"),
    path('predict/', views.predict_view, name='predict'),
    path('predict-medv/', views.predict_medv, name='predict_medv'),
    path('predict-chas/', views.predict_chas, name='predict_chas'),
    
    
]