# ml-demo2

This repo contains the code for the Kasna/Eliiza Google ML Specialisation, demo 2.

## Use-Case

Example of an end-to-end ML pipeline using the Black Friday dataset to increase profits. This demo can be implemented using either Cloud AI Platform (or Endpoints) or Dataproc, and can utilize any available ML library on GCP (e.g., XGBoost, scikit-learn, tf.Keras, Spark ML).

## Success Criteria
### Code
#### Code Repository
Partners must provide a link to the code repository (e.g., GitHub, GitLab, GCP CSR), which includes a ReadMe file.

*Evidence* must include an active link to the code repository containing all code that is used in demo # 1. This code must be reviewable/readable by the assessor, and modifiable by the customer. In addition, the repository should contain a ReadMe file with code descriptions and detailed instructions for running model/application.

#### Code origin certification
Partners must certify to either of these two scenarios: 1) all code is original and developed within the partner organization, or 2) licensed code is used, post-modification.

*Evidence* must include a certification by the partner organization for either of the above code origin scenarios. In addition, if licensed code is used post-modification, the partner must certify that the code has been modified per license specifications.

### Data
#### Dataset in GCP
Partners must provide documentation of where the data of demo #1 is stored within GCP (for access by the ML models during training, testing, and in production).

*Evidence* must include the project name and project ID for the Google Cloud Storage bucket or BigQuery dataset with the data (for demo #1).

### Whitepaper/Blog post
#### Business Goal and ML Solution
Partners must describe:
* The business question/goal being addressed.
* The ML use case.
* How ML solution is expected to address the business question/goal?

*Evidence* must include (in the Whitepaper) a top-line description of the business question/goal being addressed in this demo, and how the proposed ML solution will address this business goal.

#### Data Exploration
Partners must describe the following:
* How and what type of data exploration was performed?
* What decisions were influenced by data exploration?

*Evidence* must include a description (in the Whitepaper) of the tools used and the type(s) of data exploration performed, along with code snippets (that accomplish the data exploration).  Additionally, the whitepaper must describe how the data/model algorithm/architecture decisions were influenced by the data exploration.

#### Feature Engineering
Partners must describe the following:
* What feature engineering was performed?
* What features were selected for use in the ML model and why?

*Evidence* must include a description (in the Whitepaper) of the feature engineering performed (and rationale for the same), what original and engineered features were selected for incorporation as independent predictors in the ML model, and why. Evidence must include code snippets detailing the feature engineering and feature selection steps.

#### Preprocessing and the data pipeline
The partner must describe the data preprocessing pipeline, and how this is accomplished via a package/function that is a callable API (that is ultimately accessed by the served, production model).

*Evidence* must include a description (in the Whitepaper) of how data preprocessing is accomplished using Dataflow, BigQuery and/or Dataproc, along with the code snippet that accomplishes data preprocessing as a callable API.

#### ML Model Desgin(s) and Selection
Partners must describe the following:
* Which ML model/algorithm(s) were chosen for demo #1?
* What criteria were used for ML model selection?

*Evidence* must describe (in the Whitepaper) selection criteria implemented, as well as the specific ML model algorithms that were selected for training and evaluation purposes. Code snippets detailing the model design and selection steps must be enumerated.

#### ML model training and development
Partners must document the use of Cloud AI Platform or Kubeflow for ML model training, and describe the following:
* Dataset sampling used for model training (and for independent dev/test datasets) and justification of sampling methods.
* Implementation of model training, including adherence to GCP best practices for distribution, device usage, and monitoring.
* The model evaluation metric that is implemented, and a discussion of why the implemented metric is optimal given the business question/goal being addressed.
* Hyper-parameter tuning and model performance optimization.
* How bias/variance were determined (from the train-dev datasets) and tradeoffs used to influence and optimize ML model architecture?

*Evidence* must describe (in the Whitepaper) each of the ML model training and development bullet points (above). In addition, code snippets that accomplish each of these tasks need to be enumerated.

#### ML Model Evaluation
Partners must describe how the ML model, post-training, and architectural/hyperparameter optimization performs on an independent test dataset.

*Evidence* must include records/data (in the Whitepaper) of how the ML model developed and selected to address the business question performance on an independent test dataset (that reflects the distribution of data that the ML model is expected to encounter in a production environment). In addition, code snippets on model testing need to be enumerated.

### Proof of Deployment
#### Model application on GCP 
Partners must provide proof that the ML model/application is deployed and served on GCP with Cloud AI Platform or Kubeflow.

*Evidence* must include the Project Name and Project ID of the deployed cloud machine learning model and client.

#### Callable library/application
Partners must demonstrate that the ML model for demo #1 is a callable library and/or application.

*Evidence* must include a demonstration of how the served model can be used to make a prediction via an API call.

#### Editable model/application
Partners must demonstrate that the deployed model is customizable.

*Evidence* must include a demonstration that the deployed model is fully functional after an appropriate code modification, as might be performed by a customer.







