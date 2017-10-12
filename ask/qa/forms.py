from django import forms
from .models import Question, Answer
from django.shortcuts import get_object_or_404

class AskForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)

    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        data_title = self.cleaned_data['title']

        clear_title = data_title.strip()
        if clear_title == "":
            raise forms.ValidationError(u"Title is empty")

        return data_title

    def clean_text(self):
        data_text = self.cleaned_data['text']

        clear_text = data_text.strip()

        if clear_text == "":
            raise forms.ValidationError(u"Text is empty")

        return data_text


    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(forms.HiddenInput)

    def clean_text(self):
        data_text = self.cleaned_data['text']

        clear_text = data_text.strip()
        if clear_text == "":
            raise forms.ValidationError(u"Text answer is empty")

        return data_text

    def clean_question(self):

        data_question = self.cleaned_data['question']

        try:
            int_question = int(data_question)
        except ValueError:
            raise forms.ValidationError(u"Invalid question")

        return int_question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(Question,
                                                          pk=self.cleaned_data['question'])

        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer



