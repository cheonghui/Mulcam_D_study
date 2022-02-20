[toc]

# Algorithm Study

## 🤖 Let's do it!

백준, 프로그래머스 등에서 문제 선별하여 풀기

- 💻 [이번주 풀어야 할 문제](https://www.notion.so/12de2f1456a04e6abfd89166725456c0)
- 🤓 [풀고 싶은 문제](https://www.notion.so/8d68711b3fb74c5f80a6582af77b9756)





## 초기 설정

1. 팀장이 Repo 생성하여 README 파일 업로드
2. 팀원은 해당 Repo `Fork` 하여 자신의 Repo에서 Repo 주소 복사
3. 터미널에 바탕화면 경로로 이동하여 `git clone <Fork한 Repo주소> <파일명>`
   1. 바탕화면에 파일 생성과 동시에 git init 이 처리됨
4. 터미널 경로를 바탕화면 --> 생성된 폴더로 이동
5. `git remote -v` 하여 `origin <주소>` 2줄이 출력되는지 확인

## 파일 업로드하기

1.  터미널에 생성했던 파일로 이동 (위에서 `<파일명>` 에 해당하는 파일)
2. 터미널에 `git remote add upstream(팀장이 설정한 주소 이름) <원본 Repo 주소>` 입력
3. `git remote -v` 하여  `origin <주소>` 2줄, `upstream <주소>` 2줄이 출력되는지 확인
   1. 2번과 3번은 최초 1회만 하면 되는건지 아닌건지 잘 모르겠음
   2. 할 때마다 해보고 이미 있다는 오류 문구가 나오면 한번만 해도 될 것 같음
4. `git checkout -b <브랜치명>` 으로 새로운 브랜치를 생성하여 원본에 영향이 없게 한다.
5. `git fetch upstream` 으로 Upstream Repo에 변경이 있었는지 확인
6. 있었다면 `git pull` 을 실행시켜 똑같이 반영시킨다.
7. 작업한 파일을 `git add <파일명>` , `git commit -m '<커밋내용>'` , `git push origin <본인이 생성한 브랜치 이름>` 순서로 입력하여 문제풀이 파일을 업로드한다.
   1. 여기서 커밋내용은 위 규칙을 참고 바람
8. 자신의 깃허브로 돌아가서 `Compare & pull request` 를 눌러 원본 Repo에 반영을 요청한다.
9. 누르면 Pull Request 양식이 뜨는데 그 양식은 위 규칙을 참고 바람
10. 양식 바로 위에 Able to merge가 쓰여있으면 오케이!
11. Create Pull Request 누르기