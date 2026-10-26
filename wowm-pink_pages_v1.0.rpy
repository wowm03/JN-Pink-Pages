# Persistent store for this submod. One namespaced dict is our own "drawer" so
# our saved keys never collide with the devs' or other submods' persistent data.
default persistent._wowmtopics = {}

init 999 python:

    t = get_topic("talk_wowm_judgemento")

    if t:
        t.player_says = True
        t.nat_says = False

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_wowm_judgemento",
            unlocked=True,
            prompt="Do people ever judge you for something with no reason?",
            category=["Life", "Society"],
            player_says=True,
            nat_says=False,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_wowm_judgemento:
    if get_topic("talk_wowm_judgemento").shown_count > 0:
        n 1nnmpu "Wait...{w=0.35}{nw}"
        extend 2tdtfleqm " what?"
        n 7tllfl "Haven't we talked about this before?"
        n 3tsqfs "Hmph...{w=0.46}{nw} "
        extend 3ccsss "fine, I'll answer you again."
        n 3csrfl "Yes{w=0.3}, they do."
    else:
        n 3ccsgs "Duh!{w=0.15}{nw}"
        extend 3cslpo " All the time!"

    n 3tnmfl "Remember when I mentioned how my{w=0.56}{nw} "
    extend 6nslpu "{i}friends{/i}{w=0.5}{nw}"
    extend 3cdwaj " would be all judgey with me whenever I bring up manga?"
    n 3fcsun "...{w=0.2}"
    extend 3fdtem "it's just so{w=0.3}{nw}"
    extend 3fllaj " {i}stu{/i}{w=0.12}{nw}"
    extend 3fupaw "{i}u{/i}{w=0.12}{nw}"
    extend 3fsrdr "{i}pid{/i}{w=0.12}{nw} "
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
    n 2csgaj "Or worse,{w=0.38}{nw}"
    extend 6cuntr "{i}'I don't need to.{w=0.39} Everyone knows she's gross.'{/i}"
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
    extend 6ncsaj "'Okay,{w=0.5} I've tried this but it's not for me.'{w=0.75}{nw}"
    extend 4knmbg " It's completely fine for me."
    n 6nslaj "I don't like horror manga.{w=0.5}{nw} "
    extend 3ksgss "Doesn't mean horror manga is bad.{w=0.7}{nw}"
    extend 3ckrpo " It's just not for me."
    n 6ccsss "See how easy that is? People act like disliking something means it's objectively garbage."
    n 1knmaj "You don't have to like what I like."
    n 2flraj "Just don't be a jerk about things you haven't even tried."
    n 2fcssf "..."
    extend 1kslfr "..."
    n 2kcsfl "It just...{w=0.75} gets to me sometimes."
    n 2tkrfs "But...{w=0.35}{nw}"
    extend 3usqbg " you know what I've figured out?"
    n 6fcsbg "Those people?{w=0.3}{nw} "
    extend 7fsqbs "Total waste of my time."
    n 6ttlfl "If someone's too lazy to form their own opinions?"
    n 3fcsbg "That's a {i}them{/i} problem.{w=0.25}{nw}"
    extend 7twmbg " Not mine."
    n 3ncstr "I'd rather have one person who actually thinks for themselves...{w=0.7}{nw}"
    extend 3nsrpo " than a hundred parrots.{w=0.75}"
#addin smn shi yea sunglasses emoji
    n 3ullca "Though...{w=0.2}{nw}"
    extend 7knmfleqm " Is there a reason for why you're asking this so suddenly?"
    show natsuki option_wait_curious
    menu:
        n "Are people judging {i}you{/i}?"

        "Yes.":
            $ persistent._wowmtopics["wowmi_playa_judged"] = "true"
            n 1fsqpu "..."
            n 3cslup "Shucks..."
            n 3cchsmean "Tell me their name, I'll settle this for you."
            n 2ksremesi "Hah..."
            n 2ksrsf "I know...{w=0.4}{nw}"
            extend 3kdwemeso " I can't exactly do anything about that."
            n 6cwdaweex "{b}But!{/b}{w=0.2}{nw}"
            extend 3fcsgs " And this is a {i}big{/i} but!"
            n 3kcspuesi "..."
            n 3knmpo "I get it, I really do."
            n 3fllem "People judge for the dumbest reasons."
            n 6fcsgs "And half the time, they don't even {i}know{/i} you."
            n 3cdlem "They just see something or hear something and make up their mind."
            n 4fsgaj "But here's the thing, okay?"
            n 6cnmfl "Their opinions don't define you."
            n 2cdrss "It took me a while to figure that out.{w=0.65}"

            if Natsuki.isLove(higher=True):
                $ chosen_tease = jn_utils.getRandomTease()
                n 2cslbo "..."
                n 2fdlfl "Ugh, they're {i}so{/i} annoying,{w=0.4}{nw}"
                extend 4fnmfr " bothering you like that."
                n 3cwdwr "Who do they think they are?!"
                n 3ccsss "Only I get to tease you."
                extend 3uwlbll " Nicely."
                extend 3fchbgesm " Natsuki-styled."
                n 3nslpu "Okay but,{w=0.3}{nw}"
                extend 3kcuss " for real though,{w=0.5}{nw}"
                extend 3kchbg " I think you're beyond amazing."
                n 4csqaj "And not because of what anyone else says."
                n 4fsgss "But because of who you {i}actually{/i} are."
                n 4nwmbgl "You've shown me through time and time again,{w=0.8}{nw}"
                extend 2nchnvl " just what kind of person you really are."
                n 4fwdgsl "So stand proud!{w=0.4}{nw}"
                extend 2fnmaj " And don't let the parrots get to you,{w=0.6}{nw}"
                extend 4kwmss " okay?"
                n 2ccstr "Plus, they're not worth your time."
                n 2csgssl "You know who is?"
                n 6fcsdvf "That's right, none other but {i}me{/i}."
                n 7uchbgf "Ehehe."
                n 7nslss "And...{w=0.3}{nw}"
                extend 3ccsaj " seriously,{w=0.5}{nw}"
                extend 7fchbgean " let me note down their name, IP address, crimes and all that."
                n 3fwlbg "So I can show them what my hands can do."

            elif Natsuki.isEnamored(higher=True):
                n 1flrsf "..."
                n 2fcsan "Darn...{w=0.2}{nw}"
                extend 2fsrfl " it's just so unfair when people do that."
                n 4ccsbo "Like,{w=0.2}{nw}"
                extend 3fslem " who even gave them the {i}right{/i} to judge?"
                n 6fnman "They don't know {i}anything{/i} about you."
                n 3ccsfl "Not.{w=0.2}{nw}"
                extend 3fcsaj " One.{w=0.2}{nw}"
                extend 3fcsan " Thing."
                n 2ksrsf "..."
                n 2cwmpo "Don't you dare let the parrots get to you,{w=0.7}{nw}"
                extend 2kcspu " okay?"
                n 2kwmbg "You're way better than whatever they are."
                n 6fkrca "They're not worth your time."

            elif Natsuki.isHappy(higher=True):
                n 2ccsup "..."
                n 2cdrsl "Those people...{w=0.4}{nw}"
                extend 4fsqfl " they have no right to judge you."
                n 6cwdsc "So don't you dare go thinking it's your fault, okay?"
                n 3fslfl "You don't deserve to be judged."
                n 3ccsfl "I mean it."
                n 4fwlss "Don't let the parrots win."

            else:
                n 2csrca "Just...{w=0.2}{nw}"
                extend 4ccsfl " don't let them get to you."
                n 2ksgun "It's easier said than done, I know."
                n 4knmss "But you've got this."
                n 2kdwdv "I'm here if you need it."

        "No.":
            $ persistent._wowmtopics["wowmi_playa_judged"] = "false"
            n 1kcsflesi "Phew..."
            n 2csqfl "Okay,{w=0.2} good."
            n 2fcspo "I was about to throw hands."
            n 4knmbg "It's really good that you don't have to deal with that."
            n 3fcsun "But...{w=0.25}{nw}"
            extend 7kdtfl " is there anyone you know bothered by those judgemental people?"
            n 3cdwfl "If you know someone who's being judged,{w=0.5}{nw}"
            extend 3klrfl " stand up for them."
            n 3knmfl "You don't have to be loud about it or start a fight."
            n 6kcsss "Sometimes just saying "
            extend 3fsqem "'hey, that's not cool!' "
            extend 2ccssg "is enough."
            n 3kdwss "Check in with them afterwards, too."
            n 4fnmbg "Let them know you see what's happening and you don't agree with it."
            n 2ndwsf "..."
            n 2kchbg "I wish someone did that for me."


    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        $ chosen_endearment = jn_utils.getRandomEndearment()
        if persistent._wowmtopics.get("wowmi_playa_judged") == "true":
            n 6cdlca "That's one of the reasons why I so wanna just...{w=0.5}{nw}"
            extend 3ccsgs " be right by your side and shut those people up."
            n 2cdwfr "...{w=0.45}{nw}"
            extend 2fsltrean " I'm still fuming about the fact that you're being bothered by those stupid judgy people..."
            n 7tsqpueid "..."
            n 7twmss "Just so you know...{w=0.4}{nw}"

        if persistent._wowmtopics.get("wowmi_playa_judged") == "false":
            n 1kcsss "I know you would."
            n 2ccsbsl "You're my [player], after all."
            n 4knmbg "I'm really glad that no one's judging you unfairly."
            n 2kwmaj "Just know that if anything happens..."
            n 4kwrsm "I'm here, okay?"
            extend 2kcsbgl " I'll always be here for you."
            n 6cwdbg "And!{w=0.28}{nw}"

        extend 3uchbg " I'll always, {b}always{/b} have your back!"
        n 1knmbgl "...You're exactly that kind of person for me."
        n 4usrfll "That's...{w=0.3}{nw}"
        extend 3fcsbgf " that's why what I feel for you is real."
        n 4kwmssl "Because you're not one of the parrots."
        n 4fklbgl "I know what you feel for me is real too."
        n 6fcsbsf "I mean{w=0.25}, you come here practically screaming about how much you love me every single day, {w=0.7}{nw}"
        extend 3fsqdvl "ehehe."
        n 4kwmbgl "So when I say 'I love you'?...{w=0.5}{nw}"
        extend 4kcssmf " I actually mean it, [chosen_endearment]."
        n 4nwmbgfeaf "...Love you too, [chosen_tease]."

    elif Natsuki.isEnamored(higher=True):
        if persistent._wowmtopics.get("wowmi_playa_judged") == "true":
            n 3ckleml "If they keep bothering you though?{w=0.6}{nw}"
            extend 7fsgbll " Ya' know where to find me!"
            n 2fcsbgl "I'll give them a piece of my mind."
            n 7fwldv "And maybe a piece of my fist if they {i}really{/i} push it."
            n 3fchbg "Haha!"
            n 2cllss "Alright, I just meant that figuratively."
            n 4tnmsg "But you get what I mean, right?"
            n 2fchbg "I've got your back."
        if persistent._wowmtopics.get("wowmi_playa_judged") == "false":
            n 2tchbg "I'm pretty sure you'd do that for me too."
            n 1kcsss "I just know it."
            n 2udlbg "Plus, I don't think you just repeat what everyone else says."
            n 4ccsfll "That's...{w=0.3}{nw}"
            extend 5cdrfll " part of why I like having you around so much."
            n 2cwmeml "So...{w=0.3} thanks for being you,{w=0.5}{nw} "
            extend 2csrcal "I guess."
            n 2fslpul "Just don't let it get to your head or anything, {w=0.5}{nw}"
            extend 4fbkeml "ya' hear me?!"

    elif Natsuki.isHappy(higher=True):
        if persistent._wowmtopics.get("wowmi_playa_judged") == "true":
            n 2csrfl "Those people can be so irritating sometimes."
            n 2fcsup "Acting like they've got everything figured out."
            n 4cwmaj "You're above that, okay?"
        if persistent._wowmtopics.get("wowmi_playa_judged") == "false":
            n 2clrfl "Still though...{w=0.5}{nw}"
            extend 2ccssf " it's so wild to me how fast people make up their minds."
            n 6ftrem "One rumor and suddenly the world's upside down."
            n 3cllss "I think you're the opposite of that."
        n 2tlraj "That's just the kind of person I think you are."
        n 7tsqbg "That's kinda rare, you know?"
        n 2nsraj "So...{w=0.5} "
        extend 2nsqbg "yeah."
        n 2cnmaj "Keep staying this way,{w=0.5}{nw}"
        extend 3fchssean " or else."

    else:
        if persistent._wowmtopics.get("wowmi_playa_judged") == "true":
            n 2cslem "It's just... how people are sometimes."
            n 4cplsl "I'm sorry that you're being judged."
            n 4cnmss "It'll get better,{w=0.5}{nw}"
            extend 2kwlsm " I'm sure of it."
        if persistent._wowmtopics.get("wowmi_playa_judged") == "false":
            n 2twmfl "But... you're not like those parrots, are you?"
            n 4cdlem "I mean... you wouldn't just judge something without trying it first{w=0.5}, right?"
            n 2cdrfl "And you're not the type to just repeat what other people say without thinking,"
            n 4tsqfl "... right?"
            n 2nsrun "..."
            n 2nsrtr "Just checking."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_wowm_aascari",
            unlocked=True,
            prompt="Why do you hate horror?",
            category=["Fears"],
            player_says=True,
            nat_says=False,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_wowm_aascari:
    if get_topic("talk_wowm_aascari").shown_count > 0:
        n 7tdtaj "Huh...?"
        n 3tsqfl "Hey... didn't we talk about this already?"
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
    n 7tnmaw "Why did {i}you{/i} ask?"
    extend 4csqss " That's the real question."
    show natsuki option_wait_curious
    menu:
        n "Do {i}you{/i} like horror or something?"

        "Yes.":
            $ persistent._wowmtopics["wowmi_liky_playa_horra"] = "likes"
            n 1tnmpu "..."
            n 2nllaj "Okay, so..."
            n 2kchbgesd "I don't get it."
            extend 2ksrssess " Like, at all."
            n 2nchgn "But you do you!"
            n 4nslss "I just...{w=0.35}{nw}"
            extend 2ccsdveso " don't understand how anyone enjoys being scared."
            n 2ckraj "But I mean...{w=0.45}{nw}"
            extend 2nsqbg " I'm not gonna judge you for it."
            if get_topic("talk_wowm_judgemento").shown_count > 0:
                n 7ttlss "That would make me a hypocrite, wouldn't it?"
                n 3tchbselg "After everything I just said about people judging stuff they don't like."

            else:
                n 2fchgn "Ehehe."

            n 2tllaw "So...{w=0.35}{nw}"
            extend 7tnmbg " what do you like about it?"
            n 7tsqss "Is it the {cps=0}adrenaline?{/cps}"
            extend 6csqbg " The {cps=30}suspense?{/cps}"
            n 7twrbg "Or do you just like watching people make bad decisions and get eaten?"
            n 2nchsm "Ehehe."

        "No.":
            $ persistent._wowmtopics["wowmi_liky_playa_horra"] = "dislikes"
            n 4uspskeex "For real?!{w=0.5}"
            n 4uwdgsedz "Like, you're not just saying that?"
            n 4kctbg "I thought I was the only one!"
            n 1nchlg "This is so nice."
            n 3fkrbg "Finally, someone with actual taste."
            n 2fcsbg "You have no idea how refreshing this is."
            n 2cuppo "Because I'm {i}so{/i} done with people trying to convince me to watch scary stuff."
            n 3fnmbg "You and me?{w=0.35}{nw}"
            extend 3uchgnedz " {i}We{/i} can watch something actually good."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 2tsqpu "..."
        show natsuki 2tsqsm at jn_center
        n 3fkrbgl "And wow, you're{w=0.45}{nw}"
        extend 4fcsawl " {i}suuucchh{/i}{w=0.35}{nw}"
        extend 7tsgssl " a [chosen_endearment] for asking,{w=0.5}{nw}"
        extend 3uchgnl " ehehe."
        n 3nsrss "Most people don't care about the reason."
        n 7tnmfl "They just say{w=0.35}{nw}"
        extend 6tcsem " 'you're being dramatic'{w=0.35}{nw}"
        extend 3nslaj " or{w=0.29}{nw}"
        extend 6ttrgs " 'it's not even scary.'"
        if persistent._wowmtopics.get("wowmi_liky_playa_horra") == "likes":
            n 3nslpo "...{w=0.5}"
            n 7tdtpu "Why did you ask that initially anyway?{w=0.35}"
            n 3fchbgean "I swear, if you're planning to make me watch one with you."
            n 7tsgsm "But...{w=0.35}{nw}"
            extend 3fchgn " pretty sure you just wanna know more about me,{w=0.5}{nw}"
            extend 3uchsml " ehehe."
            n 4flrpol "It better be that, or else.{w=0.35}"
        elif persistent._wowmtopics.get("wowmi_liky_playa_horra") == "dislikes":
            n 2uchbg "Glad you're on the same page with me, though."
            n 4fspsm "We're on the same team!"
            extend 2fcsctl " As we should be, {w=0.4}{nw}"
            extend 2nchgnl "ehehe."
        n 2fwlbgl "Love you too, [chosen_tease]."
#maybe add the persistent thing haha
    elif Natsuki.isEnamored(higher=True):
        if persistent._wowmtopics.get("wowmi_liky_playa_horra") == "likes":
            n 2twmaj "I really didn't expect that you would like horror."
            extend 2kcsbg "I {i}really{/i}{w=0.25} don't get the appeal."
            n 2nsltr "But...{w=0.15}{nw}"
            extend 6ucsbg " oh well!{w=0.5}"
            n 6fnmbg "Besties gotta have something to fight about,{w=0.5}{nw}"
            extend 7fwlgn " yeah?{w=0.7}"
            n 2uchlg "Ehehe!"
        elif persistent._wowmtopics.get("wowmi_liky_playa_horra") == "dislikes":
            n 4fwdbg "Now what you up for, huh?{w=0.4}{nw}"
            extend 3fchgn " Hehe!"
            n 4fbklg "You probably can't tell, but I'm literally bouncing in my seat right now!"
            n 2cchgn "Ehehe!"
        n 2fchbgl "You're sweet for asking at first, though."
        n 2clrpo "Most people just tell me I'm being a baby about it."
        n 4ndrbo "So...{w=0.5}{nw}"
        extend 2uchnv " thanks for asking."
        n 4uwmbg "It's nice that you actually want to know about what I think."
        n 2uchsm "That means a bunch! Ehehe."

    elif Natsuki.isHappy(higher=True):
        if persistent._wowmtopics.get("wowmi_liky_playa_horra") == "likes":
            n 2tdtca "You're not gonna try and make me watch one, are you?"
            n 2csltr "Cause that's a hard no."
        elif persistent._wowmtopics.get("wowmi_liky_playa_horra") == "dislikes":
            n 2fcsfl "Thank{w=0.2}{nw}"
            extend 2cupaw " {i}god{/i}{w=0.2}{nw}"
            extend 4usqss " you of all people have taste."
        n 4fchbgl "But...{w=0.2}{nw}"
        extend 2nllss " yeah,{w=0.2}{nw}"
        extend 2ndlss " thanks for asking, I guess."
        n 2nchsm "It's kinda nice to get that off my chest."

    else:
        n 1ndrsf "So...{w=0.5}{nw}"
        extend 2ndwaj " yeah."
        n 2cllss "That's my answer."
        if persistent._wowmtopics["wowmi_playa_liky_horra"] == True:
            n 4csqfr "Don't expect me to watch one with you or anything."
        if persistent._wowmtopics["wowmi_playa_liky_horra"] == False:
            n 2ndrss "Glad that we agree on that, at least."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_wowm_takenfromeurobradi",
            unlocked=True,
            prompt="How did you stop judging people you just met?",
            category=["Life"],
            player_says=True,
            nat_says=False,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_wowm_takenfromeurobradi:
    if get_topic("talk_wowm_takenfromeurobradi").shown_count > 0:
        n 7tnmajeqmsbr "Huh..?"
        n 3tsqss "We already talked about this, didn't we?"
        n 3ndtposbr "..."
        n 1fkrcs "Alright...{w=0.5}{nw}"
        extend 7nkraw " I'll tell you again."

    else:
        n 2nsqaj "Woah..."
        extend 2csrpo " personal much."
        n 4ccsca "...{w=0.2}{nw}"
        extend 2cdwss "I'll be honest."

    n 6cslsg "I didn't just wake up one day and decide to be nice.{w=0.83}{nw}"
    extend 4ccsbg " I had to {i}learn{/i} it."
    n 6ttlgs "When I first joined the club?{w=0.65}{nw}"
    extend 3kchtsesz " I had a lot of opinions about everyone."
    n 7tlrfl "Like...{w=0.3}{nw}"
    extend 3cllun " Monika seemed way {cps=45}{i}too{/i}{/cps}...{w=0.5}{nw}"
    extend 6uchsmedz " perfect."
    n 4csrtr "Sayori seemed...{w=0.45}{nw}"
    extend 6ccsem " {i}waayy{/i} too cheerful."
    n 7ctraj "And Yuri?{w=0.5}{nw}"
    extend 7nllfl " She seemed...{w=0.53}{nw}"
    extend 2cdrpo " well,{w=0.33} you know."
    n 2kcsss "...But then I caught myself doing it:"
    extend 4clrss " Judging them based on like{w=0.45}{nw} "
    extend 5cdwdveszsbl "...{w=0.38}{nw}"
    extend 5cdltrsbl " nothing."
    n 5kchnvesd "..."
    n 3ksrss "And I thought...{w=0.67}{nw}"
    extend 4kdwss " 'wait,{w=0.37} this is exactly what people do to me.'"
    n 6ftlem "People look at me and see a short girl who likes pink and manga."
    n 2csqan "They don't bother to look deeper, and instead just assumes that I'm {i}childish{/i}."
    n 3ccsup "And I {i}hate{/i} that."
    n 2cdrun "So I asked myself..."
    extend 4cdwsf " 'why am I doing the same thing to them?'"
    n 2kchbg "...{cps=30}Aaannd{/cps} I didn't have a good answer."
    n 2ktlfs "But I'll be honest,{w=0.5}{nw}"
    extend 1cdltr " I still judge sometimes."
    n 2kcsss "It's kind of a default thing for me."
    n 6cslfs "The difference is...{w=0.5}{nw}"
    extend 3ccsss " I try to stop myself when it matters."
    n 7cdlaj "Like back then, I realised something."
    n 3ctrpo "If I kept being all judgey and closed off?"
    n 2kdwca "It was gonna add tension to the club."
    n 5csrflsbl "And {i}I{/i} was the one who needed something from them."
    n 4udttr "I knew that if I continued to be standoffish, no one would wanna help me."
    n 4ccsem "So I told myself:{w=0.6}{nw}"
    extend 2cdwaw " 'You don't have to like them right away. But you can't judge them before you know them.'"
    n 7tsqss "And after getting to know them better?"
    n 2kchbssbr "...I found out that I was wrong about all of the prejudiced assumptions I had all along."
    n 2kllpu "Monika wasn't perfect; she was just trying her best to hold everything together."
    n 2kcssf "Sayori wasn't just cheerful; she was fighting her own battles."
    n 7ktraj "And Yuri?{w=0.35}{nw}"
    extend 6kchbg " She's actually really sweet once you get past the whole...{w=0.7}{nw}"
    extend 7cdrss " tough starting."
    n 4tdlaj "So I guess...{w=0.5}{nw}"
    extend 2kcsbg " the answer is:{w=0.2} I realised I was doing the exact thing I hated."
    n 2cdwss "And I didn't and don't wanna be that person."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 3tdtss "I try to give everyone that same chance after that.{w=0.98}{nw}"
        extend 3kchct " The chance to be more than my first impression."
        n 6kwrss "It's made everything better."
        extend 4kwmfsl " Including meeting you, [chosen_endearment]."
        n 3ndlaj "I mean...{w=0.3}{nw}"
        extend 3tchbg " if I had judged you right away?"
        n 4cdrcsl "I would've missed out on...{w=0.5}{nw}"
        extend 2kcsssf " this."
        n 1uklajl "So...{w=0.21}{nw}"
        extend 4nwmsml " thanks for being worth the chance."
        n 3uchblleaf "Love you, [chosen_tease]."

    elif Natsuki.isEnamored(higher=True):
        n 2tupss "And honestly?{w=0.4}{nw}"
        extend 2kcsfs " I'm glad I learned to do that."
        n 7nsraj "Because if I hadn't?"
        n 3kchsm "I might have missed out on getting to know you."
        n 2cwrgn "Ehehe."
        n 3tplbg "So...{w=0.2}{nw}"
        extend 7uchnv " thanks for being worth the chance, [chosen_endearment]."

    elif Natsuki.isHappy(higher=True):
        n 7utrfl "And honestly?{w=0.5}{nw}"
        extend 6uwmfs " I'm glad I learned to do that."
        n 3nchsm "It's made things a lot better."
        n 1uchbg "Ehehe."

    else:
        n 2tcsaw "So...{w=0.5}{nw}"
        extend 7cupss " yeah. That's how I did it."
        n 3ndwss "It's not always easy, but it's worth it."

    return
#UNFINISHEDDDD
#YOURE THOUGHTFUL, CARING,

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_wowm_nutakecompliments",
            unlocked=True,
            prompt="Why is it hard to accept a compliment sometimes?",
            category=["Life"],
            player_says=True,
            nat_says=False,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_wowm_nutakecompliments:
    $ reason_page = 1
    if get_topic("talk_wowm_nutakecompliments").shown_count > 0:
        n 2tnmsleqm "{cps=21}Eh...?{/cps}"
        n 3tsgbg "This again?"
        n 3nllpo "..."
        n 4usrpu "Welp...{w=0.48}{nw}"
        extend 2nwmss " I'll just talk about it again."

    else:
        n 4uskaj "Oh woah{cps=29}...{/cps}{w=0.57}"
        extend 2kcsss " I get you instantly."

    n 7ttlpu "Why is it,{w=0.42} huh?"
    n 2usltr "I mean...{w=0.4}{nw}"
    extend 1cdwss " I myself don't {cps=29}{i}really{/i}{/cps}{w=0.32} have a problem with compliments..."
    extend 5csrcssbl " {cps=21}I think...?{/cps}"
    show natsuki 4fcsss
    menu:
        n "Try me.{w=0.33} I wanna see if compliments does anything on me too."

        "You're so cute.":
            n 4ccuemleex "..!"
            n 4cwmwrl "I'm {i}not{/i}!!!"
            n 1fbkwrl "Are you just making fun of me?!"

        "You're so pretty.":
            n 4uskpul "I-{w=0.29}{nw}"
            extend 4flleml "I'm not-{w=0.39}{nw}"
            extend 1fcsunl " I mean...{w=0.39}{nw}"
            extend 2klrpol " that's-{w=0.49}{nw}"
            extend 2cdwupl " ugh!"
            n 4cbkgsless "J-{w=0.19}just shut up!!!"

        "You're so lovable.":
            n 4uskgsl "W-{w=0.19}wha-?!"
            n 2cwdeml "L-{w=0.19}lovable?{w=0.5}"
            n 2cdlpol "That's such a cheesy word..."

    n 2ccspol "...{w=0.5}"
    extend 4cslfslesd "..."
    n 2fcsupl "Mmmnnnn-!"
    n 4fbkgsl "Okay!{w=0.39}{nw}"
    extend 2cllunl " {fast}{cps=0}Okay okay okay{/cps}."
    n 2ccspol "...{w=0.5}Test over,{w=0.58}{nw}"
    extend 2cdrpol " I get your point,"
    extend 5clltrl " maybe I {i}do{/i} struggle a little with compliments...{w=0.45}"
    n 2kcsaj "It's just...{w=0.47}"
    $ random_reply = renpy.random.randint(1, 2)

    if random_reply == 1:
            n 6tupsl "When someone says something nice to me?"
            n 1kllpo "I don't really know what to do with it."
            n 2kchbg "Like,{w=0.2} my brain kind of just goes...{w=0.6}{nw}"
            extend 7ccsemlesp " uhhhh..?"
            n 4fbkgsl "I just dunno what or how to reply when I'm hit with that!"
            n 3ccsajesi "..."
            n 1nslaj "Like...{w=0.37}{nw}"
            extend 6tsqss " Criticisms?{w=0.67}{nw}"
            extend 2ccssgedz " I can handle that."
            n 4fsqbg "I can argue back,{w=0.54}{nw}"
            extend 2nkrbl " ignore it,{w=0.46}{nw}"
            extend 7fdtgn " or prove them wrong."
            n 4kchsssbr "But compliments?{w=0.7}"
            n 6ksqbg "You can't exactly fight them,{w=0.77}{nw}"
            extend 3ksrpo " and ignoring em' makes you look rude as heck."
            n 6cwdgs "Plus!"
            extend 3ndlem " You can't really{w=0.7}{nw}"
            extend 6csgsr " {i}prove{/i}{w=0.55}{nw}"
            extend 1kcsfs " someone wrong for being nice."
            n 2cslpu "So I just...{w=0.43}{nw}"
            extend 2ckraj " y'know."
            n 5ksrss "I say something dumb like{w=0.86}{nw}"
            extend 2tdtaj " 'Uh,{w=0.44}{nw}"
            extend 2cslem " thanks,{w=0.5} I guess.'{w=0.67}{nw}"
            extend 4kcsawesd " or{w=0.49}{nw}"
            extend 2cupem " 'Whatever'."
            n 5kdtcsesd "Then I feel like a total donut{w=0.58}{nw}"
            extend 5kdlca " because I just made it weird."
            n 4kctnv "..."
            n 4kcsfs "It's worse when...{w=0.5}{nw}"
            extend 6ksrss " when someone actually {i}means{/i}{w=0.6} it."
            n 2ctlaj "When it's not just like a casual{w=0.67}{nw}"
            extend 3nchbsedz " 'Nice job'{w=0.56}{nw}"
            extend 3cuppo " or whatever."
            n 3kkrsl "When they're being all sincere,{w=0.67} I never know what to do with my face."
            n 6fcsca "Because what do you even reply to such a compliment when someone is being so genuine about it?"
            n 1nslpo "It's kind of...{w=0.56}{nw}"
            extend 2cdwaj " scary to me.{w=0.47}"

    elif random_reply == 2:
            n 2nsraj "I didn't really grow up hearing nice things all that often."
            n 6ttlfl "At most, people praised my cupcakes...{w=0.67}{nw}"
            extend 2ksrbg " but that was kinda it."
            n 3csgtr "And no,{w=0.4}{nw}"
            extend 6csqca " calling me 'cute' isn't registered as a nice thing to me..."
            if Natsuki.isLove(higher=True):
                extend 3fcspol " unless it's you who's saying it."
            elif Natsuki.isEnamored(higher=True):
                extend 3fcspol " unless you really mean it."
            n 1ndtfl "So when someone compliments me...{w=0.7}{nw}"
            extend 4uslun " it just feels{w=0.67}{nw}"
            extend 2csraj " off."
            n 1cdlfl "Like they're lying,{w=0.67}{nw}"
            extend 2cdrfr " or that they want something from me."
            n 2kchbgsbl "You get used to people being snippy,{w=0.7} I guess."
            n 2tsrpo "If someone's always putting you down...{w=0.78}{nw}"
            extend 1kcsbo " you start thinking{w=0.55}{nw} "
            extend 2cdrfl "'Yeah yeah,{w=0.15} I know.'{w=0.6}{nw}"
            extend 1fcssl " instead of{w=0.49}{nw}"
            extend 4fwmwrean " 'How could they?'"
            n 3klrpu "..."
            n 1nslfl "So,{w=0.14} when someone's actually being nice...{w=0.89}{nw}"
            extend 7ckraj " I get suspicious."
            n 3ccsfl "There's always a voice in my head that says:"
            extend 6cslem " 'They're just being nice.',{w=0.56}{nw}"
            extend 1cdwun " 'They don't really mean it.'{w=0.57}{nw}"
            extend 2nsraj " or{w=0.39}{nw}"
            extend 1kcsem " 'They'll change their mind later.'"
            n 2kdrbg "It's easier to believe the bad stuff,{w=0.8}{nw}"
            extend 2kklbo " since that's what I'm used to.{w=0.7}{nw}"
            extend 2ccsfs " That's what feels {i}normal{/i}."
            n 6tchsssbl "And my go-to response?"
            n 2kcsflesi "Hah..."
            n 2fdwfr "I get defensive,{w=0.5}{nw}"
            extend 3kupsssbr " act like I don't care,{w=0.6}{nw}"
            extend 5clrbgsbl " or I make a joke to brush it off."
            n 1nslsssbr "It's easier than just taking it and saying 'thanks'."

    n 4ccssl "..."
    n 5udtpo "So...{w=0.41}{nw}"
    extend 4ncsaj " yeah."
    n 2nlrpo "That's why compliments can be weird for me."
    n 7nwdfl "Maybe it's like that for you too."
    n 2uklaj "So tell me..."
    show natsuki 7twmaweqm
    jump reason_menu

$ reason_page = 1

label reason_menu:
    if reason_page == 1:
        menu:
            n "What's {i}your{/i} reason for being bad at receiving compliments?"

            "I think that I'm not worthy.":
                $ persistent._wowmtopics["no_recieve_complimens"] = "true"
                n 2knmpu "..."
                n 2kslfl "I feel you."
                n 1ccsun "Sometimes...{w=0.15} an unasked-for thought just pops into your mind,{w=0.78}{nw}"
                n 6cuptr " like...{w=0.4}{nw}"
                extend 3ksrfs " 'Why would anyone say anything nice about {i}me{/i}?'"
                n 4kwmbg "But here's the thing,{w=0.5}{nw}"
                extend 6fcsaw " you {i}are{/i} worthy."
                if Natsuki.isHappy(higher=False):
                    n 1cdreml "D-{w=0.14}don't make me say this twice."
                jump after_reason_menu

            "I'm afraid of the expectations that come with accepting it.":
                $ persistent._wowmtopics["no_recieve_complimens"] = "true"
                n 7ksrfs "Ahh.{w=0.5} I get that."
                n 3tdwfr "Like{cps=30}...{/cps}{w=0.5} they say you're good at something{w=0.6} and suddenly you gotta keep proving it."
                n 1kdlpo "That's a lot of a pressure."
                jump after_reason_menu

            "I was told to deflect it growing up.":
                $ persistent._wowmtopics["no_recieve_complimens"] = "true"
                n 4kcsfl "I see..."
                n 4knmsr "Like accepting praise means you're full of yourself,{w=0.67} huh."
                n 6kwmaj "So you just brush it off."
                n 1kcsun "That's hard to shake."
                jump after_reason_menu

            "I just don't know how to respond.":
                $ persistent._wowmtopics["no_recieve_complimens"] = "true"
                n 4uwdem "I know right?"
                n 3kkrgs "Like...{w=0.3} what are you even supposed to say?"
                n 7kcsfs "'Thanks' feels weird.{w=0.5} Anything else feels fake."
                n 5kdtcsesd "So you just freeze."
                jump after_reason_menu

            "Next page →":
                $ reason_page = 2
                jump reason_menu

    elif reason_page == 2:
        menu:
            n "What's {i}your{/i} reason for being bad at receiving compliments?"

            "I think other people are better than me.":
                $ persistent._wowmtopics["no_recieve_complimens"] = "true"
                n 2kcssr "Yeah...{w=0.34} I get that."
                n 6cdwsf "You look at everyone else and feel like you don't measure up."
                jump after_reason_menu

            "I fear they'd manipulate me.":
                $ persistent._wowmtopics["no_recieve_complimens"] = "true"
                n 2cnmfl "Ugh,{w=0.3} yeah."
                n 2kcsfl "A really valid fear,{w=0.56} sadly."
                n 1csrem "If nice words came with strings before...{w=1.2}{nw}"
                extend 2kcsun " trusting them's gonna be hard."
                n 3cwdfl "But that's not your fault at all,{w=0.56} got it?"
                jump after_reason_menu

            "I have low self-worth.":
                $ persistent._wowmtopics["no_recieve_complimens"] = "true"
                n 3kcssf "I feel that one too."
                n 3nsrfl "When you don't believe you deserve good things...{w=0.87}{nw}"
                extend 4nplsr " compliments just feel wrong."
                n 4fnmaw "But you {i}do{/i} deserve good things."
                n 4kwmss "I know it's hard to believe,{w=0.6} but it's true."
                jump after_reason_menu

            "I recieve them just fine!":
                $ persistent._wowmtopics["no_recieve_complimens"] = "false"
                n 4uwdaw "Wait...{w=0.3} really?"
                n 2tsqtr "So you're telling me...{w=0.56}{nw}"
                extend 4tsksk " you don't struggle with compliments at all?"
                n 7cdwaj "And you just...{w=0.3}{nw}"
                extend 4twdgs " accept them?"
                n 2nslpo "Here I am pouring my heart out about how hard it is..."
                n 3fcsbs "And you're just like{w=0.67} 'Nah, I'm good.'"
                #$ persistent._wowmtopics["wowmi_playa_complimen_noprob"] = "true"
                jump after_reason_menu

            "← Previous page":
                $ reason_page = 1
                jump reason_menu

label after_reason_menu:
    if persistent._wowmtopics.get("no_recieve_complimens") == "true":
        n 4kwmbg "Well...{w=0.3} thanks for sharing that with me."
        n 2ccsdvsbl "It's not always easy to talk about this stuff."
        n 1kdrbg "So...{w=0.25} I appreciate it."
        n 4nwdpu "And...{w=0.29}{nw}"
        extend 4uwmss " you're not alone in this,{w=0.45} okay?"
        n 5ckrdv "I struggle with it too."
        n 7ndraw "Whatever your reason is...{w=0.56}{nw}"
        extend 4kwmbg " It's valid."
        n 3uchfs "And I'm here if you ever want to talk about it."

    elif persistent._wowmtopics.get("no_recieve_complimens") == "false":
        n 2ccspolesd "..."
        n 4fsqsm "So...{w=0.3} "
        extend 7twmbg " you're one of the lucky ones,{w=0.6} huh?{w=0.4}{nw}"
        extend 3fsqsm " Not having to struggle with compliments."
        n 3tlrss "I'm not gonna lie."
        n 2ccspo "Part of me is jealous.{w=0.56}"
        extend 4usgct " But mostly,{w=0.3} I'm just glad.{w=0.5}{nw}"

    return

init 5 python in vent:
    import store
    import random
    import re

    streak = 0

    ALLOW = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -'.,!?:;()&/\""
    LENGTH = 500

    TYPES = {
        "angry": store.jn_admissions.TYPE_ANGRY,
        "anxious": store.jn_admissions.TYPE_ANXIOUS,
        "ashamed": store.jn_admissions.TYPE_ASHAMED,
        "confident": store.jn_admissions.TYPE_CONFIDENT,
        "excited": store.jn_admissions.TYPE_EXCITED,
        "happy": store.jn_admissions.TYPE_HAPPY,
        "hungry": store.jn_admissions.TYPE_HUNGRY,
        "insecure": store.jn_admissions.TYPE_INSECURE,
        "proud": store.jn_admissions.TYPE_PROUD,
        "sad": store.jn_admissions.TYPE_SAD,
        "sick": store.jn_admissions.TYPE_SICK
    }

#-------------------------------------------------------------------------------------
# Subtopics for each emotion
# Keywords that recognise the subtopic.
# "subtopic name": ["keyword1", "keyword2", ...]
#-------------------------------------------------------------------------------------

    SUBTOPICS = {
        "angry": [
            ("subtopic_a", ["dummyangrya", "dummyangrya2"]),
            ("subtopic_b", ["dummyangryb", "dummyangryb2"]),
            ("subtopic_c", ["dummyangryc", "dummyangryc2"]),
            ("subtopic_d", ["dummyangryd", "dummyangryd2"])
        ],
        "anxious": [
            ("subtopic_a", ["dummyanxiousa", "dummyanxiousa2"]),
            ("subtopic_b", ["dummyanxiousb", "dummyanxiousb2"]),
            ("subtopic_c", ["dummyanxiousc", "dummyanxiousc2"]),
            ("subtopic_d", ["dummyanxiousd", "dummyanxiousd2"])
        ],
        "ashamed": [
            ("subtopic_a", ["dummyashameda", "dummyashameda2"]),
            ("subtopic_b", ["dummyashamedb", "dummyashamedb2"]),
            ("subtopic_c", ["dummyashamedc", "dummyashamedc2"]),
            ("subtopic_d", ["dummyashamedd", "dummyashamedd2"])
        ],
        "confident": [
            ("subtopic_a", ["dummyconfidenta", "dummyconfidenta2"]),
            ("subtopic_b", ["dummyconfidentb", "dummyconfidentb2"]),
            ("subtopic_c", ["dummyconfidentc", "dummyconfidentc2"]),
            ("subtopic_d", ["dummyconfidentd", "dummyconfidentd2"])
        ],
        "excited": [
            ("subtopic_a", ["dummyexciteda", "dummyexciteda2"]),
            ("subtopic_b", ["dummyexcitedb", "dummyexcitedb2"]),
            ("subtopic_c", ["dummyexcitedc", "dummyexcitedc2"]),
            ("subtopic_d", ["dummyexcitedd", "dummyexcitedd2"])
        ],
        "happy": [
            ("subtopic_a", ["dummyhappya", "dummyhappya2"]),
            ("subtopic_b", ["dummyhappyb", "dummyhappyb2"]),
            ("subtopic_c", ["dummyhappyc", "dummyhappyc2"]),
            ("subtopic_d", ["dummyhappyd", "dummyhappyd2"])
        ],
        "hungry": [
            ("subtopic_a", ["dummyhungrya", "dummyhungrya2"]),
            ("subtopic_b", ["dummyhungryb", "dummyhungryb2"]),
            ("subtopic_c", ["dummyhungryc", "dummyhungryc2"]),
            ("subtopic_d", ["dummyhungryd", "dummyhungryd2"])
        ],
        "insecure": [
            ("subtopic_a", ["dummyinsecurea", "dummyinsecurea2"]),
            ("subtopic_b", ["dummyinsecureb", "dummyinsecureb2"]),
            ("subtopic_c", ["dummyinsecurec", "dummyinsecurec2"]),
            ("subtopic_d", ["dummyinsecured", "dummyinsecured2"])
        ],
        "proud": [
            ("subtopic_a", ["dummyprouda", "dummyprouda2"]),
            ("subtopic_b", ["dummyproudb", "dummyproudb2"]),
            ("subtopic_c", ["dummyproudc", "dummyproudc2"]),
            ("subtopic_d", ["dummyproudd", "dummyproudd2"])
        ],
        "sad": [
            ("subtopic_a", ["dummysada", "dummysada2"]),
            ("subtopic_b", ["dummysadb", "dummysadb2"]),
            ("subtopic_c", ["dummysadc", "dummysadc2"]),
            ("subtopic_d", ["dummysadd", "dummysadd2"])
        ],
        "sick": [
            ("subtopic_a", ["dummysicka", "dummysicka2"]),
            ("subtopic_b", ["dummysickb", "dummysickb2"]),
            ("subtopic_c", ["dummysickc", "dummysickc2"]),
            ("subtopic_d", ["dummysickd", "dummysickd2"])
        ]
    }

#-------------------------------------------------------------------------------------

    def route(label):
        global streak

        emotion = label.replace("admission_", "", 1)

        if emotion not in TYPES:
            return label

        if store.jn_admissions.last_admission_type == TYPES[emotion]:
            streak += 1

        else:
            streak = 1

        if streak < 3:
            return label

        store.jn_admissions.last_admission_type = TYPES[emotion]
        store.vent_answer = store.persistent._wowmtopics.get("vent_" + emotion)

        if streak > 3 and store.vent_answer:
            store.vent_mode = "followup"

        else:
            store.vent_mode = "ask"
            store.get_topic("talk_vent_" + emotion).unlock()

        return "talk_vent_" + emotion

    def match(emotion, text):
        text = text.lower()
        found = [
            number for number, (_, words) in enumerate(SUBTOPICS[emotion], 1)
            if any(re.search(r"\b" + re.escape(word.lower()) + r"\b", text) for word in words)
        ]
        return random.choice(found) if found else None

    renpy.config.label_overrides["player_admissions_start"] = "vent_admissions_start"

    for emotion, prompt in (
        ("angry", "What should I do when I'm angry?"),
        ("anxious", "What should I do when I'm anxious?"),
        ("ashamed", "What should I do when I'm ashamed?"),
        ("confident", "What should I do when I'm confident?"),
        ("excited", "What should I do when I'm excited?"),
        ("happy", "What should I do when I'm happy?"),
        ("hungry", "What should I do when I'm hungry?"),
        ("insecure", "What should I do when I'm insecure?"),
        ("proud", "What should I do when I'm proud?"),
        ("sad", "What should I do when I'm sad?"),
        ("sick", "What should I do when I'm sick?")
    ):
        store.registerTopic(
            store.Topic(
                store.persistent._topic_database,
                label="talk_vent_" + emotion,
                unlocked=False,
                prompt=prompt,
                category=["Emotions"],
                player_says=True,
                nat_says=False,
                affinity_range=(store.jn_affinity.HAPPY, None),
                location="classroom"
            ),
            topic_group=store.TOPIC_TYPE_NORMAL
        )

default vent_mode = None

label vent_admissions_start:
    python:
        admission_menu_items = [
            (_admission.prompt, _admission.label)
            for _admission in jn_admissions.getAllAdmissions()
        ]
        admission_menu_items.sort()

    call screen scrollable_choice_menu(admission_menu_items, ("Go back", None), 400, "mod_assets/icons/admissions.png")

    if isinstance(_return, basestring):
        $ push(vent.route(_return))
        jump call_next_topic

    jump talk_menu

#-------------------------------------------------------------------------------------
# labels for each emotion.
# all labels follow the same format for the dummy texts so ill just explain for angry here.
# O to R is advice for each of the angry subtopics from before. In order from 1 to 4 (a to d)
# S is generic advice if no keywords match any of the 4 subtopics.
# AG and AI are natsukis replies to yes and no to the followup question.
# T is the advice in the new unlocked topics.
# AD is her reply after you tell her what you do to feel better.
#-------------------------------------------------------------------------------------

label talk_vent_angry:
    if vent_mode == "ask":
        $ vent_sub = vent.match("angry", renpy.input("What's making you feel angry?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text O"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text P"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text Q"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text R"

        else:
            n 2tnmbo "Dummy Text S"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text AG"

            "No":
                n 2tnmbo "Dummy Text AI"

    else:
        n 2tnmbo "Dummy Text T"
        menu:
            n "What do you usually do when you're angry?"

#-------------------------------------------------------------------------------------
# "Listen to music":
#    $ persistent._wowmtopics["vent_angry"] = "listen to some music"
# the second line here is what natsuki will ask afterwards like in the 4th click, "Did you get a chance to listen to some music?"
#-------------------------------------------------------------------------------------

            "Listen to music":
                $ persistent._wowmtopics["vent_angry"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_angry"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_angry"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_angry"] = vent_text

        n 2tnmbo "Dummy Text AD"

    $ vent_mode = None
    return

label talk_vent_anxious:
    if vent_mode == "ask":
        $ vent_sub = vent.match("anxious", renpy.input("What's making you feel anxious?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text AL"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text AM"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text AN"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text AO"

        else:
            n 2tnmbo "Dummy Text AP"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text BD"

            "No":
                n 2tnmbo "Dummy Text BF"

    else:
        n 2tnmbo "Dummy Text AQ"
        menu:
            n "What do you usually do when you're anxious?"

            "Listen to music":
                $ persistent._wowmtopics["vent_anxious"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_anxious"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_anxious"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_anxious"] = vent_text

        n 2tnmbo "Dummy Text BA"

    $ vent_mode = None
    return

label talk_vent_ashamed:
    if vent_mode == "ask":
        $ vent_sub = vent.match("ashamed", renpy.input("What's making you feel ashamed?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text BI"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text BJ"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text BK"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text BL"

        else:
            n 2tnmbo "Dummy Text BM"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text CA"

            "No":
                n 2tnmbo "Dummy Text CC"

    else:
        n 2tnmbo "Dummy Text BN"
        menu:
            n "What do you usually do when you're feeling ashamed?"

            "Listen to music":
                $ persistent._wowmtopics["vent_ashamed"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_ashamed"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_ashamed"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_ashamed"] = vent_text

        n 2tnmbo "Dummy Text BX"

    $ vent_mode = None
    return

label talk_vent_confident:
    if vent_mode == "ask":
        $ vent_sub = vent.match("confident", renpy.input("What's making you feel confident?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text CF"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text CG"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text CH"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text CI"

        else:
            n 2tnmbo "Dummy Text CJ"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text CX"

            "No":
                n 2tnmbo "Dummy Text CZ"

    else:
        n 2tnmbo "Dummy Text CK"
        menu:
            n "What do you usually do when you're feeling confident?"

            "Listen to music":
                $ persistent._wowmtopics["vent_confident"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_confident"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_confident"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_confident"] = vent_text

        n 2tnmbo "Dummy Text CU"

    $ vent_mode = None
    return

label talk_vent_excited:
    if vent_mode == "ask":
        $ vent_sub = vent.match("excited", renpy.input("What's making you feel excited?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text DC"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text DD"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text DE"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text DF"

        else:
            n 2tnmbo "Dummy Text DG"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text DU"

            "No":
                n 2tnmbo "Dummy Text DW"

    else:
        n 2tnmbo "Dummy Text DH"
        menu:
            n "What do you usually do when you're excited?"

            "Listen to music":
                $ persistent._wowmtopics["vent_excited"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_excited"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_excited"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_excited"] = vent_text

        n 2tnmbo "Dummy Text DR"

    $ vent_mode = None
    return

label talk_vent_happy:
    if vent_mode == "ask":
        $ vent_sub = vent.match("happy", renpy.input("What's making you feel happy?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text DZ"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text EA"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text EB"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text EC"

        else:
            n 2tnmbo "Dummy Text ED"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text ER"

            "No":
                n 2tnmbo "Dummy Text ET"

    else:
        n 2tnmbo "Dummy Text EE"
        menu:
            n "What do you usually do when you're happy?"

            "Listen to music":
                $ persistent._wowmtopics["vent_happy"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_happy"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_happy"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_happy"] = vent_text

        n 2tnmbo "Dummy Text EO"

    $ vent_mode = None
    return

label talk_vent_hungry:
    if vent_mode == "ask":
        $ vent_sub = vent.match("hungry", renpy.input("What's making you feel hungry?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text EW"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text EX"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text EY"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text EZ"

        else:
            n 2tnmbo "Dummy Text FA"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text FO"

            "No":
                n 2tnmbo "Dummy Text FQ"

    else:
        n 2tnmbo "Dummy Text FB"
        menu:
            n "What do you usually do when you're hungry?"

            "Listen to music":
                $ persistent._wowmtopics["vent_hungry"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_hungry"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_hungry"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_hungry"] = vent_text

        n 2tnmbo "Dummy Text FL"

    $ vent_mode = None
    return

label talk_vent_insecure:
    if vent_mode == "ask":
        $ vent_sub = vent.match("insecure", renpy.input("What's making you feel insecure?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text FT"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text FU"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text FV"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text FW"

        else:
            n 2tnmbo "Dummy Text FX"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text GL"

            "No":
                n 2tnmbo "Dummy Text GN"

    else:
        n 2tnmbo "Dummy Text FY"
        menu:
            n "What do you usually do when you're feeling insecure?"

            "Listen to music":
                $ persistent._wowmtopics["vent_insecure"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_insecure"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_insecure"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_insecure"] = vent_text

        n 2tnmbo "Dummy Text GI"

    $ vent_mode = None
    return

label talk_vent_proud:
    if vent_mode == "ask":
        $ vent_sub = vent.match("proud", renpy.input("What's making you feel proud?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text GQ"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text GR"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text GS"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text GT"

        else:
            n 2tnmbo "Dummy Text GU"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text HI"

            "No":
                n 2tnmbo "Dummy Text HK"

    else:
        n 2tnmbo "Dummy Text GV"
        menu:
            n "What do you usually do when you're proud of something?"

            "Listen to music":
                $ persistent._wowmtopics["vent_proud"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_proud"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_proud"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_proud"] = vent_text

        n 2tnmbo "Dummy Text HF"

    $ vent_mode = None
    return

label talk_vent_sad:
    if vent_mode == "ask":
        $ vent_sub = vent.match("sad", renpy.input("What's making you feel sad?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text HN"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text HO"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text HP"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text HQ"

        else:
            n 2tnmbo "Dummy Text HR"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text IF"

            "No":
                n 2tnmbo "Dummy Text IH"

    else:
        n 2tnmbo "Dummy Text HS"
        menu:
            n "What do you usually do when you're sad?"

            "Listen to music":
                $ persistent._wowmtopics["vent_sad"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_sad"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_sad"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_sad"] = vent_text

        n 2tnmbo "Dummy Text IC"

    $ vent_mode = None
    return

label talk_vent_sick:
    if vent_mode == "ask":
        $ vent_sub = vent.match("sick", renpy.input("What's making you feel sick?", allow=vent.ALLOW, length=vent.LENGTH))

        if vent_sub == 1:
            n 2tnmbo "Dummy Text IK"

        elif vent_sub == 2:
            n 2tnmbo "Dummy Text IL"

        elif vent_sub == 3:
            n 2tnmbo "Dummy Text IM"

        elif vent_sub == 4:
            n 2tnmbo "Dummy Text IN"

        else:
            n 2tnmbo "Dummy Text IO"

    elif vent_mode == "followup":
        menu:
            n "Did you get a chance to [vent_answer]?"

            "Yes":
                n 2tnmbo "Dummy Text JC"

            "No":
                n 2tnmbo "Dummy Text JE"

    else:
        n 2tnmbo "Dummy Text IP"
        menu:
            n "What do you usually do when you're sick?"

            "Listen to music":
                $ persistent._wowmtopics["vent_sick"] = "listen to some music"

            "Talk about it":
                $ persistent._wowmtopics["vent_sick"] = "talk to someone about it"

            "Get some sleep":
                $ persistent._wowmtopics["vent_sick"] = "get some sleep"

            "Other":
                $ vent_text = ""
                while not vent_text:
                    $ vent_text = renpy.input("Other", allow=vent.ALLOW, length=vent.LENGTH).strip()
                $ persistent._wowmtopics["vent_sick"] = vent_text

        n 2tnmbo "Dummy Text IZ"

    $ vent_mode = None
    return
