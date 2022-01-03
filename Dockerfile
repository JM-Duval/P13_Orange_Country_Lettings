FROM python:3

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash newuser
RUN echo 'newuser:newpassword' | chpasswd

USER newuser
WORKDIR $dockerjm

ENV DEBUG=False
ENV PORT=8000

ADD . $dockerjm

COPY \$dockerjm requirements.txt .

RUN pip install -r requirements.txt
ENV PATH="/dockerjm:${PATH}"
COPY . /dockerjm

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT