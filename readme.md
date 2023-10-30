# Uiua Speech Input

[![Uiua-Talon Youtube Intro](https://img.youtube.com/vi/-VOxSNyaLTg/0.jpg)](https://www.youtube.com/watch?v=-VOxSNyaLTg)

## Changes Since Youtube Video

- [./edit/edit.talon](./edit/edit.talon) adopted a minimal subset of the talon default scripts for cursor movements (eg `"go way left"`). Just delete the 'edit' folder if you don't want these. They are copy pasted from `https://github.com/talonhub/community` and I hope the authors don't mind this form of redistribution. Happy to remove them if anyone feels I shouldn't have them here.

- [./keys/nicks_keys.talon](./keys/nicks_keys.talon) minimal set of keys like `"backspace"` and `"escape"`. Just delete the 'keys' folder if you don't want these.

## Usage Instructions

1. Download `Talon` <https://talonvoice.com/>
2. Follow the install instructions on the
[unofficial wiki](https://talon.wiki/getting_started/)
   - DO follow the `Configure a Speech Recognition Engine` step
     (or it literally does nothing without notifying you about the problem)
   - DON'T follow the `Install a Talon user file set` step
     - I have tried it now, it works ok if you do want to use it, just make sure you delete the 'keys' and 'edit' folder in this repo.
3. Open the the `user` directory using bash or powershell;

```bash
cd ~/.talon/user
```

or

```powershell
cd %AppData%\Talon\user
```

4. Clone this repository

```powershell
git clone https://github.com/thehappycheese/uiua-talon
```

5. Restart Talon
6. Open a text editor
7. make sure your mic is on
8. Say 

`"one strand two strand three"`

`"enter"`

`"reduce add"`

`"save"`


## Important Notes

There are some unexpected issues with the Uiua names!

For example `"bind"` and `"binding"` are too similar, and `"sine"` and `"sign"` sound the same.

To see how I dealt with this (or configure your preference) open [./uiua_glyph_lookup.py](./uiua_glyph_lookup.py) and edit the dictionary :)
