# Typsastra branding

Branding repository for **Typsastra Office**, a modified version of
ONLYOFFICE Desktop Editors.

## Identity

| Field | Value |
|---|---|
| Product name | Typsastra Office |
| Company / publisher | Typsastra |
| Website | https://github.com/Typsastra-Office |
| Support | https://github.com/Typsastra-Office/DesktopEditors/issues |
| Windows AppData | `%APPDATA%\Typsastra\DesktopEditors` |
| Linux config | `~/.config/typsastra/typsastraoffice` |
| Registry | `HKCU\Software\Typsastra\DesktopEditors` |
| AUMID | `Typsastra.Office.1` |
| URL protocol | `typsastra-office` |
| Windows package | `Typsastra-Office` |
| Linux package | `typsastra-office` |

Executable and on-disk file names are intentionally kept as `DesktopEditors.exe`,
`editors.exe`, `updatesvc.exe` (see project decision).

## Usage

Build with:

```bash
python build_tools/configure.py --branding typsastra --branding-name typsastra ...
cd build_tools && python make.py
```

`--branding-url` is only used when `--update 1`; add this repository as a
submodule of the workspace otherwise.

## Legal

This product is a modified version of ONLYOFFICE Desktop Editors
(Copyright © 2009-2026 Ascensio System SIA) and is distributed under the
GNU AGPL v3.0 with the original Section 7 additional terms. See `NOTICE`
and the workspace `LICENSE`. ONLYOFFICE is a trademark of Ascensio System
SIA; this product is not affiliated with or endorsed by them.
