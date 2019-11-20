FROM python:alpine
ARG VERSION=""
ENV VERSION=$VERSION

ENV PYTHONPATH=/app
WORKDIR /app
COPY hello.py ./

CMD ["python", "hello.py"]