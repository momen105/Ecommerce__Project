from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve

# To show media files
#from django.conf import settings
#from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home_App.urls')),
    path('account/', include('Login_App.urls')),
    path('shop/', include('Order_App.urls')),
    path('payment/', include('Payment_App.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)