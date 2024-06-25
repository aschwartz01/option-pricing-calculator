import numpy as np
from scipy.stats import norm

def d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * np.sqrt(T)

def black_scholes_call(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    price = S * norm.cdf(D1) - K * np.exp(-r * T) * norm.cdf(D2)
    return price

def black_scholes_put(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    price = K * np.exp(-r * T) * norm.cdf(-D2) - S * norm.cdf(-D1)
    return price

def delta_call(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    return abs(norm.cdf(D1))

def delta_put(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    return norm.cdf(D1) - 1

def gamma(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    return abs(norm.pdf(D1) / (S * sigma * np.sqrt(T)))

def theta_call(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    first_term = -S * norm.pdf(D1) * sigma / (2 * np.sqrt(T))
    second_term = r * K * np.exp(-r * T) * norm.cdf(D2)
    return first_term - second_term

def theta_put(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    first_term = -S * norm.pdf(D1) * sigma / (2 * np.sqrt(T))
    second_term = r * K * np.exp(-r * T) * norm.cdf(-D2)
    return first_term + second_term

def vega(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    return abs(S * norm.pdf(D1) * np.sqrt(T))

def rho_call(S, K, T, r, sigma):
    D2 = d2(S, K, T, r, sigma)
    return abs(K * T * np.exp(-r * T) * norm.cdf(D2))

def rho_put(S, K, T, r, sigma):
    D2 = d2(S, K, T, r, sigma)
    return -K * T * np.exp(-r * T) * norm.cdf(-D2)
