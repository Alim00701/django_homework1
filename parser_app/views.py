from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import parser, models, forms
from django.views import generic


class FilmListView(ListView):
    template_name = 'film_list.html'
    queryset = models.Film.objects.all()

    def get_queryset(self):
        return self.queryset


class FilmsDetailView(generic.DetailView):
    template_name = "film_detail.html"

    def get_object(self, **kwargs):
        films_id = self.kwargs.get("id")
        return get_object_or_404(models.Film, id=films_id)


class ParserFormView(FormView):
    template_name = "parser.html"
    form_class = forms.ParseForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return redirect(reverse('parser:film_list'))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
