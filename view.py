from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO


# Ask user for input
text = input("Enter text for banner: ")
background_choice = input("Choose a background color (blue, cyan, grey, green, purple): ")

# Define background colors
if background_choice.lower() == "blue":
    background_color = (0, 92, 169)  # dark blue
    background_gradient = False
elif background_choice.lower() == "cyan":
    background_color = (50, 168, 168)  # cyan
    background_gradient = False
elif background_choice.lower() == "grey":
    background_color = (128, 128, 128)  # grey
    background_gradient = False
elif background_choice.lower() == "green":
    background_color = (50, 168, 81)  # green
    background_gradient = False
elif background_choice.lower() == "purple":
    background_color = (153, 0, 255)  # purple
    background_gradient = False

else:
    background_color = (255, 255, 255)  # white
    background_gradient = True

# Define font
FONT = ImageFont.truetype("Poppins-Bold.ttf", size=80)

# Define image size and create image
WIDTH, HEIGHT = 960, 540
banner = Image.new("RGB", (WIDTH, HEIGHT), background_color)

# Draw text on image
draw = ImageDraw.Draw(banner)
text_width, text_height = draw.textsize(text, FONT)
x = (WIDTH - text_width) // 2
y = (HEIGHT - text_height) // 2
draw.text((x, y), text, fill=(255, 255, 255), font=FONT, align="center")

# Add gradient if background_gradient is True
if background_gradient:
    gradient = Image.new("L", (WIDTH, HEIGHT))
    for x in range(WIDTH):
        for y in range(HEIGHT):
            gradient.putpixel((x, y), int(255 * x / WIDTH))
    banner.putalpha(gradient)

# Save and display image
banner.save("banner.png")
banner.show()
