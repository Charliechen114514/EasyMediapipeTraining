class FractionOfDataset:
    """
        settings are here
    """
    DEF_TRAIN_FRAC = 8
    DEF_VALID_FRAC = 1
    DEF_TEST_FRAC  = 1
    """
        initialize
    """
    def __init__(self):
        self.train_frac = FractionOfDataset.DEF_TRAIN_FRAC
        self.valid_frac = FractionOfDataset.DEF_VALID_FRAC
        self.test_frac  = FractionOfDataset.DEF_TEST_FRAC

    def __str__(self):
        res = self.transform_to_mediapipe()
        return "Train: {}, Valid: {}, Test: {}"\
            .format(self.train_frac, self.valid_frac, self.test_frac) + \
            "\nwith shell set percentage at: [{}, {}]\n".format(res[0], res[1])

    def set_split_param(self, train: int, validation: int, test: int):
        self.train_frac = train
        self.valid_frac = validation
        self.test_frac  = test

    def check_params(self):
        if self.train_frac <= 0 or self.valid_frac <= 0 or self.test_frac <= 0:
            raise ValueError("Invalid Split error!")

    def transform_to_mediapipe(self):
        return [float(self.train_frac) / float(self.train_frac + self.test_frac + self.valid_frac), \
                float(self.valid_frac) / float(self.test_frac + self.valid_frac)]
