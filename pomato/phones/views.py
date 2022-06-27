from django.shortcuts import redirect, render
from .models import Brand, Phone
from django.views.generic import * 
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    phone = Brand.objects.all()

    context = {'phones' : phone}

    return render(request, "index1.html", context=context)


def brand(request):
    phone = Brand.objects.all()

    context = {'phones' : phone}

    return render(request, "brand1.html", context=context)

def contact(request):
    return render(request, "contact.html")

def special(request):
    return render(request, "special.html")

def admin(request):
    return render(request, "base_admin.html")

class BrandListView(ListView):
    template_name = "admin1.html"
    context_object_name = 'brands'


    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)

        for key, value in self.last_user_query.items():
            response.set_cookie(key, value)
        return response

        

    def get_queryset(self):


        self.last_user_query = {}

        url_data = self.request.GET
        q = Brand.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains = url_data['name'])
            self.last_user_query['name'] = url_data['name']


        return q

class BrandCreateView(CreateView):
    queryset = Brand.objects.all()
    template_name = "phone_add.html"
    fields = "__all__"

    success_url = "/admin_brand"

class BrandUpdateView(UpdateView):
    queryset = Brand.objects.all()
    template_name = "phone_add.html"
    fields = "__all__"

    success_url = "/admin_brand"

class BrandDeleteView(DeleteView):
    queryset = Brand.objects.all()
    template_name = "phone_delete.html"
    fields = "__all__"

    success_url = "/admin_brand"

class PhoneListView(ListView):
    template_name = "admin2.html"
    context_object_name = 'phones'

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)

        for key, value in self.last_user_query.items():
            response.set_cookie(key, value)
        return response

    def get_queryset(self):


        url_data = self.request.GET

        if len(list(url_data.items())) == 0:
            url_data = self.request.COOKIES

        q = Phone.objects.all()

        self.last_user_query = {}

        if 'brand' in url_data and url_data['brand']:
            q = q.filter(brand__name__icontains = url_data['brand'])
            self.last_user_query['brand'] = url_data['brand']
           

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains = url_data['name'])
            self.last_user_query['name'] = url_data['name']

        if 'ram' in url_data and url_data['ram']:
            q = q.filter(ram__icontains = url_data['ram'])
            self.last_user_query['ram'] = url_data['ram']

        if 'memory' in url_data and url_data['memory']:
            q = q.filter(memory__icontains = url_data['memory'])
            self.last_user_query['memory'] = url_data['memory']

        if 'price' in url_data and url_data['price']:
            q = q.filter(price__icontains = url_data['price'])
            self.last_user_query['price'] = url_data['price']

        return q
    

class PhoneCreateView(CreateView):
    queryset = Phone.objects.all()
    template_name = "add_phones.html"
    fields = "__all__"
    success_url = "/admin_phone"

class PhoneUpdateView(UpdateView):
    queryset = Phone.objects.all()
    template_name = "add_phones.html"
    fields = "__all__"
    success_url = "/admin_phone"


class PhoneDeleteView(DeleteView):
    queryset = Phone.objects.all()
    template_name = "delete_phones.html"
    fields = "__all__"
    success_url = "/admin_phone"

class PhonesListView(ListView):
    queryset = Phone.objects.all()
    template_name = "phones1.html"
    context_object_name = 'phones'

def user_register_view(request):
    if request.method == 'GET':
        form = UserRegisterModelForm()
        return render(request, template_name = 'user_register.html', context = {'form': form})
    else:
        form = UserRegisterModelForm(data = request.POST)
        password = request.POST['password']
        confirm = request.POST['confirm']
        if form.is_valid() and password == confirm:
            form.save()
            user = form.instance

            user.groups.add(Group.objects.get(name = 'Clients'))
            user.save()

            login(request, user)

            return redirect('administration')

        else:
            return render(request, template_name='user_register.html', context={'form':form})


def user_login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, template_name='user_login.html', context = {'form': form})
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username = username, password = password)
        
            if user:
                login(request=request, user = user)
                return redirect('administration')
            else:
                return render(request, template_name="user_login.html", context={'form':form})




