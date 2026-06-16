import argparse
import glob
import os
import sys
import PIL
from PIL import Image
from pillow_heif import register_heif_opener

FIXED_WIDTH = 1080
FIXED_HEIGHT = 1920


def output_jpg_name(prefix, index, total):
    if total == 1:
        return f"{prefix}.jpg"
    return f"{prefix}_{index + 1}.jpg"


class PathSplit:
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

    def convert_to_jpg(self, images, rename_prefix=None):
        register_heif_opener()
        images = sorted(images, key=lambda split: split[3])
        total = len(images)
        for i, split in enumerate(images):
            try:
                with Image.open(split[0]) as im:
                    print(im)
                    if rename_prefix:
                        jpg_name = output_jpg_name(rename_prefix, i, total)
                    else:
                        jpg_name = split[3] + ".jpg"
                    jpg_path = os.path.join(split[1], jpg_name)
                    w, h = im.size
                    if w > FIXED_WIDTH and h > FIXED_HEIGHT:
                        # scale to max size
                        new_im = im.resize((FIXED_WIDTH, FIXED_HEIGHT), Image.Resampling.LANCZOS)
                        new_im.save(jpg_path)
                    elif w > FIXED_WIDTH or h > FIXED_HEIGHT:
                        # scale by half
                        new_im = im.resize((w // 2, h // 2), Image.Resampling.LANCZOS)
                        new_im.save(jpg_path)
                    else:
                        im.save(jpg_path)
            except PIL.UnidentifiedImageError:
                raise Exception("Cannot open image " + split[3])


def main():
    parser = argparse.ArgumentParser(
        description="Convert HEIF file format to JPEG file format"
    )
    parser.add_argument(
        "-p",
        "--path",
        required=True,
        type=str,
        help="Path to folder containing HEIC files",
    )
    parser.add_argument(
        "-f", "--file", required=False, type=str, help="File name of HEIC file"
    )
    parser.add_argument(
        "-r",
        "--rename",
        required=False,
        type=str,
        metavar="PREFIX",
        help="Rename output files to PREFIX.jpg (single file) or PREFIX_1.jpg, PREFIX_2.jpg, ... (multiple files)",
    )
    args = parser.parse_args()

    print(args.path)
    try:
        os.stat(args.path)
    except FileNotFoundError:
        print("File path is invalid. Please try again!")
        sys.exit(1)

    files = "*.heic"
    if type(args.file) is type(str) and len(args.file) != 0:
        files = args.file

    try:
        search_path = os.path.join(args.path, files)
        heic_list = glob.glob(search_path)
        print(heic_list)
        ps = PathSplit()
        heic_splits = ps.fun_path_splits(heic_list)

        jc = JpegConversion()
        jc.convert_to_jpg(heic_splits, rename_prefix=args.rename)
    except Exception as e:
        print(e)
        sys.exit(1)

    print("Program finished. Please check your folder now")


if __name__ == "__main__":
    main()
