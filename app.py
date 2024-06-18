from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the datasets
fruits = pd.read_csv('fruits.csv')
vegetables = pd.read_csv('vegetables.csv')
indian_food = pd.read_csv('indian_food.csv')
other_foods = pd.read_csv('other_foods.csv')

# Combine all datasets
data = pd.concat([fruits, vegetables, indian_food, other_foods], ignore_index=True)

@app.route('/get_nutrition', methods=['GET'])
def get_nutrition():
    food_item = request.args.get('food_item').lower()
    result = data[data['Food Item'].str.lower() == food_item]
    if result.empty:
        return jsonify({'error': 'Food item not found'}), 404
    return result.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
