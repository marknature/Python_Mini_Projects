import qrcode
import os

def generate_qr_code(data, filename="my_qr_code.png", project_dir="pythonProject"):
    """
    Generates a QR code image and saves it to a file.

    Args:
        data (str): The data to be encoded in the QR code.
        filename (str, optional): The name of the output file. Defaults to "my_qr_code.png".
        project_dir (str, optional): The project directory where the QR code will be saved. Defaults to "pythonProject".
    """

    # Create the project directory if it doesn't exist
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)

    # Create the full file path
    file_path = os.path.join(project_dir, filename)

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified file path
    img.save(file_path)

    print(f"QR code generated and saved to {file_path}")

if __name__ == "__main__":
    data = input("Enter link to generate QR code: ")
    generate_qr_code(data)

# OR

from PIL import Image

link = input("Enter link to generate QR code: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRcode.png", scale=10)
Image.open("QRcode.png")
