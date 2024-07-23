from django.urls import path
from .views import RectangleDetectView


urlpatterns = [
    path('detect/', RectangleDetectView.as_view(), name='rectangle_detect'),
]
