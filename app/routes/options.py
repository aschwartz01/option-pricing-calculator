from flask import Blueprint, request, jsonify
from app.models.black_scholes import (
    black_scholes_call, black_scholes_put,
    delta_call, delta_put,
    gamma, theta_call, theta_put,
    vega, rho_call, rho_put
)

options_bp = Blueprint('options_bp', __name__)

@options_bp.route('/black_scholes', methods=['POST'])
def calculate_black_scholes():
    data = request.json
    S = data['S']
    K = data['K']
    T = data['T']
    r = data['r']
    sigma = data['sigma']
    
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)
    
    call_greeks = {
        'delta': delta_call(S, K, T, r, sigma),
        'gamma': gamma(S, K, T, r, sigma),
        'theta': theta_call(S, K, T, r, sigma),
        'vega': vega(S, K, T, r, sigma),
        'rho': rho_call(S, K, T, r, sigma)
    }
    
    put_greeks = {
        'delta': delta_put(S, K, T, r, sigma),
        'gamma': gamma(S, K, T, r, sigma),
        'theta': theta_put(S, K, T, r, sigma),
        'vega': vega(S, K, T, r, sigma),
        'rho': rho_put(S, K, T, r, sigma)
    }
    
    return jsonify({
        'call_price': call_price,
        'put_price': put_price,
        'call_greeks': call_greeks,
        'put_greeks': put_greeks
    })
