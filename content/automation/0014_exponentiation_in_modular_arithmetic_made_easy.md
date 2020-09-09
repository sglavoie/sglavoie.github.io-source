Title: Exponentiation in Modular Arithmetic Made Easy
Date: 2019-04-27 19:52
Tags: mathematics, python, script
Slug: exponentiation-in-modular-arithmetic-made-easy
Authors: Sébastien Lavoie
Summary: While playing around in the Python interpreter to validate answers to mathematical questions, I quickly found out that very large exponents are dealt with very inefficiently by default as they are simply evaluated as is. That's where Python came to its own rescue.
Description: While playing around in the Python interpreter to validate answers to mathematical questions, I quickly found out that very large exponents are dealt with very inefficiently by default as they are simply evaluated as is. That's where Python came to its own rescue.

[TOC]

---

# Introduction

The following Python script will by no means provide any useful idea to
compete against the
[RSA algorithm](<https://en.wikipedia.org/wiki/RSA_(cryptosystem)>)
, but it does give you an idea of how
a simple technique about reducing the size of an exponent in modular
arithmetic can bring you closer to using much larger numbers than the
ones you could normally use in the Python interpreter.

# The script in action

```{.python}
"""Compute the result of a^b (mod k) by using the exponentiation technique.
The goal here is not efficiency, even though the program is actually pretty
fast: the algorithm is applied manually for demonstration purposes.
Testing on a modest Intel Core i5, having `a` and `b` each set to a random
number containing 2,000 digits and `k` set to a modulo of a number containing
20 digits, results are printed in about 3.3 seconds."""

def binary_remainders(num_b):
    """Take `b` and return the binary equivalent in a list of remainders."""
    remainders = []
    quotient = num_b
    while True:
        prev_quotient = quotient
        quotient //= 2
        remainder = prev_quotient % 2
        remainders.append(remainder)

        if quotient == 0:
            break

    return remainders


def powers_of_two(remainders=None):
    """Return a list of the value of powers of two that form the
    exponent`b`."""
    if remainders is None:
        return None

    powers = []
    for index, remainder in enumerate(remainders):
        if remainder == 1:
            powers.append(2**index)

    return powers


def compute_intermediate_congruences(num_a, num_k, powers=None):
    """Compute all necessary intermediate results of congruence in `mod k` for
    powers of 2 in `powers` to form the number `b`."""
    if powers is None:
        return None

    go_up_to = max(powers)

    intermediate_results = {1: num_a}  # Build dictionary to store all results
    start_value = 2  # First power of two to calculate congruence
    congruence = num_a
    while start_value <= go_up_to:
        # value to use for next power of 2
        congruence = congruence ** 2 % num_k
        intermediate_results[start_value] = congruence
        start_value *= 2

    return intermediate_results


def compute_final_congruence(num_k, powers=None, intermediate_results=None):
    """Take all relevant values from `intermediate_results` matching powers in
    `powers`, multiply them together and calculate this number `mod k` to get
    the final result."""
    if intermediate_results is None or powers is None:
        return None

    # store all required values from `intermediate_results`
    congruent_results = []
    for power in powers:
        for key, value in intermediate_results.items():
            if key == power:
                congruent_results.append(value)

    total = 1
    for result in congruent_results:
        total = result * total  # Multiply all results together

    return total % num_k  # final congruence we are looking for


def compute_congruence(num_a, num_b, num_k):
    """Return `c`, the result of `a^b (mod k)`."""
    num_a = num_a % num_k  # Make sure `a` is smaller than `k`

    # Reduce `b` to list of remainders in binary
    remainders = binary_remainders(num_b)

    # Build a list of the powers of 2 forming `b`
    powers = powers_of_two(remainders)

    # Build a list of necessary intermediate results to reach
    # the value of `b` from powers of 2: finds congruence for
    # smaller powers of 2 and store them in a list.
    intermediate_results = compute_intermediate_congruences(num_a, num_k,
                                                            powers)

    # Multiply all relevant intermediate results `mod k` to get the final
    # congruence of `a^b (mod k)`.
    return compute_final_congruence(num_k, powers, intermediate_results)


if __name__ == '__main__':
    print("We will calculate a^b (mod k). Enter only integers.")
    NUM_A = int(input("Provide `a`: "))
    NUM_B = int(input("Provide `b`: "))
    NUM_K = int(input("Provide `k`: "))

    FINAL_RESULT = compute_congruence(NUM_A, NUM_B, NUM_K)
    print(FINAL_RESULT)

```

# Conclusion

It was very interesting to see how a technique that's applied manually
will work wonders with such large numbers. The Python interpreter can
barely calculate numbers with exponents with seven digits or more, while
a basic approach like the one shown above can quickly churn out the
results for seemingly quite large numbers.

As always, this code is
[available on GitHub](https://github.com/sglavoie/code-snippets/blob/master/python/mathematics/modular_arithmetic/exponentiation_mod_k.py).
