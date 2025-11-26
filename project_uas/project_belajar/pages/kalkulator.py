import streamlit as st
import math  # Module untuk operasi pangkat

# operasi matematika (functions)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:  # Var logika if untuk validasi
        return a / b
    else:
        return "Error"

def power(a, b):
    return math.pow(a, b)  #  module math

st.title("Kalkulator Sederhana")
st.write("Masukkan angka dan pilih operasi.")

# Input dengan validasi
num1 = st.number_input("Angka pertama", value=0.0, step=0.1)
num2 = st.number_input("Angka kedua", value=0.0, step=0.1)
operation = st.selectbox("Operasi", ["+", "-", "*", "/", "**"])

# logika if untuk menentukan hasil
result = None
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
elif operation == "**":
    result = power(num1, num2)

if st.button("Hitung"):
    if result is not None:
        st.success(f"Hasil: {result}")
        # Simpan riwayat menggunakan session state
        if 'history' not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(f"{num1} {operation} {num2} = {result}")
    else:
        st.error("Pilih operasi yang valid.")