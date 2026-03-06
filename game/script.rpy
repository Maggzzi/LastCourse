# =================
# CHARACTERS           
# =================
define e = Character("Eun-gyeol", color="#b77b37")
define j = Character("Han Jaehyun", color="#651102")


# The game starts here.
label start:

    #Party-intro script
    scene black
    play music "piano.ogg"
    "The Charity Ball, hosted every year by the ever so famous Han Jaehyun."
    "Said to be a real once in a life time experience, people would kill for a spot just to make connections and meet the higher-ups."
    "People would sing his prayers, try anything and everything to get on his good side, 'cause he calls the shots." 
    "Nevertheless, It's guests are VIP's only; politicians, celebrities, family members."
    "Though, despite those odds, i scored an invite, an ordinary journalist."
    "But the thing is, i didn't work hard for nothing just to waste time and make friends, i've got something {i}else{/i} in mind."

    play sound "toasting.wav"
    #scene #some place where jaehyun is ona podium holding a wineglass
    j "Goodevening everyone, i hope you all are having a wonderfull time~"
    j "it's great to see my family and close friends all in one place, but i have to make an announcement."
    j "Just like every year, someone outside of this circle gets the oppurtunity to join us, and you all know how picky i am~"
    j "If it isn't much of a bother, i would like to introduce our new guest, since some of you won't recognise him right away."
    j "i'm talking about the noteworthy journalist, Eun-gyeol!"
    e "Hello, my name's Eun-gyeol, it's nice to meet each and everyone of you here."
    j "He's been known for his famous celebrity-reputation-killing articles, i doubt that any of you folks haven't read his paper on idol xxx's scandal, revolving..."
    "Ah yes, sorry, i'm not *just* an ordinary journalist, in fact, i've written many jaw-dropping scandals involving numerous bigshots."
    "I just had to target a few people in my articles on Han Jaehyun's behalf and i got the invitation in a flash."
    "But, well.. needless to say."
    stop music
    "He's an idiot, a big one at that"
    play music "eerie.wav"
    #scene #slightly changed art of where jaehyun is hugging eungyeol, where eungyeol looks kind of sinister
    "As i said earlier, i didn't come here to make friends, i'm more focused on who the next target of my paper is gonna be, and why not go for the biggest fish in the pond?"
    "The Han Group. One of Korea's largest family-owned conglomerates"
    "Han-Jaehyun — the chairman of Han Cultural Holdings. Media, Idols, Film studios and Elite private events, He's got full control over them."
    "That kind of power doesn't come clean."
    "Men like him think money makes them untouchable."
    "Han Jaehyun... let's see how untouchable you really are."
     
    stop music
    "Objective: gather information about Han-Jaehyun, photos will be made with your camera, disguised as a pen."
    e "I should mingle with the other guests for now, i'll take notes to keep my findings in check."
    #if NOT enough notes/evidence, fail the mission= shortest ending
    #if enough notes/evidence, 
    
    screen party_map():
        add "images/bg/lounge_bg.png"

        imagebutton:
            idle "images/characters/lounge_guests.png"
            hover "images/characters/lounge_guests_fade.png"
            xalign 0.5
            yalign 0.5

            at Transform(zoom=0.8)
            action Jump("talk_guests")  
    
label louge_scene:
    scene lounge_bg
    "You look around the main lounge room, seeing allot of people conversing with eachother."
    "You decide to walk up to them, your here to scoop some juicy secrets after all!"
    call screen party_map

    return

label talk_guests:
    show image "images/characters/lounge_guests.png"
    "You approach the group of guests, they seem like the relatives of Jaehyun!"
    "Hey, you must be Eun-Gyeol, right? The *infamous* journalist, right?"
    "Heh, yeah- that's me, and you all are?"
    "We're Jaehyuns cousins, some here are brother and sister of his."
    "Yeah, we recognised you immediately."
    "Your articles have been quite remarkable, you know."
    "Sharp writing. Not many journalists dare to dig as deep as you do."
    "Thanks, i appreciate that! I'm just trying to do my job."
    "Stil, it must take courage. Jaehyun always liked people with ambition."
    "Speaking of Jaehyun.. doesn't he seem different lately?"
    "Different, that's putting it lightly."
    "When he was younger he was so quiet, always hiding behind books."
    "Now look at him, Hosting grand dinners, inviting half the city."
    "Succes changes people."
    "Or perhaps... it reveals who they truly are."
    
    return
