#Dockerfile
#Use the official Python 3.9 base image from the Docker hub
FROM python:3.9  
#Set the working directory inside the container to/app
WORKDIR /app

#Copy only requirements.txt first 
COPY requirements.txt requirements.txt

#Install Python dependencies without caching
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application code into the container
COPY . .

#Expose port 8000 so it can be accesses outside the container
EXPOSE 8002

#Define the Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]

