{user.uiua_glyph_words}: insert(user.uiua_glyph_words)

array:
    insert("[]")
    key(left)
box array:
    insert("{}")
    key(left)
function:
    insert("()")
    key(left)
char: "@"
format: "$"
string:
    insert('""')
    key(left)
placeholder: "^"
assign: "←"

pipe: "|"
vertical bar: "|"

comment: "#"
strand: "_"

dump:"dump"

# use in terminal to start session
watch me wewha:
    insert("uiua watch --no-format")
    key(enter)