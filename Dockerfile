# Base this image off of the base Linux installation with Python 3.6.4 installed
FROM python:3.6.4
MAINTAINER @wingr

# send SIGQUIT to stop container
STOPSIGNAL SIGQUIT

RUN touch /etc/inside-container

# Install all Python dependencies
COPY requirements.txt ./
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files to the container's `/app` directory and set working directory to that folder
COPY . /app
WORKDIR /app

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      build-essential \
      apt-utils \
      vim

# Run the server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app.views:app", "--timeout", "120"]
