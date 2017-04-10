# Polynomial-Expression
During the Summer 2016, the following Python programs were implemented.

Problem Statement 3:
Given a sequence of integers that fit a polynomial expression of nth degree, determine the the coefficients of the the nth  degree polynomial.

Description: 
The polynomial expression of degree 3 can be represented as

f(x) = axn+bxn-1+cxn-2+...+C

Solution:
I think that in terms of programming and mathematics, the usage of matrices would help to compute the coefficients of a nth degree polynomial. For example, the polynomial f(x) = axn+bxn-1+cxn-2+...+Ccan be represented as

AX=Y 
X = A-1Y

Examples:

Input = [1,2,3,6,11,23,47,106,235]
Output = [  -0.00203373, 0.08015873,  -1.32152778, 11.86944444, -63.14131944,  202.21944444, -376.53511904, 367.83095238, -140 ]
=> f(x) = -0.00203373x8+0.08015873x7-1.32152778x6+11.86944444x5-63.14131944x4+202.21944444x3-376.53511904+367.83095238x-140 

