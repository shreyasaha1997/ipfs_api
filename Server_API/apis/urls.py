from django.conf.urls import url
from . import views
app_name = 'ipfs'
urlpatterns = [
    url(r'^wallet_creation$', views.wallet, name= 'wallet'),
    url(r'^validation$', views.validation, name= 'validation'),
    url(r'^file_upload$',views.file_upload,name= 'file_upload'),
    url(r'^host_count$',views.file_host_count,name= 'file_host_count')
    ]
