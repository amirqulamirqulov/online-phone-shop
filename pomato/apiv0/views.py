from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from phones.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializer import *

# Create your views here.

def test_api_view(request):
    phone = Phone.objects.first()
    f_b = {
        'brand': phone.brand.name,
        'name' : phone.name,
        'ram' : phone.ram,
        'memory': phone.memory,
        'price': phone.price,
    }
    return JsonResponse(f_b)

@api_view (['GET', 'POST', 'PUT', 'DELETE'])
def phone_api_view(request, pk = 0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data = PhoneSerializer(instance=Phone.objects.all(), many = True).data, status=200)
        else:
            the_phone = get_object_or_404(Phone, pk = pk)
            return Response(data = PhoneSerializer(instance= the_phone).data, status=200)
    elif request.method == 'POST':
        ps = PhoneSerializer(data = request.data)
        if ps.is_valid():
            ps.save()
            return Response({'id': ps.instance.id}, status=201)
        else:
            return Response(ps.error_messages, status=406)
    elif request.method == 'PUT':
        the_phone = get_object_or_404(Phone, pk = pk)
        ps = PhoneSerializer(data = request.data, instance=the_phone)
        if ps.is_valid():
            ps.save()
            return Response('Updated', status=200)
        else:
            return Response(ps.error_messages, status=406)
    else:
        the_phone = get_object_or_404(Phone, pk = pk)
        the_phone.delete()
        return Response('Delete', status=200)

class PhoneListAPIView(ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneCreateAPIView(CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneUpdateAPIView(UpdateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneDestroyAPIView(DestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

       



