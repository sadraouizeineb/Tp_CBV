from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from view.models import BlogPost
from view.forms import BlogForm
class BlogView(ListView):
    model=BlogPost
    #=BlogPost.objects.all()
    context_object_name='posts'#posts à utiliser dans les pages html
    template_name="Posts/blogView.html"

class BlogCreateWithFields(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'author','created_on']  # Définition des champs
    template_name = "Posts/blogcreate.html"
    success_url = reverse_lazy('Posts:listhtml')
    
    
class BlogCreateWithForm(CreateView):
    model = BlogPost
    form_class = BlogForm  # Utilise le formulaire personnalisé
    template_name = "Posts/blogcreateForm.html"
    success_url = reverse_lazy('Posts:listhtml')
        
class blogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'author','content',]
    pk_url_kwarg = 'pk'  # Le nom de l'URL argument qui contient l'ID de l'objet à mettre à jour
    template_name = "Posts/blogUpdate.html"
    success_url=reverse_lazy('Posts:listhtml')
class blogDeleteView(DeleteView):
    model = BlogPost
    pk_url_kwarg = 'pk'
    template_name = "Posts/blogdelete.html"
    success_url=reverse_lazy('Posts:listhtml')