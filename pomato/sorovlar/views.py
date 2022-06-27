from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.views.generic import * 

# Create your views here.

def phone(request):

    authors = Author.objects.all()
    ctx = {'author' : authors}
    return render(request, 'phone.html', context=ctx)

def add_phone(request, pk = 0):
    if request.method == 'GET':

        if pk == 0:
            return render(request, template_name='add_phone.html')
        else:
            author = get_object_or_404(Author, pk = pk)
            ctx = {'author': author}
            return render(request, template_name='add_phone.html', context=ctx)  

    elif request.method == 'POST':
        if pk == 0:
            data = request.POST
            auth = Author(
                name = data['name'],
                email = data['email'],
            )
            auth.save()
        else:
            data = request.POST
            auth = Author.objects.get(pk=data['pk'])
            auth.name = data['name']
            auth.email = data['email']
            auth.save()

        return redirect( 'phone')


def delete_phone(request, pk):
    if request.method == 'GET':
        authors = get_object_or_404(Author, pk = pk)
        ctx = {'author': authors}
        return render(request, template_name='delete_authors.html', context=ctx)
    else:
        pk = request.POST.get('pk')
        print(pk)
        authors = get_object_or_404(Author, pk = pk)
        authors.delete()
        return redirect('phone')



class AuthorListView(ListView):
    queryset = Author.objects.all()
    template_name = "author.html"
    context_object_name = "author"

class AuthorCreateView(CreateView):
    queryset = Author.objects.all()
    template_name = "author_add.html"
    fields = "__all__"

    success_url = "/author"

class AuthorUpdateView(UpdateView):
    queryset = Author.objects.all()
    template_name = "author_add.html"
    fields = "__all__"

    success_url = "/author"

class AuthorDeleteView(DeleteView):
    queryset = Author.objects.all()
    template_name = "author_delete.html"
    fields = "__all__"

    success_url = "/author"

