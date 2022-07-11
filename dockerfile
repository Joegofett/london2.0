FROM python

WORKDIR /London2.0
COPY . /London2.0/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD [ "python3", "hello.py" ]
