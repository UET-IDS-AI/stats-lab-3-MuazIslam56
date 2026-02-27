# import numpy as np
# from math import comb, factorial, exp

# np.random.seed(42)

# # =========================================================
# # QUESTION 1 – Card Experiment (Without Replacement)
# # =========================================================

# N = 200_000

# # ----- Theoretical -----
# P_A = 4/52
# P_B = 4/52
# P_B_given_A = 3/51
# P_A_and_B = (4/52)*(3/51)
# independence_check = P_A_and_B == P_A * P_B

# print("QUESTION 1 – THEORETICAL")
# print("P(A):", P_A)
# print("P(B):", P_B)
# print("P(B|A):", P_B_given_A)
# print("P(A ∩ B):", P_A_and_B)
# print("Independent?:", independence_check)

# # ----- Simulation -----
# deck = np.array([1]*4 + [0]*48)  # 1 = Ace, 0 = not Ace

# count_A = 0
# count_A_and_B = 0

# for _ in range(N):
#     draw = np.random.choice(deck, size=2, replace=False)
#     if draw[0] == 1:
#         count_A += 1
#         if draw[1] == 1:
#             count_A_and_B += 1

# emp_P_A = count_A / N
# emp_P_B_given_A = count_A_and_B / count_A
# abs_error_Q1 = abs(P_B_given_A - emp_P_B_given_A)

# print("\nQUESTION 1 – EMPIRICAL")
# print("Empirical P(A):", emp_P_A)
# print("Empirical P(B|A):", emp_P_B_given_A)
# print("Absolute Error:", abs_error_Q1)


# # =========================================================
# # QUESTION 2 – Bernoulli (Light Bulb)
# # =========================================================

# p = 0.05
# N = 200_000

# # Theoretical
# theo_X1 = p
# theo_X0 = 1 - p

# # Simulation
# samples = np.random.rand(N) < p
# emp_X1 = np.mean(samples)
# abs_error_Q2 = abs(theo_X1 - emp_X1)

# print("\nQUESTION 2")
# print("Theoretical P(X=1):", theo_X1)
# print("Theoretical P(X=0):", theo_X0)
# print("Empirical P(X=1):", emp_X1)
# print("Absolute Error:", abs_error_Q2)


# # =========================================================
# # QUESTION 3 – Binomial (10 Bulbs)
# # =========================================================

# n = 10
# p = 0.05
# N = 200_000

# # Theoretical
# P_X0 = comb(n,0)*(p**0)*((1-p)**10)
# P_X2 = comb(n,2)*(p**2)*((1-p)**8)
# P_X_ge1 = 1 - P_X0

# # Simulation
# samples = np.random.binomial(n, p, N)
# emp_P_ge1 = np.mean(samples >= 1)
# abs_error_Q3 = abs(P_X_ge1 - emp_P_ge1)

# print("\nQUESTION 3")
# print("Theoretical P(X=0):", P_X0)
# print("Theoretical P(X=2):", P_X2)
# print("Theoretical P(X≥1):", P_X_ge1)
# print("Empirical P(X≥1):", emp_P_ge1)
# print("Absolute Error:", abs_error_Q3)


# # =========================================================
# # QUESTION 4 – Geometric (Die Until 6)
# # =========================================================

# p = 1/6
# N = 200_000

# # Theoretical
# P_X1 = p
# P_X3 = (1-p)**2 * p
# P_X_gt4 = (1-p)**4

# # Simulation
# samples = np.random.geometric(p, N)
# emp_P_gt4 = np.mean(samples > 4)
# abs_error_Q4 = abs(P_X_gt4 - emp_P_gt4)

# print("\nQUESTION 4")
# print("Theoretical P(X=1):", P_X1)
# print("Theoretical P(X=3):", P_X3)
# print("Theoretical P(X>4):", P_X_gt4)
# print("Empirical P(X>4):", emp_P_gt4)
# print("Absolute Error:", abs_error_Q4)


# # =========================================================
# # QUESTION 5 – Poisson (Customers per Hour)
# # =========================================================

# lam = 12
# N = 200_000

# # Theoretical
# P_X0 = exp(-lam)
# P_X15 = (lam**15 * exp(-lam)) / factorial(15)

# # Compute P(X ≥ 18)
# P_less_18 = sum((lam**k * exp(-lam)) / factorial(k) for k in range(18))
# P_ge18 = 1 - P_less_18

# # Simulation
# samples = np.random.poisson(lam, N)
# emp_P_ge18 = np.mean(samples >= 18)
# abs_error_Q5 = abs(P_ge18 - emp_P_ge18)

# print("\nQUESTION 5")
# print("Theoretical P(X=0):", P_X0)
# print("Theoretical P(X=15):", P_X15)
# print("Theoretical P(X≥18):", P_ge18)
# print("Empirical P(X≥18):", emp_P_ge18)
# print("Absolute Error:", abs_error_Q5)





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
