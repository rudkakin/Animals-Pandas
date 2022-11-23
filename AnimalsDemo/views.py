from django.shortcuts import render
from .models import*
import pandas as pd
import mimetypes
import os
from django.views import View
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import*
import pandas as pd
import json


# Create your views here.
class home:
    def home(request):
        item=Animals.objects.all().values()
        df=pd.DataFrame(item)
        df= df.sort_values(by='Size', ascending=False)
        mydict={
            "df": df.to_html()
        }
    
        return render(request, 'index.html', context=mydict)

class Api(APIView):
    def get(self, request):
        item=Animals.objects.all().values()
        df=pd.DataFrame(item)
        df= df.sort_values(by='Size', ascending=False)
        t = df.to_dict()
        return Response(t)
        
