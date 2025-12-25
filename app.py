import streamlit as st
import time

st.title("Analisis Bilangan Armstrong")
st.subheader("Iteratif vs Rekursif")

# =========================
# FUNGSI ITERATIF
# =========================
def is_armstrong_iterative(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    operations = 0
    result = 0

    for d in digits:
        result += d ** power
        operations += 1

    return result == n, operations


# =========================
# FUNGSI REKURSIF
# =========================
def armstrong_recursive_helper(digits, power, index):
    if index == len(digits):
        return 0, 0

    value, ops = armstrong_recursive_helper(digits, power, index + 1)
    return digits[index] ** power + value, ops + 1


def is_armstrong_recursive(n):
    digits = list(map(int, str(n)))
    power = len(digits)

    total, operations = armstrong_recursive_helper(digits, power, 0)
    return total == n, operations


# =========================
# INPUT USER
# =========================
number = st.number_input(
    "Masukkan bilangan",
    min_value=0,
    step=1
)

if st.button("Cek Bilangan Armstrong"):
    # =========================
    # ITERATIF
    # =========================
    start_iter = time.perf_counter()
    result_iter, ops_iter = is_armstrong_iterative(number)
    end_iter = time.perf_counter()
    time_iter = end_iter - start_iter

    # =========================
    # REKURSIF
    # =========================
    start_rec = time.perf_counter()
    result_rec, ops_rec = is_armstrong_recursive(number)
    end_rec = time.perf_counter()
    time_rec = end_rec - start_rec

    # =========================
    # OUTPUT HASIL
    # =========================
    st.header("Hasil Pengecekan")

    if result_iter:
        st.success(f"{number} adalah bilangan Armstrong")
    else:
        st.error(f"{number} bukan bilangan Armstrong")

    # =========================
    # ANALISIS EFISIENSI
    # =========================
    st.header("Analisis Efisiensi Algoritma")

    st.write("### Versi Iteratif")
    st.write(f"- Jumlah operasi: {ops_iter}")
    st.write(f"- Waktu eksekusi: {time_iter:.10f} detik")

    st.write("### Versi Rekursif")
    st.write(f"- Jumlah operasi: {ops_rec}")
    st.write(f"- Waktu eksekusi: {time_rec:.10f} detik")

    # =========================
    # KESIMPULAN
    # =========================
    st.header("Kesimpulan")
    if time_iter < time_rec:
        st.info(
            "Algoritma iteratif lebih efisien "
            "karena tidak memiliki overhead pemanggilan fungsi rekursif."
        )
    else:
        st.info(
            "Algoritma rekursif lebih efisien pada kasus ini, "
            "meskipun secara umum iteratif cenderung lebih cepat."
        )
