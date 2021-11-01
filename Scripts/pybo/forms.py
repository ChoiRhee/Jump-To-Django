from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta: # 사용할 모델과 속성을 적는 클래스
        model = Question
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        lables = {
            'content': '답변'
        }