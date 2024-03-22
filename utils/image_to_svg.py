from PIL import Image
import svgwrite

def imageToSVG(input_path, output_path):
    # Open the WebP image using Pillow
    img = Image.open(input_path)
    
    # Create an SVG image with the same dimensions
    svg_img = svgwrite.Drawing(output_path, size=(img.width, img.height))
    
    # Get pixel data from the image
    pixel_data = list(img.getdata())
    
    # Iterate over each pixel in the image
    for y in range(img.height):
        for x in range(img.width):
            # Get the RGB color value of the pixel
            r, g, b = pixel_data[y * img.width + x]
            print((r,g,b))
            
            # Create an SVG rectangle for each pixel
            svg_img.add(svgwrite.shapes.Rect(insert=(x, y), size=(1, 1), fill=f'rgb({r}, {g}, {b})'))
    
    # Save the SVG image
    svg_img.save()


imageToSVG("tkwtkicjxv.webp","tkwtkicjxv-new.svg")