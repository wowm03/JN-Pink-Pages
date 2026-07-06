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
    n "Why did {i}you{/i} ask?"
    extend "That's the real quesiton."
    show natsuki option_wait_curious
    menu:
            n "Do {i}you{/i} like horror or something?"

        "Yes.":
            n 1nchsm "..."
            n 1fcsbg "Okay, so..."
            n "I don't get it."
            extend " Like, at all."
            n "But you do you."
            n 7cllaw "I just...{w=0.5}{nw}"
            extend 7fslfl " don't understand how anyone enjoys being scared."
            extend 7fsqem " Or watching people get hurt."
            n 4fcspxa "But I mean...{w=0.45}{nw}"
            extend 4fsqsm " I'm not gonna judge you for it."
            if seentopic talk_judgement:
                n 3knmfl "That would make me a hypocrite, wouldn't it?"
                n 3fsqsm "After everything I just said about people judging stuff they don't like."

            else:
                n 4fcssm "Ehehe."

            n 7fchbgl "So...{w=0.35}{nw}"
            extend 7fsqbg " what do you like about it?"
            n 4ftrrc "Like, actually."
            show natsuki option_wait_curious
            menu:
                    n  "I'm curious about why you like horror."

        "No.":
            n 1fcsbg "The sound of silence it is, then!{w=0.5}{nw}"
            extend 1fchsm " Ehehe."

            return

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
        n 3nslpo "...{w=0.5}"
        n 7tdtpu "Why did you ask anyway?{w=0.35}"
        n 3fchbgean "I swear, if you're planning to make me watch one with you."
        n 7tsgsm "But...{w=0.35}{nw}"
        extend 3fchgn " pretty sure you just wanna know more about me,{w=0.5}{nw}"
        extend 3uchsml " ehehe."
        n 4flrpol "It better be that, or else.{w=0.35}"
        n 2fwlbgl "Love you too, [chosen_tease]."

    elif Natsuki.isEnamored(higher=True):
        n 2fchbgl "You're sweet for asking, though."
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
