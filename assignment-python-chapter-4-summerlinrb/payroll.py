# create a function to calculate various taxes for an employee
# see instructions for details


def calc_payroll_tax(gross_pay):

    medicare = (float(gross_pay * .0145))
    futa = (float(gross_pay * .006))
    ss_tax_employer = (float(gross_pay * .062))
    ss_tax_employee = (float(gross_pay * .062))
    total_tax = (float(medicare + futa + ss_tax_employee))
    net_pay = (float(gross_pay - total_tax))

    print(f"Gross Pay: $ {gross_pay:.2f}")
    print(f"Medicare Tax: $ {medicare:.2f}")
    print(f"FUTA Tax: $ {futa:.2f}")
    print(f"Social Security Tax Paid by Employer: $ {ss_tax_employer:.2f}")
    print(f"Social Security Tax Paid by Employee: $ {ss_tax_employee}")
    print(f"Total Payroll Tax Paid by Employee: $ {total_tax}")
    print(f"Net Pay: $ {net_pay}")


calc_payroll_tax(2000)

print("-" * 20)
