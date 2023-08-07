FROM python:3.6.9-alpine
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
 

# Create app directory
WORKDIR /app
 
# Install app dependencies
COPY requirements.txt ./
 
RUN pip install -r requirements.txt
 
# Bundle app source
COPY . .
 
EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]