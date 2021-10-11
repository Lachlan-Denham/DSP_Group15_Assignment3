# To be filled by students
FROM python:3.8.2

WORKDIR /DSP-assigment3-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src

COPY ./app ./app

CMD ["python", "./app/streamlit_app.py"]