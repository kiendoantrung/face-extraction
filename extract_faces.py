import os
import argparse
from retinaface import RetinaFace
import cv2
from tqdm import tqdm

def extract_faces_from_folder(folder_in, folder_out, align):
    """
    Extracts faces from images in a folder and saves them to another folder.

    Args:
        folder_in (str): Path to the input folder containing images.
        folder_out (str): Path to the output folder where the extracted faces will be saved.
        align (bool): Flag indicating whether to perform face alignment.
    """
    if not os.path.exists(folder_out):
        os.makedirs(folder_out)

    image_files = [f for f in os.listdir(folder_in) if f.endswith(('.png', '.jpg', '.jpeg'))]

    for filename in tqdm(image_files, desc="Processing images"):
        img_path = os.path.join(folder_in, filename)
        faces = RetinaFace.extract_faces(img_path=img_path, align=align)
        for i, face in enumerate(faces):
            face_rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face_filename = f"{os.path.splitext(filename)[0]}.png"
            face_path = os.path.join(folder_out, face_filename)
            cv2.imwrite(face_path, face_rgb)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract faces from images using RetinaFace")
    parser.add_argument("--folder_in", required=True, help="Path to the input folder containing images")
    parser.add_argument("--folder_out", required=True, help="Path to the output folder to save extracted faces")
    parser.add_argument("--align", default=False, action='store_true', help="Whether to align faces")

    args = parser.parse_args()

    extract_faces_from_folder(args.folder_in, args.folder_out, args.align)
