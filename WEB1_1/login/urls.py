from django.urls import path
from login.views import Index, About, Speakers, Scedule, Gallery, Price, Blog_single, Blog_details, Contact

urlpatterns = [
    path('', Index.as_view()),
    path('index.html', Index.as_view()),
    path('about.html', About.as_view()),
    path('speaker.html', Speakers.as_view()),
    path('event-schedule.html', Scedule.as_view()),
    path('event-gallery.html', Gallery.as_view()),
    path('price.html', Price.as_view()),
    path('blog.html', Blog_single.as_view()),
    path('blog-details.html', Blog_details.as_view()),
    path('contact.html', Contact.as_view()),

]
