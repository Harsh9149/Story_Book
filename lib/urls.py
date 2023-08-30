
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('all/', include('story.urls')),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogin, name="handleLogin"),
    path('signuppage/', views.signuppage, name='signuppage'),
    path('logout', views.handleLogout, name="handleLogout"),

]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

