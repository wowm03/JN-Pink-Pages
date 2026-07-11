init 999 python:

    t = get_topic("talk_judgement")

    if t:
        t.player_says = True
        t.nat_says = False

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_judgement",
            unlocked=True,
            prompt="Other people's judgements",
            category=["Life", "You", "Natsuki"],
            player_says=True,
            nat_says=False,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_judgement:

    n 3tnmfl "Remember when I mentioned how my{w=0.25}{nw} "
    extend 6nslpu "{i}friends{/i}{w=0.5}{nw}"
    extend 3cdwaj " would be all judgey with me whenever I bring up manga?"
    n 3fcsun "...{w=1.75}"
    extend 3fdtem " it's just so{w=0.2}{nw}"
    extend 3fllaj " {i}stu{/i}{nw}"
    extend 3fupaw "{i}u{/i}{nw}"
    extend 3fsrdr "{i}pid{/i}{nw} "
    extend 3ccsfl "when people trash on something they've never even tried."
    n 3fcsun "Like, {w=0.75}{nw}"
    extend 6csqan "how can you have such a strong opinion about something you know {i}nothing{/i} about?"
    n 3fplem "And it's not just manga,{w=0.2} you know?"
    n 3ccsfl "It's everything."
    n 7cllaw "Food, {w=0.5}{nw}"
    extend 7flrfl "music, {w=0.5}{nw}"
    extend 3fsqem "even {i}people{/i}."
    n 2ndtfl "Someone says{w=0.5}{nw}"
    extend 4fbksc " 'Amy is gross!'{w=0.7}{nw}"
    extend 2nslfl " and suddenly everyone repeats it like parrots."
    n 2tsrbg "But ask them to name{w=0.5}{nw} "
    extend 6tplaj "{i}one{/i}{w=0.5}{nw}"
    extend 3ndtem " specific thing they don't like about her?"
    n 2ccspuesp "Crickets."
    n 2csgaj "Or worse,{w=0.75}"
    extend 6cuntr "{i}'I don't need to.{w=0.2} Everyone knows she's gross.'{/i}"
    n 2ccsfu "Ugh, {w=0.3}{nw}"
    extend 2fsrem "that attitude makes me so mad."
    n 2nsqsl "Like, {w=0.3}{nw}"
    extend 4cdtem "congratulations on having zero curiosity and borrowing your opinions from the nearest random person."
    n 7tsglg "You know what I respect?"
    n 3nsqfl "Someone who actually{w=0.5}{nw}"
    extend 6cnmfl " {i}tries{/i}{w=0.7}{nw} "
    extend 2cslpo "something."
    n 2fcsfr "That's it.{w=0.25}{nw}"
    extend 2kslfl " That's all I ask for."
    n 3kllfl "Even if they don't like it and say, {w=0.5}{nw}"
    extend 6ncsaj "'Okay{w=0.5}, I've tried this but it's not for me.'{w=0.75}{nw}"
    extend 4knmbg " It's completely fine for me."
    n 6nslaj "I don't like horror manga{w=0.5}.{nw} "
    extend 3ksgss "Doesn't mean horror manga is bad.{w=0.7}{nw}"
    extend 3ckrpo " It's just not for me."
    n 6ccsss "See how easy that is? People act like disliking something means it's objectively garbage."
    n 1knmaj "You don't have to like what I like."
    n 2flraj "Just don't be a jerk about things you haven't even tried."
    n 2fcssf "..."
    extend 1kslfr "..."
    n 4kcsfl "...Sorry."
    n 2kcsfl "It just...{w=0.75} gets to me sometimes."
    n 2tkrfs "But...{w=0.75}{nw}"
    extend 3usqbg " you know what I've figured out?{w=0.75}"
    n 6fcsbg "Those people? "
    extend 7fsqbs "Total waste of my time."
    n 6ttlfl "If someone's too lazy to form their own opinions?"
    n 3fcsbg "That's a {i}them{/i} problem.{w=0.25}{nw}"
    extend 7twmbg " Not mine."
    n 3ncstr "I'd rather have one person who actually {i}thinks for themselves{/i}...{w=0.7}{nw}"
    extend 3nsrpo " than a hundred parrots.{w=0.75}"

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 1knmbgl "And you're exactly that person for me."
        n 4usrfll "That's...{w=0.3}{nw}"
        extend 3fcsbgf " that's why what I feel for you is real."
        n 4kwmssl "Because you're not one of the parrots."
        n 4fklbgl "I know what you feel for me is real too."
        n 6fcsbsf "I mean{w=0.25}, you come here practically screaming about how much you love me every single day, {w=0.7}{nw}"
        extend 3fsqdvl "ehehe."
        n 4kwmbgl "So when I say 'I love you'?...{w=0.5}{nw}"
        extend 4kcssmf " I actually mean it."
        n 4nwmbgfeaf "...Love you too, [chosen_tease]."

    elif Natsuki.isEnamored(higher=True):
        n 2tchbg "I'm pretty sure you're like that."
        n 2udlbg "I don't think you just repeat what everyone else says."
        n 4ccsfll "That's...{w=0.3}{nw}"
        extend 5cdrfll " part of why I like having you around so much."
        n 2cwmeml "So...{w=0.3} thanks for being you,{w=0.5}{nw} "
        extend 2csrcal "I guess."
        n 2fslpul "Just don't let it get to your head or anything, {w=0.5}{nw}"
        extend 4fbkeml "ya' hear me?!"

    elif Natsuki.isHappy(higher=True):
        n 2tllaj "I think you're like that."
        n 7tsqbg "That's kinda rare, you know?"
        n 2nsraj "So...{w=0.5} "
        extend 2nsqbg "yeah."
        n 2cnmaj "Keep staying this way,{w=0.5}{nw}"
        extend 3fchssean " or else."


    else:
        n 2twmfl "But...{w=0.3} you're not like those parrots, are you?"
        n 4cdlem "I mean...{w=0.3} you wouldn't just judge something without trying it first{w=0.5}, right?"
        n 2cdrfl "And you're not the type to just repeat what other people say without thinking,"
        n 4tsqfl "... right?"
        n 2nsrun "..."
        n 2tslaj "Just checking."

    return

default persistent.player_likes_horror = None

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_scari",
            unlocked=True,
            prompt="Why do you hate horror?",
            category=["Natsuki"],
            player_says=True,
            nat_says=False,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_scari:
    if get_topic("talk_scari").shown_count > 0:
        n 7tdtaj "Huh..?"
        n 3tsqfl "Hey... didn't we talked about this already?"
        n 3csrpo "..."
        n 2ccspo "Hmph...{w=0.35}{nw}"
        extend 2nwmpo " fine...{w=0.4}{nw}"
        extend 2nsqss " I'll humour you and tell you again."
    else:
        n 3tnmfl "You wanna know why I don't like horror?"
    n 3cslpol "...{w=0.35}"
    n 1fcseml "I-{w=0.2}it's not even that it scares me.{w=0.5}"
    n 2fsrpul "Well...{w=0.3}{nw}"
    extend 2fcspul " okay,"
    extend 5cllajless " {size=12}maybe just a little bit.{/size}{w=0.3}{nw}"
    n 4ccsajl "B-{w=0.2}{nw}"
    extend 4fbkeml " but that's not the main thing!"
    n 2cllfl "Horror makes me feel...{w=0.75}{nw}"
    extend 4ccssf " powerless."
    n 2cdlaj "Like, {w=0.3}{nw}"
    extend 2ccsup "what's the point?"
    n 3clrfl "Someone gets chased.{w=0.55}{nw}"
    extend 4kllem " Someone gets hurt.{w=0.55}{nw}"
    extend 4kwmss " Maybe they survive.{w=0.7}{nw}"
    extend 4ccsun " Maybe they don't.{w=0.55}"
    n 3fnmem "And for what?"
    n 4cdlpu "Just...{w=0.3}{nw}"
    extend 2kcsfl " suffering for entertainment."
    n 2klrsr "...{w=0.35}"
    n 2kwmss "I like stories where people get a chance to actually{w=0.35}{nw} "
    extend 6ccsaj "{i}solve{/i} things."
    n 3klrss "Where kindness matters. "
    extend 4fsqbg " Where cleverness wins."
    n 4kdwss "Where characters help each other instead of just...{w=0.7}{nw}"
    extend 2cslca " running and screaming."
    n 4cdrfl "Anyone can draw blood."
    n 6ccsss "It takes skill to make me cry over a character being {i}happy{/i}."
    n 4cdlfl "Horror just feels...{w=0.35}{nw}"
    extend 2ccsem " mean."
    #yo change expression
    n 2kwmss "Why did {i}you{/i} ask?"
    extend 2kwmss "That's the real quesiton."
    show natsuki option_wait_curious
    menu:
            n "Do {i}you{/i} like horror or something?"

        "Yes.":
            $ persistent.player_likes_horror = True
            n 1tnmpu "..."
            n 2nllaj "Okay, so..."
            n 2kchbgesd "I don't get it."
            extend 2ksrssess " Like, at all."
            n 2nchgn "But you do you!"
            n 4nslss "I just...{w=0.35}{nw}"
            extend 2ccsdveso " don't understand how anyone enjoys being scared."
            n 2ckraj "But I mean...{w=0.45}{nw}"
            extend 2nsqbg " I'm not gonna judge you for it."
            if get_topic("talk_judgement").shown_count > 0:
                n 7ttlss "That would make me a hypocrite, wouldn't it?"
                n 3tchbselg "After everything I just said about people judging stuff they don't like."

            else:
                n 2fchgn "Ehehe."

            n 2tllaw "So...{w=0.35}{nw}"
            extend 7tnmbg " what do you like about it?"
            n 7tsqss "Is it the {cps=0}adrenaline?{/cps}"
            extend 6csqbg "The {cps=30}suspense?{/cps}"
            n 7twrbg "Or do you just like watching people make bad decisions and get eaten?"
            n 2nchsm "Ehehe."

        "No.":
            $ persistent.player_likes_horror = False
            n 2kwmss "For real?!{w=0.5}{nw}"
            n 2kwmss " Like, you're not just saying that?"
            n 2kwmss "I thought I was the only one!"
            n 2kwmss "This is so nice."
            n 2kwmss "Finally, someone with actual taste."
            n 2kwmss "You have no idea how refreshing this is."
            n 2kwmss "Because I'm {i}so{/i} done with people trying to convince me to watch scary stuff."
            n 2kwmss "You and me?{w=0.35}{nw}"
            extend 2kwmss " {i}We{/i} can watch something actually good."


    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 2tsqpu "..."
        show natsuki 2tsqsm at jn_center
        n 3fkrbgl "And wow, you're{w=0.45}{nw}"
        extend 4fcsawl " {i}suuucchh{/i}{w=0.35}{nw}"
        extend 7tsgssl " a sweetheart for asking,{w=0.5}{nw}"
        extend 3uchgnl " ehehe."
        n 3nsrss "Most people don't care about the reason."
        n 7tnmfl "They just say{w=0.35}{nw}"
        extend 6tcsem " 'you're being dramatic'{w=0.35}{nw}"
        extend 3nslaj " or{w=0.29}{nw}"
        extend 6ttrgs " 'it's not even scary.'"
        if persistent.player_likes_horror == True:
            n 3nslpo "...{w=0.5}"
            n 7tdtpu "Why did you ask that initially anyway?{w=0.35}"
            n 3fchbgean "I swear, if you're planning to make me watch one with you."
            n 7tsgsm "But...{w=0.35}{nw}"
            extend 3fchgn " pretty sure you just wanna know more about me,{w=0.5}{nw}"
            extend 3uchsml " ehehe."
            n 4flrpol "It better be that, or else.{w=0.35}"
        elif persistent.player_likes_horror == False:
            n 2uchbg "Glad you're on the same page with me, though."
            n 4fspsm "We're on the same team!"
            extend 2fcsctl " As we should be, {w=0.4}{nw}"
            extend 2nchgnl "ehehe."
        else:
            n 3nslpo "...{w=0.5}"
            n 7tdtpu "Why did you ask that initially anyway?{w=0.35}"
            n 3fchbgean "I swear, if you're planning to make me watch one with you."
            n 7tsgsm "But...{w=0.35}{nw}"
            extend 3fchgn " pretty sure you just wanna know more about me,{w=0.5}{nw}"
            extend 3uchsml " ehehe."
            n 4flrpol "It better be that, or else.{w=0.35}"
        n 2fwlbgl "Love you too, [chosen_tease]."
#maybe add the persistent thing haha
    elif Natsuki.isEnamored(higher=True):
        n 2fchbgl "You're sweet for asking at first, though."
        n 2fsqsm "Most people just tell me I'm being a baby about it."
        n 4fcspxa "So...{w=0.5}{nw}"
        extend 4fcspxa " thanks for asking."
        n 3fcssm "It's nice that you actually want to know about what I think."
        n 3fsqsm "That means a bunch! Ehehe."

    elif Natsuki.isHappy(higher=True):
        n 4fchbgl "You're not gonna try and make me watch one, are you?"
        n 3fcssm "Cause that's a hard no."
        n 4fchbgl "But...{w=0.5}{nw}"
        extend 4fcspxa " thanks for asking, I guess."
        n 3fsqsm "It's kinda nice to get that off my chest."

    else:
        n 4fsqsm "So...{w=0.5}{nw}"
        extend 4fsqbg " yeah."
        n 3fcssm "That's my answer."
        n 3fsqsm "Don't expect me to watch one with you or anything."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feminism",
            unlocked=True,
            prompt="What do you think about feminism?",
            category=["Daily Life", "Life"],
            player_says=True,
            nat_says=False,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feminism:
    n 4tnmajeqm "Huh?{w=0.35}{nw}"
    extend 2tnmpu " Feminism?{w=0.4}"
    n 3nllpu "That's...{w=0.55}{nw}"
    extend 7unmgs " a big question."
    n 4tsrtr "But...{w=0.25}{nw}"
    extend 2fcsbg " yeah{w=0.25}, I'm on board."
    n 3knmfl "I mean...{w=0.5}{nw}"
    extend 3fcsup " look at how people treat me."
    n 7cllaw "If I get angry?{w=0.5}"
    extend 7fsqem " I'm 'moody' or 'hysterical.'"
    n 6tsrfl "If I speak up?{w=0.5}"
    extend 2cuppo " I'm 'bossy.'"
    n 2csraj "If a guy did the same thing? {w=0.65}{nw}"
    extend 2ccsan "He's {w=0.1}{nw}"
    extend 6ctlem "'passionate' and 'confident.'"
    n 2fsrem "It's so dumb."
    n 3ccswr "And don't even get me started on the {w=0.75}{nw}"
    extend 6csqaj "'cute' {w=0.25}{nw}"
    extend 3nslbo "thing."
    n 2cklfl "I like pink. {w=0.35}{nw}"
    extend 6cllem "I like cute stuff. {w=0.4}{nw}"
    extend 3fcsun "So what?"
    n 2ndtfl "That doesn't mean I'm weak or inferior."
    n 6tsqfl "And you know those people who act like feminism is just 'hating men'?"
    n 4fcsup "They've just never actually listened to anyone talk about it."

    n 4fcsup "Now don't you dare get me wrong, okay?"
    n 4fcsup "It's not like I don't think guys deserve those positive labels too."
    n 4fcsup "They do."
    n 4fcsup "A guy can be passionate. A guy can be confident. That's not a bad thing."
    n 4fcsup "But it {i}is{/i} unfair how the same behavior gets judged differently depending on who's doing it."
    n 4fcsup "That's what feminism is about to me."
    n 4fcsup "Not 'women good, men bad.'"
    n 4fcsup "It's about...{w=0.35}{nw}"
    extend 4fcsup " everyone being able to be themselves without stupid stereotypes getting in the way."
    n 4fcsup "Like...{w=0.3}{nw}"
    extend 4fcsup " guys should be able to like cute stuff too without getting made fun of."
    n 4fcsup "They should be able to show emotions without being called 'weak.'"
    n 4fcsup "That's not fair to them either."
    n 4fcsup "It's about...{w=0.5}{nw}"
    extend 4fcsup " being treated like a person."
    n 4fcsup "That's it."
    n 4fcsup "Not being dismissed because of your gender."
    n 4fcsup "Not having your opinions ignored."
    n 4fcsup "Not being judged for what you like or how you dress."
    n 4fcsup "So, yeah."
    n 4fcsup "I guess I {i}am{/i} a feminist."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 4klrbgl "..."
        n 3knmpol "You know what I really appreciate about you?"
        n 4klrpol "You've never once made me feel like I'm 'too much.'"
        n 4klrbgl "You just...{w=0.3}{nw}"
        extend 4klrpol " treat me like a person."
        n 4flrpol "So...{w=0.5}{nw}"
        extend 4klrbgl " thanks for that."
        n 3klrpol "It's part of why I love you, [chosen_tease]."
        n 4flrpol "You treat me like an equal."
        n 4klrbgl "And that means everything."
        n 4klrbgl "Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 2fchbgl "You're kinda nice to talk to about this."
        extend 2fsqsm "Since you actually listen."
        n 4fcspxa "Most people just tell me I'm overreacting."
        n 3fsqsm "So...{w=0.5}{nw}"
        extend 3fchbgl " thanks for that."
        n 4fcssm "Ehehe."

    elif Natsuki.isHappy(higher=True):
        n 4fchbgl "You know..."
        n 4fcssm "You're one of the few people who actually listens when I talk about stuff like this."
        n 3fsqsm "Most people just nod and change the subject."
        n 4fchbgl "So...{w=0.5}{nw}"
        extend 4fcspxa " thanks for being cool about it."
        n 3fcssm "Ehehe."

    else:
        n 4fsqsm "So...{w=0.5}{nw}"
        extend 4fsqbg " yeah."
        n 3fcssm "That's what I think."
        n 3fsqsm "It's not complicated."
        n 4fchbgl "Ehehe."

    return

label talk_menstruation:
    n 2tslpu "Huh?{w=0.75}{nw}"
    extend 2csqfl " Is it rude to ask about periods?"

    n 4fcsun "......"
    n 4fslbo "....."

    n 3ftrrc "That's...{w=0.5}{nw}"
    extend 3fcspxa " actually a really good question."

    n 7cspxs "Okay, so..."
    n 7csqgo "Here's the honest answer."

    n 4ftrrsd "It depends."

    n 2cspxa "If you're asking because you actually {i}care{/i}?"
    n 2fsqsm "Not rude at all."
    n 4fcspxa "If you're asking to be weird or gross or make someone uncomfortable?"
    n 4fcsup "Yeah, that's rude."

    n 3knmfl "Context matters, you know?"

    n 7tslfl "Like...{w=0.5}{nw}"
    extend 7fcspxa " if someone's clearly in pain or having a rough day?"
    n 4ftrrc "Asking 'hey, are you okay? do you need anything?'"
    n 4fsqsm "That's not rude. That's called being a decent person."

    n 2cspxs "But if you just walk up to someone and go 'hey, you on your period or something?'"
    n 2fsrem "Yeah, that's rude."
    n 2csqem "Don't do that."

    n 4fcspxa "Also?{w=0.75}{nw}"
    extend 4fsqsm " Don't ask in front of other people."
    n 4ftrrsd "That's just embarrassing for everyone involved."

    n 7fchbgl "So...{w=0.5}{nw}"
    extend 7fsqbg " the short version?"
    n 3fcssm "Ask if you care. Not if you're trying to be funny."
    n 3fsqsm "And definitely don't use it as an insult."

    n 4fcsun "..."
    n 4fslbo "......"

    n 2fsqsm "But you?"
    n 2fcspxa "You're asking because you actually want to know."
    n 4fchbgl "That's...{w=0.3}{nw}"
    extend 4fcssm " kind of nice, actually."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 4klrbgl "Most people don't bother to think about stuff like this."
        n 3knmpol "They just...{w=0.3}{nw}"
        extend 3kllfl " assume or make jokes or avoid it completely."
        n 4klrpol "But you?{w=0.5}{nw}"
        extend 4klrbgl " You actually want to get it right."
        n 3klrpol "That's...{w=0.3}{nw}"
        extend 4klrbgl " that's why I love you, [chosen_tease]."
        n 3knmpol "Because you care about getting things right."
        n 4flrpol "Not just for me, but in general."
        n 4klrbgl "So...{w=0.5}{nw}"
        extend 4klrpol " keep asking questions like this, okay?"
        n 3klrpol "The world needs more people who {i}think{/i} before they speak."
        n 4flrpol "Love you, dummy.{w=0.5}{nw}"
        extend 1klrbgl " Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 2fchbgl "You're...{w=0.3}{nw}"
        extend 2fslbo " actually really sweet for asking."
        n 2fsqsm "Most people don't care if it's rude or not."
        n 4fcspxa "They just...{w=0.3}{nw}"
        extend 4csqfl " say whatever."
        n 3fcssm "So...{w=0.5}{nw}"
        extend 3fchbgl " thanks for being thoughtful."
        n 3fsqsm "That means a lot."
        n 4fcssm "Ehehe."

    elif Natsuki.isHappy(higher=True):
        n 4fchbgl "You know..."
        n 4fcssm "You're kinda sweet for asking this."
        n 3fsqsm "Most people just don't think about it at all."
        n 4fchbgl "So...{w=0.5}{nw}"
        extend 4fcspxa " here's the short version:"
        n 3fsqbg "Ask if you care. Don't be weird. Don't do it in public."
        n 4fcssm "That's literally it."
        n 3fchbgl "See? Not that hard."
        n 4fcssm "Ehehe."

    else:
        n 4fsqsm "So...{w=0.5}{nw}"
        extend 4fsqbg " yeah."
        n 3fcssm "That's my answer."
        n 3fsqsm "It's not rude if you actually care."
        n 4fchbgl "And you seem like you care, so..."
        n 3fcssm "you're fine."
        n 3fsqsm "Thanks for asking, though."
        n 4fcssm "Seriously."

    return
YOURE THOUGHTFUL, CARING,
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_period_care",
            unlocked=True,
            prompt="How should I treat you when you're on your period?",
            category=["Daily life", "Health"],
            player_says=True,
            nat_says=False,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_period_care:
    n 2tslpu "Huh?{w=0.75}{nw}"
    extend 2csqfl " How to...{w=0.3}{nw}"
    extend 4ccsem " treat me?"

    n 2fcsun "......"
    n 2fslbo "....."

    n 4csqfl "That's...{w=0.5}{nw}"
    extend 4fslfl " actually really thoughtful."

    n 3fcsun "Okay, so..."
    n 3fcspxa "Here's the thing."

    n 7ftrrc "First of all?{w=0.75}{nw}"
    extend 7fsqbg " Don't be weird about it."
    n 4ftrrsd "Like, don't act grossed out or change the subject when I mention it."
    n 4csqfl "It's a normal thing.{w=0.5}{nw}"
    extend 4fsqem " Half the population deals with it."

    n 2cspxa "Second?"
    n 2fsqsm "Ask what I need."
    n 7fcspxa "Sometimes I want snacks. Sometimes I want a heating pad."
    n 7fslfl "Sometimes I just want to be left alone."
    n 3knmfl "And all of those are okay."

    n 4ftrrc "Third?{w=0.75}{nw}"
    extend 4fcsup " Don't say 'you're being dramatic' or 'it can't be that bad.'"
    n 4ftrrsd "Because trust me...{w=0.5}{nw}"
    extend 4csqem " it {i}can{/i} be that bad."

    n 3fchbgl "Fourth?{w=0.75}{nw}"
    extend 3fcssm " Snacks."
    n 3fsqbg "Chocolate. Warm drinks. Maybe some cupcakes if I'm feeling ambitious."

    n 2fcspxa "And fifth?...{w=0.5}{nw}"
    extend 2fslbo " Just be patient with me."
    n 2kcsfl "If I snap at you for no reason?"
    n 4fslfl "I probably don't mean it."
    n 4kcsfl "I'm just...{w=0.3}{nw}"
    extend 4fslbo " tired and crampy and over it."

    n 7fcspxa "But honestly?{w=0.75}{nw}"
    extend 7fsqsm " The fact that you're even asking?"
    n 7fchbgl "That already puts you ahead of most people."

    n 3fcssm "Ehehe."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 4klrbgl "Most guys just...{w=0.3}{nw}" there are people who
        extend 4csqfl " ignore it."
        n 4csqfl "Or act like it's some kind of secret." taboo
        n 3knmpol "But you?{w=0.5}{nw}" but you actually
        extend 3klrpol " You want to know how to make it {i}easier{/i} for me."
        n 4klrbgl "That's...{w=0.3}{nw}"
        extend 4klrpol " that's why I love you, [chosen_tease]."
        n 3knmpol "Because you care about the messy stuff too."
        n 4flrpol "Not just the fun parts."
        n 4klrbgl "So...{w=0.5}{nw}"
        extend 4klrpol " just keep being you, okay?"
        n 3klrpol "And maybe bring me chocolate."
        n 4flrpol "Love you, dummy.{w=0.5}{nw}"
        extend 1klrbgl " Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 2fchbgl "You're...{w=0.3}{nw}"
        extend 2fslbo " actually really sweet for asking."
        n 2fsqsm "Most people don't care." people avoid the topic
        n 4fcspxa "So...{w=0.5}{nw}"
        extend 4fcssm " thanks."
        n 3fsqsm "Just... be patient. Bring snacks. Don't make me feel like a burden."
        n 4fchbgl "That's really all I need."
        n 3fslbo "And maybe don't talk to me for the first hour after I wake up."
        n 4fcssm "Ehehe."

    elif Natsuki.isHappy(higher=True):
        n 4fchbgl "You know..."
        n 4fcssm "You're kinda sweet for asking."
        n 3fsqsm "Most people just avoid the topic altogether."
        n 4fchbgl "So...{w=0.5}{nw}"
        extend 4fcspxa " here's the short version:"
        n 3fsqbg "Snacks, patience, and don't be weird about it."
        n 4fcssm "That's literally it."
        n 3fchbgl "Oh, and maybe a heating pad if you have one."
        n 4fcssm "Ehehe."

    else:
        n 4fsqsm "So...{w=0.5}{nw}"
        extend 4fsqbg " yeah."
        n 3fcssm "That's what I'd want."
        n 3fsqsm "Snacks, patience, and don't act grossed out."
        n 4fchbgl "Not that complicated, right?"
        n 3fcssm "Thanks for asking, though."
        n 3fsqsm "Seriously."

    return
INSOMINAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
