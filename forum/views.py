from django.http import HttpResponseRedirect
from django.views import generic

from .models import Topic, Comment, Category


class TabView(generic.ListView):
    model = Category
    template_name = 'forum/index.html'
    context_object_name = 'categories_list'

    def get_queryset(self):
        """Return published topics."""
        return Topic.objects.order_by('-pub_date')[:]

    def get_context_data(self, **kwargs):
        context = super(TabView, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        context['categories'] = Category.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Topic
    template_name = 'forum/topic_details.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context


class CategoryView(generic.DetailView):
    model = Category
    template_name = 'forum/category_details.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context

def create_topic(request):
    try:
        cat = Category.objects.get(category_name=request.POST['category'])
    except Category.DoesNotExist:
        cat = None

    if cat==None:
        cat = Category(category_name=request.POST['category'])
        cat.save()
    t = Topic(title=request.POST['title'], topic_text=request.POST['topic_text'], user=request.POST['user_name'],
              category=Category.objects.get(category_name=request.POST['category']))
    t.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_comment(request, pk):
    c = Comment(user=request.POST['user'], comment_text=request.POST['text'], topic=Topic.objects.get(pk=pk))
    c.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


