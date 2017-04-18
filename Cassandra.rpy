image cass default = "images/cass_default.png"

define cass = Character('Cassandra', color="#FFFFFF", window_left_padding=160, what_prefix="\"", what_suffix="\"")
############################################################################################
label CassTutorial:
    
    $ CassNick = "Cassandra"
    $ CassTutorialBasics = False
    $ CassTutorialYourself = False
    
"When you pick the option on your VISOR, the words fade away, and the door slides open."
show cass default at right with fade
"A voluptuous figure is standing in the doorway. After a moment you realize those overly wide curves aren't natural for an umari - this Consort is an augment."
"You would have identified the clone faster, but that artificially colored hair is against Matrosa policy - as is the recolor of the uniform Cassandra is wearing, actually."
"On second thought, Cassandra is clearly a breeder-class augment, and Matrosa doesn't lease those out, so Cassandra must be fully separated from that corp."
"You've never actually met an augment in person - they're usually owned by those fairly high up in a corporation. And of course, any Ashley that escaped to the slums would probably be a lot more violent and angry than the sort of people you'd want to meet."
"The clone's full lips part in a wide grin as they see you, and they hurry into your room and take your hand in both of theirs, squeezing tightly."
cass "[name]! So good to finally meet you! I got picked to explain the basics to you. I'm not really sure how up to speed you are, but a little time with me and you'll know all there is, no worries!"
"Cassandra is -very- happy to greet you, apparently."
cass "After you're done with me Taylor has a quick demo for you - he's the mechanic that altered your shell for your customizations - and then you can start your first day's work."
jump CassTutorialMenu
############################################################################################

label CassTutorialMenu:
menu:
 "What are you going to ask about?"
 "Ask for a general summary of the situation." if not CassTutorialBasics:
  jump CassTutorialBasics
 "Ask about Cassandra." if not CassTutorialYourself:
  jump CassTutorialYourself
 "Say you've asked enough questions." if CassTutorialBasics and CassTutorialYourself:
  jump CassTutorialScene
############################################################################################

label CassTutorialBasics:
$ CassTutorialBasics = True
pc "So... the basics? I sort of jumped in headfirst here."
# show cass smile animation or whatever
cass "Of course, of course! I mean, you know the very basics at least - you're here in the Pleasure Dome in your new apartment and this custom shell body because you contracted to work for up to a year."
"Cassandra waits for a moment, until you nod - you suppose you could technically have brain damage from being put into the braincase yesterday, so it makes sense to check."
cass "Right! Well, obviously the reason we contracted you with such a great offer is because Minerva has decided it's more than likely you'll be truly converted over the course of your contract."
cass "Minerva isn't about to explain ever decision They make, even to us Consorts... but I do wonder why They went with this plan for you. I was a true believer long -before- I got any benefits."
menu:
    "Do you want to speculate on why you got the offer you did?"
    "Tell Cassandra you're pretty skeptical of the whole 'religion' idea.":
        pc "I just don't understand what anyone gets out of the whole 'worshipper' thing. I've made that stance pretty clear on the extranet - whoever headhunted me must have realized I'd be a hard sell."
    "Not really.":
        "You just shrug noncommitally."

jump CassTutorialMenu

############################################################################################


label CassTutorialYourself:
$ CassTutorialYourself = True
pc "Tell me a little about youself? I gather you know all about me from whatever master file you've got in the system."
cass "Oh, how rude of me! I'm feminine, so she/her pronouns. I mean, probably any free alpha uses those pronouns, but it's always polite to check."
cass "I've been a Consort for... over ten years now, I think. The first alpha in the Consortium, though it was a much smaller organization in general back then."
cass "From what I read, most deities would have a rank structure, but under Minerva it's just Consort or not, even if someone doesn't have any granted magic at all, like yourself."
cass "So here you are on your first day, equals with a longterm follower!"
"Cassandra waves her left hand around a bit, a blue glow radiating from inside her skin."
cass "And of course, if your employment here becomes more heartfelt instead of purely contractual, you'll probably get your hands on some magic as well."
      
jump CassTutorialMenu


############################################################################################

label CassTutorialScene:
cass "Anyhow, that's about it - you just have to meet with people who are coming to Minerva for help, and do whatever you can to help them out. Sex is optional of course, but you'll have plenty of chances if that's your thing."
"Cassandra lets out a little laugh at that comment."
cass "I mean, trust me, you can really bang all day as a Consort if you like."
"You notice Cassandra shifting her stance to rub her thighs together a bit."
cass "It's great really, being able to help Minerva just by getting off again and again."
##cass wide grin and touching herself
cass "Actually, would you like to? Fuck, that is? You're a sweetie, and I'm just soaked inside this bodysuit."
"Cassandra glances down, and you realize you can make out a faint sheen of wetness that's been seeping out of her bodysuit's seam. It must have been dripping down her thighs the whole time she's been talking to you."
cass "Not a problem at all if you'd rather not, of course! I'll just use a drone for a quick release after we're done talking if you're not interested."

menu:
 "Are you interested in sleeping with Cassandra?"
 "You're interested (sex scene)":
  jump CassTutorialSceneCont
 "You're not interested right now (scene turndown)":
  jump CassTutorialSceneNo
 "You're not interested in Cassandra (character turndown)":
  jump CassTutorialSceneNever
      
      
############################################################################################

label CassTutorialSceneCont:
"You nod, smiling."
pc "That sounds like it could be fun, yeah."
"Cassandra gets a little glint in her eyes as you express your interest."
cass "Alright then hun. I've read your psychological profile... I give you full sweeping consent! Let's do whatever you want."

##if wearing bodysuit
menu:
 "Cassandra's still clothed, what will you do about that?"
 "Zip her down the rest of the way, and bend her over your couch - there's no time to waste before you start banging her brains out.":
  jump CassCouchScene
 "Shower her in kisses while you strip her out of that bodysuit.":
  jump CassStripherScene
 "Ask her to strip for you.":
  jump CassSelfstripScene

menu:
 "What exactly do you want to do with Cassandra?"
 "You just want to bend Cassandra over a couch and see how quickly you can bang her to orgasm.":
  jump CassCouchScene
 "You want to be more intimate and make it all about her, and give Cassandra a nice long eating out.":
  jump CassCunnilingusScene
 "You're not interested in Cassandra (character turndown)":
  jump CassTutorialSceneNever
      

jump gameover
############################################################################################

label CassTutorialSceneNo:
jump gameover
############################################################################################

label CassTutorialSceneNever:
jump gameover
############################################################################################
  
label CassCouchScene:
"You step forward, keeping your eyes locked intently with Cassandra's, and take a hold of her zipper."
"As you unzip her bodysuit and your hand reaches her groin, Cass's posture shifts - she puts her arms behind her back, hands clasping together, and inches her hips forward a bit as she stands up straighter."
"The move presses her mound into the palm of your hand. The synthetic bodysuit material covering her labia is slippery with her juices and just wonderfully warm to the touch."
"Despite your plan to get her undressed quickly, you can't help but press your hand into her crotch more purposefully, letting your fingers rest there while beads of her vaginal secretions start run down your skin."
##close eyes open mouth
"As you cup her sex for a moment, the zipper still not quite undone, Cassandra's eyes close and her mouth opens a little to let out a low moan. Her tongue moves just a little with each anticipatory breath she lets out now."
cass "Unff...\", she barely whispers, \"oh... please..."

menu:
 "How do you continue?"
 "Finish the unzipping, and bend her over the couch.":
  jump CassCouchSceneA
 "She's just too cute like this - you want to hold her on the edge with your fingers.":
  jump CassCouchSceneB
  
############################################################################################
  
label CassCouchSceneA:
    
############################################################################################
  
label CassCouchSceneB:

pc "Oh my goodness, you're too cute! I can't turn away from that face right now."
pc "You just stand perfectly still there, [CassNick]."
cass "Yes [honorific], of course,\" she softly whimpers and nods slightly. \"Whatever you say."
"You get the impression that what the augment really wants to do is grab hold of your hand and grind ferociously against it."
"You pull your hand slowly away, stroking your fingertips along her snugly clad labia. Cassandra's body tries to follow along with your hand, her back arching to let her push her hips further towards you."
##Cass titsout
"The movement causes her enormous but perky breasts to finally pop free of the unzipped upper bodysuit. It really is a marvel how pertly they stand before you considering their weight. Genetic engineering at it's finest."
"Your fingers fully part from Cassandra's mound for barely a second when you can here the beginning of a whine coming from the back of her throat. You reverse the motion of your hand, your fingers slipping in between her skintight outfit and her actual flesh."
"Cassandra's whine turns into a gasp as your digits stroke against the fleshy folds of her vulva."
  
jump gameover
############################################################################################

label CassCunnilingusScene:
jump gameover
############################################################################################
  