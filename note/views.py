from django.shortcuts import render

# Create your views here.
notes = []

def home_page(request):
    global notes

    if request.method == "POST":

        if "add" in request.POST:
            new_note = request.POST.get("notes-input")

            notes.append(new_note)

            print(new_note)
            print(notes)

    return render(
        request,
        template_name="index.html",
        context={
            "notes":notes,
        }
    )
