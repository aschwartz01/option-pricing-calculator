from flask import Blueprint, request, jsonify
from app.models.black_scholes import black_scholes_call, black_scholes_put
from app.models.binomial_tree import binomial_tree_call
from app.models.monte_carlo import monte_carlo_call

options_bp = Blueprint('options_bp', __name__)

@options_bp.route('/black_scholes_call', methods=['POST'])
def calculate_black_scholes_call():
    data = request.json
    S = data['S']
    K = data['K']
    T = data['T']
    r = data['r']
    sigma = data['sigma']
    call_price = black_scholes_call(S, K, T, r, sigma)
    return jsonify({'call_price': call_price})

# Add similar endpoints for black_scholes_put, binomial_tree_call, and monte_carlo_call
