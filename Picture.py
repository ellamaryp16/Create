from PIL import Image, ImageFilter
cake = Image.open('C:/Users/jtsul/Desktop/Capture.PNG')
apple = cake.load()
print(apple[400, 234])
apple[400, 234] = (0, 0, 0)
cake.load()
WHITE = 255
BLACK = 0
MODE = 'L'


def draw_circle(r, color, location, image):
    px = image.load()
# x_pixel and y_pixel are pixel that the program is examining at any moment
    x_pixel = image.size[0]
# x_location and y location are the center point
    x_location = location[0]
    y_location = location[1]
    while x_pixel >= 0:
        y_pixel = image.size[1]
        while y_pixel >= 0:
            # this part makes two values to use in the equation
            x = x_pixel - x_location
            y = y_pixel - y_location
            if x**2 + y**2 <= r**2:
                px[x_pixel, y_pixel] = color
            y_pixel -= 1
        x_pixel -= 1
    return image


def amount_of_color(image, color):
    pix = image.load()
    image_x = image.size[0]
    amount_color = 0
    while image_x >= 0:
        image_y = image.size[1]
        while image_y >= 0:
            if pix[image_x-1, image_y-1] == color:
                amount_color += 1
            image_y -= 1
        image_x -= 1
    return amount_color


def compare_image_num_color(image1, image2, color):
    image1_size = image1.size[0] * image1.size[1]
    image2_size = image2.size[0] * image2.size[1]
    image1_percent_color = amount_of_color(image1, color)/image1_size
    image2_percent_color = amount_of_color(image2, color)/image2_size

    difference = abs(image1_percent_color - image2_percent_color)
    return 100 - 100*difference


def all_colors(image):
    # find all colors in an image and return a list that contains all of those colors
    px = image.load()
    x = 0
    y = 0
    colors = []
    while x < image.size[0]:
        y = 0
        while y < image.size[1]:
            pixel = px[x, y]
            if pixel not in colors:
                colors.append(pixel)
            y += 1
        x += 1
    return colors


def compare_all_colors(image1, image2):
    colors = all_colors(image1) + all_colors(image2)
    colors = list(dict.fromkeys(colors))
    i = 0
    total = 0
    while i <= len(colors)-1:
        total += compare_image_num_color(image1, image2, colors[i])
        i += 1
    average = total / len(colors)
    return average


myImage = Image.new('L', (100, 100), color=WHITE)
draw_circle(4, BLACK, (50, 50), myImage)
myImage.show()
myImage2 = Image.new('L', (100, 100), color=WHITE)
draw_circle(8, BLACK, (50, 50), myImage2)
myImage2.show()
print(compare_image_num_color(myImage, myImage2, BLACK))
print(compare_all_colors(myImage, myImage2))

