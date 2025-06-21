import streamlit as st
import pandas as pd
from io import BytesIO
from flat_interest_calculator import FlatInterestLoanCalculator
from plot import plot_monthly_breakdown

st.set_page_config(page_title="Flat Interest EMI", layout="centered")
st.title("Flat Interest Loan Calculator")

# Input fields
principal = st.number_input("Loan Amount (₹)", value=900000)
rate = st.number_input("Annual Interest Rate (%)", value=12.0)
years = st.number_input("Years", min_value=0, value=5)
months = st.number_input("Months", min_value=0, max_value=11, value=0)

# Perform calculation
if st.button("calculate:"):
    calc = FlatInterestLoanCalculator(principal, rate, years, months)
    df, total_payment, total_interest = calc.calculate_schedule()

    st.session_state.df = df
    st.session_state.total_interest = total_interest
    st.session_state.total_payment = total_payment

# Show results
if "df" in st.session_state:
    st.markdown(f"#### Total Interest: ₹{st.session_state.total_interest}")
    st.markdown(f"#### Total Payment: ₹{st.session_state.total_payment}")
    
    st.subheader("Monthly Payment Schedule")
    st.dataframe(st.session_state.df)

    # Download button
    buffer = BytesIO()
    st.session_state.df.to_excel(buffer, index=False)
    st.download_button("⬇️ Download Schedule", buffer.getvalue(), file_name="Loan_payment_schedule.xlsx")

    # Chart
    st.subheader("Payment Trend")
    st.plotly_chart(plot_monthly_breakdown(st.session_state.df))
