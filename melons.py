"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """Abstract class for melon orders"""

    def __init__(self, species, qty, order_type, tax_percent):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax_percent = tax_percent
        self.shipped = False

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax_percent) * self.qty * base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty,
                                                  "domestic",0.08 )


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code

        super(InternationalMelonOrder, self).__init__(species, qty,
                                            "international", 0.17)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
