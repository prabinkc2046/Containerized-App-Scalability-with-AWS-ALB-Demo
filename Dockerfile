# pull the python as the base image
FROM python:3.10-slim

# Set the working directory in side the container
WORKDIR /app

# Copy the source code to the container
COPY . .

# install the required dependencies
RUN pip install pip --upgrade pip && pip install  --no-cache-dir -r requirements.txt

#Expose the port 8000
EXPOSE 8000

# run the app with uvicorn
ENTRYPOINT ["uvicorn","main:app","--host", "0.0.0.0", "--port", "8000"]

