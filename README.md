# Face Extraction using RetinaFace

This script extracts faces from images in a specified input folder and saves the extracted faces to an output folder. It uses the RetinaFace library for face detection and allows for optional face alignment. The script also includes a progress bar using `tqdm` to show the processing status of each image.

## Requirements

- Python 3.11+
- retinaface
- opencv-python
- tqdm

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kiendoantrung/face-extraction.git
   cd face-extraction
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the script without align, use the following command:

```bash
python extract_faces.py --folder_in /path/to/input/folder --folder_out /path/to/output/folder
```

To run the script with align, use the following command:

```bash
python extract_faces.py --folder_in /path/to/input/folder --folder_out /path/to/output/folder --align
```
