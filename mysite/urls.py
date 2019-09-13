
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from mysite.loginform import views 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
	path('homes',views.homes,name="homes"),

	path('',views.main,name="main"),
	path('finance',views.logo,name="logo"),
    path('trade',views.trade,name="trade"),
	
	path('home',views.home,name="home"),
	path('index',views.index,name="index"),
	
	#path('signup',views.signup,name="signup"),
	path('^oauth/', include('social_django.urls', namespace='social')),
    #path('accounts/  ',include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('loginpage', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
        )
    