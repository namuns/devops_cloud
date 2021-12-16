from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# ToDo email을 추가로 입력받으려합니다.
# user 모델에 대한 modelForm
# -Meta.fields => ["Username"]
# -추가 form fields => password1, password2
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "email"]
    pass


class LoginForm(AuthenticationForm):
    answer = forms.CharField(

        lable="퀴즈답",
        help_text="3 + 3 = ?",
    )

    def clean_answer(self):
        answer = self.clean_data.get("answer")
        if answer != '6':
            raise forms.ValidationError("떙!!")
        return answer
