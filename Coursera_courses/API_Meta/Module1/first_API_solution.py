#Shell commands
# Activate virtual environment using pipenv
# pipenv shell
# pipenv install
#
# # Making migrations
# python3 manage.py makemigrations
# python3 manage.py migrate

#Solution code for models.py
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]



from django.urls import path
from . import views

urlpatterns = [
    path('books',views.books),
    # path('books/<int:pk>',views.book),
]

# Solution code for urls.py (app-level):

#Solution code for urls.py (app-level)
from django.urls import path
from . import views

urlpatterns = [
    path('books',views.books),
]

#Solution code for views.py
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.
@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"books":list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(book), status=201)