from django.views.generic import ListView
from django.utils import timezone
from datetime import timedelta
from app.models import BlogPost

class RecentPostsView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'  # Specify your template
    context_object_name = 'posts'        # Name of the context variable in the template

    def get_queryset(self):
        thirty_days_ago = timezone.now() - timedelta(days=30)
        return BlogPost.objects.filter(published_date__gte=thirty_days_ago).order_by('-published_date')
class ReviewView()