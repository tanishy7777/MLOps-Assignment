## CI/DD for machine learning using MLRun

This code is part of the assignment for the course "Software Tools and Techniques for AI" @IITGN.

[Assignment Report](https://docs.google.com/document/d/1y7NeY8e8ibu1PvV-tvC4s5Q2ooxOd4X_gh6VaiwQ_cg/edit?usp=sharing) showing all the steps from installation of MLRun on arch linux(Endeavor OS) to deploying to docker hub.
It also includes debugging steps for some of the errors that were encountered.

Using MLRun to create a CI/CD workflow for Breast Cancer Classification using Random Forests on various parameters.

The workflow was divides into 3 steps:
1. Data prep Container
2. Trainer Container: Trained the RandomForest Classifier model on the data from the previous step. Used a permutation of different hyperparameters for n_estimators
   and max_depth.
4. Deployement Container: Created the image and pushed it to docker hub.

![image](https://github.com/user-attachments/assets/e7e7bee4-46ea-491f-9951-841622a0a8a2)
Image showing the MLRun Workflow

Report of the Assignment Showing
![image](https://github.com/user-attachments/assets/6d25228f-c8bc-44e2-ae27-74406ef77718)
Data Prep Artificat (dataframe)

![image](https://github.com/user-attachments/assets/f0535174-9938-466a-9f2b-87ee6ca3851b)
Confusion matrix 

![image](https://github.com/user-attachments/assets/492c4007-1734-44a1-a697-7ac2993472dd)
Feature importance



Learnings:

will introduce students to CI/CD for Machine Learning using MLRun, a powerful orchestration and automation framework for deploying ML pipelines. 
Students will learn to create a function, deploy it using Kubernetes/Nuclio, and set up a simple retraining pipeline. 
