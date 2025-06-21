import pandas as pd

class FlatInterestLoanCalculator:
    def __init__(self, principal, rate_of_interest, years, months):
        self.principal = principal
        self.rate_of_interest = rate_of_interest
        self.years = years
        self.months = months
        self.tenure_months = (self.years * 12) + self.months
        self.monthly_principal = self.principal / self.tenure_months
        self.monthly_rate = self.rate_of_interest / (12 * 100)

    def calculate_schedule(self):
        balance = self.principal
        monthly_data = []
        total_interest = 0

        for month in range(1, self.tenure_months + 1):
            interest = balance * self.monthly_rate
            total_payment = self.monthly_principal + interest
            total_interest += interest
            balance -= self.monthly_principal

            monthly_data.append({
                "Month": month,
                "Principal Paid": round(self.monthly_principal, 2),
                "Interest Paid": round(interest, 2),
                "Total Payment": round(total_payment, 2),
                "Remaining Balance": round(max(balance, 0), 2)
            })

        total_paid = self.principal + total_interest
        return pd.DataFrame(monthly_data), round(total_paid, 2), round(total_interest, 2)
