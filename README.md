# ConvertHeicToJpg

A command-line tool that converts HEIC/HEIF images to JPEG format.

## Install

### Windows

Download `convert-to-jpg.exe` from [GitHub Releases](https://github.com/user-olof/ConvertHeicToJpg/releases). No Python installation required.

```powershell
.\convert-to-jpg.exe -p C:\Users\You\Pictures
```

#### Verify download

Download both `convert-to-jpg.exe` and `SHA256SUMS` from the same release, then verify integrity:

```powershell
$expected = (Get-Content SHA256SUMS).Split(" ")[0]
$actual = (Get-FileHash convert-to-jpg.exe -Algorithm SHA256).Hash.ToLower()
$expected -eq $actual   # should be True
```

Checksums confirm the file was not corrupted or altered after publish. They do not replace code signing — Windows may still show a SmartScreen warning for the unsigned executable.

### Linux

Install with [pipx](https://pipx.pypa.io/) (recommended):

```bash
pipx install git+https://github.com/user-olof/ConvertHeicToJpg.git
convert-to-jpg -p ~/Pictures
```

Or with pip:

```bash
pip install git+https://github.com/user-olof/ConvertHeicToJpg.git
convert-to-jpg -p ~/Pictures
```

## Usage

```bash
convert-to-jpg -p /path/to/folder              # convert all .heic files in a folder
convert-to-jpg -p /path/to/folder -f photo.heic   # convert a single file
convert-to-jpg -p /path/to/folder -r vacation      # vacation_1.jpg, vacation_2.jpg, ...
convert-to-jpg -p /path/to/folder -f photo.heic -r vacation   # vacation.jpg
convert-to-jpg -h                              # show help
```

Converted JPG files are saved in the same folder as the source HEIC files.

## Build from source (developers)

Requires Python 3.7+.

```bash
git clone https://github.com/user-olof/ConvertHeicToJpg.git
cd ConvertHeicToJpg

python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements-dev.txt
pyinstaller convert_to_jpg.spec
```

The binary is written to `dist/convert-to-jpg` (or `dist/convert-to-jpg.exe` on Windows).

Test it:

```bash
./dist/convert-to-jpg -h
```

## Release (maintainers)

Push a version tag to trigger the GitHub Actions build and create a release with the Windows binary:

```bash
git tag v1.0.1
git push origin v1.0.1
```

You can also trigger a build manually from the Actions tab using **workflow_dispatch**.
