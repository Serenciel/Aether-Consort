
image overlay = "images/visor_overlay.png"
image pc default = "images/pc_default.png"

define pc = Character('You', color="#7F00FF", window_left_padding=10, what_prefix="\"", what_suffix="\"")
define i = Character('You', color="#7F00FF", window_left_padding=60, what_prefix="{i}", what_suffix="{/i}") ##player's internal thoughts


############################################################################################

label start:
$ narrator = Character(None, window_left_padding=60) ##generic actions happening in te word, facts
$ name = "Izdra"
$ ArabellaMet = False
$ YaelMet = False
$ HakuMet = False


play music "audio/FtF26-b.mp3" loop

jump intro
    

############################################################################################

label dayChoice:
menu:
 "Now then, who is there to talk to today?"
 "NEW: A scientist from inSys." if not ArabellaMet:
  jump Arabella
 "Meet with Arabella." if ArabellaMet:
  jump Arabella
 "NEW: A vampire. Interesting!" if not YaelMet:
  jump Yael
 "Invite Yael over for a chat." if YaelMet:
  jump Yael
 "NEW: Looks like a youth wearing a splice's ears..." if not HakuMet:
  jump Haku
 "Spend the day with Haku." if HakuMet:
  jump Haku
 "Actually, I'll just ignore the supplicants for today and play with a sex drone.":
  jump sexbot

############################################################################################

label Yael:
"What a cute little bloodsucker."
jump gameover

############################################################################################

label Haku:
"Such a good boy."
jump gameover

############################################################################################


label sexbot:
"There's a wide selection of these toys."
jump gameover

############################################################################################

label gameover:
scene black with dissolve
"--- the 'game is not done' ending ---"
return