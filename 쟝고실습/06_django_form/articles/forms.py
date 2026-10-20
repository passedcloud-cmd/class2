from django import forms

# class ArticleForm(forms.Form):
#     # 사용자로부터 입력받을 필드를 정의
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

from .models import Article

# 게시판을 다룰 거니까 ModelForm이 더 적합함
# ModelForm 정의
class ArticleForm(forms.ModelForm):
    # Meta 클래스는 그저 ModelForm의 설정 값을 작성하는 곳일 뿐이다. 
    class Meta:
        model = Article #호출하지 말고 이름만 등록
        fields = '__all__'