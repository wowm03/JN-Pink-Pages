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
            category=["Natsuki", "Fears"],
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
        n 2ccspo "Hmph...{w=0.5}{nw}"
        extend 2nwmpo " fine...{w=0.7}{nw}"
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
    n 7tdtss "Why did {i}you{/i} ask?{w=0.5}{nw}"
    extend 7tsqpu " That's the real quesiton."
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
            n 7tsqss "Is it the {b}adrenaline{/b}?"
            n 6csqbg "The {cps=10}suspense?{/cps}"
            n 7twrbg "Or do you just like watching people make bad decisions and get eaten?"
            n 2nchsm "Ehehe."

        "No.":
            $ persistent.player_likes_horror = False
            n 4uspskeex "For real?!"
            n 4ucugsedz "Like, you're not just saying that?"
            n 4kctbg "I thought I was the only one!"
            n 2uchlg "This is so nice."
            n 7fsqgn "Finally, someone with actual taste."
            n 6fcsbs "You have no idea how refreshing this is."
            n 3fcspo "Because I'm {i}so{/i} done with people trying to convince me to watch scary stuff."
            n 6fwlbg "You and me?{w=0.35}{nw}"
            extend 3fcssgedz " {i}We{/i} can watch something actually good."


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
        n 2fwlbgl "Love you too, [chosen_tease]."

    elif Natsuki.isEnamored(higher=True):
        n 2fchbgl "You're sweet for asking at first, though."
        n 2fsqsm "Most people just tell me I'm being a baby about it."
        n 4fcspxa "So...{w=0.5}{nw}"
        extend 4fcspxa " thanks for asking."
        n 3fcssm "It's nice that you actually want to know about what I think."
        n 3fsqsm "That means a bunch! Ehehe."
        if persistent.player_likes_horror == True:
            n 7tsraj "Though...{w=0.35}{nw}"
            extend 7tsqtr "I don't know that part with you liking horror..."
            n 3fchbs "Ahaha!"
        elif persistent.player_likes_horror == False:
            n 3uwmbg "And now I know that you're on my side with this one."
            n 3nchdv "Ehehe!"

    elif Natsuki.isHappy(higher=True):
        if persistent.player_likes_horror == True:
            n 4fchbgl "You're not gonna try and make me watch a horror movie though, are you?"
            n 3fcssm "Cause that's a hard no."
        elif persistent.player_likes_horror == False:
            n 7tsqbg "We see eye to eye, huh."
            n 3uchgn "Crazy, right?"
        n 4fchbgl "And...{w=0.5}{nw}"
        extend 4fcspxa " thanks for asking, I guess."
        n 3fsqsm "It's kinda nice to get that off my chest."

    else:
        n 4fsqsm "So...{w=0.5}{nw}"
        extend 4fsqbg " yeah."
        n 3fcssm "That's my answer."
        if persistent.player_likes_horror == True:
            n 3fsqpo "Don't expect me to watch one with you or anything."
        elif persistent.player_likes_horror == False:
            n 3nwmss "And we agree for once."

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
