class LoggableList(list, Loggable):
    def append(self, *args):
        self.log(*args)
        self += list(args)
