FROM python:3.8.10

ADD /requirements.txt q_app/requirements.txt
ADD /app/api/config.txt q_app/app/api/config.txt
ADD /app/api/server.py q_app/app/api/server.py
ADD /app/api/utils.py q_app/app/api/utils.py
ADD /app/db/client/client.py q_app/app/db/client/client.py
ADD /app/db/interaction/interaction.py q_app/app/db/interaction/interaction.py
ADD /app/db/models/models.py q_app/app/db/models/models.py
ADD /app/db/exceptions.py q_app/app/db/exceptions.py

RUN pip install -r q_app/requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/q_app/app"
WORKDIR /q_app


EXPOSE 5000

CMD ["python", "./app/api/server.py", "--config=./app/api/config.txt"]