FROM python:3.11

# Set environment variables
ENV FLASK_APP api.py

# Install Google Chrome
RUN apt-get update && apt-get install -y wget gnupg2
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Download and install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver
RUN rm /tmp/chromedriver.zip

# Create the workdir
WORKDIR /code

# Copy the code to the workdir
COPY . /code

# Install the app requirements
RUN pip3 install -r requirements.txt

# Expose the app port
EXPOSE 5001

# Run the setup script and start the Flask app with a sleep command
CMD sleep 20 && python api_setup.py && flask run --host=0.0.0.0 --port=5001
