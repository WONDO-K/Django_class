from django import forms
from.models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):

    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'Enter the title',
                'maxlength' : 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content',
                'place' : 'Enter the content',
                'row' : 5,
                'cols' : 50,
            }
        ),
        error_messages={'required' : '내용을 입력해주세요'}
    )

    class Meta:
        model = Article # 어떤 모델연동? 
        fields = '__all__' # 사용자가 입력하는 부분들 전체 인식
