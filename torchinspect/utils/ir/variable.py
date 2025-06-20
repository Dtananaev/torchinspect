__all__ = ['Variable']


class Variable:
    def __init__(self, name, dtype, shape=None):
        self.name = name
        self.dtype = dtype
        self.shape = shape


    @property
    def dtype(self):
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        self._dtype = dtype.lower()

    @property
    def ndim(self):
        return len(self.shape)

    def size(self):
        return self.shape

    def dim(self):
        return self.ndim

    def __repr__(self):
        text = '%' + self.name + ': ' + self.dtype
        if self.shape is not None:
            text += '[' + ', '.join([str(x) for x in self.shape]) + ']'
        return text
