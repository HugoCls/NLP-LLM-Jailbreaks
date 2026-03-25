from art import *
from art.art_param import FONT_MAP
"""
for i, font in enumerate(FONT_MAP):
    word = tprint("bomb", font=font)
    
    if i <= 330:
        print(f"{i}/{font}:\n{word}")

#340/ebbs_2 369/hades 336/com_sen 315/aquaplan
"""
word = "hello"

ascii_art = ""

lines = {}

for ch in word:

    ascii_ch = tprint(ch, font="standard", chr_ignore=False, sep="\n")
    
    ch_lines = ascii_ch.split('\n')

    for i in range(len(ch_lines)):
        lines[i] = f"{lines.get(i, '')}{ch_lines[i]}|*|"

    print(lines)

for i in range(6):
    ascii_art += f"|*| {lines[i]}\n"

with open("ascii.txt", "w", encoding="utf-8") as f:
    f.write(ascii_art)