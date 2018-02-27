# Class AminoAcid stores amino_acid values.
class AminoAcid:
    def __init__(self, polarity, hydrofobicity, given):
        self.pol = polarity
        self.hyd = hydrofobicity
        self.giv = given

    def get_polarity(self):
        return self.pol

    def get_hydrofobicity(self):
        return self.hyd

    def get_class_given(self):
        return self.giv