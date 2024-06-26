# Demo2_Black_Friday

![alt text](https://th.bing.com/th/id/OIP.889-xOWEo84kZ8WNb9zecwHaGu?rs=1&pid=ImgDetMain)

The objective of this project is to build a Vertex AI Kubeflow pipeline to streamline a regression task. The dataset utilized here is the **Black Friday Sales dataset**. The pipeline components are namely, _ingest_, _feature_selection_, _train_validation_test_split_, _hyperparameter_tuning_, _model_building_, _upload_model_to_vertex_ai_, and _model_evaluation_. The project demonstrates how to use the services offered by Google Cloud Platform.

The main files in the project are:

- _Assets_
  - images

- _Pipeline component files_
  - Black_Friday_Sales_Prediction.ipynb
  - Preprocessing.py
  - fairness & bias.ipynb
 
1. `Black_Friday_Sales_Prediction.ipynb`: This file contains custom pipeline components, each built to handle a particular machine learning task. It also contains the code to create the pipeline and register the model.
2. `Preprocessing.py`: This file contains custom components that perform preprocessing and feature engineering. These components will be called in the main file, which is _Black_Friday_Sales_Prediction.ipynb_
3. `fairness & bias.ipynb`: Code instructions that evaluate if the model is biased towards sensitive groups..


# Prerequisites/Requirements


# Setup


# Running the pipeline

1. Open the `Black_Friday_Sales_Prediction.ipynb` file and run it.
2. Make necessary changes to suit your dataset's needs.
3. Follow these instructions:
  - Ingest data from a bucket
  - Since each component is a containerized entity, the required libraries must be downloaded each time.
  - Define the components
  - Run the pipeline
4. Once the pipeline is created, you can examine the output artifacts in the output path you have mentioned.


# Additional Information

## Black_Friday_Sales_Prediction.ipynb

1. **_Input[Dataset]_**: Pipeline components utilize this syntax to pass complex structures like _DataFrames_ between them. The path mentioned by this is used to read in the data.
2. **_Output[Dataset]_**: This syntax specifies a path to write the dataset. These paths usually point to the root path mentioned when running the pipeline code. From here, the next component can read in the data using the aforementioned syntax.
3. **_Input[Artifact]_**: This refers to other complex data structures.


# Additional Resources

Vertex AI Documentation : https://cloud.google.com/vertex-ai/docs/pipelines/build-pipeline

Kubeflow Documentation : https://www.kubeflow.org/docs/components/pipelines/v1/introduction/
