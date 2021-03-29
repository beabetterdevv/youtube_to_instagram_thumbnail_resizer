# Our source image is 1280x720
sourceImageWidth = 1280 
sourceImageHeight = 720  

# We want to convert it to a new image that is 1080x1080
destinationImageWidth = 1080
destinationImageHeight = 1080

# How? We need to reduce our source's width to 1080. The height must also be reduced by a the same 
# percentage drop. Then, we center the image by offsetting by the new height

from PIL import Image

#Don't forget to run `pip install Pillow`

def resize():
	# 1. Determine drop percentage
	sourceImageWidthDropAmount = sourceImageWidth - destinationImageWidth # i.e. 1280 - 1080 = 200
	sourceImageDropPercent = float(sourceImageWidthDropAmount / sourceImageWidth) 

	# 2. Reduce the height by the same percentage the width dropped
	adjustedSourceImageWidth = 1080.0
	adjustedSourceImageHeight = sourceImageHeight - (sourceImageHeight * sourceImageDropPercent)

	# Now, we have the new width and height of our source image, adjusted for 1080x1080
	print('new width: ' + str(adjustedSourceImageWidth))
	print('new height: ' + str(adjustedSourceImageHeight))

	# 3. Create a temporary image with black background in the desired width x height
	tempBlack = Image.new('RGB', (destinationImageWidth, destinationImageHeight), (0,0,0))

	# 4. Open our source image and adjust it using the new height
	img = Image.open('thumbnail.png')
	img = img.resize((int(adjustedSourceImageWidth), int(adjustedSourceImageHeight)))

	# 5. Determine where our resized image should start
	adjustedImageStartingHeight = (destinationImageHeight - adjustedSourceImageHeight) / 2

	# 6. Paste the resized image onto the black background at width 0 and height the value above
	tempBlack.paste(img, (0, int(adjustedImageStartingHeight)))

	# 7. Save the temp image 
	tempBlack.save('thumbnail_ig_resized.png')


resize()

