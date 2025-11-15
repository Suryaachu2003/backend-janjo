from django.urls import path, include

from .views import ProductViewSet



urlpatterns = [path('send',senddata,name='send'),
               path('get',getdata,name='get'), 
               
               path('view-product/',product_page)   
]
