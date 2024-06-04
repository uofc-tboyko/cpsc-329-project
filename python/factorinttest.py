import sympy
import time

def test_factorint_time(n):
    start_time = time.perf_counter()
    factors = sympy.factorint(n)
    end_time = time.perf_counter()
    return end_time - start_time, factors

# Function to generate the product of two large primes
def generate_large_semiprime(digits):
    p = sympy.randprime(10**(digits-1), 10**digits)
    q = sympy.randprime(10**(digits-1), 10**digits)
    return p * q

# Test different sizes of semiprimes (product of two primes)
digits_list = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

for digits in digits_list:
    semiprime = generate_large_semiprime(digits)
    time_taken, factors = test_factorint_time(semiprime)
    print(f"Time taken to factor a semiprime with approximately {2*digits} digits: {time_taken:.6f} seconds")
    print(f"Factors: {factors}")