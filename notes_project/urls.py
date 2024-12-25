from django.urls import path, include

urlpatterns = [
    path('', include('notes.urls')),
    path('calculator/', include('calculator.urls')),  # Include calculator app URLs

]

