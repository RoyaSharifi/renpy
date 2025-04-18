define s = Character("Sam", color="#4DA6FF")
define r = Character("Roya", color="#FF66B2")
define rm = Character("Roya's Mom")
define rd = Character("Roya's Dad")

transform scale_to_1080:
    xysize (1920, 1080)
    fit "fill"

label start:

    scene expression "images/campus_scene.png" at scale_to_1080
    play music "bgm_campus.mp3"
    "A quiet afternoon on campus. Birds chirp, and students pass by."

    s "Oh no, I’m so sorry! Are you okay?"
    r "Yeah, don’t worry. My sketchbook's still in one piece."

    "They both laugh awkwardly but with warmth."

    menu:
        "Ask Roya to grab coffee":
            s "Would you maybe want to grab a coffee? There’s a place nearby I really like."
            r "Hmm... sure, why not?"
            jump coffee_scene

        "Say goodbye":
            s "Well... I guess I’ll see you around."
            r "Yeah, take care!"
            return

label coffee_scene:

    scene expression "images/coffee.png" at scale_to_1080
    play music "coffee.mp3"
    "The café is cozy, filled with quiet music and the scent of roasted beans."

    s "So... theatre or club? If you're up for a second date."

    r "Smooth move. Alright, surprise me!"

    menu:
        "Go to Theatre":
            r "I love plays. Let’s do the theatre!"
            jump theatre_scene

        "Go to Club":
            r "I could use a good dance. Let’s hit the club!"
            jump club_scene

label theatre_scene:

    scene expression "images/Theatre.png" at scale_to_1080
    play music "Theatre.mp3"
    "The stage glows in warm light. Sam and Roya watch the performance in awe."

    s "It’s beautiful, isn’t it?"
    r "Yeah... and kind of reminds me of us."

    "Their hands rest close on the armrest. A small touch, but full of meaning."

    jump family_scene

label club_scene:

    scene expression "images/club.png" at scale_to_1080
    play music "club.mp3"
    "Colorful lights dance as Sam and Roya move with the beat."

    r "You’re not bad for someone who said he doesn’t dance!"
    s "I’m motivated by good company."

    "They laugh, the crowd around them fading away as they focus on each other."

    jump family_scene

label family_scene:

    scene expression "images/family.png" at scale_to_1080
    play music "family.mp3"
    "A few days later, Sam joins Roya and her parents for dinner at a quiet restaurant."

    rm "So, Sam, Roya tells us you're into nature?"
    s "Yes, I actually hike a lot when I need to think."

    rd "That’s good. Nature has a way of clearing the mind."

    r "He even wants to show me a garden he loves..."

    "Everyone smiles. The dinner feels warm, even familiar."

    scene expression "images/family.png" at scale_to_1080
    "Later, more family members arrive. They laugh over old photos and tell stories of Roya as a child."

    rm "We’re really glad you came, Sam. It’s rare we get to see her with someone who truly listens."

    s "It means a lot to me too. Your family is wonderful."

    "Sam squeezes Roya’s hand under the table."

    jump garden_scene

label garden_scene:

    scene expression "images/garden_scene.png" at scale_to_1080
    play music "love.mp3"
    "Golden hour paints the garden in warm light. Flowers sway in the breeze."

    "Sam and Roya walk quietly, fingers intertwined."

    s "This garden always felt peaceful to me... but today it feels different."

    r "Because I’m here?"

    s "Exactly. Roya, since the moment we met on campus... everything’s felt brighter."

    "He stops by a patch of roses and kneels."

    s "I know this might feel sudden, but to me, it feels right."

    s "Roya... will you marry me?"

    menu:
        "Yes!":
            r "Yes! A thousand times yes!"
            "She laughs through tears and hugs Sam tightly."
            "The sun dips below the horizon as petals fall softly around them."
            return

        "I need time":
            r "Sam... I care about you, deeply. But I need time."
            s "Of course. I’ll wait. For as long as it takes."
            return
