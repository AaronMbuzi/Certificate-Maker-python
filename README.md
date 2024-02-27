# Certificate-Maker Documentation
Simple Python Script used for creating Certificates from an image template with a list of Names provided.

Open the Certificate Maker.py file using a text editor of your choice (VSCode, Notepad, Pycharm...).

Load the certificate template image, Ensure the full name with image extention (png,jpg...) in the same location as the python script.
```python
template = Image.open("certificate_template.png")
```
Type the font type and font size of your choice in the argument below.
```python
font = ImageFont.truetype("arial.ttf", 50)
```
Define the initial position of the name on the certificates using x and y coordinates Below. You are free to adjust the corodinates to ensure the names fit where they are supposed to on the certificate.
```python
x = 730
y = 620
```
Load the list of names to appear on the certificates as shown below.
```python
names = ["James Muldowney", "Korinne Balsinger", "Angella Tiley"]
```
## Example
There is a template certificate named certificate_template.png that is already loaded with the script with a set of the following names; James Muldowney, Korinne Balsinger, Angella Tiley. Make sure you have python installed with the Pillow module. if not use the following command:
```python
pip install Pillow
```
If all have been installed, run the python script and wait for it to create your certificates. 
This will only work with images.

by Aaron Mbuzi
