import numpy as np
from PIL import Image


class RifImage:
    """
    RifImage is a custom image file format for educational purposes.
    It contains a 9-byte header specifying the image's dimensions followed by 
    a sequence of 3-byte groups representing RGB values.
    """
    def __init__(self, file: str, is_jpeg: bool = False) -> None:
        """
        Initializes the RifImage object.

        Args:
            file (str): The path to the image file.
            is_jpeg (bool, optional): If the given file is in JPEG format. Defaults to False.
        """  # noqa: E501
        if is_jpeg:
            self.image_pixels_array = np.array(Image.open(file).convert('RGB'))
        else:
            self.image_pixels_array = RifImage._convert_rif_to_numpy_array(file)

    @staticmethod
    def _convert_rif_to_numpy_array(rif_file_name: str) -> np.ndarray:
        """
        Convert a RIF file to a NumPy array.

        Args:
            rif_file_name (str): The path to the RIF file.

        Returns:
            np.ndarray: The image represented as a NumPy array.
        """
        with open(rif_file_name, 'rb') as f:
            header_w, header_h = f.read(9).decode('utf8').split('x')
            header_w, header_h = int(header_w), int(header_h)
            total_bytes = 3 * header_w * header_h
            byte_data = f.read(total_bytes)

        return np.frombuffer(byte_data, dtype=np.uint8).reshape(header_w, header_h, 3)

    def convert_rif_to_jpg(self, file_name: str) -> None:
        """
        Convert the RIF image to JPEG and save it.

        Args:
            file_name (str): The path to save the JPEG image.
        """
        Image.fromarray(self.image_pixels_array).save(file_name, format='JPEG')

    def save(self, file_name: str) -> None:
        """
        Write the image data to a RIF file.

        Args:
            file_name (str): The path to save the RIF file.
        """
        h, w, _ = self.image_pixels_array.shape
        with open(file_name, "wb") as f:
            f.write(f'{h:04}x{w:04}'.encode('utf8'))
            f.write(bytes(self.image_pixels_array.flatten()))
