FROM python:3.11

RUN mkdir -p /coffe_shop

WORKDIR /coffe_shop

COPY ./__init__.py /coffe_shop

COPY ./build/database_init.py /coffe_shop

COPY ./app/start_server.py /coffe_shop

COPY ./build/dataset /coffe_shop/dataset

COPY ./build/requirements.txt /coffe_shop

COPY ./config.ini /coffe_shop

RUN pip install --no-cache-dir --upgrade -r /coffe_shop/requirements.txt

COPY ./app /coffe_shop/app

CMD python ./database_init.py && python ./start_server.py



