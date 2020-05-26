
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
    path('posts/', posts_views.list_posts, name='feed')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
