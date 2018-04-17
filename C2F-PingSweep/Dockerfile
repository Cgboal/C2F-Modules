FROM python:2.7-alpine

ADD ./C2Wrapper.py /code/C2Wrapper.py
ADD ./C2-SDK /code/SDK

WORKDIR /code/SDK
RUN set -ex && \
    python setup.py install && \
    pip install netaddr

RUN set -ex && chmod 755 /code/C2Wrapper.py

ENTRYPOINT ["python"]
CMD ["/code/C2Wrapper.py"]