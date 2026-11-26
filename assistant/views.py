from django.shortcuts import render
from .forms import AssistantForm


# Create your views here.
def home(request):
    # user_text = ""
    # action = ""
    result = ""

    if request.method == "POST":
        form = AssistantForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data["user_text"]
            action = form.cleaned_data["action"]

            result = f"Your text: {user_text}\n" f"Selected action: {action}"
    else:
        form = AssistantForm()
    context = {"form": form, "result": result}
    return render(request, "assistant/index.html", context)
    # user_text = request.POST.get("user_text", "").strip()
    # action = request.POST.get("action", "")

    # context = {"user_text": user_text, "action": action}
    # return render(request, "assistant/index.html", context)
