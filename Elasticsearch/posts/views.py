from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from posts.models import *
from .documents import *
from .serializers import *
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)

def generate_random_data():
    url = 'https://newsapi.org/v2/everything?q=apple&from=2023-09-29&to=2023-09-29&sortBy=popularity&apiKey=df41c1532d434d099582aec0d04e92bc'
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    for data in payload.get('articles'):
        ElasticDemo.objects.create(
            title = data.get('title'),
            content = data.get('description')            
        )

def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200})


class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'first_name'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
   
    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
       'title',
        'content',
    )
    filter_fields = {
       'title' : 'title',
        'content' : 'content',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,)
        
  
