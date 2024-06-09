# /front/Dockerfile
FROM node:14-alpine

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy project files
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Start the React application
CMD ["npm", "start"]
