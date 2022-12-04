from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from first_blog import settings
from app_blog import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', cache_page(60)(views.HomePage.as_view()), name='home'),
    path('about/', views.about, name='about'),
    path('add_review/', views.AddReview.as_view(), name='add_review'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', views.ShowReview.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.FilmReviewCategory.as_view(), name='category'),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


