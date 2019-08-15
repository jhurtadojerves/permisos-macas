from django.forms import ModelForm

from .models import Absence


class MyCreateForm(ModelForm):
    class Meta:
        model = Absence
        fields = (
            "employee",
            "absense_type",
            "start_date",
            "end_date",
            "number_of_days",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start_date"].widget.attrs.update({"type": "date"})
        self.fields["end_date"].widget.attrs.update({"type": "date"})
