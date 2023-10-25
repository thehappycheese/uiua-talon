from talon import Module, Context, actions
from .uiua_glyph_lookup import glyph_dict
mod = Module()
ctx = Context()

import logging
logger = logging.getLogger()
logger.log(logging.DEBUG, "UIUA GLYPHS PYTHON RUNNING")


mod.list("uiua_glyph_words", desc="List of UIUA glyphs")

ctx.lists["user.uiua_glyph_words"] = glyph_dict


# @mod.capture(rule="{self.uiua_glyph_words}")
# def uiua_glyph_words(m) -> str:
#     return uiua_glyphs[]

# @mod.action_class
# class UiuaActions:
#     def insert_glyph(glyph_name: str):
#         """Insert the glyph corresponding to the given name"""
#         print(f"UIUA_GLYPH {glyph_name}")
#         actions.key("up")



# from talon import Module

# mod = Module()
# #mod.tag("uiua", desc="Tag for UIUA glyphs commands")
# mod.list("uiua_glyphs", desc="List of UIUA glyphs")

# glyph_dict = {
#     'duplicate': '.',
#     'over': ',',
#     'flip': '∶',
#     'pop': ';',
#     'identity': '∘',
#     'not': '¬',
#     'sign': '±',
#     'negate': '¯',
#     'absolute value': '⌵',
#     'sqrt': '√',
#     'sine': '○',
#     'floor': '⌊',
#     'ceiling': '⌈',
#     'round': '⁅',
#     'equals': '=',
#     'not equals': '≠',
#     'less than': '<',
#     'less or equal': '≤',
#     'greater than': '>',
#     'greater or equal': '≥',
#     'add': '+',
#     'subtract': '-',
#     'multiply': '×',
#     'divide': '÷',
#     'modulus': '◿',
#     'power': 'ⁿ',
#     'logarithm': 'ₙ',
#     'minimum': '↧',
#     'maximum': '↥',
#     'atangent': '∠',
#     'length': '⧻',
#     'shape': '△',
#     'range': '⇡',
#     'first': '⊢',
#     'reverse': '⇌',
#     'deshape': '♭',
#     'bits': '⋯',
#     'transpose': '⍉',
#     'rise': '⍏',
#     'fall': '⍖',
#     'where': '⊚',
#     'classify': '⊛',
#     'deduplicate': '⊝',
#     'box': '□',
#     'unbox': '⊔',
#     'match': '≍',
#     'couple': '⊟',
#     'join': '⊂',
#     'select': '⊏',
#     'pick': '⊡',
#     'reshape': '↯',
#     'take': '↙',
#     'drop': '↘',
#     'rotate': '↻',
#     'windows': '◫',
#     'keep': '▽',
#     'find': '⌕',
#     'member': '∊',
#     'indexof': '⊗',
#     'reduce': '/',
#     'scan': '\\',
#     'each': '∵',
#     'rows': '≡',
#     'distribute': '∺',
#     'tribute': '≐',
#     'table': '⊞',
#     'cross': '⊠',
#     'repeat': '⍥',
#     'group': '⊕',
#     'partition': '⊜',
#     'pack': '⊐',
#     'invert': '⍘',
#     'gap': '⋅',
#     'dip': '⊙',
#     'both': '∩',
#     'fork': '⊃',
#     'bracket': '⊓',
#     'under': '⍜',
#     'fill': '⬚',
#     'level': '≑',
#     'fold': '∧',
#     'combinate': '◳',
#     'rock': '⋄',
#     'surface': '~',
#     'deep': '≊',
#     'abyss': '≃',
#     'seabed': '∸',
#     'bind': "'", 'if': '?',
#     'try': '⍣',
#     'assert': '⍤',
#     'break': '⎋',
#     'random': '⚂',
#     'eta': 'η',
#     'pi': 'π',
#     'tau': 'τ',
#     'infinity': '∞',
#     'trace': '⸮'
# }

# @mod.capture(rule="{self.uiua_glyphs}")
# def uiua_glyphs(m) -> str:
#     return m.uiua_glyphs

# @mod.action_class
# class Actions:
#     def insert_glyph(glyph_name: str):
#         """Insert the glyph corresponding to the given name"""
#         glyph = glyph_dict.get(glyph_name)
#         if glyph:
#             # Code to insert the glyph
#             print(f"Inserting glyph: {glyph}")
#         else:
#             print(f"Glyph not found for: {glyph_name}")