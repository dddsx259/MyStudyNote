# Lecture 2: Representing and Manipulating Information

## 1. Integer Representation

Here are two main type of integer representation:
### 1.1 Unsigned Representation
The following formula is used to convert a binary string to an unsigned integer:
$$
B2U_w(x_{w-1}, x_{w-2}, \dots, x_0) = \sum_{i=0}^{w-1} x_i \cdot 2^i
$$

### 1.2 Two's Complement Representation
The following formula is used to convert a binary string to a two's complement integer:
$$
B2T_w(x_{w-1}, x_{w-2}, \dots, x_0) = -x_{w-1} \cdot 2^{w-1} + \sum_{i=0}^{w-2} x_i \cdot 2^i
$$

The advantage of two's complement representation is that it can represent negative numbers in a more efficient way. We can simply just do the binary addition for two numbers without any special handling for negative numbers, so that we can use the same hardware for both positive and negative numbers.

How to extend the bits of a two's complement integer? Here is a funny way:
+ Input: A $w$-bit signed integer x
+ Output: A $w+k$-bit signed integer y
+ Rule: Just repeat the most significant bit of x for k times.
  + i.e. Suppose $x=(x_{w-1}x_{w-2}\dots x_0)_2$, then $y=(x_{w-1}x_{w-1}\dots x_{w-1}x_{w-2}\dots x_0)_2$.
+ Mathematical theory:
  + Consider the $B2U$ function, we have the equation:
    $$x_{w-1}\cdot(\sum_{i=w-1}^{w+k-2} 2^i - 2^{w+k-1})= - x_{w-1}\cdot 2^{w-1}$$