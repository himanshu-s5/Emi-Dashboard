import pandas as pd

class EmiCalculator:
    def __init__(self, principal, rate_of_interest, years, months):
        self.principal = principal
        self.rate_of_interest = rate_of_interest
        self.years = years
        self.months = months
        self.tenure_months = (self.years * 12) + self.months
        self.monthly_rate = self.rate_of_interest / (12 * 100)

    def calculate_emi(self):
        if self.monthly_rate == 0:
            self.emi = self.principal / self.tenure_months
        else:
            self.emi = (
                self.principal
                * self.monthly_rate
                * (1 + self.monthly_rate) ** self.tenure_months
            ) / ((1 + self.monthly_rate) ** self.tenure_months - 1)

        self.total_payment = self.emi * self.tenure_months
        self.total_interest = self.total_payment - self.principal
        return round(self.emi, 2), round(self.total_payment, 2), round(self.total_interest, 2)

    def generate_monthly_breakdown(self):
        balance = self.principal
        self.calculate_emi()
        month_data = []

        for month in range(1, self.tenure_months + 1):
            monthly_interest = balance * self.monthly_rate
            monthly_principal = self.emi - monthly_interest
            balance -= monthly_principal

            month_data.append({
                "Month": month,
                "EMI": round(self.emi, 2),
                "Principal Paid": round(monthly_principal, 2),
                "Interest Paid": round(monthly_interest, 2),
                "Remaining Balance": round(max(balance, 0), 2)
            })

        return pd.DataFrame(month_data)

    def generate_yearly_breakdown(self):
        balance = self.principal
        self.calculate_emi()
        year_data = []
        months_remaining = self.tenure_months

        for year in range(1, (self.tenure_months // 12) + 2):
            interest_paid = 0
            principal_paid = 0
            months_in_year = min(12, months_remaining)

            for _ in range(months_in_year):
                monthly_interest = balance * self.monthly_rate
                monthly_principal = self.emi - monthly_interest
                balance -= monthly_principal
                interest_paid += monthly_interest
                principal_paid += monthly_principal
                months_remaining -= 1

            year_data.append({
                "Year": year,
                "Principal Paid": round(principal_paid, 2),
                "Interest Paid": round(interest_paid, 2),
                "Remaining Balance": round(max(balance, 0), 2)
            })

            if months_remaining <= 0:
                break

        return pd.DataFrame(year_data)
