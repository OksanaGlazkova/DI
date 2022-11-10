FROM python:3.7-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /add
RUN pip install datetime
RUN pip install pipenv
COPY Task1.py /add
COPY Task2.py /add
RUN chmod +x Task1.py
RUN chmod +x Task1.py
EXPOSE 8000
CMD ["python","Task1","Task2"]
