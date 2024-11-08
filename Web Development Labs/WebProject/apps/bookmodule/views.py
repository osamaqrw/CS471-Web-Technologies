from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.db.models import Min, Max, Sum, Avg, Count
from .models import Address
def index(request):
        name = request.GET.get('name') or 'world!'
        return render(request, 'bookmodule/index.html', {'name' : name})

def index2(request, val1=0):
        return HttpResponse('value1 = '+str(val1))

def viewbook(request, bookId):
        # assume that we have the following books somewhere (e.g. database)
        book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
        book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
        targetBook = None
        if book1['id'] == bookId: targetBook = book1
        if book2['id'] == bookId: targetBook = book2
        context = {'book':targetBook} # book is the variable name accessible by the template
        return render(request, 'bookmodule/show.html', context)

def index(request):
        return render(request, "bookmodule/index.html")

def list_books(request):
        return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
        return render(request, 'bookmodule/one_book.html')

def aboutus(request):
        return render(request, 'bookmodule/aboutus.html')

def links(request):
        return render(request, 'bookmodule/books/html5/links.html')

def formatting(request):
        return render(request, 'bookmodule/books/html5/text/formatting.html')

def listing(request):
        return render(request, 'bookmodule/books/html5/listing.html')

def tables(request):
        return render(request, 'bookmodule/books/html5/tables.html')

def search(request):
        if request.method == "POST":
                string = request.POST.get('keyword').lower()
                isTitle = request.POST.get('option1')
                isAuthor = request.POST.get('option2')
                # now filter
                books = __getBooksList()
                newBooks = []
                for item in books:
                        contained = False
                        if isTitle and string in item['title'].lower(): contained = True
                        if not contained and isAuthor and string in item['author'].lower():contained = True
                        if contained: newBooks.append(item)
                return render(request, 'bookmodule/bookList.html', {'books':newBooks})
        else:
                return render(request, 'bookmodule/books/search.html')

def __getBooksList():
        book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
        book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
        book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
        return [book1, book2, book3]

def createbook(request):
        mybook = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D.Farley', edition = 1)
        mybook.save()
        return HttpResponse('Book created.')

def simple_query(request):
        mybooks=Book.objects.filter(title__icontains='i') # <- multiple objects
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
        mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='i').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
        if len(mybooks)>=1:
                return render(request, 'bookmodule/bookList.html', {'books':mybooks})
        else:
                return render(request, 'bookmodule/index.html')

def lab8_task1(request):
        mybooks=Book.objects.filter(Q(price__lte = 50))
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lab8_task2(request):
        mybooks=Book.objects.filter(Q(edition__gt = 2) & Q(Q(title__contains = 'qu') | Q(author__contains = 'qu')))
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lab8_task3(request):
        mybooks=Book.objects.filter(~Q(edition__gt = 2) & ~Q(Q(title__contains = 'qu') | Q(author__contains = 'qu')))
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lab8_task4(request):
        mybooks=Book.objects.filter().order_by('title')
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lab8_task5(request):
        bookCount = Book.objects.filter().count()
        totalPrice = Book.objects.aggregate(total = Sum('price', default = 0))['total']
        averagePrice = Book.objects.aggregate(average = Avg('price', default = 0))['average']
        maxPrice = Book.objects.aggregate(max = Max('price', default = 0))['max']
        minPrice = Book.objects.aggregate(min = Min('price', default = 0))['min']
        context = {
        'bookCount': bookCount,
        'totalPrice': totalPrice,
        'averagePrice': averagePrice,
        'maxPrice': maxPrice,
        'minPrice': minPrice,
        }
        return render(request, 'bookmodule/books/lab8/task5.html', context)

def lab8_task7(request):
        countCity = Address.objects.annotate(student_count=Count('student'))
    
        context = {'city_counts': countCity,}
        return render(request, 'bookmodule/books/lab8/task7.html', context)
