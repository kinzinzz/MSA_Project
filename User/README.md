## CMD
- bash 파일 생성 :touch 파일명

## Celery
- Server resources are limited
- Celery = Task + Process manager(Task Queues)
- Celery → execute processes(Tasks) → Different thread
- Task Queues → Distribute Workloads

## Message Broker
- Django → Task Messages → Message Broker(RabbitMQ/Redis)
- Django → RabbitMQ → Celery(work processes) 
- celery -A 프로젝트명 worker -l info
- docker에서 연결시 반드시 amqp url 연결
- shell 실행시 바로 실행 X → 프로젝트 __init__.py에 import 후 실행

## Workflow with Gmail
- Client → Django → RabbitMQ(Broker) → Celery
