# Photo Blur Sorter

Sorts photos based on blurriness, moving blurry images to a separate folder.

This tool helps you quickly identify and organize blurry photos, cleaning up your image library. It analyzes images for sharpness and moves blurry ones to a designated folder.

## Features

*   Detects blur using the Laplacian variance method.
*   Handles various image formats, including RAW files (DNG, CR2, NEF, etc.).
*   Creates an output folder (default: `blurry_images`) within the input directory.
*   Customizable blur threshold.

## Installation

1.  **Python:** Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).
2.  **Dependencies:** Open your terminal or command prompt and install the required libraries:

    ```bash
    pip install opencv-python rawpy
    ```

## Usage

1.  **Save the script:** Download the `blursorter.py` file and save it to a convenient location.
2.  **Run from the command line:** Open your terminal, navigate to the directory where you saved `blursorter.py`, and run:

    ```bash
    python blursorter.py /path/to/your/photos
    ```

    Replace `/path/to/your/photos` with the actual path to the directory containing your images.

## Options

*   `-t` or `--threshold`: Adjust the blur sensitivity. Lower values (e.g., 50, 80) detect more subtle blur. The default is 100.
*   `-o` or `--output`: Change the name of the output folder for blurry images. The default is `blurry_images`.

## Examples

*   Sort blurry images with the default threshold (100) and output folder name:

    ```bash
    python blursorter.py /my/pictures/vacation
    ```

*   Sort blurry images with a lower threshold (80) and a custom output folder name:

    ```bash
    python blursorter.py /my/pictures/wedding -t 80 -o bad_shots
    ```

## How it works

The script reads each image in the specified directory, converts it to grayscale, and calculates the Laplacian variance. This value is a measure of image sharpness. If the variance is below the specified threshold, the image is considered blurry and moved to the output folder.

## Contributing

Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.

## License

[MIT License](LICENSE) (Add a LICENSE file to your repository)
