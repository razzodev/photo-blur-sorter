# photo-blur-sorter

## Quickly Find Your Blurry Photos!

This simple tool helps you find and move blurry photos so you can clean up your image library.

**What it does:**

*   Analyzes photos for blurriness.
*   Moves blurry photos to a new "blurry_images" folder (or a folder of your choice).

**How to use:**

1.  **Install:** Make sure you have Python installed. Then open your computer's terminal or command prompt and type:
    *   `pip install opencv-python`
    *   `pip install rawpy` (for RAW files)
2.  **Save the script:** Save the Python code as `blur_filter.py`.
3.  **Run:** Open your terminal, navigate to where you saved the script, and type:

    ```bash
    python blur_filter.py /path/to/your/photos
    ```

    Replace `/path/to/your/photos` with the folder where your photos are.

**Options:**

*   `-t`: Adjust how sensitive the blur detection is (lower numbers find more blur). Example: `-t 80`
*   `-o`: Change the name of the output folder. Example: `-o bad_photos`

**Example:**

```bash
python blur_filter.py /my/pictures -t 70 -o to_delete
```

This will check the `/my/pictures` folder, move blurry photos (using a sensitivity of 70) to a folder named `to_delete`.

**That's it!**
