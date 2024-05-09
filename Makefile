.PHONY: train run build-docker run-docker

train:
	python notebooks/model_training.ipynb

run:
	python app/app.py

build-docker:
	docker build -t diabetes_prediction_app .

run-docker:
	docker run -p 5000:5000 diabetes_prediction_app

test:
	python -m pytest tests/
