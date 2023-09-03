<img src="logo.png" align=right width=30%>

<div align="center">
<hr>

# `folder2osz`
### *osu!* Beatmap Compilation Tool
###### [Download](https://github.com/silvncr/folder2osz/releases/latest)

<hr>
</div>

## Build

On Windows 10/11, run `py2exe.bat`, then find `folder2osz.exe` in the `dist` folder.

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
