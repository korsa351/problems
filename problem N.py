class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, number):
        if number > 0:
            self.extend([number])
        else:
            raise NonPositiveError()
