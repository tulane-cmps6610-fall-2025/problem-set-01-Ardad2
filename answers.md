  # CMPS 6610 Problem Set 01
## Answers

**Name:** Arjun Dadhwal


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

### **1a.** Is $2^{n+1} \in O(2^n)$? Why or why not?

- Let $g(n) = 2^{n+1}$ and $f(n) = 2^n$.  
- For $2^{n+1} \in O(2^n)$ to be true, $f(n)$ must **asymptotically dominate** $g(n)$.

- By the definition of Big-O, there must exist constants $c > 0$ and $n_0 > 0$ such that:

$$
g(n) \le c \cdot f(n) \quad \forall n \ge n_0
$$

- **Subsituting $g(n)$ and $f(n)$:**

$$
2^{n+1} \le c \cdot 2^n \quad \forall n \ge n_0
$$

- **Dividing both sides by $2^n > 0 to get potential values for c$:**

$$
2 \le c
$$

c has to be greater than or equal to 2.


- **Choosing $c = 2$:**

$$
2^{n+1} \le 2 \cdot 2^n \quad \forall n \ge n_0
$$

$$
2^{n+1} \le 2^{n+1} \quad \forall n \ge n_0
$$

Since the **LHS** and **RHS** are equal, the inequality will hold for any $n_0 > 0$. 


**Conclusion:**  

Because $f(n) = 2^n$ asymptotically dominates $g(n) = 2^{n+1}$, we conclude that:

$$
\boxed{2^{n+1} \in O(2^n)}
$$


  - 1b    
 
  - 1c

  - 1d

  - 1e

  - 1f

  - 1g

2. **SPARC to Python**

  - 2b

3. **Parallelism and recursion**

  - 3b

  - 3d

  - 3e
  
4. **GCD**
