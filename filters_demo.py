from PIL import Image




def deep_fried(image):
    img = Image.open(image)
    img.show()
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r += 100**3
            g -= 50*3
            b -= 500**3
            
            pixmap[i,j] = (r, g, b)
    img.show()
    img.save("Kermit.jpg")
    
def swap(image):
    img = Image.open(image)
    img.show()
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixmap[i,j]
            r += g
            g += b
            b += r
            
            pixmap[i,j] = (r, g, b)
    img.show()
    
def shaded(image):
    img = Image.open(image)
    img.show()
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(0,img.size[1],5):
            r, g, b = pixmap[i,j]
            r += 100
            g += 50*6
            b += 25
            
            pixmap[i,j] = (r, g, b)
    img.show()
    img.save("Chicken.jpg")
    
def average(image):
    img = Image.open(image)
    img.show()
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(0,img.size[1],5):
            r, g, b = pixmap[i,j]
            r += ((r+g+b) /3)
            g += ((r+g+b) /3)
            b += ((r+g+b) /3)
            
            pixmap[i,j] = (r, g, b)
    img.show()

def sda(image):
    img = Image.open(image)
    img.show()
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(0,img.size[1],5):
            r, g, b = pixmap[i,j]
            255 - r = r
            255 - g = g
            255 - b = b
            
            pixmap[i,j] = (r, g, b)
    img.show()
    
if __name__ == "__main__":
    #deep_fried("Kermit.jpg")
    #swap("beach.jpg")
    #shaded("Chicken.jpg")
    #average("beach.jpg")
    pass