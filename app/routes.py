from flask import Blueprint, render_template, request, jsonify
from app.explanation_generator import generate_explanation
from app.diagram_generator import generate_diagram

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/explain', methods=['POST'])
def explain():
    query = request.json['query']
    explanation = generate_explanation(query)
    diagram = generate_diagram(query)
    return jsonify({'explanation': explanation, 'diagram': diagram})