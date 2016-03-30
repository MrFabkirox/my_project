from django.shortcuts import render

from .forms import SignUpForm

# Create your views here.
def home(request):
    title = "welcome (is variable user is empty)"
    #if request.user.is_authenticated():
    #    title = "My Title %s" %(request.user)

    #add a form
    form = SignUpForm(request.POST or None)

    #if request.method == "POST":
    #    print request.POST

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print instance.email
        print instance.timestamp

    context = {
    #    "template_title": title,
        "title": title,
    #    "abc" : 123,
        "form": form
    }
    return render(request, "home.html", context)
