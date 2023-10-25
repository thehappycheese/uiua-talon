# Uiua Speech Input

## Usage Instructions

1. Download `Talon` <https://talonvoice.com/>
2. Follow the install instructions on the
[unofficial wiki](https://talon.wiki/getting_started/)
   - DO follow the `Configure a Speech Recognition Engine` step
     (or it literally does nothing without notifying you about the problem)
   - DON'T follow the `Install a Talon user file set` step
     - I haven't checked for conflicting command words, and
     - unless you intend to spend hours learning the default command set, it is not needed.
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