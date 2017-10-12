from django import forms
from .models import Question, Answer
from django.shortcuts import get_object_or_404

def is_epmty(some_str, er_mes):
    return (some_str == "", u"Empty %s" % er_mes)

def is_correct_len(some_str, er_mes, max_length = 255):
    return (some_str > max_length, u"To much %s lenght" % er_mes)

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        try:
            data_title = self.cleaned_data['title']
        except KeyError:
            raise forms.ValidationError(u"No title")

        clear_title = data_title.strip()
        errors_list = [is_epmty, is_correct_len]

        for error in errors_list:
            error_res, error_mes = error(clear_title, u"title")
            if error_res:
                raise forms.ValidationError(error_mes)

        return data_title

    def clean_text(self):
        try:
            data_text = self.cleaned_data['text']
        except KeyError:
            raise forms.ValidationError(u"No text")

        clear_text = data_text.strip()
        errors_list = [is_epmty]

        for error in errors_list:
            error_res, error_mes = error(clear_text, u"text")
            if error_res:
                raise forms.ValidationError(error_mes)

        return data_text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(forms.HiddenInput)

    def clean_text(self):
        try:
            data_text = self.cleaned_data['text']
        except KeyError:
            raise forms.ValidationError(u"No text")

        clear_text = data_text.strip()
        errors_list = [is_epmty]

        for error in errors_list:
            error_res, error_mes = error(clear_text, u"text")
            if error_res:
                raise forms.ValidationError(error_mes)

        return data_text

    def clean_question(self):

        try:
            data_question = self.cleaned_data['question']
        except KeyError:
            raise forms.ValidationError(u"No question")

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



