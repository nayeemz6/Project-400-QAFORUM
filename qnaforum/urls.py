from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Users import views
from Users.views import profile_view

admin.site.site_header = "QAFORUM Admin Dashboard"
admin.site.site_title = "QAFORUM ADMIN"
admin.site.index_title = "QAFORUM"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('Users.urls')),
    path('', include('Blog.urls')),
    path('', include('qaadmin.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<username>', views.profile_view, name="profile"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
