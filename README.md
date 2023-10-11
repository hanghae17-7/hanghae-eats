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