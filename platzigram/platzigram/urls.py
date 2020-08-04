
from django.urls import path
from django.conf import settings 
from django.contrib import admin
from platzigram import views as local_views
from posts import views as posts_views
from django.conf.urls.static import static
from users import views as users_views


urlpatterns = [
    #path('hello-world/', platzigram_views.hello_world),
    #path('hi/', views.hi),
    #path('hiyou/<str:name>/<int:age>/',views.say_hi),

    path('admin/', admin.site.urls),

    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),

    path('', posts_views.list_posts, name='feed'),
    path('posts/new/', posts_views.create_post, name='create_post'),
    
    path('users/signup/', users_views.signup, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
