import numpy as np
import functions
import matplotlib.pyplot as plt

mu = np.array([[0.999782],
               [1.001739],
               [1.000747],
               [1.000638],
               [1.000847]])  # Ekspektasi return dari 5 saham, terlampir pada data excel

C = np.array([[0.00045399, 4.6289*(10**-5), 0.000268437, -1.71065*(10**-5), 0.00021397],
              [4.629*(10**-5), 0.000206049, 5.11614*(10**-5), -1.44092*(10**-6), 2.08724*(10**-5)],
              [0.000268437, 5.11614*(10**-5), 0.00060127, 1.97699*(10**-6), 0.000211709],
              [-1.7106*(10**-5), -1.44092*(10**-6), 1.97699*(10**-6), 0.000261628, 1.06961*(10**-5)],
              [0.00021397, 2.08724*(10**-5), 0.000211709, 1.06961*(10**-5), 0.000464829]])
"""
C merupakan matrix variansi-kovariansi yang digunakan dari 5 saham yang dianalisis. Untuk keterangan mengenai variansi
dan kovariansi antar-saham apa yang terdapat pada matrix C, dapat dilihat secara jelas pada file excel yang terlampir.
"""

coeffs = functions.PF_EFMVcoeff(mu, C)  # Mendapatkan koefisien-koefisien yg dibutuhkan.
ret_var = functions.PF_EFMVplot(0, 0.5, 50, coeffs['alpha0'],
                                coeffs['alpha1'], coeffs['beta0'], coeffs['beta2'])  # Mendapatkan array untuk plotting

'''Plotting Return vs Variance Efficient Frontier Line dari Portofolio 5 Saham.'''
plt.title("Grafik Efficient Frontier Return vs Variance Line Portofolio 5 Saham")
plt.xlabel("Variansi Portofolio")
plt.ylabel("Return Portofolio")

plt.plot(ret_var["sigma2p"][0], ret_var["mup"][0])  # Mu_P atas
plt.plot(ret_var["sigma2p"][0], ret_var["mup_bawah"][0], linestyle='dashed')  # Mu_P bawah
plt.plot(coeffs['beta0'], coeffs['alpha0'], "o", color="black")  # titik dengan variansi terendah
plt.annotate("<--- portofolio yang memiliki nilai variansi terkecil", (coeffs['beta0'], coeffs['alpha0']))

plt.grid()
plt.show()

'''Plotting Return vs Std. Dev Efficient Frontier Line dari Portofolio 5 Saham'''
ret_std = functions.PF_EFMSDplot(0, 0.5, 50, coeffs['alpha0'],
                                 coeffs['alpha1'], coeffs['beta0'], coeffs['beta2'])
plt.title("Grafik Efficient Frontier Return vs Std Deviation Line Portofolio 5 Saham")
plt.xlabel("Std Dev Portofolio")
plt.ylabel("Return Portofolio")

plt.plot(ret_std["stdvp"][0], ret_std["mup"][0])  # Mu_P atas
plt.plot(ret_std["stdvp"][0], ret_std["mup_bawah"][0], linestyle='dashed')  # Mu_P bawah
plt.plot(coeffs['beta0']**0.5 , coeffs['alpha0'], "o", color="black")  # titik dengan std dev terendah
plt.annotate("<--- portofolio yang memiliki nilai std dev terkecil", (coeffs['beta0']**0.5, coeffs['alpha0']))
plt.grid()
plt.show()

'''Optimisasi Portofolio dengan Target Return'''
rp = 1.0024
x = functions.optimize(mu, C, rp)
print(f"Proporsi portofolio yang optimal adalah {x[0][0]} saham ITMG, {x[1][0]} saham BMRI, "
      f"{x[2][0]} saham PTBA, {x[3][0]} saham ICBP"
      f",dan {x[4][0]} saham UNTR.")

