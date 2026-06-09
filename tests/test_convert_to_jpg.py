from convert_to_jpg import PathSplit, output_jpg_name


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


def test_fun_path_splits(fs):
    fs.create_dir("/photos")
    fs.create_file("/photos/a.heic")
    fs.create_file("/photos/b.heic")
    splits = PathSplit().fun_path_splits(["/photos/b.heic", "/photos/a.heic"])
    assert len(splits) == 2
    assert splits[0][3] == "b"
    assert splits[1][3] == "a"
