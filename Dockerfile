# To be filled by students
FROM python:3.8.2

WORKDIR /DSP-assigment3-app

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8501

COPY ./src ./src

COPY ./app ./app

ENTRYPOINT [ "streamlit", "run" ]

CMD ["app/streamlit_app.py"]