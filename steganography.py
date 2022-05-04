from modules import Image
from modules import numpy as np


# Encoding function
def Encode(source, message, destination, stg):

    # open image in read mode
    img = Image.open(source, 'r')

    # get image dimensions
    width, height = img.size

    # convert img data to numpy array - collection of channels of pixels (decimals)
    image = np.array(list(img.getdata()))

    # number of image channels (4 for PNG - RGBA)
    channel = 4

    # number of pixels = image size / channel
    total_pixels = image.size//channel

    # extend message with delimiter
    message += "$t3g0"

    # convert message to binary messsage (decimal to binary)
    binary_message = ''.join([format(ord(i), "08b") for i in message])

    # number of pixels to be altered
    req_components = len(binary_message)

    # check if required pixels are present in image
    # if not, raise error
    # else proceed encoding 
    if req_components > total_pixels:
        stg.GreaterSizeRequired()
    else:
        # reference to message bit to be encoded
        message_index = 0
        # for every pixel in image
        for pixel in range(total_pixels):
            # for every component of pixel
            for colour in range(0, 3):
                # if message still left to be encoded,
                # then encode,
                # else break
                if message_index < req_components:
                    # change the LSB-bit of the pixel's component:
                    # grab the binary form of the component value(R/G/B),
                    # remove the LSB
                    # append the message bit
                    # convert back to int
                    # save the new value calculated
                    image[pixel][colour] = int(
                        bin(image[pixel][colour])[:-1] + binary_message[message_index], 2)
                    message_index += 1

        # reshape matrix
        image = image.reshape(height, width, channel)

        # covert the numpy img data to image file (.PNG)
        enc_img = Image.fromarray(image.astype('uint8'), img.mode)

        # save the image at the destination folder
        enc_img.save(destination)

        # open the success dialog
        stg.OpenSuccessDialog()


# Decoding function
def Decode(src, stg):

    # clear previous decoded message on window
    stg.text_.delete(1.0, "end")
    
    # open image in read mode
    img = Image.open(src, 'r')

    # convert img data to numpy array - collection of channels of pixels (decimals)
    image = np.array(list(img.getdata()))

    # number of image channels (4 for PNG - RGBA)
    channel = 4

    # number of pixels = image size / channel
    total_pixels = image.size//channel

    # bits to decoded from the encoded image
    hidden_bits = ""

    # for every pixel in image
    for pixel in range(total_pixels):
        # for every component of pixel
        for colour in range(0, 3):
            # grab the LSB of every component of pixel
            hidden_bits += (bin(image[pixel][colour])[-1])

    # split the bits into groups of 8 bits to form it into ASCII character later
    hidden_bytes = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    # decoded message
    message = ""

    # for every byte in hidden bytes
    for i in range(len(hidden_bytes)):
        # if delimiter is found then break
        if message[-5:] == "$t3g0":
            break
        # convert binary to int to character using ASCII values
        # and append in message
        message += chr(int(hidden_bytes[i], 2))
    
    # if image was encoded (at least delimiter is present)
    if "$t3g0" in message:
        # remove the delimiter
        stg.decoded_message = message[:-5]
        # clear decoded message window
        stg.text_.delete(1.0, "end")
        # display decoded message
        stg.text_.insert("end", stg.decoded_message)
    # if image was not encoded, delimiter will be absent
    else:
        # clear decoded message window
        stg.text_.delete(1.0, "end")
        # open no message found window
        stg.NoHiddenMessageDialog()