import streamlit as st
from emi_calculator import EmiCalculator
from emi_plot import plot_monthly_breakdown, plot_yearly_breakdown

st.title("EMI Calculator with Visualizations")

# Inputs
principal = st.number_input("Loan Amount (₹)", value=400000)
rate = st.number_input("Annual Interest Rate (%)", value=15.0)
years = st.number_input("Years", min_value=0, value=1)
months = st.number_input("Months", min_value=0, max_value=11, value=2)

# Calculate and store in session state
if st.button("Calculate EMI"):
    calc = EmiCalculator(principal, rate, years, months)
    emi, total_payment, total_interest = calc.calculate_emi()

    st.session_state.emi = emi
    st.session_state.total_payment = total_payment
    st.session_state.total_interest = total_interest
    st.session_state.df_monthly = calc.generate_monthly_breakdown()
    st.session_state.df_yearly = calc.generate_yearly_breakdown()

# Display values and visuals
if "emi" in st.session_state:
    st.markdown(f"### 📊 EMI: ₹{st.session_state.emi}")
    st.markdown(f"**Total Payment:** ₹{st.session_state.total_payment}")
    st.markdown(f"**Total Interest:** ₹{st.session_state.total_interest}")

    st.subheader("Monthly Breakdown")
    st.dataframe(st.session_state.df_monthly)
    st.plotly_chart(plot_monthly_breakdown(st.session_state.df_monthly))

    st.subheader("Yearly Breakdown")
    st.dataframe(st.session_state.df_yearly)
    st.plotly_chart(plot_yearly_breakdown(st.session_state.df_yearly))
