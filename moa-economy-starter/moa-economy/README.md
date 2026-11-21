# Moa Economy ♡

하루 한 개의 무료 공개 경제 영어 뉴스로 공부하는 GitHub Pages 사이트.

## 시작하기
1. GitHub에서 **moa-economy**라는 새 공개 저장소를 만듭니다. 기존 moa-note 저장소와 분리하세요.
2. 이 ZIP 안의 **내용물 전체**를 새 저장소의 최상위(root)에 업로드합니다. `.github/workflows/daily-news.yml`도 함께 업로드되어야 합니다.
3. Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)` → Save.
4. 주소: `https://mintpink-hub.github.io/moa-economy/`

## 매일 자동 업데이트 활성화
1. GitHub 저장소 Settings → Secrets and variables → Actions → New repository secret.
2. 이름 `OPENAI_API_KEY`에 본인의 OpenAI API 키를 입력합니다. **API는 별도 유료 과금이 발생할 수 있습니다.** ChatGPT 구독과 별개입니다.
3. Actions 탭에서 `Update daily economic English news` → Run workflow로 먼저 테스트합니다.
4. 이후 매일 한국 시간 오전 9:10에 자동 실행되도록 예약되어 있습니다. GitHub Actions 예약 실행은 지연되거나 생략될 수 있으므로 매일 정시 발행을 보장하지 않습니다.

## 참고
- 초기 `news.json`은 **실제 2026-11-21 뉴스가 아닌 기능 확인용 예시**입니다. 자동 업데이트가 성공하면 해당 날짜의 실제 기사 기반 학습 자료로 대체됩니다.
- 자동 생성은 BBC Business RSS에 노출된 제목과 짧은 설명만 근거로 합니다. 기사 전문을 복사하지 않으며 기사 사실과 일반 경제 설명을 혼동하지 않도록 생성 프롬프트를 구성했습니다. 자동 생성 결과는 오류가 있을 수 있습니다.
- BBC 사이트의 기사 접근 가능 여부는 지역·정책에 따라 달라질 수 있으니 무료 접근을 보장하지 않습니다.
- 이전 날짜는 자동 업데이트 이후 저장된 기사만 달력에서 열 수 있습니다.
- 학습 완료 표시는 브라우저 localStorage에 저장되므로 기기 간 동기화되지 않습니다.
