from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# Views
from .views import company_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', company_view.company_list),
    path('company/<int:id>', company_view.company_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
