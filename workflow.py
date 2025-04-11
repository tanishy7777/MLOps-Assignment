from kfp import dsl
import mlrun

@dsl.pipeline(name="Breast Cancer Classifier Pipeline")
def pipeline():
    project = mlrun.get_current_project()

    data_prep = project.run_function(
        "Data-prep",
        outputs=["dataset"]         
    )

    train = project.run_function(
        "trainer",
        outputs=["model"],            
        inputs={"dataset": data_prep.outputs["dataset"]},
        hyperparams={
        "n_estimators": [10, 100, 200],
        "max_depth": [2, 5, 10]
        },
        selector="max.accuracy",
    )
    

    deploy = mlrun.deploy_function(
        "serving",
        models=[{"key": "my_model", "model_path": train.outputs["model"], "class_name": "ClassifierModel"}],
    )