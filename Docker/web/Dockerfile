FROM python:3.12
LABEL maintainer="shun850211@gmail.com"

# 設定工作目錄
WORKDIR /web

# 複製專案檔案到容器中
COPY . /web/

# 安裝虛擬環境套件
RUN python3 -m venv /web/venv

# 激活虛擬環境並安裝 Django 和其他依賴
RUN /web/venv/bin/pip install --upgrade pip setuptools
RUN /web/venv/bin/pip install django
RUN /web/venv/bin/pip install -r requirements.txt
RUN /web/venv/bin/pip install django-cors-headers
RUN /web/venv/bin/pip install mysqlclient
RUN /web/venv/bin/pip install requests
RUN /web/venv/bin/pip install Pillow
RUN /web/venv/bin/pip install uwsgi
# 設定容器啟動時的工作目錄
WORKDIR /web/shop
RUN /web/venv/bin/python3 manage.py collectstatic --noinput
EXPOSE 8000
# 使用虛擬環境啟動 Django 
CMD ["/web/venv/bin/python3", "manage.py", "runserver", "0.0.0.0:8000"]
