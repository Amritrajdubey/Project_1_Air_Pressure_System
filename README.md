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

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

## To initialize source code :

git clone <github_url>

## Clone/ Downlaod github repo in your system

git add file_name

## You can given file_name to add specific file or use "." to add everything to staging are Create commits

git commit -m 'message'

## To push the code to origin 

git push origin main

## To push code from origin

git pull origin main

# Code to install docker image in Aws EC2 but need to run one by one

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker


