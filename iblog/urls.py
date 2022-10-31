"""iblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views # for reset password


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),

    # eset password

    # url name is fixed (taken from django docs)

    path('reset-password/',auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset-password-sent/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # uidb64: The user’s id encoded in base 64.

    # token: Token to check that the password is valid.

    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset-password-complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
