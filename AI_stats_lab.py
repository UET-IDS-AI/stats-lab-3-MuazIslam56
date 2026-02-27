



import random
import math
from math import comb, exp

# ------------------------------
# QUESTION 1 – Card Experiment
# ------------------------------
def card_experiment(N=200_000):
    # Theoretical
    P_A = 4/52
    P_B_given_A = 3/51
    P_AB = P_A * P_B_given_A

    # Simulation
    emp_A_count = 0
    emp_B_given_A_count = 0
    for _ in range(N):
        deck = list(range(52))
        random.shuffle(deck)
        first, second = deck[:2]
        if first < 4:  # Ace indices 0-3
            emp_A_count += 1
            if second < 4:
                emp_B_given_A_count += 1

    emp_A = emp_A_count / N
    emp_B_given_A = emp_B_given_A_count / emp_A_count if emp_A_count != 0 else 0
    error = abs(emp_B_given_A - P_B_given_A)
    
    return P_A, None, P_B_given_A, P_AB, emp_A, emp_B_given_A, error

# ------------------------------
# QUESTION 2 – Bernoulli Light Bulb
# ------------------------------
def bernoulli_lightbulb(N=100_000, p=0.05):
    # Theoretical
    theoretical = p
    theoretical_zero = 1 - p

    # Simulation
    empirical = sum(random.random() < p for _ in range(N)) / N
    error = abs(empirical - theoretical)
    return theoretical, theoretical_zero, empirical, error

# ------------------------------
# QUESTION 3 – Binomial (10 bulbs)
# ------------------------------
def binomial_bulbs(N=100_000, n=10, p=0.05):
    # Theoretical
    P0 = (1-p)**n
    P2 = comb(n,2)*(p**2)*((1-p)**(n-2))
    P_ge_1 = 1 - P0

    # Simulation
    count_ge1 = 0
    for _ in range(N):
        bulbs = [random.random() < p for _ in range(n)]
        if sum(bulbs) >= 1:
            count_ge1 += 1
    emp_ge_1 = count_ge1 / N
    error = abs(emp_ge_1 - P_ge_1)
    
    return P0, P2, P_ge_1, emp_ge_1, error

# ------------------------------
# QUESTION 4 – Geometric Die
# ------------------------------
def geometric_die(N=100_000):
    # Theoretical
    P1 = 1/6
    P3 = (5/6)**2 * (1/6)
    P_gt_4 = (5/6)**4

    # Simulation
    count_gt4 = 0
    for _ in range(N):
        rolls = 0
        while True:
            rolls += 1
            if random.randint(1,6) == 6:
                break
        if rolls > 4:
            count_gt4 += 1
    emp_gt_4 = count_gt4 / N
    error = abs(emp_gt_4 - P_gt_4)
    
    return P1, P3, P_gt_4, emp_gt_4, error

# ------------------------------
# QUESTION 5 – Poisson Customers
# ------------------------------
def poisson_customers(N=100_000, lam=12):
    # Theoretical
    P0 = exp(-lam)
    P15 = (lam**15 * exp(-lam)) / math.factorial(15)
    # P(X>=18) = 1 - P(X<=17)
    P_cum_17 = sum((lam**k * exp(-lam)) / math.factorial(k) for k in range(18))
    P_ge_18 = 1 - P_cum_17

    # Simulation
    count_ge_18 = 0
    for _ in range(N):
        x = random.poisson(lam) if hasattr(random, 'poisson') else sum(random.random() < lam/N for _ in range(N))  # Approx Poisson
        if x >= 18:
            count_ge_18 += 1
    emp_ge_18 = count_ge_18 / N
    error = abs(emp_ge_18 - P_ge_18)
    
    return P0, P15, P_ge_18, emp_ge_18, error

# ------------------------------
# Example of running all functions
# ------------------------------
if __name__ == "__main__":
    print("Card Experiment:", card_experiment())
    print("Bernoulli Lightbulb:", bernoulli_lightbulb())
    print("Binomial Bulbs:", binomial_bulbs())
    print("Geometric Die:", geometric_die())
    print("Poisson Customers:", poisson_customers())
