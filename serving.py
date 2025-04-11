from mlrun.serving import V2ModelServer
import joblib

class ClassifierModel(V2ModelServer):
    def load(self):
        model_file, extra_data = self.get_model('.pkl')
        self.model = joblib.load(model_file)

    def predict(self, body):
        features = body["inputs"]
        return self.model.predict(features).tolist()
    
