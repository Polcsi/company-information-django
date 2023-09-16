from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# Views
from .views import company_view
from .views import employee_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # Company URLs
    path('company/', company_view.company_list),
    path('company/<int:id>', company_view.company_detail),
    # Employee URLs
    path('employee/', employee_view.employee_list),
    path('employee/<int:id>', employee_view.employee_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
