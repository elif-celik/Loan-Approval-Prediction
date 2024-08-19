import pickle
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

model_path = 'model.pickle'
with open(model_path, 'rb') as file:
    model = pickle.load(file)


@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    cities = ['Ankara', 'Ýstanbul', 'Ýzmir', 'Bursa', 'Erzurum']
    num = ['income_annum', 'loan_amount', 'cibil_score', 'residential_assets_value',
           'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value']

    scaler_prameters = {'income_annum': {'min': 200000, 'diff': 9700000},
                        'loan_amount': {'min': 300000, 'diff': 39200000},
                        'cibil_score': {'min': 300.0, 'diff': 600.0},
                        'residential_assets_value': {'min': -100000.0, 'diff': 29200000.0},
                        'commercial_assets_value': {'min': 0, 'diff': 19400000},
                        'luxury_assets_value': {'min': 300000, 'diff': 38900000},
                        'bank_asset_value': {'min': 0, 'diff': 14700000}}
    for e in num:
        data[e] = (data[e] - scaler_prameters[e]['min']) / scaler_prameters[e]['diff']

    features = [
        data['no_of_dependents'],
        cities.index(data['City']),
        data['income_annum'],
        data['loan_amount'],
        data['loan_term'],
        data['cibil_score'],
        data['residential_assets_value'],
        data['commercial_assets_value'],
        data['luxury_assets_value'],
        data['bank_asset_value']
    ]

    prediction = model.predict([features])

    result = "Approved" if prediction[0] == 0 else "Rejected"
    return jsonify({"prediction": result})


if __name__ == '__main__':
    app.run(debug=True)
