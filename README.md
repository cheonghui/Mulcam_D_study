[toc]

# Algorithm Study

## 🤖 Let's do it!

백준, 프로그래머스 등에서 문제 선별하여 풀기

- 💻 [이번주 풀어야 할 문제](https://www.notion.so/12de2f1456a04e6abfd89166725456c0)
- 🤓 [풀고 싶은 문제](https://www.notion.so/8d68711b3fb74c5f80a6582af77b9756)

## 🤙🏻 Convention

🍒 Code

- 코드마다 이 코드가 어떤 목적으로 작성되었는지 주석을 단다.
- 변수와 함수 이름은 어떤 역할을 하는지 알 수 있도록 한다.
- code 마지막 줄은 한 줄 비운다. (add, commit 하기 전에 확인 요망) 
- code 파일명은 되도록 공백 없이 작성 (예) BOJ_10000.py

🍒 Commit

- 한번에 `gitt add .` 하지 말고 각각 type에 맞게 분리하도록 한다.

```
docs : README.md 등 문서 작성 및 수정
code : 코드 작성
fix : 코드 수정
add : 기존 문제에 대한 또 다른 풀이방법 코드 추가
merge : 내 레포에서 올린 pull request를 현재 Mulcam_D_study 레포에 합치기
```

- 예

```
git commit -m 'code : 본인이름_문제플랫폼_문제번호_문제유형'

<문제 코드>
git add BOJ_10000.py
git commit -m 'code_Jiho_BOJ_10000'
```

🍒 Pull Request

- 제목

  - 본인이름 \_문제플랫폼\_문제번호\_문제유형

- 메시지

  - 간단한 코드 리뷰
  - 주의깊게 봤으면 하는 내용
  - 강조하거나 중요한 내용
  - 해결이 안 될 때 피드백을 부탁하는 내용 등
  - 자신이 전달하고자하는 내용이 들어가는 것을 지향합니다.

  

🍒 Review

- 다른 팀원 풀이 보고 간단한 피드백이나 느낀점도 좋아요!
- 같은 문제여도 풀이는 다양하니까요!!!





## 초기 설정

1. 팀장이 Repo 생성하여 README 파일 업로드
2. 팀원은 해당 Repo `Fork` 하여 자신의 Repo에서 Repo 주소 복사
3. 터미널에 바탕화면 경로로 이동하여 `git clone <Fork한 Repo주소> <파일명>`
   1. 바탕화면에 파일 생성과 동시에 git init 이 처리됨
4. 터미널 경로를 바탕화면 --> 생성된 폴더로 이동
5. `git remote -v` 하여 `origin <주소>` 2줄이 출력되는지 확인
6. 터미널에 `git remote add upstream(팀장이 설정한 주소 이름) <원본 Repo 주소>` 입력
7. `git remote -v` 하여  `origin <주소>` 2줄, `upstream <주소>` 2줄이 출력되는지 확인
   1. 2번과 3번은 최초 1회만 하면 되는건지 아닌건지 잘 모르겠음
   2. 할 때마다 해보고 이미 있다는 오류 문구가 나오면 한번만 해도 될 것 같음

## 파일 업로드하기

1.  터미널에 생성했던 파일로 이동 (위에서 `<파일명>` 에 해당하는 파일)
2. 본인의 이름 파일로 이동
3. `git checkout -b <브랜치명>` 으로 새로운 브랜치를 생성하여 원본에 영향이 없게 한다.
4. `git fetch upstream` 으로 Upstream Repo에 변경이 있었는지 확인
5. 있었다면 `git pull` 을 실행시켜 똑같이 반영시킨다.
6. 작업한 파일을 `git add <파일명>` , `git commit -m '<커밋내용>'` , `git push origin <본인이 생성한 브랜치 이름>` 순서로 입력하여 문제풀이 파일을 업로드한다.
   1. 여기서 커밋내용은 `위 규칙` 을 참고 바람
7. 자신의 깃허브로 돌아가서 `Compare & pull request` 를 눌러 원본 Repo에 반영을 요청한다.
8. 누르면 Pull Request 양식이 뜨는데 그 양식은 `위 규칙` 을 참고 바람
9. 양식 바로 위에 Able to merge가 쓰여있으면 오케이!
10. Create Pull Request 누르기

