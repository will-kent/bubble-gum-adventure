# =============================================================================
# script.rpy - The Amazing Bubble Gum Caper
#
# How to use this file:
# 1. Download the Ren'Py SDK from https://www.renpy.org/
# 2. Create a new project in Ren'Py.
# 3. Open the project folder and go into the 'game' directory.
# 4. Replace the existing 'script.rpy' file with this one.
# 5. Create an 'images' folder inside the 'game' directory.
# 6. Add your background and character images to the 'images' folder,
#    making sure the filenames match the ones defined below.
# =============================================================================

# -- Step 1: Define Characters -----------------------------------------------
# You can define characters with different text colors.
# The narrator is used for text that isn't spoken by a character.
define narrator = Character(None, kind="nvl")
define wilfred = Character("Wilfred", color="#390099")
define mrs_higgins = Character("Mrs. Higgins", color="#9E0059")
define baron = Character("Baron von Whiskers", color="#FF0054")
define character_1 = Character("Character", color="#FF5400")
define character_2 = Character("Character_2", color="#FFBD00")


# -- Step 2: Declare Images --------------------------------------------------
# Ren'Py will look for these files in your project's "game/images/" folder.
# Replace "placeholder.png" with your actual image files (e.g., "street.jpg", "baron_mad.png").
# You can use .png, .jpg, .webp, etc.

# Backgrounds
image bg street = "images/placeholder.png"
image bg shed = "images/placeholder.png"
image bg factory = "images/placeholder.png"
image bg park = "images/placeholder.png"
image bg doghouse = "images/placeholder.png"

# Character Sprites (optional, but recommended)
image baron normal = "images/placeholder.png"
image baron scheming = "images/placeholder.png"
image butch the bulldog = "images/placeholder.png"


# -- Step 3: The Game Script -------------------------------------------------
# This is the main story flow. It starts with the "start" label.

label start:
    # Set the scene with a background and music (optional)
    scene bg street
    # play music "audio/your_music_file.ogg" # Uncomment to add music

    # The 'nvl clear' command clears the screen for the next block of text.
    # This makes it feel more like a book.
    nvl clear

    narrator "It's a blazing hot Tuesday. You've just spent your last dollar on a single piece of 'Galaxy Gum' from a weird-looking gumball machine. As you pop it in your mouth, it fizzes with power!"
    narrator "Suddenly, you see your grumpy neighbor's cat, Baron von Whiskers, snatching Mrs. Higgins' prize-winning petunias!"

    # This is a menu of choices for the player.
    menu:
        "Blow a super-sticky bubble to trap him!":
            jump page_2
        "Create a bouncy bubble to bounce over the fence.":
            jump page_3
        "Blow a giant bubble and float up to see what's happening.":
            jump page_14

label page_2:
    nvl clear
    # show baron normal at center # You can show character sprites like this
    narrator "You blow a glistening pink bubble that shoots out and encases the Baron! He's stuck."
    narrator "Just then, Mrs. Higgins rushes out."
    mrs_higgins "'My petunias! Oh, thank you! But... how did you do that?' she asks."

    menu:
        "'It was this amazing gum!'":
            jump page_4
        "'I found this... sticky net thing.'":
            jump page_5

label page_3:
    nvl clear
    narrator "You blow a huge, shimmering blue bubble and bounce over the fence. The surprised Baron drops the flowers and flees."
    narrator "As he disappears, you notice a strange humming sound coming from your neighbor's garden shed."

    menu:
        "Peek inside the shed.":
            jump page_6
        "Grab the flowers and bounce back.":
            jump page_7

label page_4:
    scene bg factory
    nvl clear
    mrs_higgins "'Magic gum?' Her eyes widen. 'A hero is just what this town needs! The Gigantic Sprinkle Co. was just robbed of its entire winter supply! The ice cream is all plain! Will you help?'"

    menu:
        "For great ice cream! I'll do it!":
            jump page_8
        "That sounds a bit dangerous...":
            jump page_9

label page_5:
    nvl clear
    mrs_higgins "'A net? Oh. Well, thank you anyway, dear.' She gives you a cookie, and you go on your way, the secret of the Galaxy Gum safe with you."
    narrator "You saved the flowers, and got a snack. A pretty good day."
    # Ending
    "A Quiet Victory"
    jump start

label page_6:
    scene bg shed
    nvl clear
    # show baron scheming at center
    narrator "You slowly creak the door open. Inside is a high-tech command center! Baron von Whiskers is at a console, with blueprints for a giant 'Yarn-Ball-o-Tron 5000' on the screen."
    baron "'So, you've discovered my secret. Join me, and we shall control all the yarn in the tri-state area!'"

    menu:
        "I'm in! Let's get that yarn.":
            jump page_10
        "Your cozy tyranny ends now, Baron!":
            jump page_11
        "Try to reason with him.":
            jump page_21

label page_7:
    nvl clear
    narrator "You decide not to poke around. You use another bouncy bubble to hop back to Mrs. Higgins' yard, flowers in hand."
    mrs_higgins "She's overjoyed and promises you fresh-baked cookies for a week. You're a local hero!"
    # Ending
    "Cookies Earned!"
    jump start

label page_8:
    scene bg doghouse
    nvl clear
    # show butch the bulldog at center
    narrator "You head to the sprinkle factory. The only clue is a single, perfect dog hair. Following the trail, you find Butch, the bulldog from down the street, sitting on a mountain of sprinkles in his doghouse."

    menu:
        "Create a bubble distraction.":
            jump page_12
        "Try to reason with the bulldog.":
            jump page_13
        "Make a bubble decoy of a mailman.":
            jump page_24

label page_9:
    nvl clear
    narrator "You politely decline. Solving a sprinkle shortage is a bit much for a Tuesday. You head home to watch cartoons, enjoying the memory of your one heroic act. Sometimes, small victories are the sweetest."
    # Ending
    "The Simple Life"
    jump start

label page_10:
    nvl clear
    narrator "You and the Baron become the ultimate duo of dastardly deeds. You use your bubble gum to pull off elaborate yarn heists. The world is soon wrapped in your cozy, chaotic vision."
    # Ending
    "Partners in Crime"
    jump start

label page_11:
    nvl clear
    narrator "You blow a giant bubble that lifts the Yarn-Ball-o-Tron high into the sky, where it pops harmlessly. The Baron, defeated, is distracted by a laser pointer dot you create with a bubble. You've saved the world from... too much yarn?"
    # Ending
    "Yarn-tastrophe Averted"
    jump start

label page_12:
    nvl clear
    narrator "You blow a series of tiny, shimmering bubbles that float around Butch like magical butterflies. While he's mesmerized, you quickly and quietly scoop up the sprinkle barrels and return them to the factory. The town's ice cream is saved!"
    # Ending
    "The Sprinkle Saviour"
    jump start

label page_13:
    nvl clear
    narrator "You try to talk to Butch, but he just growls and stands defensively over his treasure. Your quest for sprinkles ends in a stalemate. At least you tried."
    # Ending
    "Bulldog Stalemate"
    jump start

label page_14:
    scene bg park
    nvl clear
    narrator "You blow a massive, iridescent bubble that gently lifts you off your feet! From above, you see the Baron scurrying away and Mrs. Higgins looking confused. The whole neighborhood stretches out below you."

    menu:
        "Float towards the park.":
            jump page_15
        "Try to get back down.":
            jump page_16

label page_15:
    nvl clear
    narrator "You drift over to the park. A kid is crying below a tall oak tree. 'My kite!' he wails. You see it tangled in the highest branches, hopelessly stuck."

    menu:
        "Use a sticky bubble to retrieve the kite.":
            jump page_17
        "You're distracted by the ice cream truck music.":
            jump page_18

label page_16:
    nvl clear
    narrator "You try to push the air out of the bubble to descend, but it's harder than you think. You end up tumbling out and landing in a large, conveniently placed inflatable swimming pool. Your adventure ends with a splash."
    # Ending
    "Splashdown!"
    jump start

label page_17:
    nvl clear
    narrator "You carefully blow a long, sticky strand of gum that latches onto the kite. You gently pull it free and float down to deliver it to the grateful kid. You're a high-flying hero!"
    # Ending
    "Kite Rescuer"
    jump start

label page_18:
    nvl clear
    narrator "That music is just too catchy! You float towards the sound, completely forgetting the kite. By the time you get to the truck, your bubble pops, and you land softly on the grass. You don't have any money for ice cream."
    # Ending
    "Empty-Handed"
    jump start

label page_21:
    scene bg shed
    nvl clear
    narrator "You hold up your hands. 'Wait! What is this all for?'"
    baron "The Baron sighs, his evil facade crumbling. 'I just want to build the ultimate cat paradise... a scratching post so magnificent it can be seen from space!'"

    menu:
        "Help him find a better way.":
            jump page_22
        "That's ridiculous. I'm leaving.":
            jump page_23

label page_22:
    nvl clear
    narrator "You suggest a community bake sale to raise funds. It's a huge success! With the money, you and the Baron build an epic, but reasonably-sized, cat tree in the park. The Baron becomes a local feline hero, and you're his trusted deputy."
    # Ending
    "Project Cat Paradise"
    jump start

label page_23:
    nvl clear
    narrator "You decide this is way too weird for a Tuesday and back out of the shed. The secret of the Yarn-Ball-o-Tron 5000 is safe, for now. You'll never look at Baron von Whiskers the same way again."
    # Ending
    "Ignorance is Bliss"
    jump start

label page_24:
    scene bg doghouse
    nvl clear
    narrator "You blow a life-sized bubble in the shape of a mailman, complete with a hat. Butch's eyes go wide, and he takes off after the wobbly decoy, barking furiously. The mountain of sprinkles is unguarded."

    menu:
        "Return all the sprinkles.":
            jump page_25
        "Take one barrel for your trouble.":
            jump page_26

label page_25:
    nvl clear
    narrator "While Butch is distracted, you use a series of sturdy bubbles to float all the sprinkle barrels back to the factory. Ice cream is saved for everyone, and you're the hero of dessert!"
    # Ending
    "Sprinkle Hero"
    jump start

label page_26:
    nvl clear
    narrator "You decide a hero's fee is in order. You grab one barrel of rainbow sprinkles and head home. The factory gets most of their supply back, and your personal ice cream will never be plain again. A win-win."
    # Ending
    "The Sweetest Tax"
    jump start
