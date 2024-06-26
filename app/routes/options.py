import numpy as np
from flask import Blueprint, request, jsonify
from app.models.black_scholes import black_scholes_call, black_scholes_put
from app.models.binomial_tree import binomial_tree_call, binomial_tree_put

options_bp = Blueprint('options_bp', __name__)

@options_bp.route('/black_scholes', methods=['POST'])
def calculate_black_scholes():
    data = request.json
    S = float(data['S'])
    K = float(data['K'])
    T = float(data['T'])
    r = float(data['r'])
    sigma = float(data['sigma'])
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)
    return jsonify({'call_price': call_price, 'put_price': put_price})

@options_bp.route('/binomial_tree_volatility', methods=['POST'])
def calculate_binomial_tree_volatility():
    data = request.json
    S = float(data['S'])
    K = float(data['K'])
    T = float(data['T'])
    r = float(data['r'])
    sigma = float(data['sigma'])
    N = 100  # Fixed number of steps
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = np.exp(-sigma * np.sqrt(dt))
    print(f"Inputs - S: {S}, K: {K}, T: {T}, r: {r}, sigma: {sigma}, u: {u}, d: {d}, N: {N}")
    call_price, call_p = binomial_tree_call(S, K, T, r, u, d, N)
    put_price, put_p = binomial_tree_put(S, K, T, r, u, d, N)
    print(f"Call Price: {call_price}, Put Price: {put_price}, Probability p: {call_p}")
    return jsonify({'call_price': call_price, 'put_price': put_price, 'p': call_p})

@options_bp.route('/binomial_tree_uptick_downtick', methods=['POST'])
def calculate_binomial_tree_uptick_downtick():
    data = request.json
    S = float(data['S'])
    K = float(data['K'])
    T = float(data['T'])
    r = float(data['r'])
    u = float(data['u'])
    d = float(data['d'])
    N = 100  # Fixed number of steps
    print(f"Inputs - S: {S}, K: {K}, T: {T}, r: {r}, u: {u}, d: {d}, N: {N}")
    call_price, call_p = binomial_tree_call(S, K, T, r, u, d, N)
    put_price, put_p = binomial_tree_put(S, K, T, r, u, d, N)
    print(f"Call Price: {call_price}, Put Price: {put_price}, Probability p: {call_p}")
    return jsonify({'call_price': call_price, 'put_price': put_price, 'p': call_p})