from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse

from .models import News, Choice


class IndexView(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.all()


class NewsDetail(DetailView):
    model = News
    template_name = 'news/detail.html'


class ResultsView(DetailView):
    model = News
    template_name = 'news/results.html'


def vote(request, pk):
    news = get_object_or_404(News, pk=pk)
    try:
        selected_choice = news.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'news/detail.html', {
            'news': news,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('news:results', args=(news.id,)))
