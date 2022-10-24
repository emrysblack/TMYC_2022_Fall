class Image():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._dimensions = self.width * self.height
        self._pixels = []
        
    def load(self, data):
        if len(data) % self._dimensions != 0:
            raise ValueError(f'Could not load image data to dimensions {self.width} x {self.height}')
        
        self._layers = int(len(data) / self._dimensions)
        self._pixels = self.__get_display_data(data)
        return self
    
    def load_from_file(self, path):
        with open(path, mode ='r') as file:
            data = file.read()
            return self.load(data)

    def display(self):
        # define terminal color values for display
        colors = {'0': "\033[40m \033[0m", '1': "\033[47m \033[0m", '2': " "}
        # print image
        for i in range(0, self._dimensions, self.width):
            row = self._pixels[i:i + self.width]
            print(''.join([colors[pixel] for pixel in row]))
    
    def __get_display_data(self, data):
        """
        flattens layered data into a single display layer
        """
        return [
            # get first non-transparent pixel for each position
            next(filter(lambda x: x != "2", data[i::self._dimensions]),"2") 
            for i in range(self._dimensions)
        ]