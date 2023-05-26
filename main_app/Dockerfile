FROM python:3.11

# Set environment variables
ENV FLASK_APP app.py
ENV SECRET_KEY RfHb55ca63Jf6u

# Create the workdir
WORKDIR /code

# Copy the code to the workdir
COPY . /code

# Install the app requirements
RUN pip install -r requirements.txt

# Expose the app port
EXPOSE 5000

# Run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
