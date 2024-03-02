# UnityNeovimOpener

`UnityNeovimOpener` is a Python script designed to integrate Unity with Neovim. It allows Unity to open scripts in Neovim, and directly jump to a specific line number. This is particularly useful for developers who use Neovim as their primary code editor and are working on Unity projects.

Warning! Only tested on Windows.

## Features

- Opens files from Unity in Neovim.
- Jumps to specific line numbers in Neovim, matching Unity's editor behavior.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed [Neovim](https://neovim.io/).
- You have Python installed on your system.

## Setting Up

To use `UnityNeovimOpener` with Unity, follow these steps:

1. Place the `UnityNeovimOpener.py` script in a suitable location on your system.

2. Open Unity and go to `Edit` > `Preferences`.

3. Navigate to the `External Tools` section.

4. Set the External Script Editor to your Python interpreter path (e.g., `C:\Path\To\Python\python.exe`).

5. In the External Script Editor Args field, enter the following arguments:
   
```Path\To\UnityNeovimOpener.py "$(File)" "$(Line)"```

Replace `Path\To\` with the actual path where you saved the script.

... or, if installed Python from MS Store, just put those values:

External Script Editor: UnityNeovimOpener.py (select the file)
External Script Editor Args: $(File) $(Line)

The first time you open a script the system will ask you what to use to open .py file, select Python app.

## Usage

Once configured, opening a script from Unity will automatically launch Neovim and navigate to the specified line number (if any).

## Contributing to UnityNeovimOpener

To contribute to `UnityNeovimOpener`, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me, you can reach me at `inbox@potatogam.es`.
