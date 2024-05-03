from django.shortcuts import redirect, render
from django.db import models
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from film.models import Film, Actor, Genre, Review
from film.forms import ReviewForm, FilmForm


def main_view(request):
    return render(request, "main.html")


class FilmListView(ListView):
    model = Film
    template_name = "films/list.html"
    context_object_name = "films"
    paginate_by = 10


class FilmDetailView(DetailView):
    model = Film
    template_name = "films/detail.html"
    context_object_name = "film"
    pk_url_kwarg = "film_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review_form"] = ReviewForm()
        return context


class ActorListView(ListView):
    model = Actor
    template_name = "actors/list.html"
    context_object_name = "actors"

    def get_queryset(self):
        return Actor.objects.all().annotate(rating=models.Avg("films__rating")).order_by("-rating")
    

class ActorDetailView(DetailView):
    model = Actor
    template_name = "actors/detail.html"
    context_object_name = "actor"
    pk_url_kwarg = "actor_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Решение используя Python
        # actor_rating = sum([film.rating for film in self.object.films.all()]) / len(self.object.films.all()) if self.object.films.all() else 0

        # Решение используя Django ORM
        actors_rating = self.object.films.aggregate(models.Avg("rating"))["rating__avg"]

        context["actor_rating"] = actors_rating
        return context


class ReviewCreateView(CreateView):
    model = Review
    fields = ["text", "rating"]
    template_name = "films/detail.html"
    pk_url_kwarg = "film_id"

    def form_valid(self, form):
        film = Film.objects.get(id=self.kwargs["film_id"])
        form.instance.film = film
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("film_detail", kwargs={"film_id": self.kwargs["film_id"]})
    

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = "films/create.html"
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)