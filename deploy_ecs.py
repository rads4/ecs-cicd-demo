import boto3

ecs = boto3.client("ecs", region_name="ap-south-1")

cluster_name = "3tier-ec2-cluster"

services = [
    "3tier-ec2-frontend-v2-service",
    "3tier-ec2-backend-service"
]

for service in services:
    print(f"Deploying {service}...")
    ecs.update_service(
        cluster=cluster_name,
        service=service,
        forceNewDeployment=True
    )

print("Deployment triggered for all services")
