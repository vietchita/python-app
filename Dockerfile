# Sử dụng image Python
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy file requirements.txt và cài đặt các dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Thiết lập biến môi trường cho Flask
ENV FLASK_APP=app.py

# Mở port 5000
EXPOSE 5000

# Chạy ứng dụng
CMD ["flask", "run", "--host=0.0.0.0"]

