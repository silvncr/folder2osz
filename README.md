<img src="logo.png" align=right width=30%>

<div align="center">
<hr>

# `folder2osz`
### *osu!* beatmap compilation tool
###### [Download](https://github.com/silvncr/folder2osz/releases/latest)

<hr>
</div>

## About

`folder2osz` **is**:

- A tool for compiling beatmaps for the rhythm game *osu!*, allowing the user to convert a folder containing the necessary files for a beatmap into a `.osz` file that can be imported into the game, or vice versa. This makes it easier to download beatmaps from online sources, create backups of beatmaps, or share beatmaps with other players.
- Able to be built into an executable file or run as a Python script.

`folder2osz` **is not**:

- Necessarily perfect. This program is still in development, and there may be bugs. If you encounter any bugs, please report them in the [Issues](https://github.com/silvncr/folder2osz/issues) tab. If you want to contribute, feel free to submit a pull request.
- Affiliated with *osu!* or its creator, Dean "peppy" Herbert. For official information about *osu!*, visit [osu.ppy.sh](https://osu.ppy.sh).

## Features

- Compile many beatmaps from many folders at one time
- Extract many beatmaps from many `.osz` files at one time

## Build

### Build to `.exe`

On Windows 10/11, run `build.bat`, then find `folder2osz.exe` in the `dist` folder.

```sh
$ git clone https://github.com/silvncr/folder2osz.git
```

### Python script

Alternatively, have `app/main.py` take the place of `folder2osz.exe`.

```sh
$ git clone https://github.com/silvncr/folder2osz.git
$ cd folder2osz
$ python -m pip install -r requirements.txt
```

## Usage

Copy-and-paste `folder2osz.exe` into a folder and run it.

### Compiling beatmaps (folder to `.osz`)

```sh
Mode: [c]ompile or [e]xtract
> c
```

The program will create a `.osz` file for every folder and subfolder that contains a `.osu` file. Files generated from subfolders will be placed in the same subfolder.

Each `.osz` file will be named after the folder it was created from. If you're downloading beatmaps from an online source, the folder will usually be named after the map.

### Extracting beatmaps (`.osz` to folder)

```sh
Mode: [c]ompile or [e]xtract
> e
```

The program will generate a folder for every `.osz` file in the current folder and its subfolders. Folders generated from subfolders will be placed in the same subfolder.

Each folder will be named after the `.osz` file it was created from. If you're downloading beatmaps from an online source, the `.osz` file will usually be named after the map.
