import numpy as np
import matplotlib.pyplot as plt


def PF_EFMVcoeff(mu, C):
    """
    Fungsi ini mengambil array ekspektasi return dari masing-masing saham beserta matrix variansi kovariansi
    Mengembalikan output berupa alpha0, alpha1, beta0, beta2, h0, dan h1
    Berdasarkan penurunan rumus, beta1 bernilai 0 sehingga tidak dicari lagi.
    :param mu:
    :param C:
    :return:
    """
    e11 = np.ones([5, 1], int)
    temp1 = np.matmul(np.linalg.inv(C), e11)
    temp2 = np.matmul(np.transpose(temp1), e11)
    h0 = temp1/temp2
    temp3 = np.matmul(np.linalg.inv(C), mu)
    temp4 = np.matmul(np.transpose(e11), temp3)
    h1 = np.subtract(np.matmul(np.linalg.inv(C), mu), (temp4*h0))
    alpha0 = np.matmul(np.transpose(mu), h0)
    alpha1 = np.matmul(np.transpose(mu), h1)
    beta0 = np.matmul(np.matmul(np.transpose(h0), C), h0)
    beta2 = np.matmul(np.matmul(np.transpose(h1), C), h1)
    answer = {"alpha0": alpha0, "alpha1": alpha1, "beta0": beta0, "beta2": beta2, "h0": h0, "h1": h1}
    return answer


def PF_EFMVplot(t_bawah, t_atas, delta_t, alpha0, alpha1, beta0, beta2):
    """
    Fungsi ini mengambil input berupa parameter-parameter dibawah, dan mengembalikan nilai-nilai dari variansi dan
    return untuk di plot.
    :param t_bawah:
    :param t_atas:
    :param delta_t:
    :param alpha0:
    :param alpha1:
    :param beta0:
    :param beta2:
    :return:
    """
    t = np.linspace(t_bawah, t_atas, delta_t)
    mup = alpha0 + t*alpha1
    mup_bawah = alpha0 - t*alpha1
    sigma2p = beta0 + (t**2)*beta2
    return {"mup": mup, "sigma2p": sigma2p, "mup_bawah": mup_bawah}


def PF_EFMSDplot(t_bawah, t_atas, delta_t, alpha0, alpha1, beta0, beta2):
    """
    Fungsi ini mengambil input berupa parameter-parameter dan mengembalikan nilai return dan standar deviasi untuk
    diplot.
    :param t_bawah:
    :param t_atas:
    :param delta_t:
    :param alpha0:
    :param alpha1:
    :param beta0:
    :param beta2:
    :return:
    """
    t = np.linspace(t_bawah, t_atas, delta_t)
    mup = alpha0 + t*alpha1
    mup_bawah = alpha0 - t*alpha1
    stdvp = (beta0 + (t**2)*beta2)**0.5
    return {"mup" : mup, "stdvp": stdvp, "mup_bawah": mup_bawah}


def optimize(mu, C, rp):
    """
    Fungsi ini mengambil parameter berupa return, matriks variansi kovariansi, dan TARGET RETURN
    Fungsi ini mengembalikan nilai proporsi dari saham yang harus dibeli dengan constraint total proporsi = 1
    Fungsi ini MEMPERBOLEHKAN adanya pelaksanaan SHORT-SELL.
    :param mu:
    :param C:
    :param rp:
    :return:
    """
    e11 = np.ones([5,1], int)
    a = np.matmul(np.matmul(np.transpose(mu), np.linalg.inv(C)), e11)
    b = np.matmul(np.matmul(np.transpose(e11), np.linalg.inv(C)), e11)
    c = np.matmul(np.matmul(np.transpose(e11), np.linalg.inv(C)), mu)
    d = np.matmul(np.matmul(np.transpose(mu), np.linalg.inv(C)), mu)
    alpha = (rp*b - a)/(d*b - c*a)
    beta = (d - rp*c)/(d*b - c*a)
    x = alpha*np.matmul(np.linalg.inv(C), mu) +beta*np.matmul(np.linalg.inv(C), e11)
    return x








