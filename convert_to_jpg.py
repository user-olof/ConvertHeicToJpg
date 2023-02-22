import argparse
import glob
import os
import sys
import PIL
from PIL import Image
from pillow_heif import register_heif_opener

class PathSplit():
    def split_all_parts(self, path):
        dir = os.path.dirname(path)
        base = os.path.basename(path)
        parts = (path, dir, base)
        ext_split = os.path.splitext(base)
        parts = parts + tuple(ext_split)
        return parts

    def fun_path_splits(self, heic_list):
        return tuple(self.split_all_parts(h) for h in heic_list)


class JpegConversion:

    def convert_to_jpg(self, images):
        register_heif_opener()
        for i, split in enumerate(images):
            try:
                with Image.open(images[i][0]) as im:
                    print(im)
                    jpg_path = os.path.join(images[i][1], images[i][3] + '.jpg')
                    im.save(jpg_path)
            except PIL.UnidentifiedImageError:
                raise Exception("Cannot open image " + images[i][3])


def main():
    parser = argparse.ArgumentParser(description='Convert HEIF file format to JPEG file format')
    parser.add_argument('-p', '--path', required=True, type=str, help='Path to folder containing HEIC files')
    parser.add_argument('-f', '--file', required=False, type=str, help='File name of HEIC file')
    args = parser.parse_args()

    print(args.path)
    try:
        os.stat(args.path)
    except FileNotFoundError:
        print('File path is invalid. Please try again!')
        sys.exit(1)

    files = "*.heic"
    if type(args.file) == type(str) and len(args.file) != 0:
        files = args.file

    def join_tuple(tuple_elem) -> str:
        return " ".join(tuple_elem)

    try:
        search_path = os.path.join(args.path, files)
        heic_list = glob.glob(search_path)
        print(heic_list)
        # create tuple of tuples holding the elements of the heic file paths
        ps = PathSplit()
        heic_splits = ps.fun_path_splits(heic_list)

        # converting the file format from HEIF to JPEG
        jc = JpegConversion()
        jc.convert_to_jpg(heic_splits)
    except Exception as e:
        print(e)
        sys.exit(1)

    print("Program finished. Please check your folder now")


