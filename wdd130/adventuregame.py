hallway_stairs = "question 1"
closet_fight = "question 2"
sword_fist = "question 3"
bedroom_bathroom = "question 4"
steal_nap = "question 5"
jump_leave_wait = "question 6"

print("You enter an extremely spooky mansion")
hallway_stairs = input("You walk into the mansion and find that there are two paths to take: The HALLWAY and the STAIRS. Which one do you choose? ")
if hallway_stairs.lower() == "hallway":
    closet_fight = input("You enter the hallway to find that there is a huge werewolf waiting at the end of it for you. You have two options: Do you hide in the CLOSET or FIGHT the werewolf? ")
if closet_fight.lower() == "closet":
    print("You hide in the closet but the werewolf saw you before you acted. It opens the door and kills you. YOU LOSE! Start over again? ")
if closet_fight.lower() == "fight":
    sword_fist = input("You realize there is no other option but to fight this creature. You have two options here: Do you pick up the sword on the ground or do you fight the werewolf with your fists? ")
if sword_fist.lower() == "sword":
    print("You pick up the sword and realize it's heavy but bearable. You take action and the werewolf hurts you but you are able to kill it with one blow. YOU WIN! Start over again? ")
if sword_fist.lower() == "fist":
    print("You don't pick up the sword and soon realize it was a mistake. The werewolf comes at you with blinding speed and take you out in one blow. YOU LOSE! Start over again? ")
if hallway_stairs.lower() == "stairs":
    bedroom_bathroom = input("You go up the stairs and see that there are only two rooms that aren't locked to you. Which one do you choose: The BATHROOM or the BEDROOM? ")
if bedroom_bathroom.lower() == "bedroom":
    steal_nap = input("You walk into the bedroom and you see a huge and comfy bed there just waiting for you but also many precious and priceless items on the ground and all over the room. Do you: Take a NAP in the bed or STEAL from the mension owners? ")
if steal_nap.lower() == "nap":
    print("You decide you've had a long day and you lay down in the bed and take a peaceful nap. As you wake up you notice a werewolf standing over you not pleased you are in it's bed. It kills you for being there. YOU LOSE! Start over again? ")
if steal_nap.lower() == "steal":
    print("You decide that taking the priceles objects is worth is and grab over a million dollars in items. You start to leave when you see a werewolf standing by the front door because it heard your noises. You try to run but it catches you and kills you. YOU LOSE! Start over again? ")
if bedroom_bathroom.lower() == "bathroom":
    jump_leave_wait = ("You enter the bathroom and realize you're trapped there becuase a werewolf has just showed up behind you. You have only three options: Do you JUMP out of the window of the bathroom going outside, try to just LEAVE the bathroom in peace, or do you WAIT for something to happen to you knowing you're dead? ")
if jump_leave_wait.lower() == "jump":
    print("You jump out of the window successfully and realize it's a long fall. You break a leg but survive. You look back and see that the werewolf is watching you but doesn't follow. YOU WIN! Start over again? ")
if jump_leave_wait.lower() == "leave":
    print("You say sorry to the werewolf for intruding in it's mansion and start to leave the bathroom when the werewolf stops you and thanks you for being polite and leaving when realizing the mansion was preccupied. YOU WIN! Start over again? ")
if jump_leave_wait.lower() == "wait":
    print("You just wait there and eventually the werewolf gets tired of you being in it's home. It decides to eat you. YOU LOSE! Start over again? ")