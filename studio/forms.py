from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models

class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            Field('description'),
            HTML(
            	"""<label for='date_expired'>Deadline date*</label>
            		<div class="input-group date">
    					<input id='date_expired' required='true' type="date" name='date_expired' class="form-control">
					</div>
			"""),
            Submit('update', 'Submit', css_class="btn-success"),
            )

    class Meta:
        model = models.Task
        fields = ['name','description','date_expired']