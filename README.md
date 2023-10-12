## hanghae-eats

## 시작

### 1. 가상환경 설치 및 실행

```
python -m venv venv
venv\Scripts\activate
```

### 2. 라이브러리 설치

```
pip install -r requirements.txt
```

### 3. 실행

```
flask run
```

## git branch 만들기.

> branch 이동하기 전 commit & push.

### 1. branch 생성

```
git branch <사용할 브랜치명>
```

### 2. branch 이동

```
git checkout <이동할 브랜치명>
```

### 3. branch 리스트 확인

```
git branch
```

### 4. merge

```
git add .
git commit -m "<커밋 내용>"
git push

git checkout <합칠 브랜치>
git merge <가져올 브랜치명>
```

### 5. jwt 토큰 유효성 검증 및 현재 접속한 user의 email 추출하기

```
from flask import Blueprint, redirect, render_template
from models.user import User

# getUserEmail : 토큰에서 email 추출
# isTokenVaild : 토큰에서 로그인 유효시간 추출하여 아직 로그인 상태가 유효하다면 True, 유효하지않으면 False
from myJWT import getUserEmail, isTokenVaild


bp = Blueprint('myaccount', __name__, url_prefix='/myaccount')

@bp.route('/')
def myaccount():
    # 2 유효성 검증
    if (isTokenVaild() == False):  # 현재 쿠키의 토큰이 유효하지 않으면
        return redirect("/login")  # 다시 로그인 페이지로
    # 3 필요하다면,  user email 토큰에서 꺼내기
    email = getUserEmail()

    # 4. 3 에서 추출한 email은 아래처럼 활용할 수 있습니다.
    user = User.query.filter_by(email=email).first()
    return render_template('myaccount.html', user=user)
```

### 6. dev브랜치로 머지하기전 requirements.txt 업데이트하기
새로 추가한 라이브러리가 있는 경우 다른사람이 작업하기 편하도록 어떤 라이브러리가 필요한지 알려줍시다.

```
pip freeze > requirements.txt
```


### 7. dev브랜치의 내용을 Feature 브랜치로 머지하고 나서 import error가 발생할 경우

필요한 라이브러리가 설치되지 않은 경우입니다.
![image](https://github.com/hanghae17-7/hanghae-eats/assets/93697934/02f6f76c-f630-4db9-a5ac-f952b6dfa235)
vscode 환경에서 위의 사진처럼 requirements.txt 파일에 설치되지 않은 라이브러리를 확인할 수도 있고, 아래 명령어를 입력하여 자동으로 설치할 수도 있습니다.
```
pip install -r requirements.txt
```

**만약 requirements.txt에 있는 모든 라이브러리가 설치되어있는 경우라면 누군가 실수로 6.번의 과정을 하지 않은거니까 에러메세지 보고 합시다..

