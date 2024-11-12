## EVRS
The EVRS aims to reduce delays for emergency vehicles caused by traffic congestion. Traditional lights and sirens are insufficient in many cases, especially in urban areas or noisy environments. This system employs technology to notify nearby vehicles, helping them vacate lanes and allowing emergency vehicles to pass quickly.


## Emergency Vehicles Routing System (EVRS) Backend
This repository contains the backend implementation of the Emergency Vehicles Routing System (EVRS), which facilitates real-time communication and routing for emergency vehicles. The backend processes vehicle location updates, traffic data, and notifications for efficient traffic management.

#Features
Real-time routing based on traffic conditions.

Notification system for alerting nearby drivers.

Integration with cloud services for scalability.

API endpoints for mobile app interaction.

Deployable on Vultr Compute Instances and Kubernetes.
# Tech Stack
Backend Framework: Node.js (Express)

Database: PostgreSQL (or MongoDB)

Cloud Platform: Vultr Cloud Services

Containerization: Docker

Kubernetes: Vultr Kubernetes Engine for scalability

Web Server: Nginx for reverse proxy

APIs: Google Maps API for traffic data

# Getting Started

Prerequisites

Node.js (v18.x or later)

Docker (for containerization)

Vultr Cloud Account

Kubernetes CLI (kubectl)

Git

# Installation

Clone the repository:
```
git clone https://github.com/your-username/evrs-backend.git

cd evrs-backend
```
Install dependencies:
```
npm install
Create a .env file:
```
```
touch .env
```
Add the following variables:

```
PORT=3000
DB_HOST=<database_host>
DB_PORT=5432
DB_USER=<database_user>
DB_PASSWORD=<database_password>
DB_NAME=evrs
GOOGLE_MAPS_API_KEY=<your_google_maps_api_key>

```
Start the server:

```
node server.js
```
# Deployment
1. On Vultr Compute Instance
SSH into your instance:

```
ssh root@<your_instance_IP>
Clone the repository and follow the installation steps.
```
Configure Nginx for reverse proxy:

```
Add the configuration in /etc/nginx/sites-available/evrs.
```
Restart Nginx:
```
systemctl restart nginx
```
2. On Vultr Kubernetes

Build the Docker image:

```
docker build -t <your_dockerhub_username>/evrs-backend:latest .

docker push <your_dockerhub_username>/evrs-backend:latest
```
Deploy to Kubernetes:


Apply the backend-deployment.yaml and backend-service.yaml files:
```
kubectl apply -f backend-deployment.yaml.

kubectl apply -f backend-service.yaml.

```
Verify the deployment:

kubectl get pods.

kubectl get service evrs-backend-service.
# API Endpoints

Method	Endpoint	Description.

GET	/api/status	Check backend status.

POST	/api/alerts	Broadcast emergency vehicle alerts.

GET	/api/routes	Get optimized route for vehicles.

POST	/api/register	Register new users or vehicles.

# Environment Variables

PORT: Port number for the backend server.

DB_HOST: Database host address.

DB_PORT: Database port number.

DB_USER: Database username.

DB_PASSWORD: Database password.

DB_NAME: Database name.

GOOGLE_MAPS_API_KEY: API key for Google Maps integration.

# Contributing

Fork the repository.

Create a feature branch:
```
git checkout -b feature-name
```
Commit your changes.
```
git commit -m "Description of changes"
```
Push to your fork.
```
git push origin feature-name.
```
Open a pull request.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Contact

For questions or feedback, please contact.

## Team ATHENA

Email: kushagrajager@gmail.com, himanshukumar914656@gmail.com
