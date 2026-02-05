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
    print(f"Gross salary with bonus after AF: {salary_with_bonus}")
    return salary_with_bonus
