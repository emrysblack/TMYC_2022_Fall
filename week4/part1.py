
def part1(data, width, height):
    # get layers
    layers = [data[i:i+width*height] for i in range(0, len(data), width*height)]
    # get frequency of layer with least '0'
    frequencies = sorted(
        [{i: layer.count(i) for i in set(layer)} for layer in layers], 
        key=lambda x: x.get("0", 0)
    )
    min_layer = frequencies[0]

    return min_layer.get("1",0) * min_layer.get("2",0)

def main():
    with open("week4/image.txt", mode ='r') as file:
        data = file.read()
    # verify file contents with width and height
    assert(len(data) % (25*6) ==0)
    
    print("part 1: ", part1(data, 25, 6))

if __name__ == "__main__":
    main()
