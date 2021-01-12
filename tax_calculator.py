
import ast

class TaxRates:
    def __init__(self):
        self.fed_tax = []
        self.state_taxes = []
        self.year = 0
        self.state = ""

    def addFederalTaxLevel(self, tax_level):
	    self.fed_tax.append(tax_level)

    def printFederalTax(self): 
	    print("Federal tax: ", self.fed_tax)


def main():
    tax_rate_2020 = TaxRates()

    with open('taxes.txt') as f:
	    data = f.read()

    tax_dict = ast.literal_eval(data)

    yearly_tax = {}
    for tax_rate in tax_dict:
        curr_tax_rates = TaxRates()
        curr_tax_rates.fed_tax = tax_rate["federal_tax_bracket"]
        curr_tax_rates.year = tax_rate["year"]
        curr_tax_rates.state = tax_rate["state"]

        yearly_tax[ ( tax_rate["year"], tax_rate["state"] ) ] = curr_tax_rates

    for yearly_tax_rate_idx in yearly_tax:
        print("Year: ", yearly_tax[yearly_tax_rate_idx].year)
        print("State: ", yearly_tax[yearly_tax_rate_idx].state)
        print("Federal Taxes: ", yearly_tax[yearly_tax_rate_idx].fed_tax)

main()