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

Because $f(n) = 2^n$ asymptotically dominates $g(n) = 2^{n+1}$, we conclude that:

$$
\boxed{2^{n+1} \in O(2^n)}
$$

-----

### **1b.** Is $2^{2^n} \in O(2^n)$? Why or why not?

Let $g(n) = 2^{2^n}$ and $f(n) = 2^n$.  
For $2^{2^n} \in O(2^n)$ to be true, $f(n)$ must **asymptotically dominate** $g(n)$.

By the **definition of Big-O**, there must exist constants $c > 0$ and $n_0 > 0$ such that:

$$
g(n) \le c \cdot f(n) \quad \forall n \ge n_0
$$

**Substitute $g(n)$ and $f(n)$:**

$$
2^{2^n} \le c \cdot 2^n \quad \forall n \ge n_0
$$

Divide both sides by $2^n > 0$:

$$
2^{2^n - n} \le c
$$

Take $\log_2$ of both sides:

$$
2^n - n \le \log_2 c
$$


As $n \to \infty$, the term $2^n - n \to \infty$.  

**left-hand side** grows without bound, while $\log_2 c$ is constant for any fixed $c$.  

Therefore, **no constant** $c > 0$ can make this inequality hold for all $n$, especially when they become larger.


- $f(n) = 2^n$ **cannot** asymptotically dominate $g(n) = 2^{2^n}$, therefore:

$$
\boxed{2^{2^n} \notin O(2^n)}
$$

-----
### **1c.** Is $n^{1.01} \in O(\log^2 n)$? Why or why not?

**Answer:**

By definition of Big-O, for $n^{1.01} \in O(\log^2 n)$, there must exist constants $c > 0$ and $n_0 > 0$ such that:

$$
n^{1.01} \le c \cdot (\log n)^2 \qquad \text{for all } n \ge n_0.
$$

Equivalently, we need the ratio to stay bounded:

$$
\frac{n^{1.01}}{(\log n)^2} \le c.
$$



Let $n = e^t$, so that $t = \log n$. Substituting:

$$
\frac{n^{1.01}}{(\log n)^2}
= \frac{(e^t)^{1.01}}{t^2}
= \frac{e^{1.01t}}{t^2}.
$$



As $t \to \infty$:

$$
\frac{e^{1.01t}}{t^2} \to \infty,
$$

because **exponential growth dominates polynomial growth**.


Since the ratio grows without bound, there is **no constant** $c$ that can satisfy the inequality. Therefore:

$$
\boxed{\,n^{1.01} \notin O(\log^2 n)\,}
$$

______

### **1d.** Is $n^{1.01} \in \Omega(\log^2 n)$?

**Answer:** Yes.

By definition of Big-$\Omega$, there must exist constants $c > 0$ and $n_0 > 0$ such that:

$$
n^{1.01} \ge c \cdot (\log n)^2 \qquad \text{for all } n \ge n_0.
$$

Equivalently, the ratio must eventually be bounded **below** by a positive constant:

$$
\frac{n^{1.01}}{(\log n)^2} \ge c.
$$



**Substitution (same style as 1c):**

Let $n = e^t$, so $t = \log n$. Substituting:

$$
\frac{n^{1.01}}{(\log n)^2}
= \frac{(e^t)^{1.01}}{t^2}
= \frac{e^{1.01t}}{t^2}.
$$


**Step 2. Analyze the limit:**

As $t \to \infty$:

$$
\frac{e^{1.01t}}{t^2} \to \infty,
$$

because **exponential growth dominates polynomial growth**.


For any fixed $c > 0$, there exists $t_0$ (and $n_0 = e^{t_0}$) such that:

$$
\frac{n^{1.01}}{(\log n)^2} \ge c
\qquad \text{for all } n \ge n_0.
$$

Thus, the inequality holds for large $n$. Taking $c = 1$ is enough.

**Final Answer:**

$$
\boxed{\,n^{1.01} \in \Omega(\log^2 n)\,}
$$



_______

### **1e.** Is $\sqrt{n} \in O(\log^3 n)$?

**Answer:** No.

By definition of Big-$O$, we need constants $c > 0$ and $n_0 > 0$ such that:

$$
\sqrt{n} \le c \cdot (\log n)^3 \qquad \text{for all } n \ge n_0.
$$

Equivalently, the ratio must eventually be bounded by some constant:

$$
\frac{\sqrt{n}}{(\log n)^3} \le c.
$$

**Step 1. Substitution:**  
Let $n = e^t$, so $t = \log n$. Substituting:

$$
\frac{\sqrt{n}}{(\log n)^3}
= \frac{(e^t)^{1/2}}{t^3}
= \frac{e^{t/2}}{t^3}.
$$


**Step 2. Limit analysis:**  
As $t \to \infty$:

$$
\frac{e^{t/2}}{t^3} \to \infty,
$$

because **exponential growth dominates any fixed-degree polynomial** (formally, this can be shown using L’Hôpital’s rule applied three times).

**Step 3. Conclusion:**  
Since the ratio grows without bound, no constant $c$ can satisfy the inequality for sufficiently large $n$. Therefore:

$$
\boxed{\,\sqrt{n} \notin O(\log^3 n)\,}
$$


### **1f.** Is $\sqrt{n} \in \Omega(\log^3 n)$?

**Answer:** Yes.

By definition of Big-$\Omega$, we need constants $c > 0$ and $n_0 > 0$ such that:

$$
\sqrt{n} \ge c \cdot (\log n)^3 \qquad \text{for all } n \ge n_0.
$$

Equivalently, the ratio must eventually be bounded **below** by some positive constant:

$$
\frac{\sqrt{n}}{(\log n)^3} \ge c.
$$

**Step 1. Substitution:**  
Let $n = e^t$, so $t = \log n$. Substituting:

$$
\frac{\sqrt{n}}{(\log n)^3}
= \frac{(e^t)^{1/2}}{t^3}
= \frac{e^{t/2}}{t^3}.
$$

**Step 2. Limit analysis:**  
As $t \to \infty$:

$$
\frac{e^{t/2}}{t^3} \to \infty,
$$

because **exponential growth dominates any fixed-degree polynomial**.


**Step 3. Conclusion:**  
Since the ratio tends to infinity, for any positive constant $c$ we can choose a sufficiently large $n_0$ such that:

$$
\frac{\sqrt{n}}{(\log n)^3} \ge c
\qquad \text{for all } n \ge n_0.
$$

Therefore:

$$
\boxed{\,\sqrt{n} \in \Omega(\log^3 n)\,}
$$



_____
### 1g. Prove that $o(g(n)) \cap \omega(g(n)) = \varnothing$

Assume $g(n)$ is eventually positive (standard in asymptotic analysis).  
Suppose, for contradiction, that $f \in o(g)$ and $f \in \omega(g)$.

From $f \in o(g)$, taking $c = 1$, there exists $n_0$ such that:

$$
f(n) \le g(n) \qquad \text{for all } n \ge n_0 .
\tag{1}
$$

From $f \in \omega(g)$, taking $c = 2$, there exists $n_1$ such that:

$$
f(n) \ge 2\,g(n) \qquad \text{for all } n \ge n_1 .
\tag{2}
$$

Let $N = \max(n_0, n_1)$.  
For all $n \ge N$, both (1) and (2) must hold simultaneously, giving:

$$
f(n) \le g(n) 
\qquad \text{and} \qquad
f(n) \ge 2\,g(n),
$$

which is a contradiction.

Therefore, no such function $f$ exists, and we conclude:

$$
\boxed{o(g(n)) \cap \omega(g(n)) = \varnothing}
$$
ing}\,.
$$

---
___


2. **SPARC to Python**

### 2b. What does this function do, in your own words?

The function uses the Euclid's algorithm to as to calculate the Greatest Common Divisor (GCD) of two given integers, which is the largest number that divides both without leaving a remainder. At each step of the recursion, \((a, b)\) is replaced with:

\[
(\min(a, b),\ \max(a, b)\ \bmod\ \min(a, b))
\]

Where
- The **first value** becomes the smaller of \(a\) and \(b\).
- The **second value** becomes the remainder when the larger number is divided by the smaller number.


- This goes on until one of the number becomes 0 and the remaining number is therefore the Greatest Common Divisor (GCD).

- 

3. **Parallelism and recursion**

  - 3b

  - 3d

  - 3e
  
4. **GCD**
