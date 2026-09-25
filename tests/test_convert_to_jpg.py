from unittest.mock import MagicMock, patch

from convert_to_jpg import JPEG_QUALITY, JpegConversion, PathSplit, output_jpg_name


def test_output_jpg_name_single_file():
    assert output_jpg_name("pic", 0, 1) == "pic.jpg"


def test_output_jpg_name_multiple_files():
    assert output_jpg_name("pic", 0, 3) == "pic_1.jpg"
    assert output_jpg_name("pic", 1, 3) == "pic_2.jpg"
    assert output_jpg_name("pic", 2, 3) == "pic_3.jpg"


def test_path_split_parts(fs):
    fs.create_dir("/photos")
    fs.create_file("/photos/photo.heic")
    parts = PathSplit().split_all_parts("/photos/photo.heic")
    assert parts[0] == "/photos/photo.heic"
    assert parts[1] == "/photos"
    assert parts[3] == "photo"


def test_convert_keeps_size_and_lowers_quality():
    im = MagicMock()
    im.__enter__.return_value = im
    with patch("convert_to_jpg.register_heif_opener"), patch(
        "convert_to_jpg.Image.open", return_value=im
    ):
        JpegConversion().convert_to_jpg(
            [("/photos/photo.heic", "/photos", "photo.heic", "photo", ".heic")]
        )
    im.resize.assert_not_called()
    im.save.assert_called_once_with(
        "/photos/photo.jpg", quality=JPEG_QUALITY, optimize=True
    )


def test_fun_path_splits(fs):
    fs.create_dir("/photos")
    fs.create_file("/photos/a.heic")
    fs.create_file("/photos/b.heic")
    splits = PathSplit().fun_path_splits(["/photos/b.heic", "/photos/a.heic"])
    assert len(splits) == 2
    assert splits[0][3] == "b"
    assert splits[1][3] == "a"
