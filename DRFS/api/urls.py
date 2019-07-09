from django.urls import path,include
from .views import (
                     APIView,
                     StatusListAPIView,
                     StatusDetailAPIView)




urlpatterns = [
       path('',StatusListAPIView.as_view(),name='list'),
       # path('create/',StatusCreateAPIView.as_view(),name='create'),
       path('detail/<int:pk>/',StatusDetailAPIView.as_view(),name='detail'),
       # path('delete/<int:pk>/',StatusDeleteAPIView.as_view(),name='delete'),
       # path('update/<int:pk>/',StatusUpdateAPIView.as_view(),name='update'),

]
