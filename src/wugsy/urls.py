from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import questionnaire.urls
import game.urls
import stories.urls
import insights.urls
from game.views import generate_data, game_result
from . import views
from game.views import GamePage, generate_data
from django.contrib import admin

apps = [
    path(r'game', include(game.urls)),
    path(r'questionnaire', include(questionnaire.urls)),
    path(r'insights', include(insights.urls)),
    path(r'accounts', include(accounts.urls)),
    path(r'generate_data', generate_data, name='generate_data'),
    path(r'game_result', game_result, name='game_result'),
]

urlpatterns = [
    path(r'', views.HomePage.as_view(), name='home'),
    path(r'tour', views.TourPage.as_view(), name='tour'),
    path(r'game', include('game.urls')),
    path(r'stories', include('stories.urls')),
    path(r'health', include('health.urls')),
    path(r'generate_data', generate_data, name='generate_data'),
    path(r'admin', admin.site.urls),
    path(r'about', views.AboutPage.as_view(), name='about'),
    #path(r'^users/', include(profiles.urls)),
]
urlpatterns = apps + urlpatterns

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path(r'__debug__', include(debug_toolbar.urls))]
