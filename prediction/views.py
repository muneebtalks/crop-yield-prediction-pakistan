from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import joblib
import os
from django.conf import settings

# Safe load model - if files missing, show message instead of crash
MODEL_PATH = os.path.join(settings.BASE_DIR, 'ml_model', 'yield_model.pkl')
ENCODER_PATH = os.path.join(settings.BASE_DIR, 'ml_model', 'crop_encoder.pkl')

try:
    model = joblib.load(MODEL_PATH)
    le = joblib.load(ENCODER_PATH)
    crops = le.classes_.tolist()
except:
    model = None
    le = None
    crops = ['Wheat', 'Maize (corn)', 'Potatoes', 'Sorghum']  # fallback

def home(request):
    return render(request, 'home.html')

def predict(request):
    if model is None:
        return render(request, 'error.html', {'message': 'Model not loaded. Run train_model.py first!'})

    if request.method == 'POST':
        try:
            crop = request.POST['crop']
            year = int(request.POST['year'])
            area = float(request.POST['area'])

            crop_encoded = le.transform([crop])[0]
            pred_yield = model.predict([[crop_encoded, year]])[0]
            total_prod = pred_yield * area / 10000

            context = {
                'crop': crop,
                'year': year,
                'area': area,
                'yield': round(pred_yield, 1),
                'total': round(total_prod, 1),
            }
            return render(request, 'result.html', context)
        except Exception as e:
            return render(request, 'error.html', {'message': str(e)})

    return render(request, 'predict.html', {'crops': crops})