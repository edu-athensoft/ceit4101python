"""
Tkinter

Label widget

Font
families
"""

from tkinter import *
from tkinter import font

root = Tk()
root.title('Font Families')
fonts = list(font.families())
fonts.sort()

for f in fonts:
    print(f)


"""
@Arial Unicode MS
@Fixedsys
@MS Gothic
@MS PGothic
@MS UI Gothic
@Malgun Gothic
@Malgun Gothic Semilight
@Microsoft JhengHei
@Microsoft JhengHei Light
@Microsoft JhengHei UI
@Microsoft JhengHei UI Light
@Microsoft YaHei UI
@Microsoft YaHei UI Light
@MingLiU-ExtB
@MingLiU_HKSCS-ExtB
@Noto Sans CJK Black
@Noto Sans CJK Bold
@Noto Sans CJK DemiLight
@Noto Sans CJK Light
@Noto Sans CJK Medium
@Noto Sans CJK Regular
@Noto Sans CJK Thin
@PMingLiU-ExtB
@SimSun-ExtB
@System
@Terminal
@Yu Gothic
@Yu Gothic Light
@Yu Gothic Medium
@Yu Gothic UI
@Yu Gothic UI Light
@Yu Gothic UI Semibold
@Yu Gothic UI Semilight
@仿宋
@宋体
@带心的可爱字体
@微软雅黑
@微软雅黑 Light
@新宋体
@楷体
@猫咪字体
@等线
@等线 Light
@黑体
Agency FB
Algerian
Arabic Transparent
Arial
Arial Baltic
Arial Black
Arial CE
Arial CYR
Arial Greek
Arial Narrow
Arial Rounded MT Bold
Arial TUR
Arial Unicode MS
Bahnschrift
Bahnschrift Condensed
Bahnschrift Light
Bahnschrift Light Condensed
Bahnschrift Light SemiCondensed
Bahnschrift SemiBold
Bahnschrift SemiBold Condensed
Bahnschrift SemiBold SemiConden
Bahnschrift SemiCondensed
Bahnschrift SemiLight
Bahnschrift SemiLight Condensed
Bahnschrift SemiLight SemiConde
Baskerville Old Face
Bauhaus 93
Bell MT
Berlin Sans FB
Berlin Sans FB Demi
Bernard MT Condensed
Blackadder ITC
Bodoni MT
Bodoni MT Black
Bodoni MT Condensed
Bodoni MT Poster Compressed
Book Antiqua
Bookman Old Style
Bookshelf Symbol 7
Bradley Hand ITC
Britannic Bold
Broadway
Brush Script MT
Calibri
Calibri Light
Californian FB
Calisto MT
Cambria
Cambria Math
Candara
Candara Light
Castellar
Centaur
Century
Century Gothic
Century Schoolbook
Chiller
Colonna MT
Comic Sans MS
Consolas
Constantia
Cooper Black
Copperplate Gothic Bold
Copperplate Gothic Light
Corbel
Corbel Light
Courier
Courier New
Courier New Baltic
Courier New CE
Courier New CYR
Courier New Greek
Courier New TUR
Curlz MT
DejaVu Sans Mono
Dosis
Ebrima
Edwardian Script ITC
Elephant
Engravers MT
Eras Bold ITC
Eras Demi ITC
Eras Light ITC
Eras Medium ITC
Felix Titling
Fixedsys
Footlight MT Light
Forte
Franklin Gothic Book
Franklin Gothic Demi
Franklin Gothic Demi Cond
Franklin Gothic Heavy
Franklin Gothic Medium
Franklin Gothic Medium Cond
Freestyle Script
French Script MT
Gabriola
Gadugi
Garamond
Georgia
Gigi
Gill Sans MT
Gill Sans MT Condensed
Gill Sans MT Ext Condensed Bold
Gill Sans Ultra Bold
Gill Sans Ultra Bold Condensed
Gloucester MT Extra Condensed
Goudy Old Style
Goudy Stout
GreenPoint
Haettenschweiler
Harlow Solid Italic
Harrington
High Tower Text
HoloLens MDL2 Assets
Impact
Imprint MT Shadow
Informal Roman
Ink Free
Javanese Text
Jokerman
Juice ITC
Kristen ITC
Kunstler Script
Lato
Lato Black
Leelawadee UI
Leelawadee UI Semilight
Lucida Bright
Lucida Calligraphy
Lucida Console
Lucida Fax
Lucida Handwriting
Lucida Sans
Lucida Sans Typewriter
Lucida Sans Unicode
MS Gothic
MS Outlook
MS PGothic
MS Reference Sans Serif
MS Reference Specialty
MS Sans Serif
MS Serif
MS UI Gothic
MT Extra
MV Boli
Magneto
Maiandra GD
Malgun Gothic
Malgun Gothic Semilight
Marlett
Matura MT Script Capitals
Microsoft Himalaya
Microsoft JhengHei
Microsoft JhengHei Light
Microsoft JhengHei UI
Microsoft JhengHei UI Light
Microsoft New Tai Lue
Microsoft PhagsPa
Microsoft Sans Serif
Microsoft Tai Le
Microsoft YaHei UI
Microsoft YaHei UI Light
Microsoft Yi Baiti
MingLiU-ExtB
MingLiU_HKSCS-ExtB
Mistral
Modern
Modern No. 20
Mongolian Baiti
Monotype Corsiva
Montserrat
Myanmar Text
Niagara Engraved
Niagara Solid
Nirmala UI
Nirmala UI Semilight
Noto Sans CJK Black
Noto Sans CJK Bold
Noto Sans CJK DemiLight
Noto Sans CJK Light
Noto Sans CJK Medium
Noto Sans CJK Regular
Noto Sans CJK Thin
OCR A Extended
Old English Text MT
Onyx
Open Sans
Open Sans ExtraBold
Open Sans Light
Open Sans SemiBold
Oswald
PMingLiU-ExtB
Palace Script MT
Palatino Linotype
Papyrus
Parchment
Perpetua
Perpetua Titling MT
Playbill
Poor Richard
Pristina
Rage Italic
Ravie
Rockwell
Rockwell Condensed
Rockwell Extra Bold
Roman
Script
Script MT Bold
Segoe MDL2 Assets
Segoe Print
Segoe Script
Segoe UI
Segoe UI Black
Segoe UI Emoji
Segoe UI Historic
Segoe UI Light
Segoe UI Semibold
Segoe UI Semilight
Segoe UI Symbol
Showcard Gothic
SimSun-ExtB
Sitka Banner
Sitka Display
Sitka Heading
Sitka Small
Sitka Subheading
Sitka Text
Small Fonts
Snap ITC
Source Sans Pro
Source Sans Pro Black
Source Sans Pro Semibold
Stencil
Sylfaen
Symbol
System
Tahoma
Tempus Sans ITC
Terminal
Times New Roman
Times New Roman Baltic
Times New Roman CE
Times New Roman CYR
Times New Roman Greek
Times New Roman TUR
Trebuchet MS
Tw Cen MT
Tw Cen MT Condensed
Tw Cen MT Condensed Extra Bold
Verdana
Viner Hand ITC
Vivaldi
Vladimir Script
Webdings
Wide Latin
Wingdings
Wingdings 2
Wingdings 3
Yu Gothic
Yu Gothic Light
Yu Gothic Medium
Yu Gothic UI
Yu Gothic UI Light
Yu Gothic UI Semibold
Yu Gothic UI Semilight
仿宋
宋体
带心的可爱字体
微软雅黑
微软雅黑 Light
新宋体
楷体
猫咪字体
等线
等线 Light
黑体
"""

