# ✿ Moa Economy ♡ — 완전 무료 버전

AI, OpenAI API, 유료 번역 API, 패키지 설치 없이 작동합니다.

## 기능
- BBC Business RSS에서 매일 기사 **제목, 짧은 소개, 원문 링크** 1개를 저장합니다.
- 기사 전문을 복사하거나 자동 번역하지 않습니다. BBC 원문에서 공부할 문장을 사용자가 직접 입력합니다.
- 문장별 **구글 번역 작은 별도 창**(브라우저가 새 탭으로 열 수도 있음), 음성 읽기, 해석 작성, 단어 추가
- 날짜별 단어장, 단어 암기 카드, 공부 완료 달력, 백업/복원
- 기록은 현재 브라우저의 localStorage에 저장됩니다. 기기 간 자동 동기화는 없습니다.

## GitHub Pages 설치
1. ZIP 압축을 풀고 **폴더 안의 파일**을 `moa-economy` 저장소 최상위에 업로드합니다. `.github/workflows/daily-news.yml`도 포함하세요.
2. 기존 `index.html`, `news.json`, `update_news.py`, `README.md` 및 `.github/workflows/daily-news.yml`을 **교체**합니다. 이전 AI용 워크플로는 남기지 마세요.
3. Settings → Pages → Deploy from a branch → `main` → `/ (root)` → Save.
4. Actions 탭 → `Daily BBC economy article` → `Run workflow`를 한 번 실행해 첫 실제 BBC 기사를 가져옵니다.
5. 이후 GitHub Actions가 한국 시간 오전 8시 10분 전후로 실행을 시도합니다. GitHub 예약 실행은 지연되거나 누락될 수 있으며, 무료 사용량 정책 및 저장소 권한에 영향을 받습니다.

## 유의사항
- GitHub Actions의 `contents: write` 권한이 필요합니다. 저장소 설정의 Actions Workflow permissions에서 읽기/쓰기 권한을 허용해야 할 수 있습니다.
- RSS는 BBC에서 제공하는 제목/소개만 활용합니다. BBC 콘텐츠의 이용 조건을 지키고 원문을 사이트에 복제하지 마세요.
- RSS가 일시적으로 작동하지 않으면 작업이 실패하며, 마지막으로 저장된 기사가 유지됩니다.
- GitHub Pages의 공개 저장소와 일반적인 개인 사용은 무료 범위로 운영할 수 있지만 GitHub 정책/한도는 바뀔 수 있습니다.
- 개인 공부 기록은 서버로 전송하지 않습니다. 브라우저 데이터 삭제 시 사라질 수 있으니 단어장에서 백업 파일을 저장하세요.
