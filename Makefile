# 개발용 FastAPI 서버 실행
dev:
	docker compose -f docker-compose.dev.yml up --build

# 컨테이너 중지 및 정리
down:
	docker compose -f docker-compose.dev.yml down

# 컨테이너 재시작 (중지 후 다시 실행)
restart:
	docker compose -f docker-compose.dev.yml down
	docker compose -f docker-compose.dev.yml up --build

# 로그 출력
logs:
	docker compose -f docker-compose.dev.yml logs -f

# 이미지 없이 완전 새로 실행 (캐시 무시)
fresh:
	docker compose -f docker-compose.dev.yml down
	docker compose -f docker-compose.dev.yml up --build --force-recreate
