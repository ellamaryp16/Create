from PIL import Image, ImageFilter
cake = Image.open('C:/Users/jtsul/Desktop/Capture.PNG')
#gale = Image.open('')
apple = cake.load()
print(apple[400,234])
apple[400,234] = (0,0,0)
cake.load()
WHITE = 255
BLACK = 0
MODE = 'L'

def draw_circle(r, color, location, image):
    px = image.load()
#x_pixel and y_pixel are pixel that the program is examining at any moment
    x_pixel = image.size[0]
#x_location and y location are the center point
    x_location = location[0]
    y_location = location[1]
    while x_pixel >= 0:
        y_pixel = image.size[1]
        while y_pixel >= 0:
            #this part makes two values to use in the equation
            x = x_pixel - x_location
            y = y_pixel - y_location
            if x**2 + y**2 <= r**2:
                px[x_pixel,y_pixel] = color
            y_pixel -= 1
        x_pixel -= 1
    return image
def amount_of_color(image, color):
    pix = image.load()
    imagex = image.size[0]
    amount_color = 0
    while imagex >= 0:
        imagey = image.size[1]
        while imagey >= 0:
            if pix[imagex-1,imagey-1] == color:
                amount_color+= 1
            imagey -= 1
        imagex -= 1
    return amount_color
def compare_image_num_color(image1, image2,color):
    image1_size = image1.size[0] * image1.size[1]
    image2_size = image2.size[0] * image2.size[1]
    image1_percent_color = amount_of_color(image1,color)/image1_size
    image2_percent_color = amount_of_color(image2, color)/image2_size

    difference = abs(image1_percent_color - image2_percent_color)
    return 100 - 100*difference

myImage = Image.new('L', (100, 100), color=WHITE)
draw_circle(4,BLACK, (50,50), myImage)
myImage.show()
myImage2 = Image.new('L', (100, 100), color=WHITE)
draw_circle(4, BLACK, (50,50), myImage2)
myImage2.show()
print(compare_image_num_color(myImage, myImage2, BLACK))






