from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from models import Book,Author
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def ab_bro(request):
    authors = Author.objects.all()
    if request.method == "POST":
        if 'author_name' in request.POST:
            return HttpResponse(request.POST['author_name'])
        if 'allbook' in request.POST:
            return HttpResponseRedirect('/show_all')
        else:
            new_book = Book(
            ISBN = request.POST["ISBN"],
            Title = request.POST["Title"],
            AuthorID = Author.objects.get(AuthorID = request.POST["AuthorID"]),
            Publisher = request.POST["Publisher"],
            PublishDate = request.POST["PublishDate"],
            Price = request.POST["Price"])
            new_book.save()
            return HttpResponseRedirect('/show_all')
            
    return render_to_response("ab_bro.html",{'authors':authors})
    
@csrf_exempt
def author_search(request):
    if request.method == "POST":
        if request.POST:
            post = request.POST
            author_name = post["author_name"]
            """
            author_list = Author.objects.all()
            for author in author_list:
                
                if author.Name == author_name :
                    author_id = author.AuthorID
                    book_list = Book.objects.filter(AuthorID=author_id)
                    c = Context({"book_list":book_list,"author_name":author_name})
                    """
            s = Author.objects.filter(Name = author_name)
            if s:
                author = Author.objects.get(Name = author_name)
                ID = author.AuthorID
                book = Book.objects.filter(AuthorID = ID)
                
                return render_to_response("author_search.html",{'book_list':book,'author':author})
            else:
                return render_to_response("author_search.html")
                   # return render_to_response("author_search.html",c)
    return render_to_response("author_search.html")
 
@csrf_exempt       
def add_author_success(request):
    if request.method == "POST":
        return HttpResponseRedirect("dsf")
        if request.POST:
            post = request.POST
            new_author = Author(
            AuthorID = post["AuthorID"],
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"]
            )
            new_author.save()
            return render_to_response("add_author_success.html")
    
    return render_to_response("add_author_success.html")

@csrf_exempt
def book_info(request,i):
        isbn = i
        book = Book.objects.get(ISBN=isbn)
        if request.method == "GET":
            if 'delete' in request.GET:
                isbn = request.GET['delete']
                book = Book.objects.get(ISBN=isbn)
                book.delete()
                return HttpResponseRedirect('/show_all')
        return render_to_response("book_info.html",{'book':book})

@csrf_exempt
def delete_book(request):
    if request.GET:
        get = request.GET
        book_isbn = get["book_isbn"]
        book = Book.objects.get(ISBN=book_isbn)
        book.delete()
        return render_to_response("delete_book.html")

@csrf_exempt
def add_author(request):
    if request.POST:
            post = request.POST
            new_author = Author(
            AuthorID = post["AuthorID"],
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"]
            )
            new_author.save()

    return render_to_response("add_author.html")

@csrf_exempt
def show_all(request):
    book_list = Book.objects.all()
    c = Context({"book_list":book_list,})
    return render_to_response("show_all.html",c)
    
@csrf_exempt
def add_book(request):
    if request.POST:
        post = request.POST
        return HttpResponse("END")
        author_id = post["AuthorID"]
        new_book = Book(
            ISBN = post["ISBN"],
            Title = post["Title"],
            AuthorID = post["AuthorID"],
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],
            Price = post["Price"]
        )
        author_list = Author.objects.all()
        return HttpResponse("END")
        for author in author_list:
            return HttpResponse(author.AuthorID)
            if author.AuthorID == author_id:
                new_book.save()
                return HttpResponseRedirect("/add_book/")
    else:
        return HttpResponseRedirect("/add_author/")