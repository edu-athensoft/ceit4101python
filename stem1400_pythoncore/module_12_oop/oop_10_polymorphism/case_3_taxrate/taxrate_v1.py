"""
Tax Rate
version: v1
"""


class Tax:
    def __init__(self, pst=0, province='unknown'):
        self.province = province
        self.gst = 0.05
        self.pst = pst


class TaxGST(Tax):
    def getTaxRate(self):
        return self.gst


class TaxHST(Tax):
    def __init__(self, pst, province):
        super().__init__(pst, province)
        self.hst = self.gst + self.pst

    def getTaxRate(self):
        return self.hst


class TaxGPST(Tax):
    def getTaxRate(self):
        return self.gst + self.pst


class ClientApp:
    def queryTaxRate(self, taxObj):
        print(f'{taxObj.province} sets the tax rate at {taxObj.getTaxRate():.3%}.')

# main
myapp = ClientApp()

# Quebec
qcTax = TaxGPST(0.09975, 'Quebec')
myapp.queryTaxRate(qcTax)
print()

# Ontario
onTax = TaxHST(0.08, 'Ontario')
myapp.queryTaxRate(onTax)
print()

# Alberta
abTax = TaxGST(province='Alberta')
myapp.queryTaxRate(abTax)
print()

# BC
bcTax = TaxGPST(0.07, 'British Columbia')
myapp.queryTaxRate(bcTax)