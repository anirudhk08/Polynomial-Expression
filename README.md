# Polynomial-Expression
During the Summer 2016, the following Python programs were implemented. One of the tasks was to understand integer sequences (Reference: http://oeis.org) and try to implement them in Python. This involves taking a sequence of integers as input and fit a polynomial expression of nth degree, determine the the coefficients of the the nth  degree polynomial.

Description: 
The polynomial expression of degree n'th degree can be represented as

f(x) = a*x^n + b*x^(n-1) + c*x^(n-2) + ... + C

Solution:
I think that in terms of programming and mathematics, the usage of matrices would help to compute the coefficients of a nth degree polynomial. For example, the polynomial f(x) = a*x^n + b*x^(n-1) + c*x^(n-2) + ... + C can be represented as

A*X = Y 
X = A' * Y

In the above, A, X and Y are matrices and A' is the inverse of matrix A. 

The numpy package of Python was used to solve the matrix of co-efficients.

Examples:

Input = [1,2,3,6,11,23,47,106,235]
Output = [  -0.00203373, 0.08015873,  -1.32152778, 11.86944444, -63.14131944,  202.21944444, -376.53511904, 367.83095238, -140 ]
=> f(x) = -0.00203373x^8 + 0.08015873x^7 - 1.32152778x^6 + 11.86944444x^5 - 63.14131944x^4 + 202.21944444x^3 - 376.53511904x^2 + 367.83095238x - 140 

