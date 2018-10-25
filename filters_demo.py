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


def right_flip(image):
    img.show()
    pixmap = img.load()
    for i in range(img.size[0]//2):
        for j in range(img.size[1]):
            pixmap[i,j] =pixmap[img.size[0]-1-i, j]
    img.show()

def background_flip(image):
    img.show()
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]//2):
            pixmap[i,j] = pixmap[img.size[0]-1-i, j]
    img.show()

def top_flip(image):
    img.show()
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]//2):
            pixmap[i,j] = pixmap[i, img.size[1]-1-j]
    img.show()

if __name__ == "__main__":
    img = Image.open("beach.jpg")
    #deep_fried("Kermit.jpg")
    #swap("beach.jpg")
    #shaded("Chicken.jpg")
    #average("beach.jpg")
    #left_flip("beach.jpg")
    top_flip("beach.jpg")