from django.shortcuts import render
from .models import*
import pandas as pd
# Create your views here.
def home(request):
    item=Animals.objects.all().values()
    df=pd.DataFrame(item)
    df= df.sort_values(by='Size', ascending=False)
    mydict={
        "df": df.to_html()
    }
    
    return render(request, 'index.html', context=mydict)