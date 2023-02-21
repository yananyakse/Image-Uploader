from django.shortcuts import render
from . models import Upload
from . forms import Images

# Create your views here.
def index(request):
    if request.method == 'POST':
        forms = Images(data=request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            ins = forms.instance
            return render(request, 'index.html', {'ins':ins})
    else:
        forms = Images()
    rep = Upload.objects.all()
    return render(request, 'index.html',{'forms':forms, 'rep':rep})