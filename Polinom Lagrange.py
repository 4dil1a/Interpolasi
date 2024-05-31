import numpy as np
import matplotlib.pyplot as plt

# Diberikan titik-titik data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk menghitung polinomial dasar Lagrange
def lagrange_basis(x, i, xi):
    terms = [(xi - x[j]) / (x[i] - x[j]) for j in range(len(x)) if j != i]
    return np.prod(terms, axis=0)

# Fungsi untuk mengevaluasi polinomial Lagrange
def lagrange_polynomial(x, y, xi):
    n = len(x)
    result = 0
    for i in range(n):
        result += y[i] * lagrange_basis(x, i, xi)
    return result

# Menghasilkan titik-titik untuk plot polinomial
x_interp = np.linspace(min(x), max(x), 500)
y_interp = [lagrange_polynomial(x, y, xi) for xi in x_interp]

# Ukuran window
plt.figure(figsize=(8, 6))

# Plot titik-titik data yang diberikan
plt.scatter(x, y, color='red', label='Data Points')

# Plot polinomial interpolasi
plt.plot(x_interp, y_interp, label='Interpolasi Polinom Lagrange')

# Menambahkan judul dan label
plt.title('Interpolasi Polinom Lagrange\n', fontsize=16)
plt.xlabel("Tegangan\nkg/mm^2", fontsize=12)
plt.ylabel("Waktu Patah\nJam", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
