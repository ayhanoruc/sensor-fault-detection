# Sensor-Fault-Detection
This is a supervised machine learning  binary classification problem focusing on detecting APS failure cases.
### Description: 
-> The Scania Air Pressure System(APS) is an integral component in heavy trucks, responsible for generating pressurized air used in vital functions such as braking and gear changing.
### Goal: 
-> We want to reduce the cost of maintanance checks and unnecessary repairs. So it is crucial to minimize the false predictions. 

## Solution Proposed
- Train a successful classifier model to predict failures beforehand and maintain & scale & modulerize the project architecture.  
- Note: Check EDA file located at notebook folder.

## Tech Stack Used
1. Python: core Python and OOP, and some common 3rd party libraries
2. FastAPI
3. Machine learning Supervised Classification algorithms
4. Docker
5. MongoDB
6. Continuous Integration-Continuous Delivery- Continuous Deployment: CI/CD


## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions

## HOW TO RUN:
Prior to running the project, make sure that you are having MongoDB in your local system, with Compass as we use MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

### STEP1: CLONE THE REPO
`https://github.com/ayhanoruc/sensor-fault-detection.git`

### STEP2: Create a conda environment after opening the repository
`conda create -n venv python=3.11 -y`

### STEP3: Install the requirements
`pip install -r requirements.txt`

### STEP4: Adjust your related env. variables:
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
  - AWS_DEFAULT_REGION
  - MONGODB_URL

### STEP5: Run the app
`python main.py`

### STEP6: Train the model through this route
`http://localhost:8080/train`

### STEP7: Predict with your dataset through this route
`http://localhost:8080/predict`




