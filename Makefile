# Start the API in detached mode
up:
	@echo "Starting the API in detached mode..."
	@docker-compose up -d

# Stop and remove containers, networks, volumes, and images created by up
down:
	@echo "Stopping and removing containers, networks, volumes, and images..."
	@docker-compose down

# Build the Docker images
build:
	@echo "Building Docker images..."
	@docker-compose build

# Run the API container
start-api:
	@echo "Running the API container..."
	@docker-compose run --rm popular-repo-api

# Run tests
run-test:
	@echo "Running tests..."
	@docker-compose run --rm tests

# Clean up test artifacts
clean:
	@echo "Cleaning up test artifacts..."
	@docker-compose down --volumes --remove-orphans
