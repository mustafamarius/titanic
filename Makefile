truc: 
	echo "This is a Makefile example."

install :
	@echo "Installing the application..."
	pip-compile requirements.in
	pip install -r requirements.txt --quiet
	pip install -e . --quiet
	@echo "✅ Application installed successfully. "

.PHONY : train
train : 
	@echo "Training the model..."
	@echo "This may take a while, please be patient."
	@echo "Running training script..."
	python -c "from main import train; train()"
	@echo "✅ Model trained successfully."

.PHONY : tests
tests :
	@echo "Running tests..."


###################################################

# Web

run_api:
	@echo "Starting the FastAPI application..."
	uvicorn api.webapi:api --host 0.0.0.0 --port 8000 --reload

test_api:
	@echo "Running API tests..."
	curl -X 'GET' 'http://127.0.0.1:8000/' \
		 -H 'accept: application/json'


###################################################

# Docker
docker_build:
	@echo "Building Docker image..."
	docker build -t titanic_api:latest .

login:
	gcloud auth login 
	gcloud auth configure-docker $(europe-west9)-docker.pkg.dev

build_gcp:
	docker build -t europe-west9-docker.pkg.dev/neon-bank-461713-j6/mustafa-repo/titanic_api:latest .

docker_push:
	docker push europe-west9-docker.pkg.dev/neon-bank-461713-j6/mustafa-repo/titanic_api:latest

deploy: docker_push
	gcloud run deploy titanic-api\
		--image europe-west9-docker.pkg.dev/neon-bank-461713-j6/mustafa-repo/titanic_api:latest \
		--platform managed \
		--region europe-west9 \
		--allow-unauthenticated \
		--project neon-bank-461713-j6