
class ValueOutOfTheBoundError(Exception):
    """Exception raised for values out of the specified range."""

    def __init__(self,
                 value: float,
                 lower_bound: float,
                 upper_bound: float) -> None:
        self.value = value
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        super().__init__(f"Value '{value}' is out of the specified range [{lower_bound}, {upper_bound}].")
