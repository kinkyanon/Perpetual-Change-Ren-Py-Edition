# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Large ASCII text settings:
#Website: http://www.kammerl.de/ascii/AsciiSignature.php
#Style: Basic


#define e = Character("Eileen")
define cs = Character("C.S.")
define lr = Character("L.R.")
define ecl = Character("Eclair", color="#c5d4d9")
define mrn = Character("Marna", color="#faa9b6")
define vin = Character("Vince")
define drk = Character("Derek")
define mrie = Character("Marie")

transform fliphoriz:
    xzoom -1.0

$ immaturity = 0

$ pickedUpBriefs = false

$ putOnBriefs = false

$ money = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    cs "Ready to go to work?"

    lr "Yeah, yeah, in a second. As soon as this stupid P.O.S. tech boots up."

    cs "You know that stuff is very advanced and very sensitive right?"

    pause 1.0

    lr "And?"

    cs "And hitting it won’t make it go any faster...."

    pause 1.0

    lr "And?"

    cs "And hitting the console is more likely to damage something important than make it work properly."

    pause 1.0

    lr "And?"

    cs "AND THIS IS A VERY DELICATE OPERATION AND MAYBE WE SHOULDN’T BE SO CAVAL-…"

    pause 1.0

    cs "oh, there it goes."

    lr "Yup. Works every time."

    cs "Seems like everything is functioning within normal parameters. Reality Pulse Generators are still functioning well within the green."

    lr "Mental Maturity Sync Systems are fully operational."

    cs "All cameras around the island are active and as of yet, undiscovered."

    lr "Everything’s green. Let’s do this!"

    cs "Okay,{w=1.0} activating Reality Pulse Generator."

    scene bg eclair bedroom original inbed dark at truecenter

    lr "Waaaaaaaiiit!"

    cs "... {w=1.0}What now?!"

    lr "Wanna make a bet about who it’s gonna affect this time?"

    cs "Seriously?{w=1.0} Are you really doing this?"

    lr "What? Nothing major. Loser buys winner lunch. If it’s a tie, nothing happens."

    cs "How callous can you be? Do you have any idea how significant this process can be for the affected? {p=1.0} ...My money is on the red head on Camera 87."

    lr "Nah, I’m going for the black haired bookworm with the glasses by her nightstand. Camera 31. See?"

    cs "Her? Why her?"

    lr "Call it a sixth sense."

    cs "I don’t want to know anything about your “senses”."

    lr "Pretty judgmental for a guy who keeps a diary. “Dear Diary, I had that dream again…”"

    cs "You read my diary?!"

    lr "Oh what’s that?{w=1.0} Sorry, I can’t hear you. I’m counting down! Fivefourthreetwooneblastoff!"

    "Reality Pulse and Mental Maturity Sync Initiated!"

    scene bg eclair bedroom original inbed accident dark at truecenter

    ecl "Mmmmm..."

    lr "AAAAAAAAND WE! HAVE! LIFTOFF! Right there! Camera 31! In your face!"

    scene bg eclair bedroom original inbed accident at truecenter

    ecl "*Yawn* That was a weird dream. Really felt like I was..."

    scene bg eclair bedroom original accident at truecenter

    "{i}The girl looks down at her urine soaked sheets.{/i}"

    show eclair underwear accident at right
    with easeinright

    ecl "OHMYGAWD, OHMYGAWD, OHMYGAWD!"

    "{i}The girl leaps out of bed and looks at her wet sleepwear, her face is a mixture of horror and disgust.{/i}"

    "{i}She stands bow legged and arms spread wide. She’s too overwhelmed to even touch herself.{/i}"

    ecl "How the hell did that happen?! I haven’t wet the bed since I was in pre-school!"

    "{i}The girl strips naked, throwing her soiled clothes onto her soiled bed{/i}"

    show eclair nude sad2 at right

    ecl "*Exhales deeply* It’s okay. It’s okay.  I can handle this. Just gotta act quickly. Just gotta get these sheets and things in the laundry and get a shower before Mom-"

    hide eclair nude sad2
    show eclair pose1 nude sad2 at left
    with easeinleft
    show marna pose3 smile at right, fliphoriz

    mrn "Good morning, honey! Time to wake up!"

    ecl "Mother! Get out! Private!"

    mrn "Oh pshaw, you’re just getting ready for your shower, like you do every morning."

    ecl "Wait...{w} what?!"

    mrn "You woke up wet, like you usually do, and now you’re going to go get cleaned up before school.{p}Right, cupcake?"

    ecl "But...I...I don’t’...I mean..."

    mrn "Don’t be so self-conscious, Eclair. You’ve always had a weak bladder and a little bit of a bed wetting problem."

    ecl "I have?"

    lr "Looks like we got one more. Check out Camera 52. Hat trick! Behold my mad skills!"

    cs "You just pushed a button."

    lr "Don’t care. Behold my mad button pushing skills!"

    #Shower scene

    scene backgroundhere

    cs "That’s weird."
    lr "What’s weird about it? She peed the bed. They all do at first. Standard procedure."
    cs "Yeah…but she’s blushing.{w} Doesn’t that seem weird to you?"
    lr "Considering what our jobs are, not really.{w}But hey if “girl blushing after wetting the bed” is your thing, who am I to judge?"
    cs "No, you jackass! I mean {i}why{/i} is she embarrassed?"
    cs "Everyone affected by the technology is supposed to have next to no realization that anything is different."
    cs "Why would she be embarrassed about wetting the bed when she’s supposed to think she’s been doing it her whole life?"
    lr "There’s plenty of things that I’ve been doing my whole life that I’m embarrassed about. Maybe she’s just uh… an embarrassed bed wetter?"

    #Should be nude
    show eclair pose1 underwear neutral1 at right

    ecl "Why did I wet the bed? Why is Mom acting so casual about it?"
    cs "See!{w} Right there! ! She knows!!{w} She knows something is up!"
    lr "So?"
    cs "So?! !{w} So?! Nothing like this has happened before! We’ve got to fix this so that things don’t get out of hand."
    cs "We’ve never had three tributes at the same time, and none of them has ever been aware that their world was changing."
    lr "I mean…there was that one that had the daughter. The daughter might’ve realized something was-"
    cs "We almost got fired that last time!!{w} Do you want to get fired?"
    lr "…I do not. Want me to call management?"
    cs "Want me to tell management that you were beating on the panel like you were a prizefighter?"
    lr "…{w}Nope…{w}don’t like that either. So what do you suggest, oh wise one?"
    cs "Let’s just sit back and watch. We normally do this in increments, anyways, for just this reason. We’ll make sure she’s distracted enough, and fine tune the Sync System later tonight."
    lr "So…just wait and see? Like no more talking to each other?"
    cs "God,{w} I hope so."

    #Eclair in underwear

    ecl "I should talk to mom."

    #Walks into bedroom with Marna at bed

    show marna pose1 smile at left

    mrn "And there we go.{w} Good as new; till tomorrow morning anyways.*sigh* The things a mother will do for love."
    ecl "Uh…{w} Mom? I need to get dressed, now."

    show marna pose3 smile at left
    mrn "Well, don’t let me stop you, honey. I’m just getting clean sheets onto your bed.It’s a good thing we’ve got this plastic sheet on the mattress. Otherwise, this bed would have been ruined many times over."
    ecl "Plastic...? Whatever.  Mom, can I have some privacy please?"
    mrn "Privacy?{w} Well, alright then. I’ll meet you downstairs for breakfast. Just be quick, dear, I don’t want you to miss breakfast or school."

    hide marna
    with dissolve

    ecl "What is up with Mom today? I wet the bed and she acted like it was no big deal."

    #Eclair removes her underwear(?) and puts on clothes

    "I mean…{w}I wouldn’t expect her to freak out about it, or anything, but she was beyond relaxed about it. She didn’t even expect me to clean it up."
    "Like it happened all the time, or something. And what did she mean about me having a weak bladder? Is that some kind of joke or something?"
    "Whatever.{w} Time to go get some breakfast."

    #Interior, Kitchen

    show marna pose3 smile at left, fliphoriz

    mrn "So, Eclair, I’ve been thinking."
    ecl "About?"
    mrn "College."
    ecl "What about college? I’ve already got a scholarship for next year."
    mrn "I just wanted to bring it up now, first thing in the morning before you had any potential…accidents… that might affect your mood."
    ecl "Mom, what in the world are you talking about?"
    mrn "*sigh* Eclair, you’re my daughter, and I will always love you, but you’re going to want a place of your own when you’re a bit older.{p} Soon you won’t want things like your mother waking you up before school so she can change your wet bedsheets."
    ecl "I am {i}so{/i} confused right now."
    mrn "Don’t interrupt, dear. You’ve just…had this little problem for a long time, and I don’t think it’s going away anytime soon."
    ecl "{i}What{/i} problem?"
    mrn "And that’s okay. A lot of people wet the bed, but they don’t all have their mothers around to clean up after them."
    ecl "This is the first time it’s happened since, like, forever!"
    mrn "Are you embarrassed?"
    ecl "Uh..yeah…kind of!"
    mrn "Well good. It wouldn’t be quite normal if you weren’t at least a little embarrassed at your age. The fact that you shooed me out of your room while you got dressed shows that you’re maturing."
    ecl "????"
    mrn "My point being, that maybe you could start wearing some…ahem…protection to bed when you go to sleep at night."
    mrn "Help protect the mattress. It’d be less work for me. And when you start living away from home, and you don’t have to worry about getting a plastic sheet or laundering wet sheets every day."
    ecl "What does any of this have to do with college?!"
    mrn "You don’t think I’m going to follow you to college and come change your wet sheets for you, do you? It just might be easier if you wore a little something more…absorbent to bed."
    ecl "I wet the bed…one time…and you want me to wear diapers?!"
    mrn "Incontinence products, dear. They’re not called diapers when they’re for adults."
    ecl "It was just an accident!"
    mrn "Is it really an accident if it’s certain to happen, honey?"
    ecl "Mom, I’m going to level with you.  I have no idea what you’re talking about.  If this is some kind of joke or prank, it’s already gotten older than the internet. I’m not laughing. I’m done eating. I’m going to school. I’m going to pretend that this conversation never happened."
    mrn "Eclair!"
    ecl "What?"
    mrn "Just think it over, alright?"

    #      []What to say?
    # <Choices:>  Yeah, sure.
    # <Choices:>  Goodbye, mother.
    menu:
        "What to say?"

        "Yeah, sure.":
            ecl "Yeah, sure. Whatever."

        "Goodbye, mother.":
            ecl "*huff* {i}Goodbye{/i} Mother!"

    mrn "What’s gotten into her, today?"

# [Marna]Before you come home, I’ve placed an order at the store. Would you mind picking it up from Mr. Sayers and bringing it home?
# [Eclair]*huff* Fine…
# [Marna]Oh and Eclair?
# [Eclair]Yes Mother?
# [Marna]Don’t forget your lunch.
# [Eclair]Oh yeah, right. Thanks.
# [Marna]And Eclair?
# [Eclair]Yeah?
# [Marna]I love you.

    #Eclair exits the house

    ecl "Promised I’d meet Mishelle and Vince today before school."

    menu:
        "Where to first?"

        "Mischelle's house":
            jump optionaldialougemariaday1

        "Vince's house":
            jump vincehousemorningday1

label optionaldialougemariaday1:

    ecl "Hey, Marie."
    mrie "Hey Eclair."
    ecl "Mishelle ready for school?"
    mrie "Nuh-uh. My mom forgot to wake her up, and so she just hopped into the shower.  You know how it is."
    ecl "I…do?"
    mrie "Oh…am I…am I not supposed to know? I mean… sorry. I am sooooo sorry. No offense. Uh…just... my mom told me to tell you to come back in a little bit."
    ecl "Oooookay….?(Did Mishelle also…? Nah, that’s impossible. And  even if she did, how would Mishelle’s kid sister know that I wet the bed this morning, too?)"

    "Let's try Vince's then"
    jump vincehousemorningday1

label vincehousemorningday1:
    ecl "Hey, Vince."
    vin "Sup?"
    ecl "Something the matter?"
    vin "I’m not talking about it right now."
    ecl "That bad, huh?"
    vin "I’ve had worse."
    ecl "But you’re not talking about it?"
    vin "Nope."
    ecl "Suit yourself. Still coming to school?"
    vin "Mmmm..hmmm. I don’t see the point though. It’s a week before Summer Break, and we’ve already taken all the finals that they can throw at us."
    ecl "Well you know Miss Georgette. She always finds some curveball or another. Maybe it’ll be fun today. She said she had a surprise."
    vin "Maybe. Hey, where’s Mishelle?"
    ecl "She’s running late. We’ll need to double back if we’re going to all walk to school together."
    vin "Got in the shower late?"
    ecl "Yeah...how did-?"
    vin "*grumbles*"
    ecl "Huh? What was that?"
    drk "HEY VINCE! YOU FORGOT TO CHANGE WET SHEETS THIS MORNING!"
    vin "I’LL TAKE CARE OF THEM, LATER!"
    drk "Allllriiiight! But don’t blame me when your whole room smells like pee!"
    vin "*sighs* Yeah. Like I was saying…call it intuition. I’m betting your mom is the only one that woke you up in time, today. I didn’t even have time to change my sheets."
    ecl "What the heck is with everyone today?"
    vin "Well, if we’re going to get to school on time AND walk with Mishelle, then we better book it.  Race ya!"
    ecl "Hey! Wait up! What is going on?! Why is everyone…? {w}Errrrgh…AND YOU ARE NOT BEATING ME!"

#Mishelle's house dialouge here

# [Vince]*Pant, pant* I…won.
# [Eclair]*Pant, pant* No…fair…you…cheated. *Pant, pant* You…had a….head…start.
# [Mishelle]Hey guys. Sorry. I woke up late and my mom… Well, y’know.
# [Vince]Yeah…we know.  Happened to me too. It’s a drag, but what are you gonna do?
# [Mishelle]I would have been ready sooner, but my mom wanted to have a talk with me.
# [Eclair]About what?
# [Mishelle]About me getting…protection. So that maybe my mom won’t have to deal with wet sheets every morning, anymore.
# [Vince]Yeah…I got a bad feeling my dad and I are gonna have that talk when we get back from school.
# [Eclair]Okay, guys, what is going on, here?
# [Mishelle]What do you mean, Eclair?
# [Eclair]I woke up with a wet bed this morning, too. And my mom is trying to convince me to wear diapers to bed. And all of this is just coming out of nowhere, and I have no idea what’s going on.
# [Vince]Hmmm….you too?
# [Mishelle]That \iis\i weird.
# [Eclair]I know, right?!
# [Vince]Our parents must be talking to each other.
# [Mishelle]They wanted to spring this on us all at once so that maybe we’d all start wearing them together.
# [Eclair]...
# [Vince]Typical.
# [Mishelle]Very.
# [Eclair]...
# [Mishelle]You don’t suppose that’s why they woke us up late, do you? Make night time protection seem even more convenient?
# [Vince]I wouldn’t put it past them. Adults, man.
# [Eclair]What in the heck are you guys talking about?!
# [Mishelle]Um…our bed wetting problem…?
# [Vince]Quiet down, Mishelle. I thought we agreed we don’t talk about it unless we’re behind closed doors. You don’t want the rest of the island to know, do you?
# [Mishelle]I was barely talking above a whisper.
# [Eclair]Guys!\p[10] We’re!\p[10] Not!\p[10] Bed wetters!\p[10]
# [Mishelle]Since when?
# [Vince]I mean…we don’t go broadcasting it or anything.
# [Eclair]Because there’s nothing to broadcast!
# [Mishelle and Vince]*Sigh* Denial.
# [Mishelle]Don’t you remember, Eclair? We all became friends when we realized we all had the same…ahem… problem? That’s why we didn’t go to other kids’ sleepovers back in the day? Hey, Vince, remember what our parents used to call our sleepovers?
# [Vince]*sigh* Soggy Slumber Parties.
# [Eclair]Oh my gawd!  That is gross.
# [Vince]Yeah…that’s why I don’t like thinking about it.

#If Eclair went to Mishelle's house first

# [Mishelle]Oh, that reminds me. Eclair, Marie says “sorry” if she offended you.  She didn’t mean anything by it. And I didn’t tell her either. I think she just figured it out…a while ago.
# [Eclair]There’s nothing to figure…! *Deep breath* I don’t know what has made everyone in my life go so crazy, but it is officially older than the internet, now.
# [Eclair]It is so old, we are now decades away from even binary code, and have gone back to quill and ink.

#Else

# [Eclair]*Deep breath* I don’t know what has made everyone in my life go so crazy, but it is officially older than the internet, now.
# [Eclair]It is so old, we are now decades away from even binary code, and have gone back to quill and ink.

# [Mishelle]What are you talking about?
# [Eclair]Nothing. Just nothing. Let’s just get to school before we’re all late.
# [Vince]Finally.
# [L.R.]Holy crud! All three of the affected are friends? How unlikely is that?!
# [C.S.]This could work to our advantage. Let’s just keep watching till an opportunity presents itself.
# [L.R.]Roger that.



#The gang arrives at school

# [Fiona]And five...
# [Fiona]...Four...
# [Fiona]...Three...
# [Fiona]...Two...
# [Fiona]...One...
# [Fiona]Late for class, again, losers. What happened?  Did your Mommies and Daddy forget to wake you up again this morning?
# [Mishelle]Actually…
# [Vince]…Mishelle.
# [Fiona]They’re called alarm clocks, you big babies, and they do more than double as night lights. Later, losers.
# [Vince]What did we ever do to her? What did anybody ever do to her?
# [Mishelle]She has a point though.
# [Vince]Mishelle...
# [Mishelle]Maybe if we got alarm clocks and set them earlier we wouldn’t…y’know.
# [Vince]Mishelle...
# [Mishelle]Or we could have them wake us up in the middle of the night so we could go to…
# [Vince]Mishelle...
# [Mishelle]…instead of.
# [Vince]MISHELLE! That’s private talk.
# [Mishelle]Oh yeah…sorry.
# [Eclair]Well, Fiona’s still a bitch. So there’s at least one thing that’s normal. Mishelle still overshares, and Vince talks mostly to stop other people from talking too much.  So that checks out. Still…
# [Eclair]*Pinches herself*
# [Eclair]OW! Nope, still real enough.


#  .o88b.  .d8b.  d8888b. d88888b d88888b d8888b.   d8888b.  .d8b.  db    db
# d8P  Y8 d8' `8b 88  `8D 88'     88'     88  `8D   88  `8D d8' `8b `8b  d8'
# 8P      88ooo88 88oobY' 88ooooo 88ooooo 88oobY'   88   88 88ooo88  `8bd8'
# 8b      88~~~88 88`8b   88~~~~~ 88~~~~~ 88`8b     88   88 88~~~88    88
# Y8b  d8 88   88 88 `88. 88.     88.     88 `88.   88  .8D 88   88    88
#  `Y88P' YP   YP 88   YD Y88888P Y88888P 88   YD   Y8888D' YP   YP    YP

$ grannyComplete = false
$ cavesComplete = false
$ storeComplete = false
$ nurseryComplete = false
$ observatoryComplete = false
$ harbourComplete = false
$ farmComplete = false
$ mayorComplete = false

#Day 1, In School
#Interior, Classroom

# [Miss Georgette]Come on in, Eclair. Our lesson is about to start. Now we have only seven days left before the summer break, and I thought to myself “What would be the best way to spend them?”
# [Mishelle]Oooh! Oooh! Miss Georgette! Miss Georgette! Pick me! Pick me!
# [Miss Georgette]It was a rhetorical question, Mishelle, but thank you.
# [Mishelle]Oh…you’re welcome.
# [Miss Georgette]As you young people know, next year will be your final year of schooling.
# [Fiona]Thank God!
# [Miss Georgette]I’m choosing to ignore that, Fiona. Moving on.  But as you all know, we do not have any Colleges or higher education facilities here on Farzon, despite having many college educated adults here on the island. Does anyone know why that is?
# [Vince]Because they want us to leave.
# [Miss Georgette]Well, Vincent, you are correct in that, though I wouldn’t be so cut and dry about it. We do encourage our young people to go out into the world, though. This is by design actually. Quick quiz : who is credited as the founder of our island?
# [Mishelle]Oooh! Oooh!
# [Miss Georgette]Mishelle?
# [Mishelle]The original owner of the island of Farzon was Doctor Harkness Milner. He’s also the man who paid for the observatory at Hane Shore!
# [Miss Georgette]Correct on all counts! Most of this island’s layout is by his original design, including the lack of education after high school. But that’s a little weird isn’t it?
# [Miss Georgette]We’ve got our own food supply, our own power supply, law enforcement, mines, and forest. We’ve got a nearly perfect ecosystem for our little community here.
# [Miss Georgette]And you may not realize it or appreciate it, but despite our looks, our little community is much more advanced than it seems. In some areas of technology, we’re actually decades ahead of the rest of the world.
# [Fiona]Pffft, yeah right. The computers around here all look older than Granny Vincenza; and she’s older than the internet.
# [Miss Georgette]Oh really, Fiona? Then tell me, why are they operating over three times as fast as last year’s Pear models out on the mainland?
# [Fiona]Umm….
# [Eclair]Ha!
# [Miss Georgette]And Eclair, have you noticed that there’s no power plants on Farzon, yet everything is still powered?
# [Eclair]Uh…not till you just said it, no.
# [Maxwell]Tsk tsk tsk.
# [Miss Georgette]Maxwell, so nice of you to join the discussion. How does your father manage to grow vegetables for the entire island?
# [Maxwell]Emm…machines?
# [Miss Georgette]What \ikind\i of machines?
# [Maxwell]…Tractors?
# [Miss Georgette]Maxwell, think for a second, dear. You live on that farm. Have you ever seen a tractor there?
# [Maxwell]*Sighs* No.
# [Miss Georgette]Where do most of our goods come from if they’re not manufactured here, Vince?
# [Vince]My dad works at the docks…so…boats?
# [Miss Georgette]And where do the boats get their supplies from. What do we offer in trade or payment for our amenities?
# [Vince]*Shrugs*
# [Miss Georgette]What about our books for the library?
# [Vince]…I have no idea.
# [Miss Georgette]And how is it possible that we all have homes, a general store, a school, an ice cream shop, a kindergarten, a plantation, mines, forests, a café, an observatory, a port, a lighthouse, a library, and a public nursery,
# [Miss Georgette]and yet we have no power plant, nor garbage disposal service, nor farming equipment, and computers that are older and yet faster than the most top of the line technology out there?
# [Miss Georgette]How can we have all of these things, while contrarily lack some of the most basic services that these other things depend on? How are we managing to thrive in this little town, on this little island?
# [Eclair]I…don’t know. I guess we’ve kind of taken it all for granted.
# [Miss Georgette]Exactly! You’ve all lived here your entire lives, and yet you know next to nothing about the little world we call home. One day, you will all go out into the world so that you may  better know it and understand it.
# [Miss Georgette]But before you do that, you need to know about the world around you right here. You need to learn about your community.
# [Fiona]I don’t like where this is going.
# [Miss Georgette]I’m going to let you all take lunch a little early, today.
# [Fiona]Never mind. This is working out.
# [Miss Georgette]And then when you’re done, you’re to go around the island and interview different members of the community. Learn what they do, and how they do it.
# [Miss Georgette]Learn about the different services they provide around town and how they do it.
# [Fiona]*Huff* Great…Career Day. Never mind my never mind.
# [Miss Georgette]Find out why things are the way they are around here. Learn about the history of your home. Then, tomorrow, be ready to present what you’ve learned to your friends.
# [Eclair]*snicker* I guess that leaves Fiona out. You have to have friends.
# [Fiona]Watch it, you immature little brat.
# [Miss Georgette]Ladies, you will respect each other while you’re in my classroom.
# [Fiona and Eclair]Sorry ma’am.
# [Miss Georgette]Class dismissed for lunch.

# [Miss Georgette]Hey Eclair, would you do me a favor?
# [Eclair]What’s that?
# [Miss Georgette]Keep an eye on Fiona for me. She always gets particularly…difficult… around this time of year, it seems.  I think she could really use a friend right about now.
# [Eclair]You have no idea what you’re asking me to do.
# [Miss Georgette]Fiona’s had it hard. She never really knew her mother, and I think it’s affected her deeply. I’ve tried to do what I can with her, but I think she’d respond more with a peer.
# [Eclair]Fiona’s the very definition of a bully and an antisocial snob. If there’s a way to help her, I’m not the one to do it.
# [Miss Georgette]*sighs* Fine. Could you do me one other favor?
# [Eclair]What favor?
# [Miss Georgette]Would you consider going to an arts college next year? It’d be nice to have some real culture around here; maybe some musical theatre or something.
# [Eclair]Ha! That’s a definite maybe, Miss Georgette. That’s a definite maybe.

#Day 1, In School, after the briefing
#Interior, Classroom

# [Miss Georgette]How’s Career Day coming along?
# [Eclair]Actually, could we interview you? You must know a whole bunch of stuff about the island.
# [Miss Georgette]Nice try. Now get out there and actually experience out little slice of paradise.

# [Miss Georgette]What are you still doing here? It’s Career Day! Go out and interview people.
# [Mishelle]Actually, were wondering, is there a book or a text file that we could read instead?
# [Vince]Mishelle….
# [Miss Georgette]Wouldn’t that be against the point of Career Day?
# [Mishelle]Not if it was at the library.
# [Vince]Mishelle….
# [Mishelle]Hey, Vince, doesn’t your big brother work at the library? Ooooh, but he gave you the business earlier this morni-
# [Vince]MISHELLE!  PRIVATE!
# [Mishelle]Oh…sorry.
# [Miss Georgette]I have no idea what you are bickering about, but get out there or it’s detention for all of you.
# [Eclair]Um…you want us to go out so you’re threatening keeping us at school?
# [Miss Georgette]…Touché Eclair, touché. Now off with you. Scat!



#Day 1, Eating lunch at school
#Interior, Lunch room

# [Maxwell]Eclair, over here!

# [Fiona]I am not wasting my time eating at the kid’s table.
# [Maxwell]What is with her all the time? She’s always in such a foul mood.
# [Eclair]I don’t think science has figured out what’s wrong with Fiona. If someone did, they’d get some kind of Nobel Prize.
# [Maxwell]And what’s with her fixation on calling people immature and babies and stuff? Are those the best insults she can come up with? How would that hurt anybody’s feelings past Kindergarten?
# [Eclair]*Shrugs* Who knows? Fiona’s always been that way as far as I can remember.
# [Mishelle]Who knows?\i Ooooh\i , maybe that’s why she’s always calling us babies! Maybe she knows!
# [Vince]Mishelle…
# [Maxwell]Knows about what?
# [Eclair]Don’t worry about it. They’re just being stupid, today. So you wanna come along with us and talk to people?
# [Maxwell]Nah, I’m just gonna ask my dad. I heard him and my big brother talking about “Career Day” before he left for college. This is kind of a tradition.
# [Eclair]So what are you going to do?
# [Maxwell]Same thing, my brother did. I’m going to get my dad to give me all the answers. All the adults on the island had to do the same thing when they were our age and they know how this place runs.
# [Maxwell]I’ll just get all the answer from my Pops. You guys should just go talk with your parents, too.
# [Eclair]Nope.
# [Vince]No.
# [Mishelle]Uh-uh.
# [Maxwell]*Shrug* Suit yourselves. I’ll be hanging out on my dad’s farm if you guys happen to come by.
# [Eclair]Whelp, let’s get this over with.

#The Gang exits the school.

# .d8888.  .d8b.  db    db d88888b d8888b. .d8888.   .d888b.    .d8888.  .d8b.  db    db d88888b d8888b. .d8888.
# 88'  YP d8' `8b `8b  d8' 88'     88  `8D 88'  YP   8P   8D    88'  YP d8' `8b `8b  d8' 88'     88  `8D 88'  YP
# `8bo.   88ooo88  `8bd8'  88ooooo 88oobY' `8bo.     `Vb d8'    `8bo.   88ooo88  `8bd8'  88ooooo 88oobY' `8bo.
#   `Y8b. 88~~~88    88    88~~~~~ 88`8b     `Y8b.    d88C dD     `Y8b. 88~~~88    88    88~~~~~ 88`8b     `Y8b.
# db   8D 88   88    88    88.     88 `88. db   8D   C8' d8D    db   8D 88   88    88    88.     88 `88. db   8D
# `8888Y' YP   YP    YP    Y88888P 88   YD `8888Y'   `888P Yb   `8888Y' YP   YP    YP    Y88888P 88   YD `8888Y'

# Sayers & Sayers, General Store, Store

label sayersStore:

    if storeComplete == false:

        #Day 1, The General store
        #Interior, General store

        # [Peter Sayers]Well, well, well.  What a pleasant surprise!
        # [Missy Sayers]What surprise is that? Oh! I wasn’t expecting any of you to come by till later in the afternoon. Did school let out early?
        # [Eclair]Sort of. Can we ask you guys a few questions?
        # [Peter Sayers]Wait, let me guess…Career Day?
        # [Mishelle and Vince]Yup.
        # [Peter Sayers]Thought so.  Knew it was getting to be that time of year again.
        # [Missy Sayers]What would you like to know, kids?
        # [Eclair]Um…well, what do you do and how do you do it?
        # [Peter Sayers]Well we run this store, obviously!
        # [Missy Sayers]Though that’s harder than it looks.
        # [Eclair]You guys have everything.  How do you manage to do all that?
        # [Missy Sayers]A better way to phrase the question, Eclair.  Well,  we have a lot of help from our IA.
        # [Peter Sayers]Our Integrated Atomizer!
        # [Vince]The thing that I use to adjust my heat?
        # [Peter Sayers]Most every building has an IA, and yes, it does link in with a home’s internal systems, but it does so much more.
        # [Missy Sayers]It’s a virtually bottomless supply cache.  Folks at the docks scan the things that get shipped in…
        # [Peter Sayers]Their IA then breaks it down to the atomic level and transports it to our IA…
        # [Missy Sayers]And then it winds up on our shelves, fully materialized.  No delivery truck needed!
        # [Eclair]Seriously?
        # [Peter Sayers]Quite serious.
        # [Eclair]Holy cow!  I just realized, I’ve never seen a delivery truck, except for movies and T.V.
        # [Missy Sayers]Ahhh youth.  They take everything for granted, don’t they dear?
        # [Peter Sayers]Not observant at all.  Probably wouldn’t notice something if it bit them right on the nose.
        # [Mishelle]Then why have a store at all?  Why not just atomize and transport everything directly to people’s homes?
        # [Missy Sayers]That has more to do with the community’s philosophy, than with our technological capabilities.
        # [Peter Sayers]That, and we have a contract with the dock workers so that they don’t beam our merchandise to other people’s places.
        # [Vince]What philosophy?  I haven’t heard of any philosophy.
        # [Peter Sayers]Well that would be best explained by Mayor Knox. Now get going, you three. We’re not going to sit around answering all of your questions. Go seek more knowledge elsewhere.
        # [Missy Sayers]Oh, Eclair, if you have a minute. *Whispers* Your mother called me earlier today. Thought I might have something to help you with your little bed wetting problem.
        # [Eclair]Et tu, Mrs. Sayer?
        # [Missy Sayers]Would you be a dear and take this package of incontinence briefs home with you to your mother?
        # [Eclair]What’s that, Mrs. Sayer? I…I didn’t get that. I think I hear my mother calling. Gotta go! She wants to ruin my life.  That must be it.
        # [L.R.]Oh come on! Why couldn’t I have pushed the button, then?!  That would have been perfect, right there with the diapers, and everything! Gray haired girl wouldn’t have known what hit her!
        # [C.S.]The timing wasn’t right. According to the manual, in order to manually initiate a sync up, she has to be in a state of great emotional distress when she goes to sleep.  It’s too early, yet. I don’t think this would have done the trick.
        # [L.R.]We have a manual?

        $ storeComplete = true

    else:

        # [Missy Sayers]Oh Eclair, have you decided to bring this package home?

        menu:
            "What to say?"

            "Yes":
                $ pickedUpBriefs = true

                # [Missy Sayers]I’ll just slip it into your backpack, and no one will be any wiser about it.
                # [Missy Sayers]I know this isn’t easy for you, but you’re being very mature about it. And don’t worry about a thing. What you buy in this store is your business and no one elses.
                # [Eclair] Promise?
                # [Missy Sayers]Cross my heart. *To Mr.Sayers* Hey honey! I win the bet! She took ‘em! Now we don’t have to refund Marna and give her an extra pack, free!
                # [Eclair]Kill me now.

            "No":

                # [Missy Sayers]Well, I suppose I can’t force you to...


    #Talking to Peter Sayers after getting the briefs

    # [Peter Sayers]So embarrassed by the silliest things… When you grow up a little, this whole bed wetting thing will seem like nothing in comparison.




# d8888b.  .d88b.  db      d888888b  .o88b. d88888b .88b  d88.  .d8b.  d8b   db   d8888b.  .d88b.  d8b   db  .d8b.  db      d8888b.
# 88  `8D .8P  Y8. 88        `88'   d8P  Y8 88'     88'YbdP`88 d8' `8b 888o  88   88  `8D .8P  Y8. 888o  88 d8' `8b 88      88  `8D
# 88oodD' 88    88 88         88    8P      88ooooo 88  88  88 88ooo88 88V8o 88   88oobY' 88    88 88V8o 88 88ooo88 88      88   88
# 88~~~   88    88 88         88    8b      88~~~~~ 88  88  88 88~~~88 88 V8o88   88`8b   88    88 88 V8o88 88~~~88 88      88   88
# 88      `8b  d8' 88booo.   .88.   Y8b  d8 88.     88  88  88 88   88 88  V888   88 `88. `8b  d8' 88  V888 88   88 88booo. 88  .8D
# 88       `Y88P'  Y88888P Y888888P  `Y88P' Y88888P YP  YP  YP YP   YP VP   V8P   88   YD  `Y88P'  VP   V8P YP   YP Y88888P Y8888D'

#Policeman Ronald

# [Ronald]Hey, gang.  Skipping school, or Career Day?
# [Eclair]Career Day.
# [Ronald]I suspected as much. You three never were ones to misbehave, even when you were little. Can’t say the same for Fiona, though. So…you’ve got questions. I’ve got answers. Go on and ask them.
# [Eclair]So you’re a cop, right?
# [Ronald]I am a police officer, yeah.
# [Eclair]How come there’s no jail, or police station?
# [Ronald]*Shrugs* Not enough crime. I mostly just make sure things are safe for the little tykes.  Enforce curfew, make sure things are up to code and that people don’t litter and whatnot. Hold that thought.. ‘Scuse me.
# [Ronald]Now I know they have their teacher’s permission to be out here, but you, young man, are clearly too young for Career Day. You’re skipping school. *Huff* Kids. You’ve gotta keep them under control or everything goes crazy. *To Eclair* Any other questions?
# [Eclair]Why is there so little crime?
# [Ronald]I guess it’s because we have good people here, mainly.  That and with no jail, the most severe punishment is getting kicked off the island. Most people don’t ever want to leave this place.
# [Mishelle]Yeah, but everybody leaves the island at some point. Or is there a Police Academy here that we don’t know about?
# [Ronald]True. But everybody who leaves to go see the outside world always comes back when they realize how good they’ve got it here. Anything else?
# [Vince]Nope.
# [Ronald]Well then, if you’ll excuse me, this little stinker needs to get back to Kindergarten.
# [L.R.]Now?
# [C.S.]Still too early.
# [L.R.]Oh come on! A cop! And a little kid! Bam! Double whammy!
# [C.S.]Not yet. Give it time.
# [L.R.]I’ll give you time. Harumph.


#  .d88b.  d8888b. .d8888. d88888b d8888b. db    db  .d8b.  d888888b  .d88b.  d8888b. db    db
# .8P  Y8. 88  `8D 88'  YP 88'     88  `8D 88    88 d8' `8b `~~88~~' .8P  Y8. 88  `8D `8b  d8'
# 88    88 88oooY' `8bo.   88ooooo 88oobY' Y8    8P 88ooo88    88    88    88 88oobY'  `8bd8'
# 88    88 88~~~b.   `Y8b. 88~~~~~ 88`8b   `8b  d8' 88~~~88    88    88    88 88`8b      88
# `8b  d8' 88   8D db   8D 88.     88 `88.  `8bd8'  88   88    88    `8b  d8' 88 `88.    88
#  `Y88P'  Y8888P' `8888Y' Y88888P 88   YD    YP    YP   YP    YP     `Y88P'  88   YD    YP

label observatory:

    #Day 1, Visiting Karlton before the Mayor
    #Interior, Laboratory
    if mayorComplete == false:

        # [Karlton]Let’s see…if you bounce the graviton particle beam off the main reflector dish... Then I might be able to stop the containment leak in the asymmetrical phaser sensors…but that would crumple the dorsal parabolic resonance engine.
        # [Eclair]Hello? Karlton?
        # [Karlton]BWAH! By everything that is Science, don’t sneak up on me! I’m working on something very delicate here.
        # [Eclair]Would you mind answering some questions for us for Career Day
        # [Karlton]Career Day? Don’t be silly. It’s not Career Day. Mayor Knox would have told me so. Now please, make yourselves scarce.
        # [Mishelle]Well, it’s not like we would get much out of Karlton that we could understand anyway.
        # [Vince]Yeah, Karlton is either a genius or a nut.
        # [Mishelle]Can’t he be both?

    else:

        # [Karlton]That should do it. Now if only I can get the quantum manifold to align properly with the focusing lenses. Oh wait!  I’ve got a paperclip! That should do the trick!
        # [Karlton]Turns around, holding a pair of goggles in the air* BEHOLD! SCIENCE! BWAH! By flubber, what are you kids doing here?!
        # [Eclair]Um…Career Day?
        # [Karlton]Career Day? Now you’re just being silly. Career Day isn’t for a couple of weeks yet. Mayor Knox would tell me if it was Career Day.
        # [Eclair]Um…Mayor Knox told us to tell you that it was Career Day.
        # [Karlton]... ... ... OH MY SAGAN! IT’S CAREER DAY ALREADY! Umm… Oh yes, questions! Questions! You must have questions for me. What questions can I answer for you?
        # [Mishelle]Well…what do you do exactly?
        # [Karlton]What do I do? What do I do?! What do I do? Oh yes! Well, as Chief Scientist, my primary job is the maintenance, upkeep, and in some rare instances, the upgrading of technology here on the island.
        # [Vince]Maintenance? Upkeep? So you’re basically just a high-tech janitor?
        # [Eclair]Vince! Cut it out.
        # [Karlton]Young man, I know more about this island than anyone alive. Only Doctor Harkness Milner himself could rival my knowledge.
        # [Vince]My brother works in the library. All he does is read. I bet he could give you a run for your money.
        # [Karlton]Derek is a fine young man, Vincent, but he’s no me. I invent things.
        # [Mishelle]Like what?
        # [Karlton]Like these babies! Oh! Oh….ooooooooooh. Still got some bugs to work out.
        # [Vince]Inventor, eh?
        # [Karlton]Even if my inventions still have some fine tuning yet to do, I am also the primary physician as well.
        # [Eclair]But we’ve never even been sick.
        # [Karlton]Well that’s probably because of all the immunity boosters and vaccines that are in the drinking water and food.
        # [Eclair]Seriously?
        # [Karlton]Completely and utterly.
        # [Mishelle]And that’s not normal?
        # [Karlton]For us it is.
        # [Eclair]Does the rest of the world still poke people with diseased needles?
        # [Karlton]Oh Logic, no. Most vaccinations are done with hypo-sprays and inhalants. Humanity has come a long way from scratching the skin with cowpox needles and the like. We’re just a little ahead of the curve and put it into our food.
        # [Vince]Not to be rude, but that makes you a medical doctor how?
        # [Karlton]Well I do have a near encyclopedic knowledge of everyone on the islands’ medical conditions. For example, all three of you have chronic nocturnal enuresis.
        # [Vince]...
        # [Mishelle]EEEEEP!
        # [Eclair]Seriously?! What is with you guys today?
        # [Karlton]Not to worry children, we still have doctor patient confidentiality. No one needs to know who doesn’t already.
        # [Eclair]New topic- What about the power? Why isn’t there a power plant?
        # [Karlton]*snorts* Oh that’s quite simple, really. The roof on every building is actually a very sophisticated solar panel.
        # [Eclair]But they don’t look like the solar panels in our science books.
        # [Karlton]I said they were sophisticated, didn’t I? Now children, I really have to get back to work on fixing my…uh… invention here. The mayor is waiting on this. Go bother some other adult.
        # [L.R.]Now?
        # [C.S.]I said not yet! Do you want all of that sensitive equipment to get peed on?
        # [L.R.]…Kinda….

        $ observatoryComplete = true

#Developer note: Is Karlton lying about the solar panels, is the island running on another source of power? Or was the original Perp. Change devs too lazy to edit the tileset to have solar panels on the houses?

# d8888b. d88888b  .d8b.   .o88b. db   db
# 88  `8D 88'     d8' `8b d8P  Y8 88   88
# 88oooY' 88ooooo 88ooo88 8P      88ooo88
# 88~~~b. 88~~~~~ 88~~~88 8b      88~~~88
# 88   8D 88.     88   88 Y8b  d8 88   88
# Y8888P' Y88888P YP   YP  `Y88P' YP   YP

#Day 1, Taking a break at the beach
#Exterior, Beach

# [Mishelle]Hey! Let’s take a break and go for a swim!
# [Vince]I could go for a dip.
# [Eclair]Sure, might as well. We can take a break as long as we make sure to get the work done. Let’s go get changed.

# [Mishelle]This is the life!  I’ll miss this when I’m off at college.
# [Vince]After this morning, I needed this.
# [L.R.]They’re just swimming! Swimming! That’s what this has come to. This was supposed to be a good day for us. That’s it! I’m done waiting! I’mma pushin’ the button!
# [C.S.]No, you idiot!
# [C.S.]All you did was make them pee in the ocean.
# [L.R.]….Yeah….I goofed on that one.
# [C.S.]Next time, wait for my signal. We’re not going to get many chances to fix this.
# [Eclair]Did you guys feel that?
# [Mishelle]Feel what?
# [Vince]The water’s a little warmer all of a sudden, but that’s about it.
# [Eclair]No.That’s not what I’m talking about. It was kind of like a wave or something.
# [Mishelle]Uh…we’re in the ocean.
# [Eclair]No I mean a different kind of wave. Like a soundwave or something, like when you stand too close to a stereo speaker.
# [Vince]I didn’t hear anything.
# [Mishelle]Me neither.
# [Eclair]It felt so close though. Never mind, I guess. Maybe it’s just me.

# [Vince]Alright, that’s enough of that. Back to work.

#  .o88b.  .d8b.  db    db d88888b .d8888.
# d8P  Y8 d8' `8b 88    88 88'     88'  YP
# 8P      88ooo88 Y8    8P 88ooooo `8bo.
# 8b      88~~~88 `8b  d8' 88~~~~~   `Y8b.
# Y8b  d8 88   88  `8bd8'  88.     db   8D
#  `Y88P' YP   YP    YP    Y88888P `8888Y'

#Caves

label caves:

    if grannyComplete == false:

        # [Ranger Michael]Whoah! Hold on, scouts! You’re not planning on
        # going to the abandoned mine are you?
        # [Eclair]That depends. Would you say “okay” if we said “yes”?
        # [Ranger Michael]Sorry guys, that’s a no go. It’s too dangerous there.
        # That whole place is prone to cave-ins. That’s why
        # they closed it.
        # [Mishelle]That’s fine. We’re just trying to get to know about the
        # island a little bit for Career Day.
        # [Ranger Michael]Career Day? Why didn’t you say so?
        # [Vince]Does that mean we can check out the mines?
        # [Ranger Michael]Nope! But I can sure as heck educate you about my
        # job and the island!
        # Would you guys like to know about the life cycle and
        # migration habits of the ruby throated blue bellied
        # swallow?!
        # [Eclair]Um…doesn’t Granny Vincenza live somewhere
        # around here? I…I think I hear her calling.
        # [Ranger Michael]Granny Vincenza? Great idea! I bet she has all sorts of stories
        # about the mine. That’s a good safe way to learn
        # about it.

    else:

        # [Ranger Michael]Hey there, scouts. Remember, no going in the mine.
        # [Eclair]We weren’t even going to mention it, sir.
        # [Ranger Michael]Good. Have you three seen Carmella around?
        # [Vince]Maxwell Hanners’s sister?
        # [Ranger Michael]She was here just a minute ago…
        # [Granny Vicenza]Mikey!
        # [Ranger Michael]It’s Michael, now, Granny; Ranger Michael.
        # [Granny Vicenza]Oh how forgetful of me, you’re right. Ranger Michael, I believe I saw a gopher tortoise laying its eggs over yonder.
        # [Granny Vicenza]Would you mind accompanying me to the site of the blessed event and tell me alllll about gopher tortoises?
        # [Ranger Michael]Would I? Ahem, I mean, of course Granny Vincenza.  I’d be happy to educate you about the gopher tortoise.
        # [Ranger Michael]You three stay out of trouble. And if you see Carmella, tell her she better not be setting up one of her pranks at the mines.
        # [Eclair]Yes sir!
        # [Mishelle]You got it!
        # [Vince]*mutters* I can’t believe that worked.
        # [Ranger Michael]What was that?
        # [Vince]I said “Of course, sir!”
        # [Mishelle]Hey is that Ranger Michael’s house?
        # [Vince]They do not pay that guy nearly enough for living out here.
        # [Mishelle]Just look at it.
        # [Vince]More importantly, look at that crane.
        # [Eclair]It’s ancient.
        # [Mishelle]Older than the internet, even.
        # [Vince]What’s even holding it together?
        # [Mishelle]I have no idea.
        # [Eclair]So, are we going inside the mine or what?
        # [Mishelle]Sure, this could be pretty cool.

#Interior, Caves

# [Eclair]So, this is it.
# [Vince]Yup. It’s abandoned alright.
# [Mishelle]Ewww…this is more like a cave than a mine. Look there’s mushrooms growing everywhere.
# [Eclair]Let’s check it out. Maybe we’ll find what Dr. Milner found all those years ago that caused him to shut the mine down.

# [Vince]What in the world were they mining for? I don’t see even a trace of any precious mineral.

# [Eclair]Hey guys! Over here! I think I found something!
# [Eclair]Look at this back wall. It’s not made of rock like the rest of this place. It’s made of metal. And look, something is carved into it. It’s…it’s a mural.

# The Mural is drawn crudely with stick figures and is made up of three sections. The first section depicts a small stick figure on all fours, crawling.
# Then as your eye travels to the right, the stick figures are standing and becoming successively bigger.
# Up in the right hand corner of the first panel is a circle with lines coming out of it. A sun perhaps. Inside the circle is another stick figure.
# The Middle Section shows two stick figures. One is significantly taller than the other. The tall one’s arms  and legs are too long and are disproportionate compared to the shorter stick figure. The sun is directly overhead. There is no man inside it now.
# The Final Section depicts the sun, once again with this longer, lankier stick man inside it. The other stick man is crawling again, surrounded by smaller crawling stick figures on either side.

# [Eclair]What do you think?
# [Vince]I think it’s graffiti.
# [Mishelle]No way, how do you carve graffiti?
# [Eclair]Besides, touch it. It’s humming.
# [VOICE]\bWHO DOUBTS MY POWERRRRR?!\b
# [Eclair]EEEEK!
# [Vince]Yikes!
# [Mishelle]Mama!
# [C.S.]Now! Press it now!
# [L.R.]Nope.
# [C.S.]You’re joking. Now you don’t want to pull the trigger on this?
# [L.R.]Trust me. It’s not the right time.
# [VOICE]\bYOU SHALL BE CURSED! ALL THREE OF YOU! CURSED I SAY! CURSED!\b
# [Eclair]Wait, I know that voice.
# [Carmella]Dang, the acoustics in this place are awesome!
# [Vince]Carmella! What’s the big idea?!
# [Mishelle]I almost wet myself, there, for a second.
# [Carmella]Hee hee…sorry guys…hee hee..I just couldn’t..heh… resist. It was too perfect. Are you okay? I hope I didn’t scare you too bad.
# [Mishelle]*slightly embarrassed* Yeah.
# [Vince]*annoyed* I guess.
# [Eclair]Carmella, what are you doing here? You should be back at school. You’re a year behind us.
# [Carmella]What, you’re the only ones who get a day off?
# [Eclair]This isn’t a day off for us, we have to go and talk to people and ask them about their jobs. It’s called Career Day.
# [Carmella]*Yawns* Sounds a little dull; not duller than school, but still dull. Exploring these mines was way more interesting. And I got to run into you guys. Hey where’s my sister?
# [Mishelle]She went back to your farm to just get all the answers from your dad.
# [Carmella]Figures Maxwell would be loafing around getting the easy answers from Dad. She’s such a disappointment. So lazy sometimes.
# [Vince]Uh...Carmella, you’re skipping school.
# [Carmella]*Smirk* So? It takes a lot more effort to come out here than it does to just go home.
# [Ranger Michael]Is that so? Didn’t I warn you kids to stay away from this place? It’s not safe.
# [Carmella]So busted.
# [Eclair]We were…just looking for bats. Nope, no bats here.
# [Mishelle]Hey Ranger Michael, how would we know if bats lived here?
# [Ranger Michael]Well first you’d want to check for signs of guano. Bats tend to leave a lot of…Now wait a minute! Don’t you go trying to change the subject. Besides, I already looked for bats a long time ago. EVERYONE! OUTSIDE! NOW!



# [Ranger Michael]Now don’t let me catch you three again. I’m giving you pass because it’s Career Day.
# [Eclair, Mishelle, Vince]Thanks!
# [Carmella]You’re great, Ranger Michael! Thanks for your understanding.
# [Ranger Michael]Now hold it right there, young lady… I did not excuse you.
# [Carmella]So busted.
# [Ranger Michael]We’re gonna have a looooong talk, unless you want me to have an equally long talk with your father.

#Day 1, The mayors office
#Interior, Mayors office ground floor

#Trying to enter without ???

# [Secretary]Sorry, kids. I’m on coffee break. I can’t buzz the Mayor for you.
# [Mishelle]But you’re not drinking coffee.
# [Secretary]The coffee maker…broke. And I can’t reasonably be expected to get back to work without my coffee!

# [Secretary]Can I help you?
# [Eclair]Can we speak to Mayor Knox, please?
# [Secretary]Concerning?
# [Vince]Career Day.
# [Secretary]Ah, go on ahead.

#Entering the harbor

# [Vince]I’m sitting this one out, guys.
# [Mishelle]Awwww, why?
# [Vince]My dad’s the foreman. I don’t want to bother him.
# [Mishelle]Is this because you wet the bed this morning?
# [Vince]Mishelle…
# [Mishelle]No wait, that happens to us every morning. Was it because you forgot to clean up after yourself and now your room ?
# [Vince]Mishelle…
# [Mishelle]Do you think he’ll talk about punishing you or making you wear diapers in public?
# [Vince]Mishelle!
# [Mishelle]I don’t mean he’d make you wear diapers in public, just that he might talk about making you wear one to bed in public.
# [Vince]MISHELLE! Take a hint! Now’s not the time!
# [Mishelle]Okay! Okay! Sorry! It’s just that all our parents are overreacting about this bed wetting thing, right Eclair?
# [Eclair]Don’t bring me into this. I have no idea what you’re talking about.
# [Vince]Denial much?
# [Eclair]You wanna go talk to your Dad with us?
# [Vince]You know I don’t.
# [Eclair]So who is denying what?
# [Vince]You got me there. Just go on without me.
# [Mishelle]Okay. Be right back.

#Talking to Vince before talking with Pietr

# [Vince]I'm not going anywhere, I’ll just be waiting here. Come back and see me when you're done.

# [Pietr]Where’s Vince?
# [Eclair]He’s…busy.
# [Pietr]Uh-huh.
# [Eclair]You don’t believe me, do you?
# [Pietr]He’ll talk to me when he’s ready. What can I do for you ladies?
# [Mishelle]It’s Career Day. Would you mind telling us about your job?
# [Pietr]*Nods* That’s no problem. The Harbor is the lifeblood of Farazon. It brings tourists and their money to our little slice of paradise.
# [Pietr]Whatever we can’t make or provide for ourselves, we trade with the Mainland. Simple as that.
# [Eclair]That’s it?
# [Pietr]Well there’s some complicated stuff involving transport,  but the idea is simple. That’s what’s great about this place. Simple concepts with advanced executions.
# [Mishelle]Ooooh I like that. Maybe we can work that into our report.
# [Pietr]Thank you. What did you say your name was, again?
# [Mishelle]Mishelle.
# [Pietr]Oh…THAT Mishelle?
# [Mishelle]What do you mean?
# [Pietr]Nevermind. It’s not my place to say. Vince will talk to you when he’s ready, too.
# [Pietr]When you see Vince, tell him I’ll see him when I get home.
# [Eclair]Oh, he’s not-
# [Pietr]*shakes head* Just tell him I’ll see him. That’s all. No need to hide nothin’

# [Vince]So…how’s my dad?
# [Eclair]Stoic. Kind of matter of fact.
# [Vince]So, the usual.
# [Mishelle]Hey, Vince?
# [Vince]Yeah?
# [Mishelle]What did your dad mean when he said that I was THAT Mishelle?
# [Vince]*Gulps* He said that?
# [Eclair]Hehehe…yup.
# [Vince]Mishelle. I am so embarassed.
# [Mishelle]Why? It’s okay if you talk to other Mishelles. I just thought I was the only Mishelle you knew.
# [Vince]*sweating* I’ve…got a pen pal.
# [Eclair]Oh Mishelle. When are you ever going to learn to take a hint?
# [Vince]Eclair…please.
# [Eclair]Okay, buddy! Okay! I can take a hint.
# [Mishelle]Yeah! Wait, what?

#Day 1, Visiting valerie for career day
#Exterior, Nursery

# [Fiona]Oh, looks like you little kids finally figured out where you belong.
# [Eclair]Look who’s talking. You just walked out of the nursery, yourself.
# [Fiona]I was applying for an internship this summer, for your information. I’m using this Career Day thing to actually get information about potential careers. Some of us plan ahead for the future.
# [Vince]You insult people by calling them immature little kids, and you want to work in childcare?
# [Mishelle]That doesn’t add up at all.
# [Fiona]*Sighs* It’s fine for people to be irresponsible little babies when they’re the right age. Then it’s not being immature because that’s how they’re supposed to act. Duh! Now out of my way. I’ve got connections to make.
# [Eclair]I just don’t get her.
# [Eclair]Hmmm, what’s this?There's a sign on the door. It Says: “No Video Recording Devices or Photography allowed on the premises. THIS MEANS YOU.”
# [Mishelle]I wonder why that is.
# [Vince]Let’s go ask.
# [Eclair]I forgot my phone at home anyways.

#Interior, Nursery

# [Valerie]\mOh! Eclair! Mishelle! Vincent!  Is that you?
# [Eclair, Mishelle and Vince]Yes Miss V.
# [Valerie]*Giggles* Oh, you don’t have to call me that. You’re practically all grown up, now. You can call me Valerie. What brings you three here?
# [Eclair]Okay, Valerie. We’re doing our Career Day assignment to find out more about the town.
# [Mishelle]So we can appreciate it more when we go to college on the mainland.
# [Valerie]Oh my, it’s your Career Day already? It seems like just yesterday that I was doing an internship here and you three were all crawling and toddling around. And now, here you are, back again.
# [Vince]You were an intern here?  I thought you always ran the nursery.
# [Valerie]Oh, I’ve been working here a long time, now, but I’m not THAT old.  Though I feel it right now with you three all but grown.
# [Eclair]Do you mind doing us one last favor, and teaching us a bit about your job?
# [Valerie]Sure, just a second.

#Music changes to lullaby

# [Valerie]Right to sleep. Works every time. Okie dokie, what do you want to know?
# [Vince]Well, where did you go to learn how to take care of little kids?
# [Valerie]Right here during my internship.
# [Mishelle]You mean you didn’t leave Farzon?
# [Valerie]*Shrugs* Didn’t have to.  I’m one of the few who’s never left the island. I grew up, took an internship, and fell in love with this place. And now, here I am.
# [Eclair]Who ran the nursery before you?
# [Valerie]Hmm…that’s odd. I can’t quite seem to remember. I guess I’ve been doing this job for a long time, after all. *Shrugs*
# [Vince]Weird. Me neither.
# [Eclair]But if Valerie started working here when she was our age, you’d think one of us would remember who ran the place before her.
# [Mishelle]To be fair, we were all really little.
# [Valerie]They must have not done as good a job as me, and that’s why they’re so forgettable.
# [Eclair]Do you always watch all of the babies by yourself?
# [Valerie]No, not always. Today’s a bit of an odd day, really. I normally have some part timers and assistants and at least one intern; but they all called out sick today.
# [Vince]Is there anything that’s noteworthy about the town that we don’t know about or we take for granted?
# [Valerie]Not that I can think of, really.
# [Mishelle]What about the diapers?
# [Valerie]...What about them?
# [Eclair]Can we please not talk about diapers, right now? It’s
# been a weird enough day.
# [Mishelle]No, I mean babies are messy and make a lot of
# garbage. Just imagine all the diapers that Miss V…. I mean Valerie has to change in one day. But it doesn’t smell that bad in here, and we don’t have a garbage dump.
# [Vince]Oh yeah!  I never thought of it that way.
# [Valerie]Oh, you don’t know about the I.A.’s? The Integrated Atomizers?
# [Eclair]What about them?
# [Valerie]They’re our garbage disposal system. We just atomize and disintegrate anything that’s garbage, and release the basic component atoms back into the air.
# [Mishelle]You mean we’re breathing in garbage?
# [Valerie]Is it really garbage if it’s all been turned back into carbon and various gases? Also, the forest works fine as a natural air filter.
# [Eclair]Hmm…that’s kind of neat.  Well, you’re kind of busy, so we’ll let you be.
# [Valerie]Thanks. I need to rest while the little ones are napping. It’s the only break I’m likely to have.
# [L.R.]Now?
# [C.S.]No. Not now. That might cause things to go overboard.
# [L.R.]Oh come on!  It’d be like poetic justice to do it here!
# [C.S.]Do you even know the meaning of the word “patience”?
# [L.R.]Yeah. Sick people who go to the doctor.
# [C.S.]I am never working with you again after this.

# [Valerie]Interested in applying for an internship?
# [Eclair]Thanks, but no.
# [Valerie]Fair enough.  Come back soon!
# [Eclair]No problem!

#Wetting scene

# [Eclair]I’ll go place them in my desk.They’ll be here for tomorrow.
# [L.R.]Almost time.
# [C.S.]What are you talking about? This won’t be traumatic enough to induce regression. There’s no one around but them!
# [L.R.]Just wait for it. If regression were an Olympic sport, I’d get the gold medal.
# [Fiona]Well, looks like it took all three of you immature little brats all day to accomplish almost the same amount of work as yours truly.
# [Eclair]Get over yourself, Fiona. You did Career day by yourself because you don’t have any friends.
# [Fiona]Pffft. Sticks and stones, kids. Sticks and stones.
# [Mishelle]Um…shouldn’t we be saying that to you? Since you’re the ones insulting us?
# [Fiona]It’s not an insult if it’s the truth, babies.
# [Vince]So we’re not insulting you when we say that nobody likes you.
# [Eclair]Yeah, that much if pretty evident. Meanwhile, none of us are-
# [L.R.]NOW!

#Show that picture, you know the one

# [Eclair]...
# [Mishelle]...
# [Vince]...
# [Fiona]Oh! My! Gosh! Best! Day! Ever!
# [Mishelle]I…
# [Vince]…Need…
# [Mishelle]…To…
# [Vince]…Go!
# [Fiona]I thought they already did! Haha! This is too rich. Looks like they went to go get their diapers changed! I can’t wait to tell everyone! Buh-bye baby-kins!
# [C.S.]Right in front of the school bully. Niiiiice.
# [L.R.]Yep, I still got it.
# [C.S.]I tip my hat to you.
# [L.R.]You’re not wearing a hat.
# [C.S.]It’s a metaphor…
# [L.R.]A meta-for what?
# [C.S.]…Don’t have kids.
# [Eclair]Oh God! This can’t be happening! This is all just a nightmare and I’ll be waking up any second now.
# [Eclair]...
# [Eclair]Crap. What do I do now?
# [Eclair]What do I do? I’ve gotta get home, but I can’t show up like this. But the only thing I have that’s dry are these. Is it better to show up in wet pants, or a dry diaper?

    if pickedUpBriefs == false:

        # [Eclair]No choice. Just gotta get home and hope Mom won’t
        # be mad.

    else:

        menu:
            "Change into the Incontinence Briefs?"

            "Yes":
                $ putOnBriefs = true

            "No":


    ecl "This is going to suck."

#Day 1, Eclair comes home

    if pickedUpBriefs == false:

        # [Marna]Eclair?
        # [Eclair]Hi...
        # [Marna]…
        # [Marna]You’re soaking wet.
        # [Eclair]I know.
        # [Marna]And not from the rain.
        # [Eclair]Yeah. I know.
        # [Marna]You peed your pants.
        # [Eclair]Yeah.
        # [Marna]And you walked all the way home in them?
        # [Eclair]Yes, ma’am.
        # [Marna]What about the supplies I asked you to pick up? Why didn’t you change into those?
        # [Eclair]I didn’t want to pick them up.
        # [Marna]*Sigh* I know. Mrs. Sayers phoned me after you left the store. Which is why I went and got some myself. I am very disappointed in you, young lady. You’re going to learn to get over your pride the HARD WAY.

        #Change to spanking picture

        # [Eclair]Mom! Don’t!
        # [Marna]I don’t want to hear it!
        # [Eclair]Oooch!
        # [Eclair]Ouch!
        # [Eclair]OOOCH!
        # [Eclair]OW!
        # [Marna]If you won’t take care of yourself like a grown woman, then I’ll just have to take care of you. LEGS UP!
        # [Eclair]*Sniff* I’m sorry!
        # [Marna]Now hold still!
        # [Eclair]EEEEP! Cold! Cold! Cold!
        # [Marna]Quit wriggling, or so help me…!
        # [Eclair]Okay, okay! Sorry! I couldn’t help it.
        # [Marna]Now hold still while I tape you up. *Huff* Never thought I’d have to do THAT again. Now come on. Your dinner’s getting cold.
        # [Eclair]Mom, wait! I can explain!
        # [Marna]Honestly, Eclair. I’m disappointed in you.
        # [Eclair]I don’t know what happened. One minute we were fine, and then we all peed ourselves.
        # [Marna]That’s not what I’m talking about. If Missy Sayers hadn’t called me to tell me about your “I hear my mother calling” stunt, you’d be out of a product you need.
        # [Eclair]But I don’t -!
        # [Marna]You walked home in wet pants!
        # [Eclair]I’m not a baby!
        # [Marna]Oh really? If a baby wet their pants, would they take care of it themselves, or would they crawl around in wet pants until a grown up helped them?
        # [Eclair]...
        # [Marna]Would an adult refuse to do a simple errand?
        # [Eclair]...
        # [Marna]You’re not immature because you have a weak bladder and had an accident. You’re immature because you shirked your responsibility and did nothing to help fix it, yourself.
        # [Marna]Bad things are going to happen to you as you grow up. How you deal with them is what makes you mature or not.
        # [Marna]You have to have change the things you can, accept the things you can’t, and have the wisdom to know the difference.
        # [Eclair]...Hmmph
        # [Marna]What’s going to happen to you when you wet the bed at college? Are you just goijng to let the sheets soak until someone else changes them for you?
        # [Eclair]I! DO! NOT! WET! THE! BED!
        # [Marna]Eclair...
        # [Eclair]Sorry.
        # [Marna]I think it’s time for you to go to bed.
        # [Eclair]Yes Mommy.

    elif putOnBriefs == true:

        # [Marna]Eclair?
        # [Eclair]Hi...
        # [Marna]…
        # [Eclair]...
        # [Marna]You’re not wearing any pants.
        # [Eclair]I know…
        # [Marna]Is this because of this morning? Is this some kind of a joke? Or rebellion?
        # [Eclair]Not exactly. I kinda had…an accident.
        # [Marna]Oh you poor thing!
        # [Marna]Here, sit down. I’ve got dinner ready. Tell me all about it.
        # [Marna]All three of you?
        # [Eclair]Yeah. Freaky, huh?
        # [Marna]I’ll say. What are the odds? Do you think you were poisoned?
        # [Eclair]Poisoned?
        # [Marna]Well, you have to admit, it’s an awfully big coincidence that all three of you had accidents at the same time in front of that…that…that BULLY. And you did mention that she was calling you babies before you ate lunch.
        # [Eclair]Huh. That is weird, isn’t it?
        # [Marna]I’d bring it up with Miss Georgette tomorrow, if I were you.
        # [Eclair]Maybe I will.
        # [Marna]Regardless, you were put in a bad situation, and you made the best of it. I’m very proud of you
        # [Eclair]You are?
        # [Marna]Of course, Eclair! That accident couldn’t be helped. That’s why it was an accident. But you just rolled with the punches and took care of the mess you were in. That’s a sign of real maturity.
        # [Eclair]Really?
        # [Marna]Sure. Maturity isn’t about acting “grown-up”. Maturity is changing what you can, accepting what you cannot and having the wisdom to know the difference.
        # [Eclair]Thanks, Mom.
        # [Marna]I just have one question.
        # [Eclair]What?
        # [Marna]Why didn’t you think to go buy new pants?
        # [Eclair]*Blushes* I honestly didn’t think to.
        # [Marna]...
        # [Eclair]...
        # [Marna]Heh-heh.
        # [Eclair]Hee-hee-hee.
        # [Marna]Hahahahahaa!
        # [Eclair]Heh-heh. Eh…heh.
        # [Marna]Oh my! Heh-heh. Oh dear. What am I ever going to do with you, Eclair?
        # [Eclair]I don’t know. Gosh, I was so embarrassed.
        # [Marna]Oh, you’re young yet. This too shall pass. If you want, tomorrow, you can blame me. Say that you did it as a way to try and embarrass me, or as a prank or something.
        # [Eclair]Seriously? You don’t mind being the bad guy?
        # [Marna]Not this time. You’re my daughter. Just because you’ve got a bed wetting problem and a weak bladder doesn’t mean I want you to be publicly humiliated.
        # [Eclair]I do not have a…! *Sigh* Thanks Mom. I’m going to go to bed. It’s been a long and crazy day.
        # [Marna]Oh, and Eclair?
        # [Eclair]Yeah?
        # [Marna]Since you’re already…wearing…maybe you could try going to bed with one on? Just this once? You might like waking up with dry sheets.
        # [Eclair]…! *Huff* Yes, Mother.

    else:

        # [Marna]Eclair?
        # [Eclair]Hi...
        # [Marna]…
        # [Marna]You’re soaking wet.
        # [Eclair]I know.
        # [Marna]And not from the rain.
        # [Eclair]Yeah. I know.
        # [Marna]You peed your pants.
        # [Eclair]Yeah.
        # [Marna]And you walked all the way home in them?
        # [Eclair]Yes, ma’am.
        # [Marna]What about the supplies I asked you to pick up? Why didn’t you change into those?
        # [Eclair]I was embarrassed.
        # [Marna]More embarrassed than walking home with pee-stained pants? If you had been in a clean incontinence brief, you could have at least played it off as a joke? There’s no faking that smell.
        # [Eclair]When you put it that way…
        # [Marna]*Sigh* Come on, honey. This is going to be embarrassing for both of us, but it’s time to get over your fear.
        # [Marna]Lie down, Eclair.
        # [Eclair]Do I have to? I’ve got clean panties here.
        # [Marna]This is to teach you a lesson. We’ll worry about what underwear you wear during the day, tomorrow. Now hold still, and legs up.
        # [Eclair]Wooooo! Cold! Cold! Cold!
        # [Marna]Sorry, hon. Should’ve worn you about the wipes. Now hold still, I’m almost done.
        # [Eclair]Yes ma’am.
        # [Marna]Well, it’s been a while, and it’s a few more tapes than I remember, but I’ve still got it. Now come on. Let’s eat dinner, and you can tell me all about what happened.
        # [Marna]So all three of you peed your pants at the same time?
        # [Eclair]Yes ma’am.
        # [Marna]Hmmm, that’s a little strange, even with all three of your weak bladders. Maybe it was sympathetic. One of you started and then the rest of you started.
        # [Eclair]But-
        # [Marna]Did any of you remember to take frequent bathroom breaks?
        # [Eclair]No, but-
        # [Marna]What about Michelle  and Vincent? Did they have any “just-in-case” clothes?
        # [Eclair]They just ran off.
        # [Marna]*Sighs* Ah you kids. What are you going to do without your parents?
        # [Eclair]Hey!
        # [Marna]I hope you at least go to different colleges on the mainland. You’re all too old for more of your little “soggy slumber parties”.
        # [Eclair]MOM!
        # [Marna]Sorry, dear. *chuckles* Sorry. What I don’t understand is why didn’t you at least put on a brief since you had access to them?  Why were you so embarrassed?
        # [Eclair]Fiona was there. I didn’t want to look like a baby any more than I already did.
        # [Marna]Oh honey, who cares about what Fiona thinks? Do you even like her? You have a genuine medical issue, and you needed a little extra protection. That’s it.
        # [Eclair]Mom, I wet my pants and you’re saying I should’ve just put on a diaper.
        # [Marna]You’re not wearing a diaper. It’s an incontinence brief.
        # [Eclair]You taped this thing on me, and then I heard you say “I’ve still got it.” How much experience do you have changing incontinence briefs?
        # [Marna]I guess I kind of got a little carried away there, didn’t I? It’s hard for parents to see that their children are going up in front of them.
        # [Eclair]But I don’t have…I mean I didn’t before-!
        # [Marna]Now, now. I’m not going to have the same discussion. You can say whatever you want, but that’s not going to change years and years of memoires, is it?
        # [Eclair](This is soooooo frustrating! Why am I the only one who remembers things differently?)
        # [Marna]All I’ll say is this. Maturity isn’t about what you wear or what you look like or what other people think of you. Maturity is being put into a bad situation and handling it with dignity and sense.
        # [Marna]It’s about changing what you can, accepting what you can’t, and being wise enough to know the difference.
        # [Eclair]I guess that makes sense. So it would’ve been more mature of me to put on a dry diaper?
        # [Marna]Almost anything would have been more mature than walking home in wet pants so that everyone could see you. I’ll admit though, that’s a bit of a tough call. At least you were mature enough to run that errand for me, even if it was a little embarrassing for you.
        # [Eclair]Thanks, I guess. So don’t freak out, and keep your cool. Is that why you made me wear one of these… things… to the dinner table?
        # [Marna]That…and I forgot how cute you looked with a padded tushie.
        # [Eclair]Mom!
        # [Marna]Sorry, I just got nostalgic. Seeing you like that reminds me of when you really were little.*Sigh* I should have had another. Oh well, just don’t make me a grandmother anytime soon.
        # [Eclair]No need to worry about that, Mom.
        # [Marna]Okay, off to bed. You’ve had a long day.  You need your rest.
        # [Eclair]Can I at least take this off? I think I’ve learned my lesson.
        # [Marna]I don’t know that you have. Off to bed. We’ll discuss what underwear you’re wearing tomorrow. Keep that on for the time being. No sense in wasting it.
        # [Eclair]Eww!
        # [Marna]Not what I mean. Just wear it tonight, just-in-case.
        # [Eclair]*Huff* Yes ma’am.





#End of day 1
#Interior, Eclairs Bedroom (Day 1 version)

$ diaperToBed = false

menu:
    "You’re about to go to bed for the night. Do you take off your incontinence brief?"

    "Yes":
        ecl "I don’t need this dumb thing. Today was a fluke."

        $ immaturity += 1

    "No":
        ecl "Better not. Today’s been weird enough. I might actually need this."

        $ diaperToBed = true

#Day 1 puzzle

# [L.R.]Alright, just type in some 1’s and some 0’s, maybe a couple of 2’s just for funzies, and this manual sync up will be good and over.
# [C.S.]Well…part over anyways
# [L.R.]What do you mean “part over”?
# [C.S.]This is a delicate process. It takes time.
# [Eclair]Huh?
# [C.S.]Oh no.
# [Eclair]Who said that?


$ puzzleWin = false

# [Eclair]OH MY GOD! WHAT HAPPENED TO MY HOUSE?!
# [L.R.]Hehe…told ya.
# [C.S.]*sigh* Miss, please forgive my co-worker, here. He’s being rather insensitive at the moment.
# [Eclair]WHAT HAPPENED TO MY HOUSE?!
# [C.S.]The thing is…you see…you’re dreaming…this is all a dream.
# [Eclair]…I’m dreaming?
# [L.R.]Yup.
# [Eclair]I’m dreaming about a big empty place right outside of my bedroom and two disembodied voices?
# [L.R.]Oh…we’re not dreams. We’re technicians.
# [C.S.]Technically.
# [Eclair]What are you doing in my dreams, then?
# [C.S.]We’re just syncing up your mind with our high tech computer.
# [Eclair]Why?
# [L.R.]So you’ll like wearing diapers!
# [Eclair]WHAT?!
# [C.S.]Why do you have to ruin everything?
# [L.R.]What? She’s gonna end up wearing them anyways. Might as well tell her the upside.
# [Eclair]What upside could there possibly be to that?
# [L.R.]You’ll…like them…?
# [C.S.]Look Miss, we’re just doing our jobs, here. I’m really sorry we’re disturbing your dreams, but we’ve got to get moving along.
# [Eclair](There’s a computer! Maybe I can use it to stop whatever these two weirdos are trying to do.)
# [L.R.]Ha! That’s a dream computer!  It’s not like interfacing with a dream computer is going to stop us! It just doesn’t work that way!
# [C.S.]Actually, because her brainwaves are being synced up with our computer, that’s exactly how it works.
# [L.R.]Crap! Well no worries. I programmed this subroutine myself. And it’s PRIMED against hacking. Heh-heh. Get it? PRIMED?!


if puzzleWin == true:

# [Mona]There you go! Diaper’s all changed. Now go and play, little one.
# [Eclair]It’s the Nursery. But who’s that? And why does she seem so…familiar?
# [Mona]Oooof…gotta go. Valerie! Where are you? I need some help, here!
# [Valerie]Just a second, boss!
# [Baby]Bwaaah!
# [Mona]I’m…ugh…coming, kiddos. Just a second.
# [Mona]Valerie I need you! Now!
# [Valerie]Just a moment, Mona! I’m coming to relieve you!
# [Mona]*Doing the potty dance*Speaking of relieve….
# [Valerie]Huh?
# [Mona]Just get in here!
# [Mona]Valerie! Please! I can’t wait any…!
# [Mona]Oh my God!
# [Valerie]Here I…am? Oh dear!
# [Mona]I…I…I…
# [Valerie]Mona, are you okay?
# [Mona]I just couldn’t…I just.  I didn’t mean…
# [Valerie]It’s okay, boss. You don’t need to be embarrassed.
# [Mona]I…I don’t?
# [Valerie]I’ve known you for years. It’s no secret that you’ve got a weak bladder. That’s why you’ve got that change of spare clothes in your office.
# [Mona]My spare clothes? Oh…yeah…that’s right. How did I forget about my “just-in-case” clothes?
# [Valerie]You once joked that you had the bladder the size of a three year old and that’s why you were so good at potty training kids. Because you knew exactly how much their bladders could hold.
# [Mona]Oh yes. Of course. I remember that story, now. It seems like forever since I told you that joke.
# [Valerie]*Shrugs* Well, I remembered it. But don’t let me keep you here. I’ve got this under control. Go get changed.
# [Mona]Good idea. I’ll be a few minutes.
# [Valerie]Oh, and Mona.
# [Mona]Yes?
# [Valerie]Do you think maybe you should wear something with a little more…um…protection…just in case?
# [Mona]Maybe you’re right. I’ll see if I can’t order something from the Sayers’ store.
# [COMPUTER]End Memory Download.
# [Eclair]Wait! What was that? Show me more!  Show me more!



# d8888b.  .d8b.  db    db   .d888b.
# 88  `8D d8' `8b `8b  d8'   VP  `8D
# 88   88 88ooo88  `8bd8'       odD'
# 88   88 88~~~88    88       .88'
# 88  .8D 88   88    88      j88.
# Y8888D' YP   YP    YP      888888D

$ skippedSchool = false
$ wetAccident = false
$ messyAccident = false

#Day 2, Eclair wakes up in her bed
#Interior, Eclair's bedroom (Day 2 version).

#If Eclair completes the puzzle

# [Eclair]*Yawn* What a weird dream. I wonder what it means.

if puzzleWin == true:

    if diaperToBed == false:
        ecl "*Looks down at her diaper* What?! Why am I wearing this?! Who could have put it on me? Did mom do this while I was sleeping? At least I’m dry."
    else:
        ecl "*Looks down at her incontinence brief* Hey! I’m dry! How about that?  I guess the bed wetting thing was  just a fluke after all."

    # [Eclair]Wait…why is my room different?
    # [Marna]Good morning! Rise and shine, sleepyhead!
    # [Eclair]EEEEP!
    # [Eclair](I no…I can’t believe I just…I just…)
    # [Marna]Oh good. You’re already up. Well, don’t let me get in your way. Go on and get showered.

else:
    # [Marna]Good morning! Rise and shine, sleepyhead!
    # [Eclair]*Yawn* What a weird dream.
    # [Marna]What kind of dream, sweety?
    # [Eclair]*Yawn* I’m already having trouble remembering. Is
    # that normal?
    # [Marna]Of course dear. Now rise and shine.
    # [Eclair]*Looks down at her bed* Hey! My bed is dry! How
    # about that? I guess the bed wetting thing was just a
    # fluke after all.
    # [Marna]Dry bed? Eclair, dear, what’s the matter with you. You
    # haven’t had a wet bed since before Kindergarten.
    # [Eclair]Finally, someone is making some sense!

    if diaperToBed == false:

        # [Eclair]*Looks down at her diaper* Why am I wearing this?
        # Did…did you?!
        # [Marna]Did I what?
        # [Eclair]Put this on me?
        # [Marna]That must’ve been some dream. You put it on yourself.
        # [Eclair]I did?

    else:

        # [Eclair]*Looks down at her incontinence brief* Oh no. I didn’t, did I?

    # [Marna]Of course you did. You’ve been almost completely urinary incontinent your entire life. It just took us that long for Karlton to diagnose you.
    # [Marna]Before, we just thought you were just slow at potty-training.
    # [Eclair](No! Not more of this craziness!) *Looks around her room* Wait…why is my room different?
    # [Marna]What do you mean, dear?
    # [Eclair]*Huff* Never mind. Mommy…I mean Mom;  How do I get out of this…thing?
    # [Marna]You go to the bathroom, rip off the tapes, and then hop in the shower, of course. Now get going.
    # [Eclair]Oh yeah…duh.
    # [Marna]You’ve been able to change yourself for years, dear. Just because you’ve got a condition, doesn’t mean you’re a baby. Now quit dawdling.
    # [Marna]Honestly, I don’t know how you’re going to manage this when you go away to college.

if puzzleWin == true:

    # []Eclair is about to rip off her incontinence brief as she realizes that the bin is full of used briefs.
    # [Eclair]This isn’t right. There shouldn’t be this many wet diapers. I just started wearing them yesterday. Something is very wrong, here.
    # [L.R]Well….fudge.
    # [C.S]The boss will not be happy about this.
    # [L.R]Assuming the boss finds out.
    # [C.S]Point taken.

else:

    # []Eclair is about to rip off her diaper as she realizes that the bin is full of wet briefs.
    # [Eclair]This isn’t right…I didn’t start wearing these things till yesterday, didn’t I?

    #Shower sfx

    # [Eclair]Ahhhh so good.
    # [L.R]Mission accomplished!
    # [C.S]No thanks to you.

"Eclair notices the pack of diapers on the bathroom floor"

if immaturity >= 4:

    ecl "Okay, the diapers would seem logical if I was having regular accidents but ... I don't have regular accidents,  do I?"

else:

    ecl "A bedwetting accident, and now diapers? I NEED to talk to Mom about this. Something is definitely wrong here."

# [Eclair]Time to get dressed for the day.
# [Eclair]*Huff* MOTHER!
# [Marna]Yes dear?
# [Eclair]Where are my panties?
# [Marna]Panties?
# [Eclair]Yes. My panties. Where are they?
# [Marna]Eclair, honey…You haven’t worn panties since before Kindergarten when we stopped trying to potty training you.
# [Eclair]…..I….whaaaaaaat?
# [Marna]You’re almost entirely urinary incontinent, dear. Karlton diagnosed you years ago. At first we thought you were just slow on potty-training, but then we found that you couldn’t help it.
# [Eclair]...
# [Marna]Are you feeling alright, dear?
# [Eclair]Uh…no…I mean…yeah. Just…just give me a minute, alright?
# [Marna]Of course dear. Breakfast will be ready for you once you’re dressed

# [Eclair]This cannot be the kind of maturity that Mom was talking about.

# [Eclair]Has Mom snapped? Did she like taking care of me so much that she’s babying me, now? Weird.

# [Eclair]Mom must be trying to punish me or something. How’d she manage to sneak in and snatch everything without waking me up?

# [Eclair]Let’s just get this over with.
# [Eclair]Wow, this feels weird. Almost like a maxi pad on
# steroids, or something. Not too bad, I suppose.
# [Eclair]I could do without the sound though. It sounds I’ve got
# a plastic grocery bag in my pockets every time I move.
# [Eclair]Yeeeaaaah…that’s gonna get old reeeeeal quick.

# [L.R.]That’s about the only thing that’s gonna get old as far
# as she’s concerned. Why are we still here again?
# [C.S.]Because we’ve got a job to do.
# [L.R.]Job? What job? She’s in a diaper. Mission accomplished!
# Now get ready to buy me lunch.
# [C.S.]The change isn’t complete yet.
# [L.R.]Heheh….you said “change”.
# [C.S.]Focus! Do you really want to leave this to chance? Do
# you want to risk that this girl might actually…grow up?
# [L.R.]Damn it, you’re right! Let’s do this!
# [C.S.]Now you’re talking!
# [L.R.]Alright! Now, what do we do?
# [C.S.]We watch…and wait…I’ve already got a plan.
# [L.R.]I hate you so much sometimes.

# [Eclair]Mom, we need to talk.
# [Marna]Sit down and eat your cereal, dear before it gets all soggy.
# [Eclair]*Sighs* Fine.
# [Marna]So, what is it you want to talk about dear?
# [Eclair]It’s the…the…
# [Marna]The \iwhat\i, dear?
# [Eclair]The diapers.
# [Marna]Are you almost out?
# [Eclair]What?! No I-
# [Marna]Because you know it’s your responsibility to tell me when you need more. If you want more privacy, then you can’t expect me to go rooting around in your dresser drawers, counting your briefs.
# [Eclair]No Mom, that’s not what I mean!
# [Marna]Well that’s good. The last package I bought from the Sayers’ store was a little thicker than what you usually wear. I thought it might help you if you didn’t have to change as often. They’re not too thick are they?
# [Eclair]Um…I…well…I guess not?
# [Marna]Because I can stop by the Sayers while you’re at school today and get the thinner ones if you’d like. I could just slip them right into your dresser for you.
# [Eclair]First you’re lecturing me about not keeping track of my… of the dia-…of the briefs in my dresser drawer and now you’re offering to go replace them and shove them right into my drawer again!  Which is it?
# [Marna]Oh my goodness, you’re right, dear. I’m sorry, honey. This is just awkward for me.
# [Eclair]This is awkward for \iyou\i?
# [Marna]I know, I know. I was young too, once, believe it or not. Well, you are at that age where you’re not quite an adult, but not quite my little girl anymore.
# [Eclair]Mom, I woke up this morning and my underwear drawer was filled with disposables! There’s a bin in the bathroom filled with balled up wet diapers!
# [Marna]…I’m not sure I see your point.
# [Eclair]Yesterday, I peed my pants, which was weird, but don’t you think replacing all of my panties with adult diapers is a little extreme?
# [Marna]Eclair, what in the world are you talking about?
# [Eclair]Last night!
# [Marna]You mean when you leaked? Honey that’s a little embarrassing, I’ll admit, but you know that sometimes happens. That’s why you always have spare clothes and spare briefs in your backpack.
# [Eclair]Seriously? Is this seriously happening right now?
# [Marna]I promise you, the thicker padding is not a punishment. It was complete coincidence. Though now that you mention it, I am a perturbed that you didn’t have any spares with you at the time. Did you run through them all or did you forget to pack them yesterday?
# [Eclair]Mom, this isn’t making any sense.
# [Marna]We’re going to have to have a looooong talk about responsibility young lady.

#Doorbell sfx

    # [Marna]Oh, it looks like Vincent and Mishelle are here to walk with you to school. Time to get along and get going.  We’ll talk after school.

        if immaturity >= 4:

            # [Eclair]But I don’t wanna go to school! I want to stay here and talk to you! This is weird, Mom!  Really weird!

        else:
            # [Eclair]Mom, something very strange is going on here. Would you please stop and listen for just a second?!

    # [Marna]Here’s your backpack, filled with extra briefs just in case. Try to make it to the toilet if you can, obviously, but don’t feel embarrassed if you don’t make it. That’s why you have protection.

#Door sfx

# [Marna]That girl, sometimes. I don’t know what she would do without me.



#Day 2, Eclair exits her house
#Exterior, Eclair's house

# [Eclair]She locked the door! Mom! Let me in![Eclair]She locked the door! Mom! Let me in!
# [Vince]You okay, Eclair?
# [Eclair]Guys! You can’t tell, can you?
# [Mishelle]Tell what?
# [Eclair]What I’m…I’m…wearing? I mean I know I checked it out this morning, and it didn’t look too bad, but be honest with me: Can you guys tell what I’m wearing?
# [Vince]Is this a trick question?
# [Eclair]I promise you it isn’t.
# [Vince]Okay. Let’s see. Shirt, pants. Sneakers. Nothing seems...
# [Mishelle]Don’t forget the diaper!
# [Eclair]EEEEEP!
# [Vince]MISHELLE!
# [Mishelle]What? We all know she’s wearing them.
# [Vince]Not the point! You know how she’s been lately! Besides, she prefers the term “briefs”, remember?
# [Mishelle]Oh yeah. Sorry Eclair, I meant “briefs”, when I was talking about the diaper.
# [Eclair]Can you see it?! Can you tell?
# [Vince]Pfffttt. Of course not.
# [Eclair]Then how…?
# [Mishelle]Is she serious?
# [Vince]She’s been weird lately.*To Eclair* Look, we’re just going to school. If you want to come, feel free.
# [Eclair](That sound!) Guys! Wait! Now go. STOP!
# [Vince]Eclair, what’s up with you?
# [Mishelle]Yeah, you’re acting even weirder today than you were yesterday.
# [Eclair]Is…is that noise coming from you guys, too?
# [Mishelle]What noise?
# [Eclair]That crinkling noise. Are you guys wearing dia-… wearing incontinence briefs too?
# [Mishelle]Oh my god! How do you still notice that sound?
# [Eclair]How do you NOT notice it?
# [Mishelle]I don’t think I’ve really thought about it in forever. It’s like the humming of a lightbulb. It’s just white noise.
# [Eclair]But that doesn’t make any sense, Mishelle. We weren’t wearing these yesterday.
# [Vince]Okay, this has gotten older than the internet. I’m gone. I’ll see you two at school if you’re coming.
# [Eclair]Wait! Please!
# [Eclair] Guys, I don’t know what’s going on. Everything seems so backwards and out of whack today. And I’ve had the weirdest dreams and everyone seems to remember things differently than I do.
# [Vince]Ugggh…this again. Eclair, you’re the one who’s been acting strangely.
# [Mishelle]Eclair, are you sure you’re okay?
# [Eclair]Just tell me: Why aren’t we wearing regular underwear?
# [Vince]Again?
# [Eclair]Again?
# [Mishelle]We had this same conversation yesterday, remember?
# [Eclair]You mean about the…the soggy slumber parties?
# [Mishelle]And the padded play-dates…
# [Eclair]The padded what now?
# [Vince]*Sighs* And all the other little euphemisms our parents came up with for us playing together because we were all pretty much incontinent.
# [Mishelle]Yeah, that’s kind of how we started being friends. Vince, it’s just us right now. You don’t have to be so cross.
# [Vince]She’s trolling us, Mishelle. She has to be.
# [Eclair]I’m really not, I swear!
# [Vince]Then why are you pretending like we haven’t been like this since we’ve known each other?
# [Mishelle]Yeah, we used to get changed right in front of each other when we were little. Sometimes side by side. Hey Vince, remember how we used to hold hands while our parents were changing us?
# [Vince]Yeah.
# [Eclair]Vince, are you blushing?
# [Mishelle]Oh you know Vince, he’s always been sooooo sensitive about this stuff
# [Vince]Mishelle…
# [Mishelle]Like you ever notice how he never says “I’m gonna go change”. It’s always something like “I’m gonna go stretch my legs.”?
# [Eclair]Um…I don’t actually.
# [Vince]Mishelle…
# [Mishelle]As if everybody doesn’t know. Why else would he need to take his backpack with him when he walks out of class to “stretch his legs”?
# [Eclair]I have no idea-
# [Vince]MISHELLE!
# [Mishelle]Oh! Sorry.
# [Mishelle]See what I mean?
# [Eclair]I am so confused right now.
# [Mishelle]It’s not like it’s a big secret, Eclair. We have a condition. Everyone knows. And everyone is cool with it.
# [Vince]Except Fiona.
# [Mishelle]Well yeah, except for Fiona. She never has let go of that whole “babies” thing, has she? But still, it’s not like it’s a secret or a reason to be embarrassed. I’m willing to bet that at least one of us is at least a little wet right now. Right, Vince?
# [Vince]I’m…gonna go stretch my legs real quick.
# [Mishelle]I honestly think it’s a little harder on him.  It’s hard to be the stoic, macho dude when you’re wearing diapers all your life.
# [Eclair]But he hasn’t…
# [Mishelle]That time in kindergarten doesn’t really count.
# [Eclair]Not what I meant-
# [Mishelle]Though what happened yesterday didn’t help.
# [Eclair]What happened yesterday?
# [Mishelle]With Fiona…?
# [Eclair]You mean the…accident that we all had yesterday?
# [Mishelle]See, you DO remember! How weird is it that all three of us flooded and leaked right there after school at the same time.
# [Eclair]\iVery weird\i.
# [Mishelle]Yeah, and don’t check your internet feeds if you haven’t already. Fiona may have been talking about it to people online last night.
# [Eclair]How many people?
# [Mishelle]Basically everyone. Everyone at school anyways. I think that’s why Vince is a little more rattled than usual.
# [Eclair]That and the fact that you’re around is making him more embarrassed than he’d otherwise be.
# [Mishelle]Why would Vince be embarrassed around me? I’m pretty sure he’s wet around me plenty of times.
# [Eclair]Diapered or not, you two are hopeless.
# [Mishelle]Why? I don’t get it.
# [Eclair]Never mind. Let’s just get to school. Let’s get this weird day over with.

#Vince returns

# [Vince]Sorry. Had to stretch my legs a bit.
# [Eclair]Uh…It’s cool.*Shrugs*
# [Vince]You still being weird?
# [Eclair]I’m not the one being weird. You are!
# [Vince]Am not!
# [Eclair]Are too!
# [Vince]Am not!
# [Eclair]Are too!
# [Vince]Are we seriously doing this?
# [Eclair]Hehehe. I guess so.
# [Vince]Alright then.
# [Eclair]A little bit, yeah. But I’m going to see how this pans out.
# [Vince]Fair enough.

#Day2, before entering the school
#Exterior, School

# [Maxwell]Hey guys!
# [Eclair]Hey, Maxwell.
# [Maxwell]So, not to be awkward, but I’ve seen some of the things that Fiona is posting about you guys online.
# [Vince]Yeah, about that…can we not talk about it?
# [Maxwell]That was really uncool of her.
# [Mishelle]*Shrugs* Yeah, but that’s Fiona, so what can you do?
# [Maxwell]Actually, me and Carmella were thinking about that.
# [Eclair]Yeah?
# [Maxwell]Yeah. So, weird piece of advice: If you guys need to umm…freshen up; you should probably do it before Fiona’s report about what she found on Career Day. If Carmella timed it right and everything goes according to plan, let’s just say Fiona will likely be in the bathroom for a looooong time.
# [Eclair]Timed what right?
# [Maxwell]Don’t worry about it. Nobody picks on my sister’s buddies and gets away with it. The rest of the school’s got your back, even if the Miss Georgette can’t technically do anything about it.
# [Eclair]Your sister’s buddies? What do you-?
# [Mishelle]Come on Eclair. Let’s get to class.
# [Maxwell]Oh, wait, one more thing!
# [Vince]What?
# [Maxwell]So I don’t know how you guys…clean up or whatever. But if it involves sitting on the toilet, like for balance or something…I wouldn’t.
# [Maxwell]Hi Fiona! Did you enjoy your morning coffee from the café?
# [Fiona]Outta my way, you immature milk drinker! I’ve got a presentation.
# [Maxwell]Huh…milk drinker. That’s a new one. Right this way, Miss Mature!
# [Maxwell]Everything go alright?
# [Carmella]Yup. Right in her coffee, and she didn’t even notice. The gang here?
# [Maxwell]Just got here.
# [Carmella]Alright! If Fiona wants to make such a big deal out of my friends wearing diapers, let’s see how she likes being stuck on a toilet for a couple hours!
# [Maxwell]Hey, is something up with Eclair, today?
# [Carmella]She’s being a little weird lately, why?
# [Maxwell]Nothing really. She’s just looked a little confused, maybe, even a little hurt that I referred to her as your friend instead of mine?
# [Carmella]Aww, she’s just in a vulnerable place right now, thanks to Fiona.
# [Maxwell]But it’s not like I hang out with you guys all that often. I mean should I?
# [Carmella]Naw…who’s wanna hang out with you anyways. *sticks out her tongue*
# [C.S.]And the first domino has been knocked down.
# [L.R.]What the heck does that mean?
# [C.S.]Just wait for it. I’ve got the smoothest of moves going down.
# [L.R.]I didn’t see you push any buttons!
# [C.S.]There are more ways to regress someone than by pushing a button.
# [L.R.]Name one!
# [C.S.]Like sending an email so a couple of sisters got an idea for revenge.
# [L.R.]You put that idea in their head?
# [C.S.]Of course.
# [L.R.]How’d you know they’d go through with it.
# [C.S.]Their farmers, and I actually have a real country family, so I knew how they’d react.
# [L.R.]Yeah, but how is this gonna destabilize the girl enough so that she regresses more?
# [C.S.]Watch and learn my friend. Watch and learn.

#Trying to leave the classroom before sitting down for Fiona's presentation

# [Miss Georgette]Eclair, now is not a good time for you to leave.

    #If Immaturity < 4

    # [Eclair]Sorry, ma’am.
    # [Miss Georgette]You have a few moments to talk to your classmates, but not enough time to go wandering.

    #Else

    # [Eclair]Um…I have to go to the bathroom?
    # [Miss Georgette]Nice try. But no.
    # [Eclair]But I reeeeallly have to go baaaad!
    # [Miss Georgette]I know what your face looks like when you’re telling stories, young lady, and the last time you had a close call where it mattered you weren’t standing like that.
    # [Eclair]No, seriously! I gotta go to the bathroom really bad. Honest!
    # [Miss Georgette]Eclair, the last time you had a close call to get to the bathroom, there was no force on earth that could stop you from dashing out.
    # [Miss Georgette]The fact that you’re having this conversation with me tells me that your emergency has long passed the point of no return- in which case a few more minutes waiting to cleanup won’t hurt you- OR you’re lying and there is no emergency.
    # [Miss Georgette]Do I need to call your mother?
    # [Eclair]I…no ma’am.
    # [Miss Georgette]Now get back here.


# [Miss Georgette]Alright class, some of us went out and interviewed the various pillars of our community. Who wants to share what they learned?
# [Eclair]I’ll go!
# [Miss Georgette]Eclair, do you need to be excused? Is that what you
# mean?
# [Eclair]No, I mean I’ll go first. I’ll present what I learned.
# []Students snicker.
# [Miss Georgette]Perhaps next year, Eclair, when you actually go and participate in Career Day.
# [Eclair]But I’ve got it right…*Looks in her desk* Hey! Where’d the notes for the report go?
# [Miss Georgette]Though, if you had wanted to do a report, Eclair, I suspect you could have just shaken down Mr. Hanners for all the information. Isn’t that right, Maxwell?
# [Fiona]Busted!
# [Miss Georgette]And I believe we have our first volunteer. Fiona, the stage is yours.
# [Fiona]Yes, Miss Georgette.
# [Mishelle]*Whispers* Pssst! Sit down. Eclair. Let someone who’s old enough do it!
# [Eclair]*Whispers* We are old enough!
# [Vince]*Whispers* Yeah, but we’re not in the right grade!
# [Mishelle]*Whispers* We got held back in Kindergarten because of the whole toilet thing.
# [Vince]By the time Karlton found something medically wrong with us and got us excused, we were too far behind to go to first grade the next year, so they had us repeat Kindergarten and move on with Carmella.
# [Eclair]*Whispers* So we’re in the same grade as Carmella, now?
# [Vince]*Whispers* Now? What do you mean “now”?
# [Mishelle]*Whispers* We’ve been in the same grade as Carmella for years. We grew up with her.
# [Miss Georgette]Eclair, have a seat.
# [Eclair]Yes ma’am.
# [Fiona]Ahem- The Island of Farzon has a simple, yet complex philosophy that has yielded…
# [Fiona]Blah blah blah...Nanites...Blah blah blah... The docks...Blah blah blah...
# [Eclair](Oh my God. Fiona’s report is so boring my brain isn’t comprehending what she’s saying! What am I going to do?)
# [Mishelle]Pssst!
# [Eclair]*Whispers* What?
# [Mishelle]*Whispers* You’re zoning out. Here: in case Miss Georgette thinks you’re not paying attention.
# [Eclair]*Whispers* What are these?
# [Mishelle]*Whispers* Notes on what Fiona has said so far.
# [Eclair](Holy cow! These are almost identical to what she wrote yesterday, but they’re in a different color ink! How did she write so much so fast?)
# [Eclair]*Whispers* Thanks.
# [Mishelle]*Whispers* Welcome.
# [Eclair](Does she really not remember what we did yesterday? Some part of her has to. Even if she can’t actively remember it, some part of her does.)
# []Eclair opens her backpack and slips the notes inside. She shudders a bit as her hand brushes the plastic backing of an adult incontinence brief inside.
# [Eclair](I shouldn’t be here. I shouldn’t have a backpack with diapers in it. I’ve got to get out of here and get to the bottom of this.)
# [Eclair](Not listen to some stupid report by one of the worst people I know. Something is definitely not right and I’m the only one who realizes it!)
# [Eclair](I can wait this out. I can be patient. Maybe there’ll be an opportunity to leave class. Or I bet I could convince Vince or Mishelle to create a distraction for me.)

# [Eclair](What should I do?)

menu:
    "What to do?"

    "Patience":
        # [Fiona]Blah, blah, blah, blah. I.A.’s. Blah blah blah. Dr.
        # Harkness Milner. Blah Blah.
        # [Eclair]Sooooooooo boring.
        # [Fiona]Yada-yada-yada...Solar panels...Yada-yada-yada-ya…
        # []Fiona looks distinctly uncomfortable.
        # [Fiona]Ya…da?
        # [Miss Georgette]Fiona? Is something the matter?
        # [Fiona]I…I…gotta go!
        # []Fiona knocks over Eclair’s backpack.
        # [Fiona]Watch it! You little…ugh *clutches stomach*…can’t talk
        # right now!
        # [Fiona]OOOOOOOOOOH! OOOOOOOOH GOD! UUUUUUGH!
        # [Carmella]Ha! I bet she wishes she had a diaper on now!
        # [Mishelle]Carmella?
        # [Vince]Don’t tell me! You didn’t, did you?!
        # [Carmella]Officially? I did nothing. *Wink* Now if you excuse me,
        # I gotta see how this plays out!
        # [Miss Georgette]CARMELLA HANNERS! YOU GET BACK HERE,
        # THIS INSTANT!
        # [Maxwell]Heheheheh…
        # [Miss Georgette]Maxwell, you better not have anything to do with this!
        # [Maxwell]Oh, no ma’am, Miss Georgette. Not a thing. In fact I’m
        # going to follow my little sister and make sure she’s not
        # causing any more trouble.
        # [Miss Georgette]That’s not what I meant!
        # [Vince]Ha! I mean…I’ll go get them!
        # [Mishelle]Me too!
        # [Miss Georgette]Stooooop!
        # [Miss Georgette]Why me? CLASS! GET BACK HERE!
        # [Eclair]Now’s my chance! Though I gotta wonder, what’s going
        # on with Fiona? Maybe I should check up on her.


    "Distraction":

        #Add 1 immaturity point

        # [Eclair](I can’t take it anymore! I’ve got to get out of here! I
        # need a diversion! But what?)
        # [Eclair]*Looks at Mishelle’s notes.* (Holy crud. Look at what she
        # wrote in the margins! I should have let Mishelle ask more
        # of the questions yesterday! These are amazing!)
        # [Eclair]*Looks at Mishelle* I’ve got it.
        # [Eclair]BORING!
        # [Miss Georgette]Eclair! This isn’t improvisational comedy. Audience
        # participation is not encouraged.
        # [Eclair]I’m sorry Miss Georgette, but I just happened to glance at
        # some of Mishelle’s notes on Fiona’s report. She brings up
        # some interesting points that I don’t think Fiona considered.
        # [Miss Georgette]Well, we’ll have a question and answer session once
        # everyone who has a presentation has gotten the chance
        # to speak. Until then-
        # [Fiona]No, it’s fine, Miss Georgette. I don’t mind answering
        # questions. Please, widdle Mishelle. What questions
        # do you have?
        # [Fiona]I’ll be happy to answer them in very simple words so
        # that everyone can understand.
        # [Mishelle]Um…are you sure?
        # [Fiona]Oh, I’m \ivery\i sure.
        # [Eclair]*Whispers* Pssst! Go for it!
        # [Mishelle]Okaaaay. But you asked for it.
        # [Fiona]Bring it.
        # [Mishelle]What’s Mayor Knox’s political party?
        # [Fiona]Um…Independent?
        # [Mishelle]Are there any other political parties on Farzon?
        # [Fiona]No…?
        # [Mishelle]Does that mean there’s only one way to implement
        # or interpret Dr. Harkness Milner’s philosophy?
        # [Fiona]I guess so?
        # [Mishelle]Also what about Mr. Hanners’s nano-bots in the soil
        # that you mentioned?
        # [Fiona]What about them?
        # [Mishelle]He told you that we hide their existence from the mainland
        # to protect our secrets, so no one can steal them and use
        # them without our permission?
        # [Fiona]Yeah, more or less.
        # [Mishelle]Then why not get a patent?
        # Wouldn’t a patent make it more difficult to copy island
        # technology and give us legal recourse in the event that
        # the technology is stolen or produced without our permission?
        # [Fiona]I didn’t…I don’t…maybe?
        # [Mishelle]And if Farzon’s technology is so advanced, yet there
        # aren’t any peer reviewed journal studies, do we know
        # if it’s actually more effective?
        # [Fiona]Wha…?
        # [Mishelle]What about…?
        # [Eclair]Everyone’s watching Mishelle completely wreck Fiona.
        # Now’s my chance to sneak out.
        # [Eclair]Okay. I can either bail now, or maybe hide out in the
        # lunchroom.

# [Miss Georgette]Fiona, are you okay in there?
# [Fiona]Ugh..of course…ugh…not!
# [Miss Georgette]What’s going on?
# [Fiona]Can’t…ugh…say…ugh…too mature…ugh…oh god…
# to talk about it.
# [Maxwell]Ha! Yeah, real mature!
# [Miss Georgette]Maxwell Hanners, I’m warning you.
# [Maxwell]Sorry, ma’am.
# [Miss Georgette]What are your symptoms? Is it stage fright? It’s stage
# fright isn’t it? Butterflies in your stomach?
# [Fiona]No. Not nauseous…ugh…at all. Why does it burn?!
# [Carmella]*Whispers* Oops! I might have slipped some of my
# pop’s powdered chili peppers in her coffee, too.
# [Vince]*Whispers* Nice! Hehehehe!
# [Mishelle]*Whispers* Oh wow! That’s devious.  Hehehe!
# [Maxwell]*Whispers*Just wait. The best is yet to come.
# [Miss Georgette]I don’t know what you’re laughing about, but this is
# hardly the time!
# What are your symptoms, honey?
# [Fiona]It’s…ugh…it’s like there’s a race out of my fanny…
# ugh…and everybody’s winning!
# [Carmella, Mishelle, Maxwell and Vince]HAHAHAHAHAHAHAHA!
# [Miss Georgette]NEXT PERSON TO UTTER EVEN A PEEP GETS
# DETENTION FOR A WEEK!
# [Carmella, Mishelle, Maxwell and Vince]...
# [Ronald]What in the blue blazes is going on here?!
# [Miss Georgette]Oh Ronald, how fortunate! It seems we’ve got a little
# situation on our hands. If I may have a word with you
# on stage left, I’ll explain.
# []Eclair feels a sudden urgency.
# [Eclair](Oh no! Please don’t! Not right now!)
# [Eclair]Fiona! Open up! I need to go! Now!
# [Fiona]Why…ugh…do you care? You’ve got a diaper on, you
# immature little…ugh!
# [Eclair]Fiona! I’m begging you, please! Don’t make me wet
# my pants!
# [Fiona]Okay…*pant* *pant* ugh…fine…I’ll be the bigger woman.
# I think the worst is over, anyways. I’m coming out.
# [Eclair]Come on! Get out of there! Hurry!
# [Fiona]I…I can’t!
# [Eclair]WHAAAAAT?!
# [Fiona]I can’t! I’m stuck!
# [Eclair] WHAT DO YOU ME-OOOOH! WHAT DO YOU MEAN
# YOU’RE STUCK?!
# [Fiona]There’s some kind of glue or something that’s keeping
# me stuck to the seat.
# [Maxwell]*gasps* Oh no!
# [Carmella]This wasn’t supposed to happen like \ithis\i!
# [Georgette and Ronald]What wasn’t to happen?!
# [Maxwell and Carmella]Nothing!
# [Eclair]PLEASE, FIONA! GET OUT BEFORE I…I…!
# []\iIt happens. Her body, unable to withstand it any longer,
# lets loose, and a strange, warm, wet, almost alien
# sensation invades her underwear.\i
# \iThe warmth spreads quickly, caressing and encasing
# her most intimate of areas. Eclair cannot deny it any
# longer: She’s done the unthinkable; this time in front\i
# \iof so many more witnesses than just Fiona. But the expected
# catharsis- the hot humiliation of urine trickling down her legs
# and pooling into a puddle on the floor- never comes.\i
# \iInstead, it all stays with her. The weight of her shame
# already begins to take shape and form as the diaper
# swells and sags ever so slightly between her legs.\i

    #Immaturiry >= 4

    # \iAnd worse yet, Eclair realizes in the back of her mind: it
    # doesn’t feel all that bad in comparison to what happened
    # yesterday.\i
    # \iIt’s rather like slipping into a warm bath if she didn’t think
    # about it too much.\i


# [Eclair]NO! PLEASE! NOT THIS! PLEASE NOT THIS!  NOT
# NOW! NOT IN FRONT OF ALL MY FRIENDS!
# [L.R.]Holy shit! Are you saying that you gave the farm
# girls the idea to prank the bully just so our target would
# get locked out of the bathroom at the right time?
# [C.S.]You got it.
# [L.R.]And you didn’t press any reality altering buttons?
# [C.S.]The only button I pressed was “Send”.
# [L.R.]That was a one in-a-million shot!
# [C.S.]And that’s how you play the game, buddy.
# [L.R.]That’s crazy that it worked!
# [C.S.]Crazy like a fox.
# [L.R.]If you had bet me that was how it was going to
# play out, I would have lost a whole lot of money
# right now.
# [C.S.]Damn…I hadn’t thought of that.

if immaturity >= 4:

    # [Miss Georgette]Eclair! What’s the matter, sweetie? Are you okay?
    # [Eclair]*sniffs* No. I’m not okay. Nothing’s going right today,
    # everything sucks. And now I…I…I just want my…my...I
    # don’t want to be here!
    # [Miss Georgette]Awww, you poor thing.*Hugs Eclair* Today is just not
    # your day, is it? How about I give you the rest of the day
    # off?
    # [Eclair]Okay!

else:

    # [Miss Georgette]Eclair! Are you alright?
    # [Eclair]*sniffs* I’m fine, I guess. I’m just really, really,
    # embarrassed is all. That’s never happened before.
    # [Miss Georgette]Not at that level it hasn’t .*Hugs Eclair* This is turning
    # out to be a strange day for everyone. Would you like to
    # take the rest of the day off?
    # [Eclair]*nods* Yes, ma’am.

# [Carmella, Mishelle, Maxwell and Vince]Hooray!
# [Miss Georgette]Not you guys. Just Eclair.
# [Carmella, Mishelle, Maxwell and Vince]Awww…
# [Miss Georgette]Everyone else, back to class.
# [Ronald]Except for the Hanners Sisters. You’re going to help
# me get Fiona unstuck.
# [Maxwell and Carmella]Why us?!
# [Ronald]Oh, I think you know why.
# [Carmella]Told you we shouldn’t have followed that anonymous
# email’s suggestion.
# [Maxwell]Shut up, Carmella.

#Day 2, after the scene with Fiona

# [Eclair]I made it out! Awesome! I’m free! In the clear! But what do I do now?
# []Eclair feels a sudden urgency.
# [Eclair](Yikes! That came on fast! Better find a bathroom, quick!)
# [L.R.]Why so glum, mi compadre?
# [C.S.]I was planning on her staying in school.
# [L.R.]Why?
# [C.S.]Never mind. It’s hard to explain. I was planning on her having an accident in front of a bunch of people.
# [L.R.]A bunch of people? Don’t worry, I think I gotcha covered.
# [C.S.]What are you doing?
# [L.R.]Just a liiiiiiitle hacking and false advertising.
# [Tourist]Excuse me!
# [Eclair]Oof sorry. Gotta get to a bathroom.
# [Tourist]Out of my way, gotta go!
# [Eclair]That makes two of us!
# [Eclair]Aaaaaah! Bathroooooooom!
# [Tourist]FREE COFFEEEEEEEEE!
# []{i}The bump, however cushioned by her padded posterior causes the dam in Eclair’s bladder to burst and let loose. The world falls into a kind of slow motion as Eclair’s body shudders with sudden relief and her mind screams with revulsion. The warm gush being absorbed into the incontinence briefs trickles into nothing as the thirsty padding swells beneath her. The garment has served its purpose.{i}
# [Eclair]NOT AGAIN! NOT AGAAAIIN! IT’S NOT FAIR! IT’S NOT FAIR!
# [C.S.]She’s right. It’s not fair.
# [L.R.]Don’t tell me you’re getting all philosophical on me.
# [C.S.]Maybe a little.
# [L.R.]Life never promises a fair ending. Sometimes you do everything right and you still lose.
# [C.S.]Yeah, I guess so. Still, it would have been nice to see my master plan in action.
# [L.R.]Oh! Phew! I thought for a second you were feeling sorry for her!
# [C.S.]Huh? No! Of course not. I’m a professional. How’d you get that crowd to block her way?
# [L.R.]I might have said that the Cafe was giving away free coffee for life to the first hundred customers that walked in the door today.
# [C.S.]You had that as a backup plan in case she got out of the school?
# [L.R.]Nope! I was gonna do that anyways, for funsies….but it worked out this time.
# [Eclair]No one is staring at me like last time. Why? *Looks down between her waist and gives the padding a gentle squeeze* Oh. That’s why. No leaks.
# [Eclair]That and, for whatever creepy reason, everyone seems to think that me wetting my pants is *cringe* normal.
# []Eclair looks into her backpack.
# [Eclair]Oh my gawd! Don’t tell me! Those things fell out of my backpack! I knew I should have zipped this thing up better!
# [Eclair](Well, I need to go change my diaper…I mean brief…. whatever. Ug…I can’t believe I’m already starting to think of them as mine.) {p} (I doubt Mom will let me back in the house. Maybe the Sayers’ store will have some I can buy.)

#Day 2, General Store
#Interior, General Store

#Before going to the cafe, resupplying.

# [Missy Sayers]Well hello, Eclair. How are you?
# [Eclair]I’ve been better.
# [Missy Sayers]Oh? Now why’s that?
# [Peter Sayers]Isn’t it obvious? She’s out of incontinence supplies and doesn’t want to go home.
# [Missy Sayers]Peter! At least be polite enough to let \iher\i tell us that!
# [Eclair]How…? How did you know?
# [Peter Sayers]Why else would you be here in the middle of a school day and blushing three shades of red? You kids get so embarrassed by the littlest things.
# [Eclair]Well, you’re right. Any chance I could get some more?
# [Missy Sayers]Sure, hon. Just grab yourself a package, and I’ll ring it up and put it on your mother’s tab.
# [Missy Sayers]Um, Eclair. Did you even look at what you were grabbing?
# [Eclair]No, why?
# [Missy Sayers]Take a look. You’re a bit big for those, I’d say.
# []Eclair looks at the package on the counter. There’s a smiling baby on the front.
# [Eclair]Eeeep! Sorry!
# [Peter Sayers]Well, that’s what I get for putting the baby diapers right next to the adult ones.
# [Eclair]These are the right ones!
# []Eclair looks at the two packages.
# [Eclair](Hold up! There’s something screwy going on here.) (The box of baby diapers say they’re just a size 6, but the size of the box and the number of diapers listed is the same as this other one!)
# [Missy Sayers]There you go. Pleasure doing business with you.
# [Eclair]Um, would it be possible to put these diapers on my mom’s tab, too?
# [Peter Sayers]Whatever for? Those aren’t going to fit you.

    #Immaturity >= 4

    # [Eclair]Uh…mine are really boring looking. These look much cuter. Maybe I could find a way to decorate mine so they look as cute as these.
    # [Missy Sayers]Well aren’t you a silly little thing?

    #Else

    # [Eclair]Uh… I’m curious to see how they compare to mine. Certain people have been calling me a baby lately, and I’m just curious to see the similarities.
    # [Missy Sayers]Fiona again?
    # [Eclair]Yes ma’am.
    # [Missy Sayers]Oh you poor thing.

# [Peter Sayers]Be that as it may, I don’t think your mother would approve of putting something that you’re too big to wear on her tab.
# [Missy Sayers]I’m afraid he’s right, dear. Best of luck.
# [Eclair]Okay. If I get a little extra spending money, maybe I’ll come back.

# []INCONTINENCE BRIEFS ADDED TO INVENTORY
# []ECLAIR LEARN "SELF CHANGE"

# []Eclair slips the Incontinence Briefs in her backpack.
# [Eclair]What’s this? It looks like a letter of some sort. Mom must’ve slipped it in my backpack, and it managed to stay inside even after the diapers fell out.



#Day 2, General store
#Interior, General store.

#If Eclair spent all her money (Bought Ice Cream and paid the fine?)

# [Peter Sayers]Hello Eclair, still looking to do some shopping?

menu:
    "What to say?"

    "Just looking":
        # [Eclair]Just looking. I had to buy other things with my money.

    "Sob story":
        # [Eclair]I would…it’s just that…*sniffs*
        # [Peter Sayers]*leans in* Just what?
        # [Eclair]It’s just…I can’t…! I can’t buy…anything…from your lovely…store! *lip trembles*
        # [Peter Sayers]Why? What’s wrong? Go on, you can tell me.
        # [Eclair]I…borrowed a book…from the library…and it was… overdue! So overdue! So, so, overdue! *rubs eyes*
        # [Peter Sayers]\iThat\i overdue, huh?
        # [Eclair]And I wanted to come back…and pay for these diapers… I really did! But all...the money I earned…had to go…to pay the fine! THE FIIINE! *breath becomes ragged*
        # [Peter Sayers]Well, that is a shame, poor kid.
        # [Eclair]I know I could’ve come…and spent it all here...but my conscience….my conscience told me…told me to pay the fine!
        # [Eclair]Otherwise….I! WOULD! BE! STEALING! FROM! THE! LIBRARY! *Buries her face in her hands and pretends to sob*
        # [Peter Sayers]Awww, heck. Do you really think that’s how libraries work?
        # [Eclair]*Looks up* You…mean…they…don’t?
        # [Peter Sayers]Of course not. It’s just a library fine. It doesn’t mean you’re a bad person.
        # [Eclair]It…doesn’t?
        # [Peter Sayers]Not at all. Here. Just take them.
        # [Eclair]Really? You mean it?
        # [Peter Sayers]Sure thing. You did a good thing, and were honest, and honestly deserves to be rewarded.
        # [Eclair]Yay! Thank you!
        # []Eclair slips the baby diapers into her backpack.
        # [Missy Sayers]Hey honey?
        # [Peter Sayers]Yes dear?
        # [Missy Sayers]I think you just got played.
        # [Peter Sayers]I always was a sucker for a sob story.

#If Eclair only has 1 money

# [Peter Sayers]Well fancy seeing you here, again, Eclair. What can I do for you?

if immaturity >= 4:
    # [Eclair]I’ve got money now, and my undies could use an upgrade.
    # [Peter Sayers]I beg your pardon…?
    # [Eclair]I just want to see if I can make my plastic backed panties a little prettier, so I’m looking to get something to model off of. Oh, and some stickers if you have them!
    # [Peter Sayers]Eclair, I can tell you’re excited about something, but you’re going to have to speak more plainly for me. I’m just not following.

else:

    # [Eclair]I came to uh…do some comparative shopping, if you know what I mean.
    # [Peter Sayers]I’m sorry….?
    # [Eclair]You know…that thing we talked about earlier today?
    # [Peter Sayers]Eclair, people are in and out of here all day every day. I can’t keep track of it all. You’ll have to refresh my memory.
    # [Missy Sayers]She means she wants to buy the baby diapers, honey!
    # [Peter Sayers]Oh! Well then why didn’t you say so? Here you are.
    # []Peter slides the diaper across the counter. Eclair digs the money out of her backpack.
    # [Peter Sayers]Well I’ll be. Looks like you went and got some spending cash.

if immaturity >= 4:

    # [Eclair]Yeah. It was easy. I’m pretty awesome.
    # [Missy Sayers]*Sarcastic* And humble, too. *Shakes her head:*
    # [Peter Sayers]With the way she’s been acting today, these diapers might be more appropriate, anyways.

else:

    # [Eclair]Thank you. I went and did some odd jobs.
    # [Missy Sayers]That’s the spirit! If you want something, you work for it!
    # [Peter Sayers]Even if it is a little odd that you would want \ithese\i.



# [Missy Sayers]Honey! I’m surprised at you! You know we don’t joke  about the customers until AFTER they leave!

if immaturity >= 4:

    # [Peter Sayers]Ooops! Where are my manners?! Here you are little miss.

else

    # [Peter Sayers]Ooops! Where are my manners?! Here you are young lady.

# After buying the baby diaper with your own money?

# [Missy Sayers]Well, I hope you’re happy with your purchase.

if immaturity >= 4:
    # [Eclair]You bet I am!
    # [Missy Sayers]Now why would something like that make you happy, though? A young lady like you should be thinking about going to college soon, not baby stuff. Not unless… Eclair, is there something going on. Are you…in the family way?

else:

    # [Eclair]It’s not a matter of happiness, it’s a matter of needing to know something.
    # [Missy Sayers]Oh honey, is it a body image thing? Do you think you’re fat? I know that extra padding adds a few inches to your hips, but buying smaller diapers will cause way more problems than you think they’ll solve.
    # [Eclair]Huh?! No, it has nothing to do with that!
    # [Missy Sayers]Phew. You had me worried for a second.

#Talking with Missy Sayers, didn't get the baby diapers

# [Eclair]So…I don’t have any money. Is there any chance I could, I don’t know, have those baby diapers…as a favor?
# [Missy Sayers]Sorry, Eclair. Not this time. Money or nothing.

#  .o88b.  .d8b.  d88888b d88888b
# d8P  Y8 d8' `8b 88'     88'
# 8P      88ooo88 88ooo   88ooooo
# 8b      88~~~88 88~~~   88~~~~~
# Y8b  d8 88   88 88      88.
#  `Y88P' YP   YP YP      Y88888P

$ scoutJobComplete = false
$ scoutJobReqFliers = 5

$ cafeCleanUpJob = false
$ cafeCleanUpJobComplete = false

$ mollyProgress = 0

$ almaAndMarieInitial = false
$ promiseIceCream = false

label molly:

    if mollyProgress == 0:

        # [Molly]Like, sup?
        # [Eclair]This place looks like a tornado came through here. What happened?
        # [Molly]Like, false advertising.
        # [Eclair]False advertising? How?
        # [Molly]Like, somebody posted a fake ad saying that I was giving away free coffee for life and everybody just rushed in here.
        # [Molly]It was louder and more crowded than the last Electric Light Digital Grunge Underground concert that I went to. They’re like, so cool. But you probably never heard of them.
        # [Eclair]This place looks trashed.
        # [Molly]Like, yeah. It’s almost as bad as a Nu Skank Pit.
        # [Eclair]A what?
        # [Molly]Like, that’s when a bunch of people are skanking in a mosh pit while Pixel Trombone- that’s this new Nu Wave Ska cover band- are jamming out.
        # [Eclair]I’m almost sure all of those were real words.
        # [Molly]Like, kids. So uncool. Almost as bad as old people. So, like, do you want a job or something?
        # [Eclair]Job? Now you’re speaking my language! What do you want me to do? Make espressos? Cook pastries? Wipe tables?
        # [Molly]Like, pass out fliers.
        # [Eclair]Pass out fliers?
        # [Molly]Like, more like pass out fliers to the scouts that I’ve already paid to pass out fliers. Like, all those people left mad, and I need to advertise to get more customers. Like, people who actually will pay money for coffee.
        # [Eclair]So what do you want me to do?
        # [Molly]Like, I already paid some scouts to pass out fliers for me. But like, if you meet them in the field, they can keep working and passing out fliers instead of having to come back here to get more. Got it?

        if immaturity >= 4:
            #Image with arms at her side, looking perky
            # [Eclair]Got it!
        else:
            #Image with arms crossed. Who even notices this?
            # [Eclair]Got it!

        # []ECLAIR RECEIVED 5 BUNDLES OF FLIERS!
        # []NEW NOTE ADDED TO THE INVENTORY!

        # [Molly]Like, give those to the scout troop members, and then
        # come back here and I’ll pay you.
        # [Eclair]Deal!

        $ mollyProgress += 1

    elif mollyProgress == 2:

        # [Molly]Like, can I help you?

        menu:
            "What do you say?"

            "No, I’m good":

                # [Eclair]No I’m good.
                # [Molly]Like, okay. Not to be uncool, but I kinda need my
                # customers back, so would you mind getting going?

            "Whine to get an easier job":

                # [Eclair]Do I haaaave to go alllll over Farzon to distribute these fliers?
                # [Molly]Like, if you want money, yah.
                # [Eclair]But I don’t need THAT much money. And my legs are already soooooo tired.
                # [Molly]*Huff* Like, fine. Just give me those fliers so I can re-sort them.
                # []Eclair gives Molly the 5 bundles of fliers.
                # [Molly]Like, here. So uncool, but whatever. I like, redistributed them into bigger stacks, so some of those scouts are going to have to work harder than others. But it’s, like, better than nothing.
                # []ECLAIR RECEIVED 3 BUNDLES OF FLIERS!

                $ immaturity += 1

        $ mollyProgress += 1

    elif mollyProgress == 3:

        # [Molly]Like, could you start working so I can get my customers back. Sometime soon? Like, now-ish?

    elif scoutJobComplete == true:

        # [Eclair]All done.
        # [Molly]LIKE, WHAT?!
        # [Eclair]I delivered the fliers.
        # [Molly]LIKE, WHAT?!
        # [Eclair]I delivered the fliers!
        # [Molly]LIKE, I CAN’T HEAR YOU!

        if immaturity >= 4:
            # [Eclair]I SAID: I! DELIEVERED! THE! FLOWERS!
            # [Molly]LIKE, WHAT? I LIKE, CAN’T HEAR YOU!
            # [Eclair]AHHHHHH! *Pulls her hair in frustration*
        else:
            # [Eclair]*Sees the earbuds in Molly’s ears* Are you listening to music?
            # [Molly]LIKE, HOLD ON! I’M LIKE, LISTENING TO MUSIC! LIKE, I WANNA FINISH THIS TUNE. IT’S, LIKE, MY JAM!
            # [Eclair]*Waits Patiently*...

        # [Molly]*Removes the earbuds blaring music* Like, sorry about that. I was, like, jamming out to my favorite band.
        # [Eclair]Pixel Trombones?
        # [Molly]Ugh, like no. Like, Pixel Trombones are sooooo five minutes ago. They’re older than the internet at this point in their careers.
        # [Eclair]But I thought you said you liked them.
        # [Molly]Ugh, like, five minutes ago.
        # [Eclair]Seriously?
        # [Molly]Like, yeah. Now I’m into The Spring Break.
        # [Eclair]Who are they?
        # [Molly]Like, The Spring Break isn’t a band, he’s a person. He’s like, a great singer and like, the world’s best laser stringed bantar player.
        # [Molly]That’s like… a cross between a banjo and a guitar where the strings have been replaced with laser motion sensors. Like, you’ve probably never heard of him.
        # [Eclair]I haven’t. Can I get paid now?
        # [Molly]Like, what?
        # [Eclair]I delivered the fliers like you asked. Can I get paid now?
        # [Molly]Like, sure, but first you gotta sweep up the place.
        # [Eclair]I what now?
        # [Molly]Like, this place needs to be clean for when the customers come in. Like, if you want your money, you’ll have to clean up the floor a little bit.

        menu:
            "What to do?"

            "Debate":

                # [Eclair]That hardly seems fair.
                # [Molly]Like, why?
                # [Eclair]You hired me to pass out fliers, and now you’re withholding what you promised until I do more than we agreed upon.
                # [Molly]Like, ohmygawd! Like, I almost acted like one of those greedy corporate conformists. So uncool. Like, here you go. Sorry.

                # ECLAIR RECEIVED MONEY!

                $ money += 20
                $ mollyProgress = 10


            "Whine":

                # [Eclair]THAT’S NOT FAIR!
                # [Molly]Like, life’s not fair. Like, my store got trashed because of false advertising. Like, if you want your money, you like, gotta help me.
                # [Eclair]*Huff* Fine!

                $ cafeCleanJob = true
                $ immaturity += 1

    elif cafeCleanUpJob == true:

        if cafeCleanUpJobComplete == true:

        # [Molly]Like, that’s better. Here’s your money.
        # [Eclair]About time.
        # [Molly]Like, what was that?
        # [Eclair]Huh? Oh nothing. IthinkIhearMishelle’smothercallinggottago!

        $ money += 20
        $ mollyProgress = 10

        else:

            # [Molly]Like, that floor still looks pretty grungy…and I don’t meangrunge in the good way.
            # [Eclair]There’s a good kind of grunge? Sounds disgusting.
            # [Molly]Pfft…like, kids.

    elif mollyProgress == 10:

        # [Eclair]What are you listening to now?
        # [Molly]Like, I just tuned into this golden oldies podcast. The songs are older than the internet, but they’re way retro. You’ve probably never heard of them. Like, “And we danced all night to the best song ever!”
        # [Eclair]Why do I have the feeling that your tastes are going to change radically in the span of the next few seconds?
        # [Molly]Like, you wouldn’t understand.

        $ mollyProgress += 1


    elif mollyProgress == 11:

        # [Molly]Like, it’s the latest thing: Techountry. It’s electronic club pop techno music spliced with Country. It actually makes Country music listenable. “We’re up all night to get lucky riding that bull.” Like, you’ve probably never heard of them.
        $ mollyProgress += 1

    elif mollyProgress == 12:

        # [Molly]Like, I found this music mix that randomly mashes up original Top 40 hits and their parodies until you can’t tell where the real one ends and the satire begins. It’s totally ironic. Like, you’ve probably never heard of it.
        $ mollyProgress += 1

    elif mollyProgress == 13:

        # [Molly]Like, I’m listening to static compositions. To the untrained, uncool ear, it sounds just like the static between radio waves or a bad transmission; but it’s actually music. Like, you’ve probably never heard of it.

label almaAndMarie:




    # [Alma]Eclair? Oh dear, I am so very sorry. I almost collided
    # into you!
    # [Eclair]I’m okay.
    # [Marie]Hi Eclair! Where’s my sister?
    # [Eclair]She’s still at school.
    # [Alma]And why aren’t you at school with her?
    # [Eclair]I had a few…let’s call them “mishaps”. One thing led to another, and now I’m here.
    # [Alma]Well, it’s the last week of school anyways, so I don’t see the harm, personally. Though if you’re playing hookie, your mother might feel differently.
    # [Eclair]Eeeep! Please don’t tell her!
    # [Alma]I wasn’t even thinking of that.  Although, now that you mention it…
    # [Eclair]Oh no! Please! I got the day off from my teacher, I swear!
    # [Alma]Are you sure your mother will believe that?

    if skippedSchool == true:
        # [Eclair]I…hope so?
    else:
        # [Eclair]She’ll have to! It’s the truth!

    # [Alma]Are you so sure?
    # [Eclair]…
    # [Alma]I could tell your mother, unless…
    # [Eclair]Unless? Unless what?!
    # [Alma]I’m going out in a few nights with some old friends from the mainland.
    # [Marie]Oh no...!
    # [Alma]I was going to have Mishelle sit with Marie. Perhaps you’d care to join her and watch Marie while I’m gone? Then we’ll call it even and I won’t tell your mother.
    # [Eclair]Deal!
    # [Marie]Nooooo!
    # [Eclair]Hey! What’d I do?
    # [Alma]Marie, what’s wrong? I thought you liked Eclair.
    # [Marie]I do. Eclair’s really cool.
    # [Alma]Then what’s the matter?
    # [Eclair]Yeah, it wouldn’t be the first time I’ve babysat you.
    # [Marie]But I’m not some little kid, anymore. I should be babysitting by now. Not being babysat.
    # [Eclair]I can kinda see your point. I was about your age when Mishelle and I started looking after you.
    # [Marie]See, Mom? I wanna take care of babies and change diapers, not get watched by someone who is still in them.
    # [Alma]Marie! Manners!
    # [Marie]No offense, Eclair.
    # [Eclair]None taken.
    # [Alma]I know you’re a very mature and responsible girl, Marie. It just helps me to know that your big sister and her friend, medical issues or not, are looking after you. You’ll get to be the big and responsible one someday soon. I promise.
    # [Eclair]Is there anything I could do to make you feel better, Marie?
    # [Marie]Well….there is one thing.
    # [Eclair]What?
    # [Marie]Ice cream? I’ve been craving the new double decker banana split boat over at the ice cream shop.
    # [Eclair]Well, I’d love to buy you a treat, but I don’t have any money. I’m doing an odd job for Molly to get some money of my own.
    # [Marie]Great! You can take me to the ice cream shop AFTER!
    # [Eclair]Well…I don’t know.
    # [Marie]Pleeeeeease! I promise I’ll be really good for you when
    # you come over and sit with me!

    menu:
        "Promise to get ice cream with Marie?"

        "Promise":

            if immaturity >= 4:
                # [Eclair]Hehehe. Okay, okay. You got me. I’ll get you some ice cream after Molly pays me, but only if you share with me.
            else:
                # [Eclair]Hehehe. Okay, okay. You got me. I’ll get you some ice cream after Molly pays me.

            # [Marie]Deal!
            # []NEW NOTE ADDED TO THE INVENTORY!

        "Don't promise":

            if immaturity >= 4:
                # [Eclair]Nope, nope, nope, nope. Not gonna do it. I need my money for other things.
            else:
                # [Eclair]Yeeeeeah, that’s not gonna work on me. I’ll sit with you and treat you fairly, but I expect you to behave; ice cream or not.

            # [Marie]Awww. Well can’t blame a kid for tryin’.
            # [Eclair]No, I can’t. I’d be doing the same thing if I were in your shoes.



#Leaving the cafe with a leaking diaper.
# [Eclair]Everyone is looking at me, I need to go home now, that job can wait.

#Leaving AFTER getting the money WITHOUT talking to Marie
# [Marie]Hey, Eclair! Wait up! You said you’d take me with you to get ice cream after you got paid!
if immaturity >= 4:
    # [Eclair]Oh yeah…right.
else:
    # [Eclair]Oh, I almost forgot. Sorry!


# [Marie]Can I ask you a personal question?
# [Eclair]Sure.
# [Marie]Is it weird wearing…y’know...*whispers*...Diapers?

if immaturity >= 4:

    # [Eclair]Naw. They’re not so bad once you get used to them. They’re actually kinda comfy.

else:

    # [Eclair]You have no idea.


if money == 0

    if promiseIceCream == true:

        # [Marie]Can we get ice cream yet? Can we get ice cream yet?! Can?! We?! Get?! Ice cream?! Yet?!

        if immaturity >= 4:

            # [Eclair]Calm down or I’m changing my mind and getting all the ice cream for myself.

        else:

            # [Eclair]Yikes! Looks like your politeness has been outmatched by your impatience!

        # [Marie]Sorry.

    else:

        # [Marie]Any chance that you’ll change your mind?
        # [Eclair]Sorry, but no.
        # [Marie]Can’t blame me for trying.

# [Marie]So, you got the money?
# [Eclair]Yup.
# [Marie]And you don’t have any more work to do?
# [Eclair]Nope.
# [Marie]Soooo…remember that deal we talked about?

if immaturity >= 4:
    # [Eclair]Yeah…are you absolutely positively sure you still want the ice cream? No chance of a rain check or an I.O.U.?
    # [Marie]Not at all.
else:
    # [Eclair]I do. And may I say you’re being very patient and polite?
    # [Marie]Thank you. I’m trying.

# [Eclair]Well…

menu:
    "What to do with the promise?"

    "Keep the promise":

        # [Eclair]Okay, squirt. A deal’s a deal.
        # [Marie]Awesome!

        if immaturity >= 4:

            # [Eclair]Let’s go get that ice cream!
            # [Alma]Aren’t you two forgetting something?
            # [Eclair]Like what?
            # [Alma]While you two were negotiating this little bribe, not once did you ask if I was okay with it.
            # [Eclair]Oh yeah…
            # [Marie] Can I, please?

        else:

            # [Eclair]Aren’t you forgetting something?
            # [Marie]What?
            # [Eclair]I don’t remember your mother giving you permission.
            # [Marie]Oh yeah…
            # [Marie]Can I, please?

        # [Alma]Hmmmm….come to think of it, this might be a good chance to test how trustworthy and responsible you are Marie.
        # [Marie]It is?
        # [Alma]Eclair, you may take Marie to get some ice cream. Marie, I want you to stay with Eclair until you get there. Once you’re at the shop, I want you to wait for me till I come and pick you up. No wandering off, is that clear?
        # [Marie]Yes, Mom. I’ll be good, I promise.

        # MARIE JOINS THE PARTY!

    "Break the Promise":

        if immaturity >= 4:
            # [Eclair]Yeahhh…I forgot that I needed all of the money for something else. Sorry, I guess…
        else:
            # [Eclair]About that…I’m sorry, Marie, but I’m going to have to go back on my word. I really need the money to buy some other things. How about I bring you some ice cream when I come sit with you?

        # [Marie]But you promised! That’s not fair!

        if immaturity >= 4:
            # [Eclair]*Shrugs* It’s just ice cream.
        else:
            # [Eclair]I know….I know…sorry. I have some difficult decisions to make, and I’ve made them.  I never should’ve made that promise to you, and that was wrong of me.
        # [Marie]I…I…I….But…I…
        # [Alma]Marie, what’s wrong? I’m sure Eclair will find a way to make it up to you.
        # [Marie]I…I don’t think I’ve ever been this mad before.

        if immaturity >= 4:
            # [Eclair]You’ll get over it.
        else:
            # [Eclair]It’ll be alright.
        # [Marie]*Stares daggers at Eclair* I’m not going to forget this.
        # [L.R]How many days before that babysitting job?
        # [C.S]Why?
        # [L.R]Just wanna set my DVR to record that hot mess of a babysitting job with an angry and vengeful pre-teen.
        # [C.S]But reality will have changed again by then.
        # [L.R]And yet I have a distinct feeling a babysitting job will still happen.
        # [C.S]But….aaaaaah. The more things change…
        # [L.R]The more things stay the same. Hey, what are you doing?
        # [C.S]Setting my DVR.

        # [Marie]Any chance that you’ll change your mind?
        # [Eclair]Sorry, but no.
        # [Marie]Can’t blame me for trying.

# [Alma]You two take care now. I’ll be by to pick Marie up after I sit in the quiet for a bit and finish my coffee.
# [Marie]Yes, Mom.

# [Alma]That was rather cruel to break your promise like that, wasn’t it?
# [Eclair]Sorry. I’ll do better next time, I promise.
# [Eclair]Yeah. I goofed.
# [Alma]I just hope for your sake that she gets over it before you babysit.



# [Eclair]So what are you doing here, ma’am?
# [Alma]I’m just here to enjoy some coffee.
# [Eclair]And why is Marie not in school?
# [Alma]I just wanted to spend some time with my little gi-
# [Marie]Mom!
# [Alma]My youngest daughter.
# [Eclair]So Marie is truant, too? Then why did you blackmail me to babysit?
# [Alma]What makes you think I would have gone through with it?
# [Eclair]You were going to ask me to babysit anyways, weren’t you?
# [Alma]*Winks* I couldn’t resist having a little fun.










#Day 2, after finishing the choice between book or diapers (or both)
#Exterior, either the general store or the library, depending on the choice.

# [Eclair]Alright. Well now that I’ve got that business taken care of, what to do next. It’s still a little early to go home, yet. But there’s no chance I’m going back to school.
# [Eclair]Maybe I could go hang with Granny Vincenzia for a little bit. She’s always got some cookies to eat at least.
# [Eclair]He!We all ate the cookies the same day we wet our pants!
# [Eclair]What if Granny had something to do with it? Maybe that’s why she encouraged us to go bother Ranger Michael.
# [Eclair]She knew we were going to wet our pants and wanted us out  of her house before we made the connection! But Ranger Michael was acting kind of fishy too, come to think of it.
# [Eclair]He really didn’t want us to go into that old mine.  And there were those strange carvings on the wall. Why didn’t he  want us to see that?
# [Eclair]Maybe I should investigate one of them? I probably only have time for one of them.

#Player makes the choice between going to granny or the caves.

# [C.S.]Looks like someone is playing detective.
# [L.R.]Heh, heh, heh. “The Padded P. I.” Nice. Sounds like
# something you’d write.
# [C.S.]I’m not a writer.
# [L.R.]Dude, I’ve read your diary, remember? You have the soul of a poet.
# [C.S.]And yesterday I found your erotic fan-fiction on the web…
# Really man? Really?
# [L.R.]What? I was bored.
# [C.S.]Those were classic cartoon characters, man! Have you
# no decency?
# [L.R.]Nope. Anyways, should we alert the boss?
# [C.S.]Nah. Let her have her fun. It’s not as if she can do anything about it.

#Player chooses granny:

#Player Chooses the caves:

# [Eclair]The wall doesn't seem different...
# A comforting warmth is emanating from the carving. Inviting you to touch it. Do you?

menu:
    "Touch the carving?"

    "Yes":

        if immaturity >= 10:

            ecl "That’s odd…I don’t feel any different."

        else:
            ecl "Mmmmm….niiiiice."
            "{i}As soon as Eclair lays her hand on the wall, a stream of urine escapes into her diaper. She doesn't even pay attention as a strange and pleasant feeling overwhelms her.{/i}"
            $ immaturity +=1


    "No":
        ecl "I better not."

ecl "Well...Nothing here, I should investigate Ranger Michael's house."

#Eclair continues with investigating Ranger Michael

#Exterior, Ranger cabin

# [Eclair]Hello? Ranger Michael? Helloooo? Good. He’s not here. Maybe there’s some evidence here to connect him with the strange things going on.

#Door sound effect

# [Eclair]Huh…a universal animal call. That’s interesting. It’s not much to go on. Might be nothing. But just in case…
# []*Eclair slips the animal call into her back pack.*
# [Eclair]Uh oh! Someone’s coming! Gotta hide!

#Door sound effect

# [Ranger Michael]Here we are my little feathered friend.
# []Chirp Chirp Chirp.
# [Ranger Michael]Now let’s see. Why aren’t you flying?
# []*Ranger Michael examines the bird.*
# [Ranger Michael]I don’t see any signs of injury. No broken wings or anything. But why…
# []Chirp Chirp Chirp!
# [Ranger Michael]Huh? That’s odd. You’re a full grown adult, but you’re begging for food like you’re a hatchling.
# [Eclair]*Gasp* (Adults being treated younger than they are! That’s too close to home to be a coincidence.)
# [Ranger Michael]You’re not the only one lately, either, little friend. I keep finding all sorts of critters acting strange near the old abandoned mine. I wonder what’s going on. Is this some kind of new disease? Like rabies? Or baby rabies? Babies? Heh…naw. Still.
# [Eclair](Oh no! What if that’s what’s causing this. Maybe I’ve caught some kind of disease.)
# []Chirp Chirp Chirp!
# [Ranger Michael]Okay, okay. I’ll feed you…like a hatchling. Just let me get my eye dropper and my bird puppet. If you’re going to do something ridiculous, you might as well do it right.
# [Eclair](Now’s my chance! Gotta make a break for it!)
# [Ranger Michael]What was that?
# [L.R]Huh…it’s affecting the woodland critters too?
# [C.S]Minor side effects from altering reality and siphoning off maturity. Their statistical outliers at most.
# [L.R]Still, you don’t think we’re getting sloppy, are you? Like this P.O.S. machinery isn’t breaking down or anything.
# [C.S]You’re the one that whacks it all the time.
# [L.R]Not my point. You don’t think that it’s getting less…picky… about what it regresses, do ya? Like maybe that’s why this Eclair chick still realizes that something’s different?
# [L.R]Maybe parts of her regression is being passed on to the animals in the woods.
# [C.S]I’m not sure, to be honest. Nothing we can do about it now, anyways. We just have to stay the course.
# [L.R]Yeah, but what if it starts regressing us, too? What if we start to act less mature?
# [C.S]You’re already criminally immature and irresponsible. How would it be possible to notice the difference?
# [L.R]Touche, salesman.

#Choice between the mayor and Valerie

# [Eclair]Well, something strange is definitely going on, here. But I’ve got a feeling I’ve investigated the wrong person.
# [Eclair]Time to go after some bigger fish. Let’s see, something strange is definitely going on over this whole island. If anyone knows something, it’s probably Mayor Knox.
# [Eclair]*Looks down below her waist. Pokes her diaper.* Then again, diapers and baby stuff definitely have something to do with this. Who would know more about that than Valerie?
# [Eclair]It’s starting to get late though. Mom will want me home for dinner. I only have time for one.

menu:
    "Who do you investigate next?"

    "Mayor Knox":

    "Valerie":



#End of Day 2

#Eclair returns home

    if skippedSchool == true:


        # [Eclair]Hi Mom! I’m home in time for dinner!
        # [Marna]...
        # [Eclair]How have you been?
        # [Marna]...
        # [Eclair]Something the matter?
        # [Marna]I just got off the phone with your teacher. Is there something you’d like to tell me?

        if immaturity >= 4:

            # [Eclair]Uh…no?
            # [Marna]Well it’s too late. I already know that you skipped school.
            # [Eclair]I couldn’t stay in school! There was so much important stuff to do today!
        else:

            # [Eclair]*Sigh* I was hoping you wouldn’t find out about that.
            # [Marna]You’ve got some serious explaining to do, young lady! You skipped out of school!
            # [Eclair]Wait! I can explain! It’s complicated! Weird things have been happening and I had to get out and figure out what was going on. Some things are more important than a single day at school!

        # [Marna]And did you do any of these really “important” things during school hours?
        # [Eclair]...Maybe
        # [Marna]What do you mean, “maybe”?
        # [Eclair]*Looks back at her backpack* I don’t know if that stuff is important yet because I haven’t gotten a chance to look at it, yet.
        # [Marna]Well then what DID you do during school hours?
        # [Eclair]*Gulps*I got a part time job and I bought some stuff.
        # [Marna]*shakes her head* I am so ashamed of you right now.

        if messyAccident == true:

            # [Marna]*sniffs* What’s that smell? Is that…is that coming from you?!
            # [Eclair]Wait, I can totally explain that!
            # [Marna]*Taps foot* I’m listening….

            if immaturity >= 4:

                # [Eclair]I was hiding somewhere, and I didn’t want to get up to go poop.

            else:

                # [Eclair]Y’know what, it doesn’t sound any better in my head. Nevermind.

        # [Marna]That’s it, I’ve just about run out of patience with you. You’re grounded.
        # [Eclair]Grounded?! But Mom! I’m a nearly an adu-!

        if immaturity >= 4:

            # [Marna]Not right now, you aren’t! And before you can even think about skipping out of this house again, I’ll be taking your pants,little missy!

        else:

            # [Marna]Not right now, you aren’t! And before you can even think about skipping out of this house again, I’ll be taking your pants, young lady!

        # [Eclair]What? No! Get away!(Mom’s gone bonkers!)
        # [Marna]GOTCHA!

        if messyAccident == true:

            #Show messy time out picture

        elif: wetAccident == true:

            #Show wet time out picture

        else:

            #Show clean time out picture


        # [Marna]If you’re going to act like some irresponsible little brat, I’m going to treat you like one. You’re in time out, and then you’re going to bed without your dinner.

        if messyAccident == true:

            # [Eclair](Ugh! No! This is so gross! I’m just… I’m just…sitting in my own…ewwww!  So mushy!)

        # [Marna]And before you even think of it, I’ll have you know that I’ve already raided your closet and taken away anything that could preserve your modesty.
        # [Marna]If you want to get out of this house, you’ll be prancing through town so that everyone can see you in your diaper.
        # [Eclair]But they’re not diapers! Their inconti-
        # [Marna]Oh, they’re diapers right now! If you act like a little kid, I’m going to call them what little kids call them!

        if messyAccident == true or wetAccident == true:

            # [Eclair]*sniff* Can you at least change me?
            # [Marna]What?! Don’t be ridiculous! You change yourself before bed, little missy.

    else:

        # [Eclair]Hi mom! I’m home from school.
        # [Marna]Welcome home, honey. Is everything alright?
        # [Eclair]Yeah. Fine. Why?
        # [Marna]Is there something you need to tell me?
        # [Eclair]Could you be more specific?
        # [Marna]Your teacher called me today. She told me there was an …incident at school and you were excused.

        if immaturity >= 4:

            # [Eclair]Oh…that...Please don’t be mad.
            # [Marna]Why would I be mad?
            # [Eclair]I peed my pants in front of everyone. Like a…like a baby.

        else:

            # [Eclair]Oh…that...I was hoping you wouldn’t find out about that.
            # [Marna]Whatever for? You know you don’t have to keep secrets from me.
            # [Eclair]Really? You told me not to be ashamed of…this. *gestures to her padded behind*.
            # [Eclair]You lock me out of the house so that I’d have to go to school…and then I have a complete breakdown in front of my whole class. You don’t think I’d want to keep that to myself?

        # [Marna]Honey, I’m not mad about that. You couldn’t help that. There was no way you could have predicted that at all. But I am proud that you apparently managed to keep busy the rest of the day. What did you do?

        if immaturity >= 4:

            # [Eclair]You know the usual…went to the library…went to the store.
            # [Marna]And did you have fun?
            # [Eclair]Kinda, yeah.
            # [Marna]Well surely that didn’t take you all day. What else did you do?
            # [Eclair]I went off on a little adventure of my own. Y’know. Spy stuff.

        else:

            # [Eclair]Well, I did a little odd jobs, and I happened to run across Marie and her mother.
            # [Marna]Oh?How is Alma, anyway?
            # [Eclair]She’s good. I might be babysitting Marie with Mishelle in a few days.
            # [Marna]Well that’s good news. What else?
            # [Eclair]I think I might have begun to figure out why I’ve been so… off lately. But I’d rather not get into it until I’m more certain.

        # [Marna]Well, as long as you feel the time was well spent and didn’t cause too much mischief with your free time, I’m happy for you.
        # [Eclair]Thanks, Mom. I am just so over today. It’s already older than the internet.
        # [Marna]Well I’m proud of you, anyways. Give me a hug.

        if messyAccident == true:

            # [Marna]*sniffs* Eclair, honey? Is that smell…? What is that smell?
            # [Eclair]Oh…yeah. I’d rather not get into that.  Is it okay if I skip dinner, take a shower and then go straight to bed?
            # [Marna]Sure honey...sure.
            # [Marna]What has gotten into her lately?

        else:

            # [Eclair]Mom, would it be okay if I skipped dinner and just went straight to bed?
            # [Marna]Sure, dear. Go right on ahead.
            # [Marna]That girl…






#Interior, Eclair's Bedroom (Day 2 version)

# []A quick shower and change later...

if skippedSchool == true:

    if immaturity >= 4:

        # [Eclair]*Huff* WHAT?!

    else:

        # [Eclair]Come in.

    # [Eclair]Oh, hey Mishelle.
    # [Mishelle]Hey, we came to visit and see how you were doing? We
    # didn’t notice that you slipped out until it was too late.
    # [Vince]Your Mom said it was okay if we came in to try and talk some sense into…

else:

    if immaturity >= 4:

        # [Eclair]Mommy?

    else:

        # [Eclair]Who is it?

    # [Mishelle]It’s just me.
    # [Eclair]Mishelle? What are you doing here?
    # [Mishelle]We came to check up on you. After what happened at school, we figured you’d need some friends.
    # [Vince]Yeah, your mom is definitely worried about…

# [Eclair]Eeeep!
# [Vince]You!
# [Vince]I’m sorry!  I’m sorry! I didn’t know you were just in your under… I mean your diap…I mean sorry! *To Mishelle* Why didn’t you tell me? I wouldn’t have come in.
# [Eclair]Ditto, Mishelle! I would have at least gotten under my blankets!
# [Mishelle]*Shrugs*What’s the big deal? We’re all best friends. Besides, she’s more covered up than when she’s wearing a bathing suit.
# [Eclair]That’s…actually…
# [Vince]Well…but…
# [Eclair]Huh…alright.
# [Vince]Yeah, good point. Still, sorry I barged in, Eclair.
# [Eclair]Apology accepted, Vince. So, how’d the rest of your day go?
# [Vince]Heh…kinda awesome.
# [Mishelle]I’m not sure if you fully registered it because of all the crazy that was going on, but Fiona got stuck on the toilet... [Vince]For hours. Carmella spiked her coffee with a nasty laxative and Maxwell put industrial fast acting superglue on the toilet seat.
# [Vince]Officer Ronald made Maxwell and Carmella try to pull her off, but she kept crying about how her delicate skin was going to get ripped off.
# [Mishelle]They eventually had to call Karlton’s lab to transport some super solvent or whatever.
# [Eclair]Ha!
# [Vince]But that’s not the best part.
# [Eclair]What was the best part?
# [Mishelle]Fiona didn’t  \iquite\i make it to the bathroom in time.
# [Eclair]You mean…?
# [Mishelle]She might’ve let a little…slip out before she managed to sit down.
# [Vince]She had a potty accident. Ruined her panties.
# [Eclair]Oh my gosh!
# [Mishelle]Wait, it gets better! Miss Georgette wouldn’t let her put the dirty underwear back on….
# [Vince]And of course she wasn’t going to be allowed to walk around in a skirt and no underwear…
# [Mishelle]And they tried calling her dad to come pick her up or bring her some new clothes, but he wouldn’t answer.
# [Vince]And of course the high school doesn’t have spare underwear on hand. That’s just not something they think about dealing with.
# [Mishelle]So guess who had the only “underwear” that could possibly fit her?
# [Eclair]*Gasp* You don’t mean…?!
# [Vince]That’s right. Miss Georgette made Fiona wear...
# [Eclair]A diaper?!
# [Mishelle and Vince]Yeah!
# [Mishelle]All day long!
# [Vince]All day long!
# [Mishelle]Everyone kept calling her a baby, and asking if she needed her diaper changed.
# [Vince]It was the textbook definition of irony. I’ve never seen her so pissed off.
# [Mishelle]I mean, I had to give up a diaper, but it was well worth it so that Fiona could see how she treats us.
# [Vince]Carmella got detention well into next year and Maxwell is going to have to replace that toilet seat, but they both agree it’s totally worth it.
# [Eclair]And I missed it.*sigh* figures.
# [Mishelle]So what did you get up to today?
# [Eclair]Oh yeah! Guys…there’s something important I need to tell you.
# [Vince]What?
# [Eclair]Come closer.
# [Eclair]Guys, I think something weird is going down on the island.
# [Vince]Like what?
# [Eclair]I think there’s a conspiracy going on the island.
# [Mishelle]What kind of conspiracy?
# [Eclair]I’m not sure, but…I think it has something to do…

#Pick between these two

# [Eclair]…with the old abandoned mine…
# [Eclair]…with why Granny Vincenzia never got married and had kids…

#And between these two

# [Eclair]…and a bunch of babies at the Daycare that never leave...
# [Eclair]… and something called “the harvest”…

# [Eclair]AND WE’RE NEXT!
# [Vince]...
# [Mishelle]...
# [Vince]Heh heh…
# [Mishelle]Hee-hee...
# [Vince]Hahahaha!
# [Mishelle]Ha ha! Hehehe..
# [Mishelle]Good one, Eclair!
# [Vince]You had us going for a second.
# [Eclair]No, I’m serious!
# [Vince]Seriously?

#If Eclair bought the baby diapers instead of the book

# [Eclair]Look, I’ll prove it. Just turn around, okay?
# [Mishelle]Okay.
# [Vince]*Shrugs* Sure.
# []*Eclair removes the package of baby diapers and opens them.*
# [Eclair]Aha! I knew it!
# [Mishelle]Can we turn around yet?
# [Eclair]Not yet. Gimme a second.
# [Eclair]BEHOLD!
# [Vince]Wow…Eclair…that’s really neat…I guess…
# [Mishelle]Yeah…really neat.
# [Vince]What are we looking at?
# [Eclair]…Seriously? You don’t see it?
# []Mishelle and Vince shake their heads.
# [Eclair]I saw these diapers at the general store, and they were labeled as baby diapers! But look they fit me!
# [Mishelle]I mean, yeah…kinda.
# [Vince]It’s a bit of a stretch, but yeah, it fits. Is this a way to tell us that you’re losing weight? Because you’re not fat.
# [Eclair]Huh? No! I mean this diaper fits me just as well as the other one.
# [Vince]No it doesn’t.
# [Mishelle]Not even close.
# [Eclair]Look at them! This one’s the adult diaper. This one’s the baby one.
# [Mishelle]Yeah we can tell.
# [Vince]Kind of obvious.
# [Eclair]Well yeah it’s obvious. This one has little baby decorations on it, and this one doesn’t. But that’s the only real difference.
# [Mishelle]And the one for kids is much smaller.
# [Vince]Much smaller.
# [Eclair]No it’s not! They’re virtually identical!
# [Mishelle]I’m pretty sure I could use that one as a stuffer for that one.
# [Eclair]You really don’t think they’re the same size?
# []Mishelle and Vince both shake their heads.
# [Eclair](Oh no! Whatever is affecting people’s memories is also affecting what they see, too.)

#If Eclair got both the book and the diapers

# [Vince]What else you got?
# [Eclair]Check this out!
# [Vince]That’s a book, alright.
# [Mishelle]Oh my! That’s impressive!
# [Eclair]Based on everything we’ve been through in the last two days, I am almost positive that there’s something in this island’s history, specifically tied to Dr. Harkness Milner that can explain why things have been so strange!
# [Mishelle]And what have you found?
# [Eclair]...What?
# [Vince]What have you read so far?
# [Eclair]I haven’t…I haven’t exactly had time to read it yet.
# [Vince]So you have no idea if your hunch has anything to back it up?
# [Eclair]No.
# [Mishelle]Aw, I’m sorry Eclair. Oooh, I know! I could read it for you! I take really good notes. It’d only take me a few days to do it.
# [Eclair]Ooooka…No. No thank, Mishelle. I think I need to this myself.
# [Vince]Do you have any other proof that things are so different than we remember them?
# [Eclair]...nothing.
# [Mishelle]Oh…well then.
# [Vince]Are you sure you’re okay? You’ve been acting kinda… How do I put this…?
# [Mishelle]Bonkers?
# [Vince]Mishelle…
# [Mishelle]Insane in the membrane?
# [Vince]Mishelle…
# [Mishelle]What? But you said…
# [Vince]MISHELLE! PRIVATE!
# [Mishelle]Ooops. Well, if you think you’re okay, Eclair, we think you’re okay.
# [Vince]We’ll see you around. Can I walk you home?
# [Mishelle]I don’t think I’ll get lost, if that’s what you mean.
# [Vince]That’s not what I mean, at all.
# [Mishelle]Is this because you’re avoiding going home and talking to your dad?
# [Vince]Mishelle…

#If Eclair only got the book?

# [Eclair]Check this out!
# [Vince]That’s a book, alright.
# [Mishelle]Oh my! That’s impressive!
# [Eclair]Based on everything we’ve been through in the last two days, I am almost positive that there’s something in this island’s history, specifically tied to Dr. Harkness Milner that can explain why things have been so strange!
# [Mishelle]And what have you found?
# [Eclair]...What?
# [Vince]What have you read so far?
# [Eclair]I haven’t…I haven’t exactly had time to read it yet.
# [Vince]So you have no idea if your hunch has anything to back it up?
# [Eclair]No.
# [Mishelle]Aw, I’m sorry Eclair. Oooh, I know! I could read it for you! I take really good notes. It’d only take me a few days to do it.
# [Eclair]Ooooka…No. No thank, Mishelle. I think I need to this myself.
# [Vince]Do you have any other proof that things are so different than we remember them?
# [Eclair]...nothing.
# [Mishelle]Oh…well then.
# [Vince]Are you sure you’re okay? You’ve been acting kinda… How do I put this…?
# [Mishelle]Bonkers?
# [Vince]Mishelle….
# [Mishelle]Insane in the membrane?
# [Vince]Mishelle…
# [Mishelle]What? But you said…
# [Vince]MISHELLE! PRIVATE!
# [Mishelle]Ooops. Well, if you think you’re okay, Eclair, we think you’re okay.
# [Vince]We’ll see you around. Can I walk you home?
# [Mishelle]I don’t think I’ll get lost, if that’s what you mean.
# [Vince]That’s not what I mean, at all.
# [Mishelle]Is this because you’re avoiding going home and talking to your dad?
# [Vince]Mishelle…


# [Eclair]I hate these dreams.
# [L.R.]Well tell ya what, just give us a few more nights and you’ll stop having them. Nothing but rainbows, and puppies, and fairy tales. Deal? Just lay back and relax.
# [Eclair]Man, you’re annoying.
# [C.S.]I know, right?
# [L.R.]Hey! Whose side are you on?
# [C.S.]What? She’s got a point.

# [Eclair]So what now?
# [L.R.]Oh believe me, you are not getting past this security program I set up. You’re better off if you just throw the fight.
# [C.S.]Actually, I’ve got this one. Computer: Initiate protocol- “Ghost House”.
# [L.R.]What?! The Ghost House Trap?! But you never finished that one!
# [C.S.]Even incomplete it’s more than she can handle. Now stand back, and watch how a master of regression does it.


$ puzzle2Win = false

if puzzle2Win = true:


    # [COMPUTER]Error. Error. Maturity Regression Subroutines compromised. Core Memory Breach.
    # [L.R.]Yeah, that showed me alright…
    # [C.S.]Shut up.
    # [COMPUTER]Memory Download Initiated. Accessing Most Recent Successful Harvest, Day 2.
    # [Eclair]What’s this?




    #End of day 2 flashback
    #Nusery in the matrix

    # [Mona]Miss Gans?
    # [Mona]Miss Gans?
    # [Mona]I need a little…urgh…help here.
    # [Valerie]I’m coming, Mona! Be right there. Tommy is just being a bit of a handful right now.
    # [Mona]Well, I need…a break…if you know what I mean.
    # [Valerie]I’ll be right there to relieve you, hon!
    # [Mona]Please don’t say relieve!
    # [Valerie]Just a second.
    # [Mona]Ugggh. No. Come on. Come on. I can’t….I can’t…I can’t…
    # [Valerie]You can’t what?
    # [Mona]Hold it!....oh no!
    # [Valerie]Okay, I’m here. What’s up?
    # [Mona]I….I….I…
    # [Valerie]Mona? What’s wrong honey?
    # [Mona]I…I had…an accident.
    # [Valerie]So? That’s why you wear your incontinence briefs, Mona. Everybody knows about your urinary incontinence. I knew it when I agreed to take you in as my intern.
    # [Valerie]*sniff* But I think one of the little ones had a different kind of accident.
    # [Valerie]Now which one of you little stinkers was it?
    # [Mona]Miss Gans.
    # [Valerie]Was it you?
    # [Mona]Miss Gans...
    # [Valerie]Or you?
    # [Mona]Miss Gans...
    # [Valerie]What about…?
    # [Mona]It was me.
    # [Valerie]You? But Mona, you told me you were only urinary incontinent.
    # [Mona]I am, ma’am. I just…I just had an accident.
    # [Valerie]How did that happen?
    # [Mona]I just needed to go, but I couldn’t leave the little ones alone… And by the time you came, it was too late.
    # [Valerie]Oh, you poor thing. Tell you what. Go use one of the tubs and get yourself cleaned up. Then when you’re done, you can take the rest of the day off and go home.
    # [Mona]Are…are you sure?
    # [Valerie]Sure as sure can be. Now get to it. I don’t want my favorite intern to get a rash.
    # [Mona]…Yes ma’am…
    # [Valerie]Oh, and Mona?
    # [Mona]Yes, Miss Gans?
    # [Valerie]You don’t have any kids, do you?
    # [Mona]No! Of course not!  I’m barely out of high school. I don’t even have a boyfriend right now. Why do you ask?
    # [Valerie]Oh, no reason. Just checking.
    # [Mona]Checking what?
    # [Valerie]I meant, “Just wondering”. Idle curiosity is all.
    # [COMPUTER]End Memory Download.

else:

    # [COMPUTER]Process Complete. Begin reality overwrite of previous day.

    # [Eclair]I! Want! My! Mamma!
    # [Teacher]*on the phone* Hello, Miss Marna? We’ve got a slight problem. Little Eclair just had another big accident, and we’re fresh out of diapers for her.
    # [Teacher]Would you mind running some over to us? Even better, would you mind picking her up? She doesn’t have a fever, but her last few have been a little…runny.
    # [Teacher]I think she might be coming down with something. I’ll write her a pass excusing her for the day. Okay, thank you very much.
    # [Vince]Bye bye!
    # [Mishelle]Bye Eclair! I hope you feel bettah!
    # [Eclair]Wait! That never happened! That never happened at all!

    return
