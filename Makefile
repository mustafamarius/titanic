truc: 
	echo "This is a Makefile example."

install :
	@echo "Installing the application..."
	pip install -r requirements.in --quiet
	pip install -e . --quiet


.PHONY : train
train : install
	@echo "Training the model..."
	python -c "print('Training the model...')"

.PHONY : tests
tests :
	@echo "Running tests..."
