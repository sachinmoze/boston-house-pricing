from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
import openai
# Create your views here.
from django.http import JsonResponse
#from trained_models import *
import os
import pickle

MODEL_FILE_PATH = os.path.join('boston_pricing', 'trained_models', 'trained_boston_housing_model.pkl')


def load_trained_model(model_file_path):
    """Load the trained model from the given file path."""
    with open(model_file_path, 'rb') as f:
        trained_model = pickle.load(f)
    return trained_model

def home(request):
    return render(request,"home.html")


def predict_medv(request):
    return render(request,"medv_home.html")

def predict_chas(request):
    return render(request,"chas_home.html")


def predict_view(request):
    if request.method == 'POST':
        # Load the trained model
        try:
            trained_model = load_trained_model(MODEL_FILE_PATH)
        except Exception as e:
            return HttpResponse(f'Error loading trained model: {str(e)}')
        
        constant = float(request.POST.get('CONST', '1.0'))
        # Get the input values from the form
        CRIM = float(request.POST.get('CRIM'))
        ZN = float(request.POST.get('ZN'))
        INDUS = float(request.POST.get('INDUS'))
        CHAS = float(request.POST.get('CHAS'))
        NOX = float(request.POST.get('NOX'))
        RM = float(request.POST.get('RM'))
        AGE = float(request.POST.get('AGE'))
        DIS = float(request.POST.get('DIS'))
        RAD = float(request.POST.get('RAD'))
        TAX = float(request.POST.get('TAX'))
        PTRATIO = float(request.POST.get('PTRATIO'))
        B = float(request.POST.get('B'))
        LSTAT = float(request.POST.get('LSTAT'))

        # Create a dictionary containing the input values
        input_data = {
            'const':constant,
            'CRIM': CRIM,
            'ZN': ZN,
            'INDUS': INDUS,
            'CHAS': CHAS,
            'NOX': NOX,
            'RM': RM,
            'AGE': AGE,
            'DIS': DIS,
            'RAD': RAD,
            'TAX': TAX,
            'PTRATIO': PTRATIO,
            'B': B,
            'LSTAT': LSTAT
        }

        # Make predictions using your model
        # Replace 'YourModel' with the name of your trained model
        # You may need to adjust this code depending on how your model is structured
        try:
            import pandas as pd
            input_df = pd.DataFrame([input_data])
            
            prediction = trained_model.predict(input_df)
            # Do something with the prediction (e.g., return it to the user)
            return render(request,"prediction.html",{"prediction_result":prediction[0]})
        except Exception as e:
            # Handle any errors that occur during prediction
            return HttpResponse(f'Error: {str(e)}')

    else:
        # If request method is not POST, render the form
        return render(request, 'home.html')
