FROM python:3.12.3

# Update pip to the latest version
RUN pip install --upgrade pip

# Set the working directory in the container
WORKDIR /app

# Expose port 5000 to the outside world
# EXPOSE 5000 Ya no usaremos el port 5000 ya que gunicorn se encargara de correrlo en el puerto 80.

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run the app using flask
# CMD ["flask", "run", "--host", "0.0.0.0"] < ahora esto cambia por que usaremos gunicorn.

CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]
