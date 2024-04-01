FROM python:3.9-alpine
RUN useradd -u 8877 john
USER john
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py /app/
ENTRYPOINT [ "python", "data_generator.py", "--rows", "100" ]
