from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from film.views import (
    main_view, 
    FilmListView,
    FilmDetailView,
    ActorListView,
    ActorDetailView,
    ReviewCreateView,
    FilmCreateView
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view),

    path("films/", FilmListView.as_view(), name="films_list"),
    path("films/create/", FilmCreateView.as_view(), name="film_create"),
    path("films/<int:film_id>/", FilmDetailView.as_view(), name="film_detail"),
    path("films/<int:film_id>/review/", ReviewCreateView.as_view(), name="review_create"),

    path("actors/", ActorListView.as_view(), name="actors_list"),
    path("actors/<int:actor_id>/", ActorDetailView.as_view(), name="actor_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
