class LoggableList(list, Loggable):
    def append(self, elem):
        super(LoggableList, self).append(elem)
        self.log(elem)
