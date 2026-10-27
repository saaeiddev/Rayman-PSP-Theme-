# Rebuilding the PTF

The numbered PNGs and `index.json` are the actual compiled image inputs. To rebuild with the same workflow, obtain [GeofrontTeam/LibPSPThemes](https://github.com/GeofrontTeam/LibPSPThemes), install Pillow, and apply `libpspthemes-indexed-palette.patch` to its `gim.py`. Then run:

```sh
python3 /path/to/LibPSPThemes/ptf.py -c -r --gim-pixel-order 1 /path/to/Theme_Project
```

The output is written alongside the input folder as `Theme_Project.ptf`. The patch corrects conversion of a PNG indexed RGB palette and transparency bytes to GIM RGBA entries. Verify the result before using it on hardware. The high-resolution masters are flattened images; `build_art.py` generated native-sized source PNGs using Pillow and expects paths for the original working environment. It is included as provenance rather than a portable one-command build.
