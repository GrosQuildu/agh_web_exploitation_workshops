FROM python:latest

RUN useradd blog

WORKDIR /home/blog

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY blog.py config.py blog.db ./

ENV FLASK_APP blog.py

RUN chown -R blog:blog ./
USER blog

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["blog.py"]
