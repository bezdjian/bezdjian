import sys


class SalaryCalculator:
    def __init__(self):
        self.default_rate = 800
        self.salary = 60000

    # Used in calculate_tax_deductions.py
    def calculate_salary_with_bonus(self, hours, hourly_rate=None):
        if hourly_rate is None:
            hourly_rate = self.default_rate

        print(f"Salary: {self.salary}")
        print(f"Hourly ate: {hourly_rate}")
        total_bonus = (hours * hourly_rate) * 0.05
        print(f"Total bonus: {total_bonus}")
        bonus_after_af = total_bonus / 1.3142
        print("Bonus after AF: %.2f" % bonus_after_af)
        salary_with_bonus = self.salary + bonus_after_af
        salary_with_bonus = int(round(salary_with_bonus, 2))
        print(f"Gross salary with bonus after AF: %.2f" % salary_with_bonus)
        return salary_with_bonus


# Main execution so call 'sbc' from command line
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing arguments. Usage: 'sbc <hours>', OR  'sbc <hours> <hourly rate>")
        sys.exit()  # Use sys.exit() to actually exit the program

    hours = float(sys.argv[1])
    hourly_rate = None
    if len(sys.argv) == 3:
        hourly_rate = float(sys.argv[2])

    calc = SalaryCalculator()
    salary_with_bonus = calc.calculate_salary_with_bonus(hours, hourly_rate)

    print(f"Salary: {calc.salary}")
    total_bonus = (hours * (hourly_rate or calc.default_rate)) * 0.05
    print(f"Total bonus: {total_bonus}")
    bonus_after_af = total_bonus / 1.3142
    print("Bonus after AF: %.2f" % bonus_after_af)
    print("Gross salary with bonus after AF:  %.2f " % salary_with_bonus)
    tax_salary = salary_with_bonus * 0.3142
    print("Tax on salary with bonus: %.2f" % tax_salary)
    net_salary = salary_with_bonus - tax_salary
    print("Net salary with bonus: %.2f" % net_salary)
