screen party_map_fam():
        add "images/bg/lounge_bg.png"

        imagebutton:
                idle "images/characters/lounge_guests.png"
                hover "images/characters/lounge_guests_fade.png"
                xalign 0.5
                yalign 0.434

                action Jump("talk_guests_fam")  


screen party_map_friends():
        add "images/bg/lounge_bg.png"

        imagebutton:
                idle "images/characters/lounge_guests_friends.png"
                hover "images/characters/lounge_guests_friends_fade.png"
                xalign 0.5
                yalign 0.434

                action Jump("talk_guests_friends")  


screen party_map_staff():

        imagebutton:
                idle Transform("images/characters/lounge_staff.png", zoom=0.75)
                hover Transform("images/characters/lounge_staff_fade.png", zoom=0.75)
                xalign 0.5
                yalign 0.434

                action Jump("talk_staff")  

screen kitchen_map():
        
        imagebutton:
                idle Transform("images/characters/kitchen_staff.png", zoom=0.75)
                #HAVE TO ADD HOVER IMG KITCHEN STAFF
                xalign 0.5
                yalign 0.434

                action Jump("talk_kitchen_staff")  
        