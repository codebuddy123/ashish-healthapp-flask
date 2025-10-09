# Ashish Hospital Flask Application Setup Guide

A Flask-based hospital management application with MongoDB backend, featuring appointment booking and responsive UI.

## Prerequisites

1. Python 3.x installed
2. MongoDB installed and running locally or use MongoDB Atlas for cloud database
3. pip package manager installed

## Creating a MongoDB User

First, create a user in MongoDB with necessary privileges:

```bash
mongosh
use admin
```

Create the user:
```javascript
db.createUser({
  user: "ashish",
  pwd: "Test123",
  roles: [ { role: "root", db: "admin" } ]
})
exit
```

## Running the Application Locally

### 1. Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application

```bash
python app.py
```

**Access the application:** [http://localhost:8000](http://localhost:8000)

### 4. Verify Data in MongoDB

After booking appointments through the UI, check the data:

```bash
mongosh -u ashish -p Test123 --authenticationDatabase admin
use ashish_hospital;
show collections;
db.appointments.find()
db.appointments.find().pretty()
```

## Containerizing the Application

### 1. Environment Configuration

Create a `.env` file in the project root:

```env
MONGODB_URI=mongodb://ashish:Test123@ashish-mongo:27017/ashish_hospital?authSource=admin
DATABASE_NAME=ashish_hospital
```

> **Note:** 
> - For local development: use `localhost` instead of `ashish-mongo`
> - For EC2 deployment: replace `ashish-mongo` with the MongoDB server IP

**MongoDB URI Explanation:**
- `mongodb://` - Protocol
- `ashish` - MongoDB username (set in container)
- `Test123` - MongoDB password (set in container)  
- `ashish-mongo` - MongoDB container name (Docker networking)
- `27017` - Default MongoDB port
- `ashish_hospital` - Database name

### 2. Create Docker Network

```bash
docker network create ashish-net
```
This ensures containers can communicate using their names.

### 3. Launch MongoDB Container

```bash
docker run -d \
  --name ashish-mongo \
  -p 27017:27017 \
  --network ashish-net \
  -e MONGO_INITDB_DATABASE=ashish_hospital \
  -e MONGO_INITDB_ROOT_USERNAME=ashish \
  -e MONGO_INITDB_ROOT_PASSWORD=Test123 \
  mongo:7
```

### 4. Build Flask Application Image

Choose one of the following based on your requirements:

```bash
# Build for current architecture (automatic)
docker build -t ashish-hospital-app .

# For ARM64 architecture
docker build --platform linux/arm64 -t ashish-hospital-app .

# For multi-platform build (AMD64 and ARM64)
docker buildx build --platform linux/amd64,linux/arm64 -t ashish-hospital-app .
```

### 5. Run Flask Application Container

```bash
docker run -p 8000:8000 --network ashish-net --env-file .env ashish-hospital-app
```

### 6. Verify Data in Container

Access MongoDB container:
```bash
docker exec -it ashish-mongo bash
```

Login to database:
```bash
mongosh -u ashish -p Test123 --authenticationDatabase admin ashish_hospital
```

Check appointment data:
```bash
db.appointments.find().pretty()
```

## Running with Docker Compose

### Prerequisites
- Docker and Docker Compose installed
- `.env` file configured (see step 1 above)

### Commands

```bash
# Start services
docker-compose up -d --build

# Stop services  
docker-compose down
```

**Access the application:** [http://localhost:8000](http://localhost:8000)

> **Note:** A `docker-compose.yml` file is already provided in the project root.

## AWS EC2 Deployment with DocumentDB

### EC2 Setup

1. Create Ubuntu 24.04 instance (t2.medium recommended)
2. Ensure Python is installed
3. Clone the repository and navigate to project folder

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### DocumentDB Configuration

#### 1. Create DocumentDB Cluster

- Create cluster with 1 replica
- Username: `ashish`
- Password: `Test1234` (minimum 8 characters)
- Ensure Security Group allows port 27017

#### 2. Download CA Certificate

```bash
wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
```

#### 3. Test Connection (Optional)

```bash
mongosh health-app.c1ku20ei673y.ap-south-2.docdb.amazonaws.com:27017 \
  --tls --tlsCAFile global-bundle.pem --retryWrites=false \
  --username ashish --password <insertYourPassword>
```

> **Note:** Install MongoDB shell if needed. See [MongoDB Shell Installation Guide](https://www.mongodb.com/docs/mongodb-shell/install/)

#### 4. Configure Environment Variables

Create `.env` file for DocumentDB:

```env
MONGODB_URI=mongodb://ashish:Test1234@health-app.c1ku20ei673y.ap-south-2.docdb.amazonaws.com:27017/ashish_hospital?tls=true&tlsCAFile=/home/ubuntu/global-bundle.pem&retryWrites=false
DATABASE_NAME=ashish_hospital
```

**Replace the following:**
- `ashish` with your DocumentDB username
- `Test1234` with your DocumentDB password  
- `/home/ubuntu/global-bundle.pem` with your CA file path
- Update the DocumentDB endpoint URL

#### 5. Verify Data in DocumentDB

After submitting appointments through the UI:

```bash
mongosh health-app.c1ku20ei673y.ap-south-2.docdb.amazonaws.com:27017 \
  --tls --tlsCAFile global-bundle.pem --retryWrites=false \
  --username ashish --password <insertYourPassword>
```

Check the data:
```bash
use ashish_hospital;
show dbs;
show collections;
db.appointments.find();
```

## Troubleshooting

- Ensure all ports are properly configured (8000 for Flask, 27017 for MongoDB)
- Check network connectivity between containers
- Verify environment variables are correctly set
- For DocumentDB, ensure security groups allow access from EC2 instance