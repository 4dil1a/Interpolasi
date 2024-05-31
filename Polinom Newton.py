import numpy as np
import matplotlib.pyplot as plt

# Diberikan titik-titik data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk menghitung perbedaan terbagi
def divided_differences(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y  # kolom pertama adalah y

    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

    return coef[0]

# Fungsi untuk mengevaluasi polinomial Newton
def newton_polynomial(coef, x_data, x):
    n = len(coef)
    result = coef[0]
    product_term = 1.0
    for i in range(1, n):
        product_term *= (x - x_data[i-1])
        result += coef[i] * product_term
    return result

# Menghitung koefisien
coef = divided_differences(x, y)

# Menghasilkan titik-titik untuk plot polinomial
x_interp = np.linspace(min(x), max(x), 500)
y_interp = [newton_polynomial(coef, x, xi) for xi in x_interp]

# Ukuran window
plt.figure(figsize=(8, 6))

# Plot titik-titik data yang diberikan
plt.scatter(x, y, color='red', label='Titik Data')

# Plot polinomial interpolasi
plt.plot(x_interp, y_interp, label='Interpolasi Polinom Newton')

# Menambahkan judul dan label
plt.title('Interpolasi Polinom Newton\n', fontsize=16)
plt.xlabel('Tegangan\n(kg/mm^2)', fontsize=12)
plt.ylabel('Waktu Patah\n(Jam)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
