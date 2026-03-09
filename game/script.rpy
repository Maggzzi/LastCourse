# =================
# CHARACTERS           
# =================
define e = Character("Eun-gyeol", color="#b77b37")
define j = Character("Han Jaehyun", color="#651102")

define cheeky = Character("Niece", color="#ffffff")
define stern = Character("Brother", color="#ffffff")
define gifter = Character("Niece 2", color="#ffffff")
define cousin = Character("Cousin", color= "#ffffff")
define sister = Character("Sister", color= "#ffffff")

define friend1 = Character("Friend 1", color= "#ffffff")
define friend2 = Character("Friend 2", color= "#ffffff")
define friend3 = Character("Friend 3", color= "#ffffff")


define staff1 = Character("Staff 1", color= "#ffffff")
define staff2 = Character("Satff 2", color= "#ffffff") 


define chef1 = Character("Chef 1", color= "#ffffff")
define chef2 = Character("Chef 2", color= "#ffffff") 

# =================
# VARIABLES           
# =================
default family_talked = set()
default friends_talked = set()
default hint_counter = 0
default wrong_choice = 0
default took_key = 0
default kitchen_hint = 0

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

    scene party_intro at Transform(zoom=1.5) with fade
    play sound "toasting.wav"
    #scene #some place where jaehyun is ona podium holding a wineglass
    j "Goodevening everyone, i hope you all are having a wonderfull time~"
    j "it's great to see my family and close friends all in one place, but i have to make an announcement."
    j "Just like every year, someone outside of this circle gets the oppurtunity to join us, and you all know how picky i am~"
    j "If it isn't much of a bother, i would like to introduce our new guest, since some of you won't recognise him right away."
    j "i'm talking about the noteworthy journalist, Eun-gyeol!"
    e "Hello, my name's Eun-gyeol, it's nice to meet each and everyone of you here."
    j "He's been known for his famous celebrity-reputation-killing articles, i doubt that any of you folks haven't read his paper on idol xxx's scandal, revolving..."
    scene black
    "Ah yes, sorry, i'm not *just* an ordinary journalist, in fact, i've written many jaw-dropping scandals involving numerous bigshots."
    "I just had to target a few people in my articles on Han Jaehyun's behalf and i got the invitation in a flash."
    "But, well.. needless to say."
    stop music fadeout 2.0
    "He's an idiot, a big one at that"
    scene party_intro_twofaced at Transform(zoom=1.5)
    play music "eerie.wav"
    #scene #slightly changed art of where jaehyun is hugging eungyeol, where eungyeol looks kind of sinister
    "As i said earlier, i didn't come here to make friends, i'm more focused on who the next target of my paper is gonna be, and why not go for the biggest fish in the pond?"
    "The Han Group. One of Korea's largest family-owned conglomerates"
    "Han-Jaehyun — the chairman of Han Cultural Holdings. Museums, art foundations, luxury events, He's got full control over them."
    "That kind of power doesn't come clean."
    "People like him think money makes them untouchable."
    scene black
    "Han Jaehyun... let's see how untouchable you really are."
    stop music fadeout 2.0
    "Objective: gather information about Han-Jaehyun, talk to get clues about Jaehyun."
    e "I should mingle with the other guests for now, i'll take notes to keep my findings in check."
    #if NOT enough notes/evidence, fail the mission= shortest ending
    #if enough notes/evidence, 
    
    
label louge_scene:
    scene lounge_bg
    "You look around the main lounge room, seeing allot of people conversing with eachother."
    "You decide to walk up to them, your here to scoop some juicy secrets after all!"
    call screen party_map_fam

    return

label talk_guests_fam:
    show image "images/characters/lounge_guests.png" at Transform(zoom=1.5) 
    "You approach the group of guests but they don't notice you, they seem deeply immersed in conversation"
    cheeky "Hey, are any of you willing to bet that our *prodigy* won't get heated again like last time?"
    "!"
    stern "Didn't Father tell us not to speak of that icident? You should be carefull about what you say."
    gifter "Oh c'mon, it's not like he's here anyway, we can finally openly talk, no elders silencing us."
    gifter "I even brought a 'lil something for this special occasion, but i'm keeping it a secret untill.."
    gifter "The main course comes."
    stern "You really shouldn't have, you'd just be enabling his.. strange craving."
    cousin "I think i already know what it is!"
    gifter "Hehe~, he can hardly enjoy his fine dining without it anyway."
    sister "I thought there wouldn't BE another.. main course this time.."
    cheeky "Are you crazy? So you think your brother went out of his way to invite everyone.."
    cheeky "Just to talk? We're all waiting for the main event, obviously"
    "Main event.. what could there possibly be happening?"
    cousin "Guys, i think someone's been eavesdropping~"
    cheeky "Oh, you must be Eun-Gyeol, the *infamous* journalist, right? hehe"
    stern "Must you always be like this, that's no way to welcome a guest."
    e "No, it's fine - that's me alright! {size=-10}(...infamous, that's one way to put it){/size}"
    e "Would you mind introducing yourselves, please?"
    cousin "No need to be so formal darling, unlike stuckup prick over there, you can be yourself around us!"
    stern "Must you all be so.. ignorant.."
    cousin "We're Jaehyuns fam, we're all related to that prodigy!"
    cousin "But other than that, let's talk about the guest of honour!"
    cheeky "We've all seen your articles, they're quite remarkable as of now."
    stern "I do admit, your writing's quite sharp."
    stern "Not many journalists have shown that much dedication than you do."
    e "Wow, I'm grateful for your generous remarks."
    e "At the end of the day, im just doing my job."
    cousin "Stil, it must take courage. Jaehyun always liked people with ambition."
    cousin "Speaking of Jaehyun.. takes me back to how he was before"
    e "Before?"
    gifter "When he was younger he was so quiet, always hiding behind books."
    gifter "Now look at him, Hosting grand dinners, inviting half the city."
    stern "Succes changes people."
    cheeky "Or perhaps... it reveals who they truly are."
    e "Ah, what would you be implying?"
    cheeky "Oh, nothing~, don't tell him i said that, heheh."
    "Looks like they know allot about Jaehyun.."
    e "Regardless, you all seem to know allot about Han Jaehyun."
    e "Outside of \"being family\", there's got be more than that, right?"
    cheeky "Talking like a real interviewer, i'll have you sign an NDA beforehand, hehe."
    cousin "An icebreaker huh? Fine by me!"
    gifter "Same for the rest of us."

    label icebreaker: 

        #check if the player talked to three people
        if len(family_talked) == 3:
            "Hmm.. i've already talked to several people, but i think i'm just wasting my time."

            #asking if player want's to continue talking
            menu:
                "Should i keep going?"
                "It's for the best":
                    "I should atleast talk to three or four people before i call it quits.."
                    jump icebreaker_questioning 

                "Forget it, let me ditch 'em":
                    #wrong_choice counter, if it meets its quota, the player will get different endings
                    $ wrong_choice += 1
                    "I think that's enough of information from the family side."
                    "I should get to people even closer or explore the rest of the place."
                    jump lounge_scene_two

        #check if player talked to everyone
        if len(family_talked) >= 5:
            "I feel like i've spoken to everyone at the table"
            jump lounge_scene_two
        
        label icebreaker_questioning:
            menu: 
                "Who should i talk to?"
                set family_talked

                "Brother":

                    $ hint_counter += 1
                    $ stern = Character("Han Do-Hyun", color="#591919")
                    stern "My name is Han Do-hyun, brother of Han Jaehyun."
                    stern "It's a pleasure to meet you, i've always wanted to meet you in person."
                    e "Oh no, the pleasure's all mine. Same goes for me, i've seen you allot in the media recently."
                    e "Plenty, if i now mention it. When i tried to capture photos, i saw you accompanying Jaehyun."
                    stern "You would be correct, i oversee Han Financial Group."
                    stern "All family members who run divisions within Han Group get involved in my brothers meaningless parties."
                    stern "Come to think of it, i meet my brother at these events more than in private.."
                    e "Ah, i get it, Sounds like these events happen more often than you'd prefer."
                    stern "No, as in, the things that get involved when those parties happen.. disturb me"
                    stern "!"
                    stern "I-it seems the ice has been broken, you can choose the other person you'd like to meet."
                    e "Hm, sounds good to me."
                    "So \"things\" have happened during Jaehyun's parties, ill note that down."
                    jump icebreaker

                "Niece":
                    "Im guessing you already know everyone in this party."
                    "I'm picturing you as the \"always prepared\" kind of guy!"
                    e "Actually, i haven't had the time to know all these people, especially all his family members."
                    cheeky "Hmm, fair enough. Guess introductions are in order!~"
                    $ cheeky = Character("Han Soo-ah", color="#603d26")
                    cheeky "Han Soo-ah's the name."
                    cheeky "I handle the media and entertainment side of the Han Group."
                    e "Ah, i see. Media and Entertainment?"
                    cheeky "That's right. Following trends till the sun don't shine."
                    cheeky "Which means I'm usually the one cleaning up the family's public image."
                    cheeky "Not that we ever need it, of course"
                    e "Of course."
                    "Hmm, I don't think i got to question something interesting..."
                    jump icebreaker

                "Cousin":
                    cousin "So, it's finally time to properly meet the well known Eun-Gyeol!"
                    e "Heh, well known as in \"infamous\" i presume? "
                    cousin "Haha! Don't let that eat you out, she's always been somewhat of a drama stirrer."
                    e "Then atleast me and her have something in common!"
                    $ cousin = Character("Han Joon-seo", color="#592222")
                    cousin "You'd be right! My name's Han Joon-seo. I oversee Han Heavy Industries."
                    cousin "Things like steel production, construction, shipbuilding - they're all up my alley."
                    e "Seems like a huge responsibility, i bet every family member's got their hands full."
                    cousin "You could say that again, i only came here for the food."
                    cousin "The main event is what makes my heart beat the most."
                    e "Eh, what happens during this \"event\"?"
                    cousin "You don't have to worry your pretty head about it."
                    e "Ehhh.. Sure thing.."
                    "That was weird, i thought i asked the perfect question and i got nowhere!"
                    jump icebreaker

                "Sister":
                    $ hint_counter += 1
                    e "I'm just guessing, but you'd be Jaehyun's sister, correct?"
                    sister "!"
                    sister "Yeah but, how did you..?"
                    e "The red hair runs in the family, no?"
                    sister "Ah, so it's like that."
                    $ sister = Character("Han Ha-eun", color="#592222")
                    sister "Yes, My name's Han Ha-eun, sister of Jaehyun."
                    e "So, what division do you run? I'm guessing something big, an important aspect of Han Groups branch."
                    sister "Uhm, actually.. i gave my position to someone else.."
                    e "Huh? Well that's a first."
                    sister "Jaehyun insisted. He said the family only needs people who can stomach everything."
                    e "Stomach everything?"
                    sister "..."
                    sister "Ah, forgot i said that."
                    "I somehow got to know something relevant to Jaehyun without asking directly. Nice."
                    jump icebreaker

                "Niece 2":
                    gifter "It's wonderful to get to know Jaehyun's new friends!"
                    gifter "He always used to keep things to himself, but now he's brags about them!"
                    e "I'm also grateful for this oppurtunity, to meet wonderful people related to the man himself."
                    gifter "You brag too much about him, he's just as ordinary as all of us."
                    $ gifter = Character("Han Seo-yoon", color="#593d22")
                    gifter "Name's Han Seo-yoon, keeping up with all modern fashion!"
                    gifter "I manage the luxury brands division~"
                    e "Wow, you also look the type, classy!."
                    gifter "Haha! Compliments'll get you nowhere!"
                    e "Though, everyone in the family knows how to dress, Jaehyun too"
                    gifter "Who do you think arranges those outfits? Credits should be given when mentioned!"
                    e "Oh, so it's like that!"
                    "I got the feeling where i couldn't ask her something, seemed to have been too deep in another topic."
                    jump icebreaker
            
label lounge_scene_two:
    "lets explore the area further."
    scene lounge_bg
    "Once again, you look at the main lounge"
    "You notice a familiar group of people, you walk up to them."
    call screen party_map_friends

label talk_guests_friends:
    show image "images/characters/lounge_guests_friends.png" at Transform(zoom=1.5) 
    "You approach a small group of guests nearby."
    "They seem allot closer, they probably must be Jaehyuns friends."
    friend1 "Hey, has anyone actually seen Jaehyun tonight?"
    friend2 "Now that you mention it... i only saw him during that speech with his new \"friend\""
    friend1 "He's probably busy with \"preperations\" again, overlooking the kitchen staff.."
    friend3 "Heheh... More like his {i}hic{/i} bodyguard dragged him off~"
    friend3 "It's almost like their glued to eachother..! HAHAHAHA"
    friend2 "Heh, you could say that again! Ever since that bodyguard showed up, Jaehyun barely reaches out anymore."
    friend1 "Yeah.. we used to see him all the time."
    friend1 "But still, we shouldn't talk behind his back like this. It's common courtesy."
    friend3 "Even so.. {i}hic{/i} you practically need to schedule a meeting three weeks in advance..."
    friend2 "If that bodyguard of his even approves it."
    friend1 "You make it sound like he's imprisoned."
    friend2 "Tell me i'm wrong."
    friend1 "...Maybe your are."
    friend1 "That guy's literally responsible for keeping everyone safe tonight. He's a one man army."
    friend1 "And no, not Jaehyun alone, but every single guest here."
    friend1 "Considering the kind of people attending this party.. I'd say that's a pretty important job."
    friend2 "...Alright, you win."
    "...Interesting."
    "So Jaehyun has a bodyguard, i should've seen that one coming."
    "But he isn't only protecting Jaehyun, he's responsible for the entire event's security??"
    "That makes him far more important than a average bodyguard.. i would ask for a raise at this point."
    $ hint_counter += 1
    friend2 "Ah, looks like we've got company."
    friend3 "Ohhh.. I know who you aree {i}hic..{/i}"
    friend3 "But why are you moving so much.. you can just stay still.. {i}hic{/i}"
    e "Uhh.."
    friend1 "Ignore him, he's got too much than what he can handle."
    e "Yeah, it would seem so."
    friend2 "But his question still stands, aren't you the \"lucky\" guest?"
    e "Some prefer to call me just \"that journalist\", but Eun-gyeol is preferred."
    friend1 "Ah, i see. Well it's nice to meet you Eun-gyeol."
    friend2 "Are you gonna interview us like in your other works?"
    e "That depends, i'm just curious to meet Jaehyuns closest friends. Like to know his taste in them."
    friend2 "W-what? So we're next?-"
    #add nudging sound
    friend1 "*Ahem*, We could say the same for you, since it's quite hard for someone like Jaehyun to share his.. thoughts."
    e "Huh.. i guess we'll have to find out."
    friend2 "Fine by me, the funniest guy is deadrunk and walking encyclopedia here is making my ears bleed."
    friend3 "I.. {i}hic{/i} i'm still alive..!"
    friend2 "Sure you are buddy."
    jump icebreaker2

label icebreaker2:
    if len(friends_talked) >= 3:
        "I feel like i've gathered quite a bit of information this time. I'll explore further"
        jump lounge_scene_three

    label icebreaker_questioning2:

        #Didn't give the people any names and no professions! 
        menu: 
            "Who should i talk to?"
            set friends_talked

            "Friend 1":
                friend1 "If your just after Jaehyun's info, why don't you go after him yourself?"
                e "Well i would {i}love{/i} to do just that, but frankly - i have no idea where he is."
                friend1 "Hmm, there {i}is{/i} one thing i can tell you about him."
                friend1 "You are likely to gain his attention promptly, as he himself has admitted."
                e "Oh? Let me guess... persuasion?"
                friend1 "Fine wine."
                friend1 "The good kind."
                friend1 "Mention the right bottle and he'll show up faster than you'd expect."
                e "So he's a collector?"
                friend1 "More like a connoisseur, he's extremely picky though."
                friend1 "He's got refined taste, as he himself says. He won't even take a glance at regular bottles."
                e "Sounds expensive."
                friend1 "Heh, everything about him is."
                "Fine wine, huh."
                "That might come in handy later."
                jump icebreaker2
            
            "Friend 2":
                $ hint_counter += 1
                friend2 "If you want to know more about Jaehyun, just know that he's an extreme perfectionist"
                friend2 "And i don't mean that in the healthy way."
                e "Hmm, how so?"
                friend2 "I once saw that poor guy redo an entire stack of paperwork. Three nights. No sleep."
                e "Three nights...? How is he even standing up, let alone function properly?"
                friend2 "That's another thing, he's so mysterious in his ways, even we don't know it."
                friend2 "But other than that, he's reliable, keeps his word. A great friend to have."
                friend2 "Just a teensy bit crazy in the head, i don't know if it's the {u}dedication or obsession{/u} of perfection he's after."
                "Huh, so he likes to be perfect in everything he does, but in a not so safe type of way, good to know."
                jump icebreaker2

            "Friend 3":
                friend3 "Huh...?"
                friend3 "Oh, hey there... four eyes.."
                e "?"
                e "I'm sorry to break it to you, but i am {i}not{/i} wearing glasses."
                friend3 "Huh.. that's strange.. {i}hic{/i}, you look like a foureyes."
                "What is that supposed to mean..."
                e "Say, how many shots have you had tonight?"
                friend3 "Heh.. your asking the wrong question..."
                friend3 "you should ask how many BOTTLES..!."
                e "Oh damn... rough night?"
                friend3 "Nahhh.... best night."
                friend3 "Free wine, fancy food... What's not to love?"
                e "Fair point."
                e "Say, since your enjoying the party so much, have you seen Jaehyun anywhere?"
                friend3 "Jaehyun...?"
                friend3 "Hmm..."
                "You see him squinting like he's trying to remember something extremely complicated."
                friend3 "Oh!"
                friend3 "Yeah, yeah... I think i saw him earlier."
                e "Where?"
                friend3 "He was..."
                friend3 "...walking somewhere."
                e "Very helpful."
                friend3 "Wait. No, no- i remember now!"
                friend3 "Kicthen."
                e "The kitchen?"
                friend3 "Yeah.. or the hallway next to it. Somewhere back there..."
                friend3 "He looked like he didnt't want anyone following him."
                "Interesting. The host of the entire event sneaking toward the kitchen?"
                "That's definitely not normal."
                friend3 "Anyway... if you find him..."
                friend3 "Tell him he still owes me a drink."
                e "I doubt that's the only thing he owes people tonight."
                jump icebreaker2

label lounge_scene_three:
    scene lounge_bg_staff at Transform(zoom=1.5)
    "From afar, you see a couple of staff members, one of them looks like their in distress."
    e "This might be a good oppurtunity to ask how it's like to work for Jaehyun."
    call screen party_map_staff

label talk_staff:
    show image "images/characters/lounge_staff.png" at Transform(zoom=0.75) 
  
    "Two staff members stand near the wall, quietly speaking to each other."
    "As you approach, one of them immediately straightens up."
    staff1 "Good evening, sir."
    e "Evening. Busy night?"
    staff1 "Yes, sir. A little more than usual."
    "The staff member seems slightly nervous, glancing at his colleague before continuing."
    e "How's work going tonight?"
    staff1 "Everything is running normally."
    staff1 "Though the chef has been making some... unusual orders."
    e "Unusual?"
    staff1 "Extra ingredients. Special requests."
    "The second staff member quickly nudges him."
    "The first staff member immediately stiffens."
    staff1 "Right. Sorry."
    staff1 "We are not allowed to discuss work duties with guests."
    staff1 "Company policy."
    "He gives a short, apologetic nod."
    staff1 "If you'll excuse me."
    "Both staff members quickly walk away."
    "As they leave, something small falls to the floor with a faint metallic sound."
    "A key."
    "It must have slipped from one of their pockets."
    "You pick it up."
    e "..."
    "They didn't seem to notice."

    menu:
        "Return the key":
            $ took_key = False
            e "I should return this. It probably belongs to the staff."

            "You decide to give the key back later."
            jump kitchen_scene

        "Keep the key":
            $ took_key = True
            e "This might be useful."

            "You quietly slip the key into your pocket."
            jump kitchen_scene
        
label kitchen_scene:
    "Okay, i've searched everywhere, talked with Jaehyuns relatives, friends and even his staff."
    #optional: show variable values of hints gathered, if shown good! if not, means player hasnt gotten any good lead > gonna fail 
    "I've gathered allot about Jaehyun, mysterious acts he's been pulling.."
    "What could he be hiding..? I think it's best to search outside of the lounge room"

    scene kitchen_bg at Transform(zoom=0.75)
    call screen kitchen_map

label talk_kitchen_staff:
    show image "images/characters/kitchen_staff.png" at Transform(zoom=0.75) 
    chef1 "Oh—hello." 
    e "Busy night?" 
    chef1 "Very." 
    e "What's it like preparing meals for Jaehyun?"
    chef1 "Well..." 
    chef1 "It's difficult." 
    chef1 "We prepare the best dishes we can, but..." 
    chef1 "He throws most of them away." 
    e "Throws them away?"
    chef1 "Yes." 
    chef1 "Nothing is ever good enough." 
    chef1 "He only likes the finest meals." 
    chef1 "Dishes that have..." 
    chef1 "...meaning." 
    chef2 "Hey." 
    chef2 "That's enough." 
    chef1 "Right. Sorry." 
    e "Meaning, huh..." 
    e "I'll keep that in mind." 
    $ kitchen_hint = True 
    jump kitchen_scene
    
return