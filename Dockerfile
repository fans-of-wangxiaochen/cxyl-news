FROM khs1994/cxyl-news:builder

COPY new.py /new.py

ENTRYPOINT ["python", "/new.py"]
