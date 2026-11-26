from django import forms


class AssistantForm(forms.Form):

    user_text = forms.CharField(
        label="Enter your text",
        min_length=3,
        max_length=2000,
        widget=forms.Textarea(
            attrs={"rows": 6, "placeholder": "Write something here..."}
        ),
    )

    ACTION_CHOICES = [
        ("summarize", "Summarize"),
        ("explain", "Explain"),
    ]

    action = forms.ChoiceField(choices=ACTION_CHOICES, label="Select Action")
