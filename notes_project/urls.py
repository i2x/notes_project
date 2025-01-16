from django.urls import path, include

urlpatterns = [
    path('', include('notes.urls')),
    path('calculator/', include('calculator.urls')),  
    path('regex/', include('regex.urls')),  # Include regex app URLs


]

