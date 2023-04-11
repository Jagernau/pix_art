## Description:
**pix_art** is a pixel art photo styling application. It splits the photo into squares according to the set granularity.
<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/Jagernau/pix_art/files/IMG_20230410_235757_975.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/Jagernau/pix_art/files/me_grider.jpg" width="100" />
</p>

##### Platform:
Python>=3.8; OpenCV; NumPy
- For Linux, you can probably do it on Windows, too.
##### What the app does:
1. Splits up a photo into squares of the size you want.
2. Averages the colors in the squares.
3. Saves the processed photo to the default folder, which is automatically created `out_pic`.
4. Outputs the color of the square on the x, y axes.
## Setup:
1. Clone the repository: `https://github.com/Jagernau/pix_art`.
2. Go to the folder with the application: `pix_art`.
3. Best of all, create a sandbox for Python:
	- If virtualenv fans: `python<version> -m virtualenv env`
	- Activate the virtual environment: `source env/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a folder `in_pic` in the program folder `pix_art`, put a jpg or png image file in the folder.

## Use:
To use this program, run the `main.py` script in your terminal with the appropriate arguments. The program itself detects the last file added to the default directory `in_pic` . You do not need to specify a filename. Here is an example usage: `python main.py -g 10 -f image.jpg`.
This will pixelate the image `image.jpg` with a grid size of 10 and save the output image to the default output directory, which is `out_pic/`.
## Arguments
- `-g`, `--grid_size`: The size of each grid square (in pixels) that the image will be divided into. Default is 10.
- `-f`, `--file_name`: The name of the input file to be pixelated. If no file name is provided, the program will pixelate latest image in the input directory.
- `-i`, `--input_dir`: The directory where the input images are stored. Default is `in_pic/`.
- `-o`, `--output_dir`: The directory where the output images will be saved. Default is `out_pic/`.

#### Example Usage
Pixelate all images in the input directory with a grid size of 15: `python main.py -g 15`

Pixelate the image `my_image.png` with a size of 20 and save the output image to a custom output directory: `python main.py -g 20 -f my_image.png -o /path/to/output/dir/`


## Collaborative development:
I'd be happy to co-develop, even for the sake of learning the great and mighty Git. Who reads this README and has free time and desire to cobble, practice in Git:
1. Clone the project repository to your computer: `git clone https://github.com/Jagernau/pix_art`.
2. Create a separate branch for your work: `git checkout -b <branch name>`.
3. Make changes to your project code `git add .` and make commits describing the changes you've made `git commit -m "Description of changes you've made"`.
4 Submit your changes to GitHub: `git push origin <branch name>`.
5. Create a pull request on GitHub and wait for the changes to be checked and discussed.
*That seems to be it.*

## How to contribute:
- Improve the OOP of python.
- To output the color of the squares in HEX.
- And most interestingly, the ability to convert colors in a given palette.
- Make it possible to remove halftones, so that all colors would be localized.

## How to report bugs:
If you have a problem with the project or would like to suggest ideas to improve it, please create a new issue on GitHub. Describe the problem or idea in detail.
