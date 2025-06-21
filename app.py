import streamlit as st
import pandas as pd
from io import BytesIO
from flat_interest_calculator import FlatInterestLoanCalculator
from plot import plot_monthly_breakdown

st.set_page_config(page_title="Flat Interest EMI", layout="centered")
st.title("🏦 Flat Interest Loan Calculator")

# Input fields
principal = st.number_input("Loan Amount (₹)", min_value=0.0, value=900000.0, format="%.2f")
rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=12.0, format="%.2f")
years = st.number_input("Years", min_value=0, value=5)
months = st.number_input("Months", min_value=0, max_value=11, value=0)

# Handle button click
if st.button("🔍 Calculate"):
    if principal <= 0:
        st.error("Loan amount must be greater than ₹0.")
    elif rate < 0:
        st.error("Interest rate cannot be negative.")
    elif years == 0 and months == 0:
        st.error("Loan duration must be greater than 0.")
    else:
        try:
            calc = FlatInterestLoanCalculator(principal, rate, years, months)
            df, total_payment, total_interest = calc.calculate_schedule()
            emi = calc.calculate_emi()

            st.session_state.df = df
            st.session_state.emi = emi
            st.session_state.total_interest = total_interest
            st.session_state.total_payment = total_payment

        except Exception as e:
            st.error(f"⚠️ Error during calculation: {e}")

# Display results if available
if "df" in st.session_state:
    st.success("✅ Calculation Successful!")
    st.markdown(f"##### Total Interest: ₹{st.session_state.total_interest}")
    st.markdown(f"##### Total Payment: ₹{st.session_state.total_payment}")
    st.markdown(f"##### Monthly EMI (Flat Avg): ₹{st.session_state.emi}")
    
    st.subheader("Monthly Payment Schedule")
    st.dataframe(st.session_state.df)

    # Download button
    buffer = BytesIO()
    st.session_state.df.to_excel(buffer, index=False)
    st.download_button("⬇️ Download Schedule", buffer.getvalue(), file_name="Loan_payment_schedule.xlsx")

    # Chart
    try:
        st.subheader("Payment Trend")
        st.plotly_chart(plot_monthly_breakdown(st.session_state.df))
    except Exception as e:
        st.warning(f"Could not render chart: {e}")
