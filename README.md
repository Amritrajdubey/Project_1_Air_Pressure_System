# Air - Pressure - Sensor - Fault - Detection

![1644215452047](https://user-images.githubusercontent.com/105154672/233306250-f0ee47f1-4af1-4d9f-a92d-44bbe5450ae2.png)

## Problem Statement

The Air Pressure System (APS) is a critical component of heavy-duty vehicle which uses compressed air to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

Problem statement is Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

## Proposed Solution

In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

## Tech used
- Python 
- Docker
- Ml Libraries
- MongoDb
- Fast API

## Infrastructure Required
- AWS S3
- AWS ECR
- AWS EC2
- Git Actions

## Steps to Run

Before we run the project, make sure to have MongoDB in local system, with Compass since we are using MongoDB for data storage. Also need AWS account to access the service like S3, ECR and EC2 instances.

## Data Collection

![l3ejlas7ozm2jgzx1-Screen Shot 2022-05-20 at 8 33 34 AM](https://user-images.githubusercontent.com/105154672/233316308-cd1e2327-da4e-4075-85d5-2af927f9e790.jpg)

## Project Architecture

![bmlp_0401](https://user-images.githubusercontent.com/105154672/233317719-10974723-e2fa-4647-87f3-01c0aa5726f0.png)

## Deployement Architecture

![lpzhautvn28rj3hoij1h](https://user-images.githubusercontent.com/105154672/233319943-5b75eb43-1e1e-4cb0-9b29-9bf126e63724.png)

# Steps Involved 

### Step 1- Clone the repo
```bash
git clone https://github.com/Amritrajdubey/Project_3_Air_Pressure_System.git
```

### Step 2- Create Conda environment after repo being cloned

```bash
conda create -n sensor python=3.7.6 -y
```

```bash
conda activate sensor
```

### Step 3- Install the requirements

```bash
pip install -r requirements.txt
```

### Step 4- Export Environment variable data

```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@mongoproject.2m81o7p.mongodb.net/?retryWrites=true&w=majority"
```

### Step 5- Run Application server

```bash
python app.py
```
### Step 6- Train Application
```bash 
http://localhost:8080/train
```
### Step 7- Prediction Application
```bash
http://localhost:8080/predict
```
## RUN LOCALLY

###1 .Check if the Dockerfile is available in the project directory
###2 .Build the Docker image
```bash
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 
```
###3 .Run the Docker image
```bash
docker run -d -p 8080:8080 <IMAGE_NAME>
```
###To run the project first execute the below commmand. MONGO DB URL:
```bash
mongodb+srv://<username>:<password>@mongoproject.2m81o7p.mongodb.net/?retryWrites=true&w=majority
```
###windows user
```bash
MONGO_DB_URL= mongodb+srv://<username>:<password>@mongoproject.2m81o7p.mongodb.net/?retryWrites=true&w=majority
```
###Linux User
```bash
mongodb+srv://<username>:<password>@mongoproject.2m81o7p.mongodb.net/?retryWrites=true&w=majority
```
###Then Run
```bash
python main.py
```
###Download Dataset
```bash
wget https://raw.githubusercontent.com/Amritrajdubey/Project_3_Air_Pressure_System/main/aps_failure_training_set1.csv
```
###To Check and reset git log
```bash
git log
git reset --soft 6afd
6afd -> last 4 digit of log. 
```
###Add and Upload to git
```bash
git add filename
we can also use . for all file(Current directory)

git commit -m "Message"
git push origin main
```
##Install Docker in AWS(EC2)
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

```bash
AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY =
AWS_REGION =
AWS_ECR_LOGIN_URI =
ECR_REPOSITORY_NAME =
BUCKET_NAME =
MONGO_DB_URL =
```
