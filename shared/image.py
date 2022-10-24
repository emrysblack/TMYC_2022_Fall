class Image():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._dimensions = self.width * self.height
        self._pixels = []
        
    def load(self, data):
        if len(data) % self._dimensions != 0:
            raise ValueError(f'Could not load image data to dimensions {self.width} x {self.height}')
        
        self._data = data
        self._layers = int(len(data) / self._dimensions)
        self.__get_display_data()
        return self
    
    def load_from_file(self, path):
        with open(path, mode ='r') as file:
            data = file.read()
            return self.load(data)

    def display(self):
        # define terminal color values for display
        colors = {'0': "\033[40m \033[0m", '1': "\033[47m \033[0m", '2': " "}
        # print image
        for index in range(0, self._dimensions, self.width):
            row = self._pixels[index:index + self.width]
            print(''.join([colors[pixel] for pixel in row]))
    
    def __get_display_data(self):
        """
        flattens layered data into a single display layer
        """
        # get first non-transparent pixel for each position
        self._pixels = [next(filter(lambda x: x != "2", self._data[i::self._dimensions]),"2") for i in range(self._dimensions)]