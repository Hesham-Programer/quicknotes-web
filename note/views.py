from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse

# Create your views here.

class NotesFunction:

    def __init__(self):
        self.notes:list = []

    def add_note(self, note_name:str):

        if note_name in self.notes:
            return False

        self.notes.append(note_name)
        return True

    def delete_note(self, note_index:int):
        del self.notes[note_index]
        print("Done")

    def rename(self, new_note:str, old_note:str):
        if old_note not in self.notes:
            return False

        note_index = self.notes.index(old_note)
        self.notes[note_index] = new_note

        return True

note_function = NotesFunction()

def home_page(request):
    global note_function

    if request.method == "POST":

        if "add" in request.POST:
            new_note = request.POST.get("notes-input")
            note_function.add_note(new_note)

        if "delete" in request.POST:
            note_index = int(request.POST.get("delete"))
            note_function.delete_note(note_index)

        if "rename" in request.POST:
            note_index = int(request.POST.get("rename"))
            note_content = note_function.notes[note_index]
            return redirect(reverse("rename", kwargs={"note_content":note_content}))


    return render(
        request,
        template_name="index.html",
        context={
            "notes":note_function.notes,
        }
    )

def rename(request, note_content):
    global note_function
    if request.method == "POST":

        if "done" in request.POST:
            new_note = request.POST.get("rename")

            if new_note in note_function.notes:
                return HttpResponse(f"This note '{new_note}' name is already exists")

            else:
                note_index = note_function.notes[note_function.notes.index(note_content)]
                note_function.rename(new_note=new_note, old_note=note_index)

                return redirect(reverse("home_page"))

    return render(request, "rename.html", context={"note_content":note_content})