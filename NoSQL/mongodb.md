# Step 1: Pull the MongoDB 4.4 Docker Image
sudo docker pull mongo:4.4

# Step 2: Run the MongoDB 4.4 Container
sudo docker run --name mongodb_4.4 -d -p 27018:27017 -v mongodbdata:/data/db mongo:4.4

# Step 3: Verify the MongoDB Container is Running
sudo docker ps

# Step 4: Connect to MongoDB
# Use the following connection string in your MongoDB client:
mongodb://localhost:27018

# Step 5: Interact with MongoDB using the MongoDB shell
sudo docker exec -it mongodb_4.4 mongo

# Step 6 (Optional): Stop and Remove the Container
sudo docker stop mongodb_4.4
sudo docker rm mongodb_4.4
