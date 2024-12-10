from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),  # Add the accounts app URLs
    path('api/', include('Repo-A.add_users.urls')),
    path('api/', include('Repo-B.delete_users.urls')),
]
