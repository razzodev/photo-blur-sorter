# Photo Blur Sorter

Sorts photos based on blurriness, moving blurry images to a separate folder.

This command-line tool helps you quickly identify and organize blurry photos, cleaning up your image library. It analyzes images for sharpness and moves blurry ones to a designated folder.

## Features

*   Detects blur using the Laplacian variance method.
*   Handles various image formats, including RAW files (DNG, CR2, NEF, etc.).
*   Creates an output folder (default: `blurry_images`) within the input directory.
*   Customizable blur threshold.
*   Operates on the current directory if no directory is specified.

## Installation

1.  **Python:** Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).
2.  **Dependencies:** Open your terminal or command prompt and install the required libraries:

    ```bash
    pip install opencv-python rawpy
    ```

## Usage

1.  **Save the script:** Download the `blursorter.py` file and save it to a convenient location.
2.  **Run from the command line:** Open your terminal, navigate to the directory where you saved `blursorter.py`, and run:

    *   To process images in the *current* directory:

        ```bash
        python blursorter.py
        ```

    *   To process images in a *specific* directory:

        ```bash
        python blursorter.py /path/to/your/photos
        ```

    Replace `/path/to/your/photos` with the actual path to the directory containing your images.

## Options

*   `-t` or `--threshold`: Adjust the blur sensitivity. Lower values (e.g., 200, 300) detect more subtle blur. The default is **500**.
*   `-o` or `--output`: Change the name of the output folder for blurry images. The default is `blurry_images`.

## Examples

*   Sort blurry images in the current directory with the default threshold (500) and output folder name:

    ```bash
    python blursorter.py
    ```

*   Sort blurry images in a specific directory with a custom threshold (600) and output folder name:

    ```bash
    python blursorter.py /my/pictures/wedding -t 600 -o bad_shots
    ```

## Threshold and Calibration

The `-t` or `--threshold` option controls the sensitivity of the blur detection. A *lower* threshold means the script will be more sensitive and identify more images as blurry. A *higher* threshold means it will only flag very obviously blurry images.

The optimal threshold value can vary significantly depending on factors like:

*   **Image resolution:** Higher resolution images generally have higher variance values.
*   **Camera settings:** Shutter speed, aperture, and ISO can affect image sharpness and therefore the variance.
*   **Type of blur:** Motion blur, defocus blur, and other types of blur produce different variance characteristics.
*   **Image content:** Images with lots of fine detail will have higher variance than images with smooth gradients.

**Calibration:**

To find the best threshold for your photos, we recommend the following calibration step:

1.  Create a small test set of images containing examples of clearly sharp images, slightly blurry images, and very blurry images.
2.  Run the script on this test set with different threshold values (e.g., 200, 500, 700).
3.  Observe the results and choose the threshold that best separates your sharp and blurry images.

This calibration process will help you fine-tune the script for your specific needs and achieve the most accurate results.

## How it works

The script reads each image in the specified directory, converts it to grayscale, and calculates the Laplacian variance. This value is a measure of image sharpness. If the variance is below the specified threshold, the image is considered blurry and moved to the output folder.

## Contributing

Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.

## License

[MIT License](LICENSE) (Add a LICENSE file to your repository)
