image bg crap_bedroom_dark = "images/bg_bedroom_dark.png"
image bg crap_bedroom_light = "images/bg_bedroom_light.png"
image bg slide_msecdraft = "images/slide_msecdraft.png"
image bg slide_sacrifice = "images/slide_sacrifice.png"
image bg slide_prebreach = "images/slide_prebreach.png"
image bg slide_breach = "images/slide_breach.png"
image bg slide_postbreach = "images/slide_postbreach.png"

label intro:
    
    
"You open your eyes."
"It's still mostly dark, but you think you can sort of make out the ceiling above you in shades of dark grey."

scene bg crap_bedroom_dark
"It must be getting close to noon already if any daylight at all is brightening up the place - the windows are facing onto another decrepit building across a narrow alley."
i "Helblast it! I'll have to stay up late tonight to fit a full day's work in at this point."
"You'll make it work somehow. Maybe you'll be able to pull in a big tip or a new client today."
i "..."
i "As if."
"You're behind for the day already, and you've absolutely drained your meager 'savings' - there's simply no way to make it work here."
"Every time you think you'll be able to scrape by, the protection rackets in the area raise their demands."
"No matter what, you definitely need to get up now. If you don't make some creds before you have to pay for anything else - like food, or water - you won't be able to pay to connect to work."
"You'll be absolutely ruined - the only way to get back enough to do your job would be something high risk, like stealing or doing day labor for a corpse."
i "I didn't survive on my own for twenty five years taking risks."
i "Not going to start now."

scene bg slide_msecdraft
i "Maybe it isn't a full half of corpses that are really M-Sec operatives making an easy collar, but the odds aren't good no matter what."
"Those pampered citizens of the corporations didn't come looking for workers for anything good anyways."

scene bg slide_sacrifice
i "Even if I didn't end up in an M-Sec cell, it'd probably end up being a cultist corpse looking for live umari to sacrifice to their deity."
i "No way am I ending up strapped to a bloody altar."

scene bg crap_bedroom_dark
"You lean forward, letting your elbows dig into the ratty old mattress you've been sleeping on."
i "I can't believe I'm still sleeping on this scrag pile."
"You only alot yourself a few quarter hours split up throughout each day for scrounging, and while you've found the occasional piece of pre-Breach clutter that's still in working order, all the other mattresses in this building seem to have been destroyed by various wildlife."

scene bg slide_prebreach
"..."
"You've only seen the world as it was then via stills and holos, or listening to interviews from older umari."

scene bg slide_breach
"You were born a few years after the Breach, in the ruins of the city it destroyed."

scene bg slide_postbreach
"Ironically, Breach City is likely the only place umari still survive on Terra."

scene bg crap_bedroom_dark
"You pause for a moment, banishing thoughts of a dark time in your, and pretty much everyone's, life."
"Anyway, even if you had found a decent pre-Breach mattress, you'd have sold it for whatever meager amount of creds you could get from another squatter."
i "It's just nice to imagine for a moment I could have something nice."
i "Even just a mattress that somehow survived unscathed since before I was born."
"You look around the dark room, making your eyes adjust to the dim sunlight seeping in."

scene bg crap_bedroom_light
"You stretch your arms behind yourself and let out a short yawn."
i "So I don't have a fancy mattress. Whatever. I'm not some pampered corpse."
i "I've survived this long, and I'll survive moving to another decrepit hole that's not even as nice as I've been able to make this one."
"You've been in this apartment for over three tendays now... almost a month in one place is past time for you to move along."
"Moving too often risks getting caught up in M-Sec sweeps, but if you camp out in one place too long you're just daring a scout to report you as an easy collar."
i "Hopefully M-Sec doesn't even have scouts in this area of the abandons."
i "Wishful thinking really. Things are never that easy."
"No doubt you're a little dot in some heartless scout's temporal map of the area, and starting to linger long enough to be marked easy prey."


"You glance around the room that's frankly a shithole, despite all your tidying."
"All that thinking about M-Sec... yeah, nevermind trying to hit your daily credit goal, you're definite going to move today."
"Even if you hadn't been here too long, the watchers on the local boards have been reporting a lot of patrol activity in the area anyways."
i "No point paying a share of their wages if I'm not going to act on the information."
"You wave your hand to pull your VISOR out of sleep mode, bright lights illuminating the air in front of your eyes and forming a screen of information."

show overlay

"Flopping back onto the ragged mattress, you authorize payment for a wider, more detailed set of the M-Sec alerts from the watchers you trust, and start feeding that data into a topographical map of the abandons." 
"Your fingers waggle in the air above you as you navigate your VISOR's menus, putting it into surround mode. The light of the screen brightens, blocking the ceiling from your eyesight."

hide bg crap_bedroom_light

"You finish setting up the familiar process in no time - but it's actually going to take a little more than an hour for that operation to fully run through."
i "Might as well work while that finishes. Got to keep my basic funds topped off if this move is going to work out."
"You log into your account at Drone Domination, paying for the connection for an hour."
"You're not going to spend the whole day working, but you need to make back the creds you just spent on the alerts."
"Unfortunately none of your regulars are online... you glance at your avatar on the side, and grin widely at the robotic curves of it's design."
i "Even on a breach-blighted day like this, connecting to a drone feels great."
"Nothing feels as good as inhabiting that body by remote, even if the pay is shit and new customers can be worse."
"You go to call up the list of open requests - you'll just find someone looking to be lightly bound, and go through some automated scripts."
"You're not going to attract a new regular that way, but the custom scripts you write are more than good enough to keep a submissive interested the first time they're with you."
"You allow yourself a conceited grin."
i "Honestly, my script work is well above what most others here can do working live."
i "Once I've got the drone scripts running, I can keep an eye on the map as it compiles..."
i "..."
i "Huh?"


## display flashing alert icon
"You're still a little groggy, so it took you a couple minutes to notice the blinking red icon of a paid priority message awaiting you."
i "That's... odd."
i "No one in the abandons has creds to waste on priority."
"You don't really have contacts that would spend those creds on you, even if they could afford to."
"You open the message, uncertain what you'll find inside."
##dismiss flashing icon


centered "Dear [name], we're happy to announce you've been selected by the deity Minerva to join the ranks of the Consortium! This offer includes a guaranteed employment contract for a full two years, with an option to be renewed as tenured employment at the end of that period."
"You're being headhunted for a corporate gig? Hel! This is the sort of thing that drunk corpless tell each other will happen to make the cold nights pass by."
i "Not something that would happen for anyone - let alone me!"
i "And it's the Consortium of all corps... why would the cult of Minerva be interested me? I don't know the first thing about gods, or magic."
i "Sure, they run the Pleasure Dome, but I just operate pleasure {b}drones{/b}... they deal in the real thing!"
"Speculation isn't really helping you figure this out - you try to relax and read the rest of the message."
centered "Over the course of the two year contract you'll be working as a probitionary Consort: if, in the course of your work, your soul finds it's way to Minerva you'll become a Consort in fact as well as title. The actual day to day work required is slightly free-form - you'll simply take a look at the list of petitioners that are approaching the Consortium for Minerva's aid, pick out the cases that seem interesting to you, and work with those petitioners to meet their needs. {vspace=30}Ideally you'll also endear the petitioners to Minerva and the Consortium in the process - but the only real job requirement is to help people with their issues. Your creative and often touching work as a remote drone operator more than qualifies you for this task - we're confident in your ability to read the needs of, and work with, the petitioners you take on. And of course, if you do get stuck on how to help someone, you'll have a wide array of colleagues you can go to for assistance."
i "That's... well, I'm not exactly sure what to make of that offer."
"Two years without having to look over your shoulder for Mirage recruitment gangs... even if you weren't salaried at all, that's a pretty tempting gig."
"But despite what the mail says, you're not confident you'll be fit for the job - and corporations don't exactly tend to have healthy exit clauses."
"Working as a Consort... you've never even been to the Pleasure Dome, despite the fact you've spent most of your life in the slightly safer part of the abandons nearby the Consortium headquarters."
"The place just sounds too intimidating - home of a deity, center of a corporation, and filled with the most skilled sex workers in the city."
"People are backlogged for months to get into the Pleasure Dome and sell their soul in exchange for a little divine bliss."
"What exactly is a corpless drone operator like yourself going to do there?"
i "I might have a knack for getting repeat customers."
i "That hardly makes me worthy of {b}divine{/b} interest!"
centered "While the Consortium is quite aware that just about any stipend is going to be a large sum for someone in your position, especially when coupled with the perks of employment, a special signing bonus has been arranged for you specifically with a calculated 99.74\% chance of getting an affirmative reply."
"You stop reading."
i "That's just cocky! Helblighted corpses really do think there's nothing that can't be bought..."
"You freeze as your eyes take in the next sentence, your breath locking in your chest."
centered "You will be provided with a cerebral extraction and a fully equipped refurbished to working order.{vspace=30}This particular shell is built around the core of an old Y-class inSys pleasure drone - you should recognize the designation as the class of drones you choose for your work."
i "Blast."
i "The drone I work through every day, the highlights of my shitty little job - that can be my actual body?"
i "Okay, so maybe they know how to go about buying people."
i "These Consortium corpses have me dead to rights."
i "My life's dream, offered on a mithril platter."

hide overlay

"You reach up and turn off your VISOR."
"Your flesh and blood body... it's never felt quite right to you."
menu:
    "For a corpse, it would be no big deal to afford hormones or the sex reassignment surgery you want.":
        "For a corpse, it would be no big deal to afford hormones or the sex reassignment surgery you want."
    "For a corpse, it would be manageable to buy the synthetic ideal body you've always craved.":
        "For a corpse, it would be manageable to buy the synthetic ideal body you've always craved."
    "For a corpse, it would be covered in any contract to medically bypass your disability by providing a shell.":
        "For a corpse, it would be covered in any contract to medically bypass your disability by providing a shell."
"But for a corpless scavenger like yourself... all the creds your scrounge up go right to staying alive."
"You tell yourself you'll save up for a shell someday... but you're just lying to yourself to help you get by."
"Multiple times a year some disaster wipes out your savings as you struggle to get by."
"What you're being offered here is walking in one day and waking up the next day in the body you've been dreaming about for years and years."
"And in the Pleasure Dome... there's literally nowhere safer to have an extraction done."
"Executive corpses dish out millions of creds for that kind of treatment, divine healers on hand if the surgery falters for even a moment."
i "There's no point in reading any further."
i "I'm taking this deal even if I have to sell my soul to this Minerva to get it."
menu:
    "Click the 'Accept' button at the bottom of the message.":
        ## play knocking
        "A reply comes immediately after you accept - but it comes in the form of a knocking at your door, not another message."
"You slowly stand."
i "Corporate efficiency at work, I guess."

##change room to crappy doorway

"Still grinning from ear to ear from the news, you walk over to the door and pull aside the coffee table you've been using to keep the door upright."
"Leveraging the door to the ground, you freeze in surprise at the figure in your doorway, letting the door fall."

show jamie default at right with fade

jamie "Relax."
i "Relax. Relax!"
i "That is very clearly an M-Sec scout standing in your doorway."
"You can't relax, but you do manage to slowly stand upright."
"Running at this point would do you no good anyways."
jamie "I'm here on Consortium business. No one's going to Mirage processing today, stay calm."
"She pauses for a moment, meeting your eyes."
i "O-okay. That makes sense. I'm not corpless anymore - I'm a corpse, a corporate asset."
i "Corporations don't let assets go unprotected."
menu:
    "So... you're here as a guard?":
        "You blink a few times, but eventually find your words."
        pc "So... the Consortium hired you? You're going to bring me to the Pleasure Dome?"
    "Good, you're here. Alright, take me to the Dome.":
        "You force a smile on your face as you speak with confidence."
        pc "Oh good, you're here. Alright then, let's head out. The sooner I'm at the Pleasure Dome the better."
"The M-Sec corpse nods."
jamie "Jamie Eldriss, here to deliver you unharmed [name]."
jamie "I know you have reason to be wary of any Mirage Security personnel."
jamie "Trust that you're worth far more to me safely in the embrace of the Consortium than awaiting a verdict in M-Sec holding cells."
"That's what you thought."
"Scared you half to death for a moment, but this makes sense."
i "Time to go to your new life!"
i "One where I don't have to fear everyone with an M-Sec look to them."
i "No more constantly looking over my shoulder..."
"You look over your shoulder at your dump of a place."
menu:
    "Eagerly leave this dump in the past.":
        i "Finally I can sleep on a mattress that isn't nearly thirty years old."
        i "Maybe get the smell of mildew off of myself."
    "Decide that while you may have some useful or treasured items... you'll be better off replacing just everything with your new salary.":
        "Your life up to now has been hard - but not empty."
        "Even so... you decide you'll be better off with a clean break and a fresh start."
pc "Alright then Jamie, let's get going."
pc "Nothing here is worth bringing along."

jump gameover











##fade in bedroom

"You stretch your synthflesh back muscles out as you yawn, marvelling at the comfort of the blankets you're wrapped in."
"Your eyes open slowly to unfamiliar room, though you're vaguely aware of having moved in a few days ago."
"You sit up slowly, realizing you're only {i}vaguely{/i} aware of, well, basically everything."
"You suddenly jerk to a stop as you move to get out of bed. It feels like you've been tethered to the wall with something..."
"You reach back behind yourself, hands wrapping around a length coming out of your back between your shoulderblades. Your fingers trace backwards, and the cord indeed has you attached to the wall."
"You slowly reach back to your neck to detach the charging cord, as you begin to recall what exactly it is."
i "Unreal."
"Sunlight sprays in through a window, warming your pale grey skin. You never got much sun, before... not many vistas in a random decrepid building."
"You blink, letting your new eyes adapt to the morning."
"Actually, it's just strange that sunlight still feels like sunlight!"
"You hold your arm up in front of yourself, giddy with excitement as you see it. The graceful, seamed digits respond perfectly. Like they were always your hands..."
"You jump out of bed, and hurry over to the mirror next to a wardrobe."
show pc default with fade
## show a huge smile
i "Wow."
"Okay - you haven't been this happy in a long time."
"You eventually stop marveling at your new body, and take in the clothes you're wearing."
""
##doorbell sound
##smaller smile
i "Oh!"
"You walk towards the door the doorbell came from, agreeing to answer it in a VISOR pop-up."
"The pop-up gives you credentials - apparently the visitor is another Consort named Cassandra, and she's here to check up on your recovery."
jump CassTutorial
 