FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Install Python and dependencies
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Install required Python libraries
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

# Add application files
COPY . /app

# Expose port and run the app
EXPOSE 5000
CMD ["python3", "app.py"]
