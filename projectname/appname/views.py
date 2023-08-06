from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,"home.html")




def resume(request):

    return render(request, "resume.html")

def r(request):
    return render(request,"r.html")


def co(request):
    return render(request,"co.html")
def edu(request):
    return render(request,"edu.html")
def ex(request):
    return render(request,"ex.html")
def ho(request):
    return render(request,"ho.html")
def lang(request):
    return render(request,"lang.html")
def sk(request):
    return render(request,"sk.html")

def summary(request):
    if request.method == 'POST':
        # Process the form data from the summary page
        summary_data = request.POST.get('summaryInput', '')

        # Redirect to the final page along with the data using URL parameters
        return redirect(f'/final/?summary_data={summary_data}')

    return render(request, 'summary.html')

def final(request):
    # Retrieve the data from the URL parameters
    summary_data = request.GET.get('summary_data', '')

    # Process the data as needed (e.g., save to a database, manipulate, etc.)

    return render(request, 'final.html', {'summary_data': summary_data})