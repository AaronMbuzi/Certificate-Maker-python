# Certificate-Maker Documentation
Simple Python Script used for creating Certificates from an image template with a list of Names provided.

Load the certificate template image, Ensure the full name with image extention (png,jpg...)
```python
template = Image.open("certificate_template.png")
```
Type the font type and font size of your choice in the argument below.
```python
font = ImageFont.truetype("arial.ttf", 50)
```
Define the initial position of the name on the certificates using coordinates Below.
```python
x = 730
y = 620
```
Load the list of names to appear on the certificates as shown below.
```python
names = ["James Muldowney", "Korinne Balsinger", "Angella Tiley"]
```
