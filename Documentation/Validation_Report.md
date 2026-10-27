# Validation report

File: Rayman_Raving_Rabbids_Universal_PSP.ptf
SHA-256: ef65933663af0d155db6c0bd8c18bb05224dd783903e60952b7c34f943ee7bdc
Size: 523,052 bytes, below PTF Studio's 768 KiB preflight threshold.

- Built a PTF v1 file with GeofrontTeam LibPSPThemes, using a locally corrected indexed palette encoder, PSP tiled GIM pixels and zlib compression. The original implementation treated RGB palette bytes as separate 32-bit entries. The local correction assembles RGBA palette entries and reads PNG transparency.
- Re-extracted the PTF with LibPSPThemes: 73 PNG resources, including the BMP wallpaper, matched the corresponding compiler input pixel-for-pixel after conversion to RGBA.
- Independently decoded all 72 GIM resources using the `decodeGim` implementation extracted from PTF Studio 1.0. Decoded RGBA pixel SHA-256 values matched all source inputs. No GIM decoding errors were observed.
- Metadata read back: title Rayman Raving Rabbids, product ID RABBIDS_UNIVERSAL, PSP version 6.20, theme version 1.0. Header metadata has no author or description field in this workflow.
- Image canvases: preview 16 × 16 and 300 × 170; wallpaper 480 × 272; eight category assets 64 × 48; 29 first-level bodies 48 × 48 and corresponding focus images 64 × 64; two second-level bodies 32 × 32 and two focus images 48 × 48. Indexed images are limited to 256 palette entries, with focus artwork generated using white alpha-only glows.
- No invented first-level records 60–65 are present. The default/fallback slot 54 and its focus 55 are populated. According to PTF Studio's model implementation, PSP Go-only System Storage and Resume Game are displayed using these fallback assets; this assertion has not been verified on a console.
- No actual PSP, PSP Go, or emulator test was performed. Parser and pixel checks do not establish firmware acceptance, icon placement, usability, or physical model compatibility. PTF Studio's full GUI export and import workflow was not run.

PTF Studio: https://github.com/S1implyBlue/PTF-Studio
LibPSPThemes: https://github.com/GeofrontTeam/LibPSPThemes
