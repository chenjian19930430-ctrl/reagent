# Architecture

## Tech Stack
- Backend: Python FastAPI
- Frontend: Vue 3 + TypeScript
- Database: PostgreSQL
- Cache: Redis
- AI: DeepSeek API
- Automation: Playwright

## System Flow
[Frontend] <-> [API Gateway] <-> [Module Services] <-> [AI Engine] <-> [LLM API]
                       |
                [Task Queue (Celery)]
                       |
            [Browser Automation (Playwright)]
