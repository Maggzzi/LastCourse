# =================
# CHARACTERS           
# =================
define e = Character("Eun-gyeol", color="#b77b37")
define j = Character("Han Jaehyun", color="#651102")


# The game starts here.
label start:

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
    "I just had to target a few people in my articles on Han Jaehyun's behalf, and i got the invitation in a flash."
    "But, well.. needless to say."
    stop music
    "He's a big idiot."
    #scene #slightly changed art of where jaehyun is hugging eungyeol, where eungyeol looks kind of sinister
    "As i said earlier, i didn't come here to make friends, i'm more focused on who the next target of my paper is gonna be, and why not go for the biggest fish in the pond?" 

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
