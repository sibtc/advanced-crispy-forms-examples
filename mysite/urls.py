from django.urls import path
from django.views.generic import RedirectView

from mysite.core import views


urlpatterns = [
    path('', RedirectView.as_view(url='/form/1/'), name='index'),
    path('form/1/', views.AddressFormView.as_view(template_name='form_1.html'), name='form_1'),
    path('form/2/', views.AddressFormView.as_view(template_name='form_2.html'), name='form_2'),
    path('form/3/', views.AddressFormView.as_view(template_name='form_3.html'), name='form_3'),
    path('form/4/', views.CrispyAddressFormView.as_view(), name='form_4'),
    path('form/5/', views.CustomFieldFormView.as_view(), name='form_5'),
    path('success/', views.SuccessView.as_view(), name='success'),
]
