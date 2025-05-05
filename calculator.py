import streamlit as st

def add(a, b):
    st.write(f"Addition of {a}+{b} is {a+b}")

def sub(s, d):
    st.write(f"Subtraction of {s}-{d} is {s-d}")

def mul(m, l):
    st.write(f"Multiplication of {m}*{l} is {m*l}")

def div(d, v):
    st.write(f"Division of {d}/{v} is {d/v}")

st.title("Calculator")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter Your First Number:", step=1)
with col2:
    num2 = st.number_input("Enter Your Second Number:", step=1)

user = st.radio(
    "Choose an operation:",
    options=["Addition", "Subtraction", "Multiplication", "Division"],
    index=0,
    horizontal=True
)

if st.button("Calculate"):
    if user == "Addition":
        add(num1, num2)
    elif user == "Subtraction":
        sub(num1, num2)
    elif user == "Multiplication":
        mul(num1, num2)
    elif user == "Division":
        if num2 == 0:
            st.error("Division by zero is not allowed!")
        else:
            div(num1, num2)