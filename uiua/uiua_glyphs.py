from talon import Module, Context, actions
from .uiua_glyph_lookup import glyph_dict
mod = Module()
ctx = Context()

import logging
logger = logging.getLogger()
logger.log(logging.DEBUG, "UIUA GLYPHS PYTHON RUNNING")


mod.list("uiua_glyph_words", desc="List of UIUA glyphs")

ctx.lists["user.uiua_glyph_words"] = glyph_dict