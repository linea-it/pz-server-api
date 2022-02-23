FROM python:3

ENV APP_HOME=/app
ENV APP_USER=userapp 
RUN groupadd -r $APP_USER && \
    useradd -r -g $APP_USER -d $APP_HOME -s /sbin/nologin -c "Docker image user" $APP_USER

WORKDIR $APP_HOME

RUN pip install --upgrade pip

# If this is set to a non-empty string, Python won’t try
# to write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE=1

# Force the stdout and stderr streams to be unbuffered.
# This option has no effect on the stdin stream.
ENV PYTHONUNBUFFERED=1

COPY requirements.txt $APP_HOME
RUN pip install -r requirements.txt
COPY . $APP_HOME

RUN chown -R $APP_USER:$APP_USER $APP_HOME
USER $APP_USER