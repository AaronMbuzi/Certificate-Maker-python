from PIL import Image, ImageDraw, ImageFont

# Load the certificate template image, Ensure the full name with image extention (png,jpg...)
template = Image.open("certificate_template.png")

# Type the font type and font size of your choice in the argument below.
font = ImageFont.truetype("arial.ttf", 50)

# Define the initial position of the name on the certificates
x = 730
y = 620

# Load the list of names to appear on the certificates.
names = ["James Muldowney", "Korinne Balsinger", "Angella Tiley"]

for name in names:
    certificate = template.copy()
    draw = ImageDraw.Draw(certificate)
    draw.text((x, y), name, fill=(0, 0, 0), font=font)
    certificate_filename = f"certificate_{name.replace(' ', '_')}.png"
    certificate.save(certificate_filename)
    print(f"Certificate for {name} created: {certificate_filename}")

