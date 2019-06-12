
# LSB-HASH

## Usage

Create a `virtualenv` and install the requirements:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, merge and unmerge your files with:

```
python steganographyHash.py.py merge --img1=res/img1.jpg --img2=res/img2.jpg --output=res/output.png
python steganographyHash.py.py unmerge --img=res/output.png --output=res/output2.png
```

To use the **steganographyHash.py** class in your **Python** code, you will need to use the **Image** module from the **Pillow** library, for example:

```python
from PIL import Image

merged_image = steganographyHash.py.merge(Image.open(img1), Image.open(img2))
merged_image.save(output)
```

**Note**: the **output image** from the **merge operation** and the **input image** for the **unmerge operation** must be in **PNG** format.

## Script
Bash commands for automated testing.

```
chmod +x
./test.sh
```