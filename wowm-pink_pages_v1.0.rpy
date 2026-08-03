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
            affinity_range=(jn_affinity.HAPPY, None),
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
    extend 3fdtem " it's just so{w=0.3}{nw}"
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
    n 2csgaj "Or worse,{w=0.25}{nw}"
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
    n 4kcsfl "...Sorry."
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
            n 6kcsss "Sometimes just saying 'hey, that's not cool' is enough."
            n 3kdwss "Check in with them afterwards, too."
            n 4fnmbg "Let them know you see what's happening and you don't agree with it."
            n 2ndwsf "..."
            n 2kchbg "I wish someone did that for me."

                #n 2kwrsmf "But it doesn't have to be."
                #n 2kwrsmf "That's why I say stuff like this."
                #n 2kwrsmf "Ehehe."
                #n 2kwrsmf "Anyway...{w=0.5}{nw}"
                #extend 2kwrsmf " I'm glad you're not dealing with that right now."
                #n 2kwrsmf "You deserve better than that."

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
        extend 4kcssmf " I actually mean it, [chosen_endearment]"
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
            n 4uspskeex "For real?!{w=0.5}{nw}"
            n 4uwdgsedz " Like, you're not just saying that?"
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
            affinity_range=(jn_affinity.HAPPY, None),
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
    extend 7nllfl " She seemed...{w=0.3}{nw}"
    extend 2cdrpo " well,{w=0.13} you know."
    n 2kcsss "...But then I caught myself doing it:"
    extend 4clrss " Judging them based on like{w=0.45}{nw} "
    extend 5cdwdveszsbl "...{w=0.3}{nw}"
    extend 5cdltrsbl " nothing."
    n 5kchnvesd "..."
    n 3ksrss "And I thought...{w=0.67}{nw}"
    extend 4kdwss " 'wait,{w=0.3} this is exactly what people do to me.'"
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
        extend 7uchnv " thanks for being worth the chance."

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
