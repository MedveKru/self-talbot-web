from django import forms


class TalbotProcess(forms.Form):
    wavelength = forms.FloatField(label='Wave length', max_value=1000, min_value=0)
    period = forms.FloatField(label='Period', max_value=100, min_value=1)
    phase_shift = forms.FloatField(label='Phase shift', max_value=1000, min_value=0)
    show_z_talbot = forms.BooleanField(label='Show Z')
    z_indent = forms.FloatField(label='Z Indent', max_value=1000, min_value=0)
