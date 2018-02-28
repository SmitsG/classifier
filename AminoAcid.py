# Class AminoAcid stores amino_acid values.
class AminoAcid:
    def __init__(self, polarity, hydrofobicity, given):
        """
        :param polarity: Polarity of a row from a csv file.
        :param hydrofobicity: Hydrofobicity from a row in a csv file.
        :param given: Given class from a row in a csv file.
        """
        self.pol = polarity
        self.hyd = hydrofobicity
        self.giv = given

    def get_polarity(self):
        return self.pol

    def get_hydrofobicity(self):
        return self.hyd

    def get_class_given(self):
        return self.giv