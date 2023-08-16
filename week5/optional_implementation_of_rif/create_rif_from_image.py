'''rif is  a custom image file format for educational purposes
it consists of a 9-byte header that specifies the dimensions of the image
followed by a series of 3 bytes representing the RGB values'''
from PIL import Image
import numpy as np
class RifImage:
    def __init__(self, file, is_jpeg=False):
        if is_jpeg:
            self.image_pixels_array = np.array(Image.open(file).convert('RGB'))
        else:
            self.image_pixels_array = RifImage.rif_to_numpy_array(file)
    @staticmethod
    def rif_to_numpy_array(rif_file_name) -> np.ndarray:
        with open(rif_file_name, 'rb') as f:
            header_w, header_h = f.read(9).decode('utf8').split('x')
            header_w, header_h = int(header_w), int(header_h)
            total_bytes = 3 * header_w * header_h
            byte_data = f.read(total_bytes)
        np_array = np.frombuffer(byte_data, dtype=np.uint8)
        return np_array.reshape(header_w, header_h, 3)


    def convert_rif_to_jpg(self, file_name):
        image = Image.fromarray(self.image_pixels_array)
        image.save(file_name, format='JPEG')
    def write_rif(self, file_name):
        '''writes a rif to a file'''
        h, w, _ = self.image_pixels_array.shape
        flattened_bytes = bytes(self.image_pixels_array.flatten())
        with open(file_name, "wb") as f:
            f.write(f'{h:04}x{w:04}'.encode('utf8'))
            f.write(flattened_bytes)



if __name__ == '__main__':
    rif = RifImage("photo-jpeg-example.jpg", is_jpeg=True)
    rif.write_rif("my_rif.rif")
    rif2 = RifImage("my_rif.rif")
    rif2.convert_rif_to_jpg("new_image.jpg")

