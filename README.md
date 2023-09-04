<img src="logo.png" align=right width=30%>

<div align="center">
<hr>

# `folder2osz`
### *osu!* beatmap compilation tool
###### [Download](https://github.com/silvncr/folder2osz/releases/latest)

<hr>
</div>

## Build

### Build to `exe`

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

<details><summary><h3>Compiling beatmaps (folder -> <code>osz</code>)</h3></summary>

```sh
Mode: [c]ompile or [e]xtract
> c
```

The program will create an `osz` file for every folder and subfolder that contains a `.osu` file. Files generated from subfolders will be placed in the same subfolder.

Each `osz` file will be named after the folder it was created from. If you're downloading beatmaps from an online source, the folder will usually be named after the map.

</details>

<details><summary><h3>Extracting beatmaps (<code>osz</code> -> folder)</h3></summary>

```sh
Mode: [c]ompile or [e]xtract
> e
```

The program will generate a folder for every `osz` file in the current folder and its subfolders. Folders generated from subfolders will be placed in the same subfolder.

Each folder will be named after the `osz` file it was created from. If you're downloading beatmaps from an online source, the `osz` file will usually be named after the map.

</details>

## Contributing

If you want to contribute to this project, feel free to fork it and submit a pull request. If you have any questions, you can contact me on Discord at `@silvncr`.

For testing purposes, error messages are numbered to make it easier to identify them. If you encounter an error, please include the error number in your bug report.
