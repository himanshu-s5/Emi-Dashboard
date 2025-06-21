# EMI Calculator with Visualizations

This is a simple and interactive EMI calculator built using **Streamlit**. It calculates monthly loan EMIs, visualizes principal and interest breakdowns over time, and displays both monthly and yearly summaries.

## Features

- Input loan amount, interest rate, and tenure (years + months)
- EMI calculation
- Monthly and yearly breakdown
- Interactive charts using Plotly
- Built with modular Python files

pip install -r requirements.txt


streamlit run app.py


emi-calculator/
│
├── app.py                  # Main Streamlit UI
├── emi_calculator.py       # EMI logic (calculation + breakdown)
├── emi_charts.py           # Plotly visualization functions
├── requirements.txt
└── README.md

