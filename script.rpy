init python:
    style.default.line_leading = 12

    style.ruby_style = Style(style.default)
    style.ruby_style.size = 25
    style.ruby_style.yoffset = -25

    style.default.ruby_style = style.ruby_style

###############################################################
#이펙트
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define lfade = Fade(1.5, 1.0, 1.0, color="#000")
define redf = Fade(0.1, 0.0, 0.5, color="#ff0000")
define bluef = Fade(0.1, 0.0, 0.5, color="#0067A3")
define fadehold = Fade(0.5, 1.0, 0.5)
define shake = ComposeTransition(flash, before=vpunch, after=hpunch)
define fadehold = Fade(0.5, 1.0, 0.5)
define change = CropMove(0.3, mode="wipeleft", startcrop=(0.0, 0.0, 0.0, 1.0), startpos=(0.0, 0.0), endcrop=(0.0, 0.0, 1.0, 1.0), endpos=(0.0, 0.0), topnew=True)
#캐릭터 개체 : 나레이터

define n2 = Character(None)
define nd = Character(None, kind=nvl_narrator, what_prefix="「",
                     what_suffix="」")
define cen = Character(None, kind=centered)
define n = Character(None, kind=nvl_narrator)

#캐릭터 개체 : 캐릭터들

define l = Character('루이', color="#544eb9")
define h = Character('화이', color="#d15999")
define am = Character('아문', color="#dccf9d")
define ak = Character('아카리', color="#50bcdf")
define ich = Character('이채', color="#bcb3e5")
define zero = Character(None, kind=nvl_narrator, what_prefix="{i}",
                        what_suffix="{/i}")
define mob1 = Character('???')
define amphone = Character('아문', color="#dccf9d", what_prefix="{font=DungGeunMo.ttf}",
                                            what_suffix="{/font}")
define nvlphone = Character(None, kind=nvl_narrator, what_prefix="{font=DungGeunMo.ttf}",
                                                what_suffix="{/font}")

#캐릭터 개체 : 연출노트


define dm = Character('연출노트', kind=nvl, color="#808080")
define dm2 = Character('연출노트', color="#808080")
####################################################################

#이미지

#로고,크레딧
image credit1="logo/credit1.png"
image credit2="logo/credit2.png"
image credit3="logo/credit3.png"
image credit4="logo/credit4.png"
image credit5="logo/credit5.png"
#콘티

image test1="conte/test001.png"
image test2="conte/test002.png"
image test3="conte/test003.png"
image test4="conte/test004.png"
image test5="conte/test005.png"
image test6="conte/test006.png"
image ref0="conte/ref0.jpg"
image ref1="conte/ref1.jpg"
image ref2="conte/ref2.jpg"
image ref3="conte/ref3.jpg"

#효과

image blood="effect/blood.png"

#배경

image mainlogo="logo/main_logo.png"
image bg room1="bg/room1.jpg"
image bg city="bg/city1.png"
image bg white="#FFFFFF"
image bg black="#000000"
image bg red="#CC0303"
image bg harlem="bg/harlem.png"
image bg bstreet="bg/bstreet1.png"
image bg office="office.png"
image bg market="bg/market.jpg"
image bg garden="bg/garden.jpg"
image bg intro1="bg/intro1.png"
image bg cyberspace="bg/cyberspace.jpg"
image bg hwairoom="bg/hwairoom.jpg"
image bg whiteroom="bg/whiteroom.jpg"
image bg whiteroom1="bg/whiteroom1.jpg"
image bg whiteroom2="bg/whiteroom2.jpg"
image bg whitestair="bg/whitestair.jpg"
image bg church="bg/church.jpg"
image bg city2="bg/city2.jpg"
#스탠딩
#루이
image Loui="standing/loui/Loui.png"
image Loui02="standing/loui/Loui02.png"
image Loui03="standing/loui/Loui03.png"
image Loui04="standing/loui/Loui04.png"
image Loui05="standing/loui/Loui05.png"
image Loui smile="standing/loui/Loui06.png"
image Loui close eye="standing/loui/Loui07.png"
image Loui smile2="standing/loui/Loui08.png"

image Loui weapon01="standing/loui/var/Loui_weapon01.png"
image Loui weapon02="standing/loui/var/Loui_weapon02.png"
image Loui attacked01="standing/loui/var/Loui_attacked01.png"
image Loui bleed01="standing/loui/Loui_bleed01.png"
image Loui bleed02="standing/loui/Loui_bleed02.png"
image Loui bleed04="standing/loui/Loui_bleed04.png"
image Loui bleed07="standing/loui/Loui_bleed07.png"
image Loui bleed08="standing/loui/Loui_bleed08.png"
image Loui injured01="standing/loui/var/Loui_injured01.png"
image Loui injured02="standing/loui/var/Loui_injured02.png"
image Loui injured03="standing/loui/var/Loui_injured03.png"

#이채(가면) st
image maskman="maskman.png"
image maskman right="maskmanb.png"

#아문 st

image Amun="standing/am/Amun01.png"
image Amun smile="standing/am/Amun02.png"
image Amun smileL="standing/am/Amun02b.png"
image Amun surprised="standing/am/Amun03.png"
image Amun surprisedL="standing/am/Amun03b.png"
image Amun surprisedL2="standing/am/Amun03c.png"
image Amun shout="standing/am/Amun04.png"
image Amun shout2="standing/am/Amun05.png"
image Amun right="standing/am/Amun01b.png"
image Amun right hand="standing/am/Amun01c.png"
image Amun right smile="standing/am/Amun02b.png"
image Amun right smile hand="standing/am/Amun02c.png"
image Amun shoot01="standing/am/var/Amun_shoot01.png"
image Amun shoot02="standing/am/var/Amun_shoot02.png"

image black = "#000"

#이벤트CG

image event01="event/event01ver2.png"
image event02="event/event02.png"
image event03="event/event03.png"
image event04="event/event04.png"
image event05="event/event05.png"
image event06="event/event06.png"
image event07="event/event07.png"
image event08="event/event08.png"
image event09="event/event09.png"
image event10="event/event10.png"
image event11="event/event11.png"
image event12="event/event12.png"
image event13="event/event13.png"
image 14="event/14.png"
image 15="event/15.png"
image 16="event/16.png"
image 17="event/17.png"
init python:
    menu = nvl_menu
    style.nvl_window.xpadding = 20
    style.nvl_window.ypadding = 20
    style.nvl_vbox.box_spacing = 1
    style.nvl_dialogue.line_spacing = 5
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

################################################################################
################################################################################
################################################################################

# 여기에서부터 게임이 시작합니다.
label start:

    scene bg black
    with lfade

    play music "audio/001.mp3" loop

    cen "도시는 각자의 빛을 내며 숨쉬고 있었다."
    n "네온. 가상현실 스크린. 지직거리는 소리. 모든 게 C시의 보편적인 풍경들."
    n "일상적인 빛이다. 그리고 그런 것들에는 이미 익숙해져 있다."
    n "그 아래에 나는 서 있었다."

    nvl clear

    n "술에 취한 것처럼 몽롱하고 어지럽다."
    n "생각을 하고 있는데도 감각이 먼저 앞선다."
    n "충동에 휩싸이는 것처럼, 강렬하다. 그렇지만 뿌옇다."
    n "손에 잡히지 않는 안개 속을 걷는 것 같았다."

    nvl clear

    n "그래서, 어쩌면 이건 현실이 아닐지도 모른다."
    n "어쩌면 가상 현실 속의 시뮬레이션일지도 모른다."
    n "옛날 옛적, 교복을 입었을 적의 망상일지도 모른다."
    n "지금 내가 숨쉬고 감각하고 있는 이 거리는 누군가가 만든 모조일지도 몰라."
    n "그런 생각이 들지만──"
    cen "이것은, 의심할 수도 없는 완벽한 현실이다. 나는 그걸 알고 있었다."

    nvl clear

    scene bg bstreet
    with lfade

    n "비틀, 비틀. {nw}"
    n "계속해서 걸으며 무언가를 좇으려 발을 움직이고 있었다."
    n "수많은 빛을 바라보던 내 시선은, 어느새 내려와 거리를 향하고 있었다."
    n "어째서인지 능동적으로 생각할 수 없다."
    n "시야가 좁다. 찌푸린 눈으로 앞을 보는 것처럼."

    nvl clear

    cen "그리고 나는 그 감각에 이름을 붙일 수 있게 되었다.{vspace=10}그래, 마치 이건───── 연극을 보는 것 같다."

    cen "무대는 2112년 C시, 배우는 나─────{vspace=10}그런 적당한 설정으로 꾸며져 있다."


    n "나는────── '내'가 거리를 비틀거리는 모습을 보고 있었다."
    n "영화를 보는 것처럼 낯설다. 걸어가는 모습을 누가 카메라로 찍은 것 같다."
    n "들려오는 소리들은 평소처럼 똑같다. 그래서────기묘한 불협화음을 자아냈다."
    n "익숙한 풍경과 낯선 시야의 충돌."
    n "곳곳에서 홀로그램을 비추는, 지직거리는 기계음과, 사람들이 중얼거리는 말소리들."
    n "매트릭스, 술, 환각 상태, 자본, 기업, 모든 것에 관한 이런저런 불평불만."

    nvl clear

    cen "────그것들 사이를────────걸어가는 '나'와"
    cen "걸어가는 나를────────────멀리서 바라보는, '나'."

    nvl clear
    window hide

    scene bg black
    with Dissolve(3.0)

    n "발걸음을 앞으로 옮길수록,"
    n "어두워지고, 어두워진다."
    n "빛은 잦아들고 오직 불길한 검은색만이 시야를 가득 메운다."
    n "계속되던 사람들의 목소리도 점점 없어지고 있다."

    nvl clear

    n "문득 손에 무언가를 쥐고 있었다는 걸 깨달았다."
    n "이게 뭐지? 하고 의문이 들어도 나는 아래를 내려다 볼 수 없다."
    n "손에서 금속의 감촉이 느껴진다."
    n "이걸로 무엇을 하려는 걸까."
    n "'나'는, 애초에 어디로 가고 있던 걸까."

    nvl clear

    n "이 세상에는 알 수 없는 것들 투성이인 것 같다."
    n "그러니까 기업에 사람들이 개처럼 이용되고 버려진다."
    n "희망 없는 세상에서 살려면 이렇게 반쯤 미쳐 있는 게 좋은가보다."

    nvl clear

    n "순간──────뒤에서 인기척이 느껴진다."
    n "감각만이 살아 있었기에 재빠르게 눈치 챌 수 있었다."
    n "습격자다, 라고 판단해버림과 동시에."
    n "팔이 움직인다."

    nvl clear

    n "머리로 생각하기도 전에 먼저 감각이 반응했다."
    n "이런, 처리해야 해──────라고 생각하기도 전에 몸이 뛰쳐 나간다."
    n "아니야───이렇게까지 격하게 반응할 생각은 없었어."
    n "분명히───이 녀석들은 날 해하려고 했어."
    n "그래도───"

    nvl clear

    cen "{cps=5}죽일 것────까지는─────────────{/cps}"


    show blood
    with redf
    play sound "crack01.mp3"
    hide window
    pause 2

    n "스릉, 하고 무언가를 베었다."
    n "그것은 종이를 잘라내는 것처럼 간단했다."
    n "그래서 오히려 칼을 휘두른다는 감각조차도 없었다."
    n "그럼에도────────"

    window hide

    scene bg red
    with shake
    play sound "crack01.mp3"

    cen "계속해서 베어갔다."
    cen "이상하게도 그들을 해치우면서 든 생각은 하나 뿐이었다."

    scene bg black
    with dissolve

    nvl clear

    n "──머나먼 기억 속의 어떤 풍경."
    n "눈동자와 목소리."
    n "실루엣과 표정."

    nvl clear

    n "누군가를 강하게 그리워하고 있었다."
    n "어딘가를 애타게 찾고 있었다."
    n "어느 때를 간절히 바라고 있었다."

    nvl clear

    #혈액과 사운드 이펙트
    scene bg intro1
    with dissolve
    cen "정신을 차려보니 거리에는 붉은 액체로 가득했다.{nw}"
    cen "정신을 차려보니 거리에는 붉은 액체로 가득했다.{fast} {vspace=10} 아까까지, 증오와 살기를 띄고 돌격해왔던 것들은 이미 숨이 끊어져 있었다."

    with redf
    cen "전부──────────────────내가 한 짓이다."

    nvl clear


    n "쏴아아, 하고 비가 쏟아진다."
    n "볼을 스치는 물의 온도는 차가웠다."
    n "나는 그곳에서 멍하니 서서 하늘을 바라보았다."
    n "네온 사인이 비에 젖어서 흔들리고 있었다."
    n "제 형체를 잃어가는 신기루 같았다."

    nvl clear

    n "목이 마르다.  문득 한기가 느껴진다. 옷이 비에 젖어간다."
    n "이곳을 떠야 하는데 좀처럼 발이 떨어지지 않았다."
    n "방금 쓰러진 녀석들에게 묻고 싶었다."

    nvl clear

    n "───어째서 이 도시를 활개하느냐고."
    n "───어째서 그녀를 데려간 거냐고."
    n "그렇지만 쓰러진 자는 말이 없다."
    n "그런 답은 스스로에서부터 찾을 수밖에 없다."

    nvl clear

    scene bg white
    with flash

    n "헤드라이트가 엄습했다. 시야가 밝아졌다."
    n "나는 그 무수한 빛들을 바라보았다. 눈이 부셔서, 멀 것 같다."
    n "누군가가 무어라 소리치고 있었다. 나는 그걸 이해하지 못한다."
    n "머릿속은 단 하나의 생각으로 가득했다."


    n "앞으로는 일이, 터무니없이 전환될 것이라는 예감."

    nvl clear

    #여기서 하늘을 바라봐야할것같은데

    n "───나는 계속해서, 애타게 무언가를 찾고 있었다."
    n "어느 순간부터 마음이 공허해져 그렇게 된 것 같았다."
    n "그것은 순간, 들어선 것이었다."
    n "그리고 질문 하나가 떠오른다."

    cen "{color=000}이 마음을 가득 채운 것은─────{nw}{/color}"
    cen "{color=000}이 마음을 가득 채운 것은─────{fast}{vspace=10} 사랑인가, 저주인가─────────────{/color}"

    cen "{color=000}그것이 무엇인지, {vspace=10}찾아야 하는 그 사람이 누구인지도 모르는 채로────{/color}"
    cen "{color=000}나는────────────────"

    scene bg black
    with fade

    stop music fadeout 1.0

    play music "piano01.mp3" fadein 1.0


    show mainlogo
    with fade
    pause


## 1장, 챕터 구분 오른다

    hide mainlogo
    with fade

    scene bg black
    with dissolve
    nvl clear

    n "이 이야기는 픽션이며, 실존하는 단체 및 인명, 지명과는 관계 없습니다."
    n "이 게임은 번쩍거리는 이미지, 화면 전환 효과 등을 포함하고 있습니다. 광과민성 증후군 유발이 의심될 경우, 즉시 플레이를 멈추고 전문 의사와 상담하시길 바랍니다."

    nvl clear

    n "비주얼 노벨에 대한 설명을 들으시겠습니까?"

    menu:
        "예":

            nvl clear
            jump tutorial





        "아니오":
            jump scene1







label tutorial:

    n "비주얼 노벨은 소리, 그림, 텍스트를 통하여 이야기를 전달하는 게임입니다."
    n "게임을 진행할 때 여러가지 선택지가 나옵니다."
    n "골목길의 피에타는, 주인공 루이의 시점에서 선택해야 하는 상황들이 많습니다."
    n "게임을 플레이하며, 자신이 좋다고 생각하는 방향으로 이야기를 진행시키세요."
    n "좋은 결말이 있을수도 있고, 나쁜 사고를 당할 수도 있습니다. 모든 것은 당신의 선택에 달렸습니다."
    n "행운을 빕니다!"

    nvl clear

label scene1:
    cen "Chapter 1 : 『2112년 가을, C시』"
    play music "audio/NonN.mp3" loop
    nvl clear

    scene bg room1
    with pixellate
    # 이 장면의 배경을 수정하도록 해요

    cen "2112년, 가을 {vspace=10} C시 어딘가의 모텔."
    with dissolve

    nvl clear

    n "밤 11시."
    n "울리는 알람 소리에 잠이 깼다."
    n "…이런 시간에 일어나는 게 간만이라, 너무나도 피곤했다."
    n "동료 \'아문'\과 함께, 밤에 만나서 회의를 하기로 했었지만."
    n "그래도 그것과 별개로 일어나는 것은 힘들다."

    nvl clear

    n "나는 일어나자마자, 버릇처럼 화장실로 간다."
    n "'그 일'이 있은 이후로부터 생긴 습관이다."
    n "딱히 특별한 행동을 하지는 않는다. 아침 목욕 같은 건 사치라고 생각한다."
    n "그러니까, 이게 지금 내게 일어난 일이 맞는 건가."
    n "그런 걸 스스로 다시 확인하는 것에 가깝다."

    nvl clear

    #조명 딸깍, CG 띄우기

    scene event01
    with fade

    l "…."

    n "남색 눈동자. 날카로운 눈매. 그 외에는.. 아무것도 없다."
    n "확실히 인간은 아니다. 그렇지만 인간처럼 생기긴 했다."
    n "나와 아문은, 이 상태를 '스틱맨'이라고 부르기로 했다."
    n "애들이 그림판에다가 사람을 그리겠답시고 휘갈기는 형태."
    n "우리가 이런 모습으로 변해버린지도, 이걸로 2주 째다."

    nvl clear

    n "처음에는 나쁜 꿈인줄로만 알았다."
    n "그렇지만 이건 명백한 현실이었다. 루이는 인간이 아니다. 이 명제는 이제 참이다."
    n "2112년, C시에서 자경단 '가디언즈'의 신분으로 순찰 임무를 돌던 루이와 아문은 수상한 일당들을 목격했다."
    n "가면을 쓴 녀석들. 공통된 징표…"
    n "틀림없이, 사이비 종교 '연화의 아이들' 녀석들이다."
    n "작게는 게릴라식 포교, 크게는 테러의 조짐이 보인다. 이들은 전적이 있기 때문에 충분히 그런 판단을 할 수 있었다."
    n "그래서 수사에 나섰다."
    n "추격전, 몸싸움, 설전──────결론적으로, 그 녀석들을 막는 건 성공했다."

    nvl clear

    n "그러나 막는 과정에서 그 녀석들에게 습격을 당했다."
    n "그들은 알 수 없는 능력을 사용하여 '섬광'을 흩뿌렸다."
    n "시야를 빼앗긴 나와 아문은 정신을 잃었다."
    n "…그리고 우리는 정신을 차려보니 인간이 아닌 존재로 변해버리고 말았고,"
    n "일당들은 반죽음 상태로 거리에 놓여 있었다."
    n "그런 알 수 없는 이야기다."


    nvl clear
    # CG끄기

    l "(..자본의 원리로 움직이는 이 도시에서, 착한 사람 노릇을 해서 그런가.)"
    l "(돌아오는게 저주밖에 없는 것 같네, 이래서는…)"


    scene bg room1
    with dissolve


    n "─몸을 돌려, 화장실에서 빠져 나온다."
    n "나는 창밖을 통해 C시의 모습을 바라보았다."
    n "기술이 고도로 발달하여, 대도시에서도 모든 생활을 할 수 있게 된 시대."
    n "그게 바로 지금, 2112년이다."

    nvl clear

    n "농작물이 없어도 먹을 수 있다. 단백질 바를 만드는 기업에서 다양한 맛이 나온다."
    n "돈이 있다면 그런 걸 사서 먹으며 생활을 연명할 수 있다."
    n "주택을 짓지 않아도, 고도로 밀집된 아파트에서 집세를 내면 누구나 방을 가질 수 있다."
    n "가사 노동은 로봇이. 험난한 일은 돈이 필요한 사람이. 그 외의 사람들, 가진 사람들은 풍족하게."
    n "그리고 없는 사람들은 빈곤하게."
    nvl clear
    n "여가 시간에는 가상현실을 즐기며, 전파를 타고 1초당 수천 개씩 흐르는 정보를 받아들인다."
    n "말하자면, C시는 조지 오웰이라고 하는 사람이 썼던 소설과는 다르다. 누구도 감시하지 않는다. 누구도 지배하지 않는다."
    n "다만 모두가 모두의 적이다. 한없는 경쟁 구도에 휩싸여 있다."
    n "그러니 누구도 서로를 도우려 하지 않는다."

    nvl clear

    n "──그런 곳에서 나는 경찰 노릇을 하고 있었다."
    n "그리고 인간이 아닌 존재로 변해버렸다."
    n "조금 이상한 능력과 함께."
    n "그리고 그 중심에는───'연화의 아이들'이라는 사이비 종교가 얽혀 있다."
    n "점점 이상한 세상으로 빠져드는 것 같은, 기분이 드는 것도 이상하지 않겠지⋯"


    nvl clear

    mob1 "(똑똑똑)"

    show Loui02
    with dissolve

    n "노크 소리가 들려왔다."
    n "나는 급하게 테라스에서 몸을 돌려 안으로 들어왔다."

    l "(…벌써 알아냈다고?)"
    l "(대체 얼마나 집요한 거야?)"
    l "(이러다가 C시에서 있을 곳이 아예 없어지겠구만……)"


    mob1 "(쾅쾅쾅)"
    #SFX
    mob1 "없나 본데?"
    mob1 "아니야, 분명 있어. 없는 척하는 거겠지. …야! 빨리 열어!"

    show Loui03

    l "젠장………"

    nvl clear

    n "잠궈둔 문이 격하게 덜컹거린다."
    n "그리고, 곧 포트를 연결하는 소리가 들려왔다."
    n "이 상태로 가만히 있는다면 붙잡히는 건 시간문제였다."
    nvl clear

    n "발소리로 들어보니, 일행은 족히 서너명은 되어 보인다."
    n "추적자들은 끈질겼다. 며칠 전부터, 계속해서 나를 쫓아다니며 '제거'하려고 한다."
    n "이것 때문에 가디언즈 본부에게 지원을 받지 못하는 상황이다."
    n "그러니────나는 선택해야 한다."
    n "이 녀석들을……"

    nvl clear

    menu:
        "처치할 준비를 한다":
            jump battle

        "조용히 지나가기로 한다":
            jump silent

    label battle:
        nvl clear


        n "나는 녀석들이 들어올 것을 대비해 바로 공격할 수 있는 곳에 위치했다."
        n "…다행스럽게도 해킹 작업은 오래 걸리는 것 같았다. 그들은 곧바로 습격하지는 않았다."
        n "나는 숨을 참고, 조용히 기다렸다."
        n "녀석들이 문을 박차고 들어오면,"
        n "바로 머리부터 노린다."

        jump scene2

    label silent:
        nvl clear
        n "나는 조용히 모텔을 빠져나가기로 했다."
        n "아무런 소리도 내지 않고, 조심스레 걸음을 옮긴다."
        n "방에서 유일한 탈출구는 창문이다."
        n "충격 낙하 프로그램을 전개한다면…"
        nvl clear
        mob1 "…됐다, 열렸어요!"
        n "───너머에서 들려 오는 불길한 목소리."

        show Loui04
        with dissolve

        l "망할, 글렀나…!"


        jump scene2


    label scene2:
        nvl clear

        n "그리고 그 때."
        n "{w}{size=+15}쾅!{/size}{w} 하는 소리와 함께 문이 열렸다."
        with vpunch
        n "나는 녀석들이 '문을 열고 처음 들어 왔을 때'에는 보이지 않는 곳에 있었다."
        n "빛이 닿지 않는, 구석진 곳."

        nvl clear

        mob1 "어딨어?!"
        mob1 "찾아! 스캔 돌리면 한 명쯤은 나오겠지!"

        n "괴물이나 요괴를 형상화한 가면. 온몸을 뒤덮은 동양풍 의상."
        n "나를 노리는 사이비 종교 - '연화의 아이들'이 운용하고 있는 요원들이다."
        n "이름은 '집행자'. 다른 말로 하면, '야차'."
        n "..하여간, 컨셉을 알 수 없는 종교다."
        n "메시아와 유일신을 내세우는데, 외관은 동양이라니."
        n "게다가 야차는 불교 용어다."
        n "여러모로 C시의 종교답다."

        nvl clear

        n "어쨌거나, 이 녀석들이 스캔 기능을 이용한다면, 도주로까지 틀어막는 건 시간 문제다."
        n "…결국, 싸움을 피할 순 없다."
        n "──────나는 숨을 깊게 들이 쉬었다."
        n "녀석들이 나를 찾는 것은 시간 문제."
        n "그렇다면 대응할 뿐이다."
        n "하지만 어떻게?"

        nvl clear

        cen "여기서, 어떻게 빠져나가란 말인가?"

        nvl clear


    #씬전환해야함
    #심장박동소리, 움찔거리는 효과
    #음악을 바꿔야함

    zero "이봐."
    zero "그래, 여기야. 이 상황을 타개할 수 있는 방법. 바로 여기 있어."
    zero "뭔지 알고 있잖아?"
    nvl clear
    n "───목소리가, 들려왔다."
    n "그것은, 내가 '알고 있다'고 말했다."
    n "확실히, 이 모습이 된 이후로 쓸 수 있게 된 능력이 있다."
    n "그 능력만큼은 쓰고 싶지 않았다. 자신이, 어떻게 되어버리는 것 같았기 때문에───"
    nvl clear
    nd "뭐라는 거야⋯! 해커냐? 지금은 바쁘니까 나중에────"
    zero "'에우레카(Eureka)'. 네가 꺼냈던 그 쌍검. 주인이라고 할 수 있지."
    nd "──────!"
    nvl clear
    n "나는 그 단어를 듣고 당황했다."
    n "에우레카라는 이름은 가칭이다. 아문과 동료들이 장난삼아 붙인 것이다."
    n "그런데 그걸 알고 있다는 것은───"
    nvl clear

    zero "왜냐하면 난 네 자신이니까."
    zero "그리고 에우레카를 관장하는 너의 일부분이기도 하지."
    zero "자, 이리로 와."
    zero "저 불한당들은 관심 끄고. 너는 나와의 시간을 가져야만 해──────루이."

    nvl clear
    n "나는, 그 말을 듣고──── 눈을 감았다."
    n "이렇게 된 이후로 이상한 일에만 휘말리는 기분이다."
    n "그 계기조차 범상치 않았다는 건 인정하지만..."
    n "...제기랄, 이제 이렇게 고민할 시간이 없어─!"

    nvl clear

    n "나는 눈을 감았다."

    nvl clear

    scene bg white
    with flash


    n "눈을 감았다───────그렇게 생각한 순간."
    n "주변이, 하얗게 물든다."
    n "분명히 거멓게 변해야 할 시야가 흰색으로 변화했다. 시야가 탁 트였다."
    n "매트릭스에 접속한 것처럼 순간, 공간이 변화했다."
    n "그렇지만 이건 디지털 공간 따위가 아니다. 기술이 이뤄낸 것이 아니다."

    nvl clear

    nd "────이건───────────대체───────"
    zero "여기야, 여기."
    zero "바보 같이 허둥대지 말고 여기를 보라고. 여───기."
    nvl clear

    #여기 빠르게 이미지를 오른쪽으로 넘기는 느낌으로 해도 괜찮지 않을까? 일요일의 하소 부탁한다
    scene event02
    with Dissolve(2.0)
    pause
    nvl clear
    n "나는 그 존재를 바라 보았다."
    n "그것은 나와 비슷한 형태를 띄고 있었다."
    n "사람이 아닌, 스틱맨의 형태. 검은색 사람이다."
    n "그것은 어떤 의미에서는 나 자신이다. 그러나─적어도 '사람'처럼 보이진 않았다."
    n "계속 히죽히죽 웃고 있는 모습이 불길하다. 기분 나쁘다."
    nvl clear
    zero "내가 보았을 때 넌 곧 죽어."
    zero "저 가면 쓴 불한당들 좀 봐. 체격도 얄쌍한 너의 1.5배잖아."
    zero "승산은 없어. 잘 훈련된 경찰 양반."
    zero "육체가 아무리 쓸만하다고 해도 기술이 부족하면 이기지 못한다──────"
    zero "네 신념이기도 했잖아?"
    nvl clear

    n "────────────들려오는, 목소리."
    n "나는 이 녀석의 목소리를 들은 적이 없다."
    n "그런데도 친숙하다."
    nvl clear

    scene event02
    with redf
    nd "─끄으윽!!!!"
    n "순간 눈 앞이 붉게 점멸하며──────떠오르는 어느 기억들."
    n "아아──────"
    n "그래, 난 이 목소리를 알고 있어."

    nvl clear

    n "첫 번째로 이 힘을 사용했을 때.{nw}{p=0}{font=KOTRALEAP.ttf}{i}그 때가 언제였지────이 녀석의 목소리를 들은 적이 있었나?{/i}{/font}"
    n "'이것'의 제안으로 나는 되살아났고, 이 모습이 되었다.{nw}  {p=0}{font=KOTRALEAP.ttf}{i}기억의 혼선──맞지 않는 사고────엄습하는 데자뷰────{/i}{/font}"
    n "메피스토펠레스, 혹은 사탄. 어느 쪽이든 좋지 않은 존재다.{nw}  {p=0}{font=KOTRALEAP.ttf}{i}섬광────헤드라이트──────구급차────나────아문───{/i}{/font}"
    n "이 녀석의 힘으로 나는- 에우레카를 꺼내서-{p=0}{font=KOTRALEAP.ttf}{i}살해──절단─────폭력───밤거리───────사이렌─────────달려오는 사람들───────{/i}{/font}"
    n "{vspace=50}그러나────────────────이것만큼은 확실하다."
    nvl clear

    n "힘을 주고, 나에게 악을 종용한다."
    n "그는──────────────────────악마다."

    nvl clear
    zero "네가 얼마나 버틸 수 있을까? 한 3분?"
    zero "이봐, 루이. 쟤네는 진심이야. 그러니까 괜히 힘 빼서 좋을 건 없어."
    zero "선수끼리 왜 이래?"

    nvl clear

    nd "{size=+20}제길… 그럼 뭐 어떻게 해야하는데!{/size}" with vpunch
    nd "{size=+20}애초에... 대체 넌 뭐지? 나한테 왜 이러는 거냐?!{/size}" with vpunch

    nvl clear
    n "나는 '그것'을 보며 일갈했다. 그것은 아무런 반응을 보이지 않는다."
    n "'그것'은 계속해서 내게 속삭였다."
    nvl clear

    zero "넌 이미 답을 알고있어, 이 친구야."
    zero "좀 더 원초적인 걸 생각하란 말이야. 애도 아니고."
    zero "쟤네는 있지, 네 좋은 머리로 계산하건대, 단순히 좀 팬다고 쓰러지지 않아."
    zero "그러니까 답은 '에우레카'에 있어."
    zero "내 선물을 거부하기만 하지 마, 친구."

    nvl clear

    scene event03
    with dissolve

    zero "루이."
    zero "난 너야. 너는 나고."
    zero "물론 난 제로라는 이름을 가지고 있지. 그렇지만──"
    zero "이 차이를 모를 정도로 바보가 아니잖아? 넌 지금 거울 속의 거울을 보고 있는 거야."
    zero "거울에는 네 몸이 비치지. 그렇다면 거울 속의 거울에는 뭐가 비칠까? 영혼? 자아?"
    zero "──선{rt}·{/rt}택{rt}·{/rt}은{rt}·{/rt} 오{rt}·{/rt}로{rt}·{/rt}지{rt}·{/rt} 너{rt}·{/rt}에{rt}·{/rt}게 {rt}·{/rt}달{rt}·{/rt}려 {rt}·{/rt}있{rt}·{/rt}어{rt}·{/rt}."

    nvl clear

    nd "크윽...."
    n "나는 이 존재가 달갑지 않다."
    n "처음 만났을 때, 이 녀석이 내 몸으로 무슨 짓을 했는지 아문에게 들었을 때───"
    n "구토감이 올라오며 생에 대한 의지를 포기하고 싶었다."

    nvl clear
    n "이 녀석은 내 손으로, 다른 사람을 반죽음 상태로 만들어가며 날 억지로 살려냈다."
    n "다른 사람에게 해를 끼쳤다────C시의 밤거리를 피로 물들여가며."
    n "그래서 나는, 수상한 무기를 꺼낼 수 있고, 신비한 힘을 준 이 존재가──가증스럽다."

    nvl clear
    nd "네가 죽으면 나도 죽는거다──이런 건가?"
    nvl clear
    zero "그래. 우리는 공생하는 관계니까."
    zero "이곳에서는 아무도 보는 사람이 없잖아? 자, 자. 부끄러워하지 말고. 어서..."
    zero "이리로 와. 다가와, 루이."
    zero "너에게 좋은 것만을 주겠다고 내가 약속할테니..."
    nvl clear

    n "나는..."

    menu:
        "그를 받아들인다":

            jump awaken

        "역시 거부한다":

            jump baded1

label baded1:
    n "제로를 거부한 루이는, 이후 들이닥친 대집행자에게 목숨을 빼앗긴다."
    n "BAD END."
    jump akari1

label akari1:
    scene bg black

    akari "우와! 세상에! 진짜로 벌써 오셨어요? 히로인을 헷갈리신 것 같은데!"
    akari "네, 네. 루이 선배. 다짜고짜 취조실에 오셔서 당황스러운 건 아시겠는데요."
    akari "여기선 제가 더 짬이 높은 건 아시죠?"
    akari "설명하자면!"
    akari "'아카리 후배의 취조실'에 어서오세요~!"
    akari "이곳은 배드 엔딩, 데드 엔딩을 보면 찾아오는 취조실이랍니다."
    akari "그래서 선배..."
    akari "왜 그러셨죠?! 설마 거기서 살아남을 수 있을 거라고 생각하셨던 건가요!"
    akari "매도하는 건 아니지만!"
    akari "골목길의 피에타는 '마음의 힘'이 어떻게 되는지 지켜보는 작품이라고요. 에헴 에헴."
    akari "그러니까 그 기분 나쁜 녀석을 한 번 받아들여 보세요!"
    akari "그럼 저는~! 이만! 아카리 후배의 취조실은 여기까지!"
    akari "이제 현실의 선배님으로 돌아오실 차례에요!"

    return

label awaken:

    scene event04
    with dissolve

    n "나는 그 악마의 속삭임에 이끌려 다가갔다."
    n "이 녀석은 나에게 힘을 줄 수 있다. 확실하다."
    n "솔직히─────────제정신이었던 건지 잘 모르겠다."
    n "처음 그의 목소리를 들었을 때도 그랬다. 갑자기 찾아온, 내면의 방문자를──"
    n "난────────────어떻게 해야 할 지, 잘 모르고 있었다. 그래서 그저 이끌리기만 했다."
    n "그러나 지금은 안다."
    n "그를 받아 들이는 것은 곧 내 안의  {b}무{rt}·{/rt}언{rt}·{/rt}가{rt}·{/rt}{/b}를 받아들이는 것과 같다는 걸────────────"

    nvl clear

    zero "옳지, 옳지..."
    zero "이제와서 하는 이야기지만───후회는 하지 않겠지?"

    nvl clear

    n "그는 그렇게 다가와서, 나에게 손을 뻗었다."
    n "나는 어떠한 불가항력에 이끌리는 것처럼 그의 손과 가까워진다."
    n "후회?"
    n "그런 것 따위는 모른다."
    n "앞으로 어떻게 될지도──모른다."
    n "그저──────────이끌리는 대로───"

    nvl clear
    n "어느새 그와 나는 아주 가까워졌다. 눈도, 코도 없이, 그저 히죽거리는 입만 있는 그의 시선을 피했다."
    n "그렇지만 결국에는 바라 보아야만 한다. 탐탁치는 않아도──"
    n "에{rt}·{/rt}우{rt}·{/rt}레{rt}·{/rt}카{rt}·{/rt}를 꺼내기 위해서는────────────"
    n "그를──────받아 들여야만, 한다."

    nvl clear

    scene event05
    with dissolve
    pause

    zero "지금부터 네 속에서 그걸 꺼내기 시작한다."
    n "────깍지를 껴오는 그의 목소리는, 낮고 달콤하다."
    nd "아───"
    n "나는 무심코, 소리를 내어버리고 만다. 크고 거친 손길이 낯설었다."

    scene event06
    with dissolve
    pause

    zero "눈을 감고 상상해. 네가 할 수 있는 최대로 끔찍한 장면을."
    zero "에우레카는 부정적인 생각이 주는 선물이니까."
    zero "너의 마음을 끌어 올려야 해."

    nvl clear

    n "그는 점점 내게로 다가오고 있었다."
    n "숨이 닿을 정도로 가깝다."
    n "부정적인 생각?"
    n "나는 그런 걸 떠올릴, 리가───없다고────"

    nvl clear
    scene event06
    with flash

    nd "아─────"
    n "떠올리고 만다."
    n "그녀의 미소와 목소리를."
    n "지금 이제 내 곁에 없는 그 모습을."
    n "소중한───추억을."

    nvl clear

    nd "화이─── 화이를────────"
    nd "나는...화이를──────"
    nd "그녀를 구해야만 해──여기서 죽는 건───싫어────────..."

    nvl clear
    zero "그렇게 되기 싫지?"
    nd "죽고 싶지 않아... 난 해야 할 일이 있어."
    zero "그 해야 할 일이란 게 뭐지?"

    nvl clear

    nd "───화이를───────"
    nd "────────────────구해내는 것."
    n "정신을 차려보니, 온몸에 힘이 빠지기 시작한다."
    n "동시에 상념이 타오르기 시작한다."
    n "계속해서 한 곳에 생각을 집중하고 있었다."

    window hide
    scene event07
    with dissolve
    pause

    nvl clear
    n "그 자리에서 털썩, 쓰러져 주저 앉고 싶었다."
    n "그렇지만 그 녀석은 그런 나를 받아 들였다."
    nvl clear


    zero "그러기 위해서 너는 살아 남아야 해. 여기서 살아남을 수 있을까?"
    zero "그러기 위해서 너는 힘이 필요해. 여기서 녀석들을 죽일 수 있어?"
    n "나는──────그 말에, 대답하지 못한다."
    n "정말로 가능할까?"
    n "다른 사람들을 죽여서 살아남는 게?"
    n "단 하나의 목적을 위해서?"

    nvl clear

    zero "나에게는 보여. 네가 가지고 있는 힘이."
    zero "지금 네가 갖고 있는 그 힘을────────"
    zero "────────────여기서 해{rt}·{/rt}방{rt}·{/rt}시켜주마."

    nvl clear

    scene event08
    with flash
    pause 1

    scene event09
    with redf
    pause

    nd "흐억────────────"
    nd "{cps=40}{size=+25}아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아악──────────────────!!!!!!!!!!!!!!!{/size}{/cps}"
    n "나는────────────비명을 질렀다."
    n "무수한 고통이 엄습해 온다. 생각하기가 힘들다. 점점, 힘들어진다."
    nvl clear

    n "압도적인 고통이다. 시야가 점멸한다. 몸의 감각이 완전해진다. 뇌가 빠르게 회전한다. 그런 식으로계속해서──────약동한다."
    n "이런것은────처음이다, 그러니 버틸 수가 없었ㄷ────"
    nvl clear

    scene event10
    with bluef
    pause

    nd "흐어어억──────허억──────크윽─────────큭────────────"
    nd "아─────────하아──────아, 살──────려줘──────"
    zero "이걸로 사람은 죽지 않아."
    zero "왜냐하면 이곳은 『관념』의 세계니까."
    zero "이곳에서의 시간은 밖에서의 시간과 달라."
    zero "이곳에서의 감각은 밖에서의 감각과 달라."
    zero "너는 지금 네 안에 있는 고통을 마주하고 있는 것이다."

    nvl clear

    n "그는 그렇게 말하고서, 선지자처럼 손가락을 들어,"
    n "내 가슴에서 빼낸 '그것'을 가리켰다."
    n "제로의 손으로부터, 불길한 기운이 실처럼 뽑아져 나왔다."

    nvl clear

    zero "잘 기억해둬."
    zero "에스페로(Espero)는 바로 이거니까."
    zero "이번에는 에우레카(Eureka)의 형태로 써야겠군."
    zero "자, 루이, 받아."

    nvl clear

    n "제로는 나를 세워 일으키고선, 내 손에 그것을 꼭 쥐어 주었다."
    n "손에 잡히지 않을 정도로 감촉이 없지만 그것은 내 손 안에 들어왔다."
    n "그리고- 어둠의 줄기가 그것을 감싸기 시작했다."
    n "그 어둠은 내가 아는 감촉으로, 모습을 바꾸었다."

    nvl clear

    cen "{color=#000}이것이, 에우레카.{/color}"
    cen "{color=#000}네 안에서 건져 올린 마음의 무기.{/color}"

    nvl clear

    n "목소리가, 멀어진다."
    n "고통도 점차 멎어들어간다."
    n "그리고 나는──────점점 부유하며─────────"
#배틀씬
#아 여기 트랜지션 어떡하냐 진짜

    scene bg room1
    with flash

    nvl clear

    n "{size=+50}──────푸슈욱{/siz}" with hpunch

    n "흉기, 같은 것이 살을 찢는 소리가 적나라하게 들려왔다."
    n "가장 앞에 있는 녀석의 심장을 노렸다."
    n "그 녀석은, 눈동자를 아래로 내리 깔아 자신의 가슴에 아주 빠른 속도로 꽂힌 그것을 바라보았다."
    n "한 자루의 검이 옷과 피부를 꿰뚫고 관통했다."
    nvl clear

    nd "아────────"

    n "나는 그의 뼈, 혈관, 모든 것을 느낄 수 있었다."
    n "그 검은 나의 손에 쥐어져 있었고, 몰려들어 구타하고 끌고 가려는 녀석들에게 저항했다."
    n "저것을 불러내었기 때문에 가능한 일이었다."
    n "─────────에우레카(Eureka)."
    n "나의 '마음'이 형상화된 무기."
    n "제로가 준, 선물."

    nvl clear

    mob1 "…!"

    show Loui weapon01
    with dissolve

    l "…당하고만 있을 줄 알았냐."
    l "사람을 쳤으면 맞을 준비도 되어 있어야 하는 게 정상 아니냐?"

    n "그렇게 말하고서 왼손에 쥔 에우레카로 다시 한 번,"
    n "그 녀석의 가슴을 관통시켰다."
    nvl clear

    n "나는, 한 녀석의 가슴에 꽂은 두 개의 검을 바라보았다."
    n "방금 전에는 피부를 꿰뚫고 뼈를 박살내는 소리가 적나라하게 들려왔었다."
    n "아직 꿰뚫지는 않았다. 내가 부순 것은, 그 녀석의 두꺼운 기계 몸체 뿐이었다."
    n "그러니 행동불능이 된 이 녀석을 죽이려면, 칼을 더 깊게 꽂아야 한다."

    nvl clear

    n "이 두 자루의 검은, 어딘가에 숨겨둔 것도, 누군가가 보내준 것도 아니었다."
    n "눈 앞에 갑자기 나타났다고 해도 좋을 정도로, 소환되었다."
    n "'연화의 아이들' 녀석들은 이걸,"
    n "'마음의 힘', {p} 에스페로(Espero)라고 부르는 모양이다."


    nvl clear

    mob1 "큭, 크헉……."


    l "선택해."
    l "이 녀석만 희생시킬지, 아니면 나랑 끝까지 싸울지."
    l "그리고…너희들도 잘 알텐데."
    l "에스페로를 쓰는 사람을, 너희 정도의 무장으로 이길 수 없다는 걸."

    n "나는 손에 힘을 주었다."
    n "이 자식의 목숨이 나에게 달려 있다. 그러니 녀석들도 쉽게 접근하진 못할 것이다."
    n "어차피 '집행자'들은 대부분 사이보그다. 그들의 외관에서부터 알 수 있었다."
    n "찢어진 소매로부터 피부가 드러났는데, 확실히 기업제 크롬이었다."
    n "그렇다면──설령 심장을 뚫는다고 해도 뇌만 보존한다면 다시 살아날 수 있을 테다."

    nvl clear

    mob1 "…안 돼. 여기서 몰살당하면 우리도 손해야."
    mob1 "그렇다고 저 녀석이 풀어줄지는…"
    l "나도 괜히 기분 더러워지고 싶은 거 아니거든."
    l "빨리 정해. 얘 죽는다."
    mob1 "젠장….. …"
    mob1 "ㅅ…선배… 저, 숨,이……."
    l "엄살부리지 마. 심장까지는 닿지도 않았어."

    n "이 방식의 전투는, 해본 적이 없지만 알 수 있었다."
    n "칼의 위력, 그리고 지금 나의 몸 상태."
    n "지금의 나로서는, 마음만 먹으면 지금 여기 있는 모두를 몇 등분으로 분해해서 도륙내버릴 수도 있다."
    n "더 이상 사람이 아닌 것으로 해체하는 것도 가능하다."

    nvl clear

    n "'집행자'들은 다친 사람들을 뒤로 보내며 나를 경계하고 있었다."
    n "나는 마지막 기회를 주기로 했다."

    nvl clear

    l "지금 물러나서, 날 못 찾았다고 해. 서로 입을 맞추는 거지. 어떤가?"

    mob1 "…"

    n "녀석들은 서로를 바라 보았다."
    n "여전히 칼──에우레카는 그 '집행자' 중 한 명의 가슴에 꽂혀 있었다."
    n "그 녀석은, 고통을 참으려는 듯 부들거리며 일그러진 얼굴을 지어 보였다."
    n "히죽."
    n "-그러다 그 녀석은, 웃어보였다."
    n "나는 거기서 알아차려야 했다."

    nvl clear

    n "────이 녀석들은 그냥 말해서 듣는 녀석은 아니었다."

    nvl clear

    n "「지금이다!」"
    with vpunch

    n "갑작스레 들려 온 함성. 녀석들은 한 번에 달려 들었다."
    n "그것에 놀라진 않았지만, 뒤이은 현상에는 조금 동요했다."
    n "「윽… 크으악……!」"
    n "가슴에 칼이 박힌 그 녀석이, 뒤로 빠르게 빠지면서 칼날을 스스로 빼냈다."
    n "그의 몸 속에 있던 에우레카가 모습을 드러냈다."
    n "인공 혈액으로 더러워진 칼날이, 짙은 푸른색을 내며 그곳에 있었다."


    nvl clear

    n "하지만 거기서 끝이 아니었다."

    nvl clear

    n "{size=+25}「거길 보면 쓰나!」{/size}"

    show Loui attacked01
    with vpunch
    with hpunch


    n "───빠각!"
    n "집행자 중 한 명이, 이 모텔 방에 있던 의자를 들어 내 머리를 가격했다."

    nvl clear

    hide Loui attacked01

    n "원래 인간이라면, 후두부를 그 정도로 가격당한다면, 죽는다."
    n "최소 기절한다."
    n "하지만────"
    nvl clear

    show Loui weapon02
    with dissolve

    l "...그게 다냐?"

    n "하지만 몰려오는 건 통증 뿐이었다."
    n "정신은 멀쩡했다. 욱씬거리는 뒷통수만 제외한다면."
    n "──────아니, 어떤 의미에서는 멀쩡하다고 볼 순 없겠지만."
    n "나는 고개를 들어 그 녀석들을 노려보고 있었다."

    hide Loui02
    with None

    show Loui weapon01
    with dissolve

    n "그리고────────즉시 에우레카를 꺼냈다."

    nvl clear

    mob1 "뭐, 뭐야...! 분명 온 힘을 다해 내려쳤는데...!"
    l "그러니까────그게 다냐고 묻잖아."
    n "나에게 처음으로 칼이 꽂힌 사람은, 뒤로 물러났다."
    n "그리고 나머지 서너명이 점점 이쪽으로 다가오고 있었다."

    nvl clear

    mob1 "눈이 완전히 맛이 갔군. 너 약이라도 했냐?"
    mob1 "얘들아, 본때를 보여주자!"

    n "그들이 들고 있는 것은 하나 같이 기계로 된 무기다."
    n "C시에서 흔히 찾아볼 수 있는 것들. 펄스건, 크롬으로 만든 칼날."

    nvl clear

    n "그렇지만 그것들은 에우레카를 이기지 못한다."
    n "나는 말없이 에우레카를 쥐고 빠르게 그 녀석들에게 달려갔다."
    n "몸이 이렇게 변하고 난 뒤로는 동작이 가벼워졌다."
    n "인간인 저 녀석들을 상대로는, 충분히 유리하다는 이야기다."

#검 이펙트

    with vpunch
    with hpunch

    n "에우레카가 사선을 긋고, 다시 내려 찍는다."
    n "춤을 추듯이 움직이는 몸. 가볍다."
    n "눈 앞에 있는 집행자들이 낙엽처럼 쓰러진다."
    n "「크흐억-!」"
    n "위에서 아래로 내려 찍듯이, 검을 휘둘렀다. 피부를 찢는 감각이 선연하다."
    n "그렇지만 여기에서 멈출 순 없다."

    nvl clear

    n "찌르고, 찌르고, 다른 팔로는 옆에서 다가오는 녀석의 얼굴을 가격한다."
    n "「이 자식이..!!」"
    n "녀석들은 멍청했다."
    n "신체 능력이 애초에 상대가 안 되는데 계속해서 달려드니 지는 게 당연하다."
    n "붙어오는 그 '집행자' 녀석들을, 팔꿈치로 세게 치거나 에우레카로 베었다."
    n "인조 피부, 인조 신경, 인조 골조- 그렇기 때문에 통증을 덜 느끼는 모양이었다."
    n "그렇다면 계속 베는 수밖에."

    nvl clear

    show Loui weapon01
    with dissolve

    n "───그나저나 공간이 좁다. 이런 곳에서는 불리하다."
    n "이 방은 약 8평 정도 되는 모텔방이다. 몸을 자유롭게 움직일 수 있는 것은 이쪽이다."
    n "여러 가지 공간을 활용해야하는 나에게, 좁은 공간은 되려 독이다."
    n "그러니 벗어나야만 했다."
    n "그리고──무리하게 싸울 필요도 없으니까."
    n "일단은 이곳에서 벗어난다. 맞받아칠지, 따돌릴지는 그때 가서 하면 되는 선택이다."

    nvl clear

    n "──녀석들은 한 번 얻어맞고 정신을 차리지 못했다."
    n "나는 그 틈을 타, 문을 가로막고 있던 녀석을 빡 하고 에우레카의 칼등으로 쳐냈다."
    n "그리고 도망친다."
    n "「-으헉…허억.. …제기랄, 도망친다!」"
    n "「잡아, 놓치지 마!」"

    nvl clear

    scene bg bstreet
    with pixellate

    show Loui weapon01
    with dissolve


    n "등지고 나선, 열린 문에서 그런 소리가 들려왔다. 나는 그걸 무시했다."
    n "그리고 사이버웨어를 작동시켰다. 눈 앞에 바로 스크린이 떠올랐다."
    n "계단을 내려가고, 복도로 뛰쳐나갔다. 그러자 C시의 흔한 풍경이 떠올랐다."
    n "네온 사인, 거리에 아무렇게나 나뒹구는 부랑자, 그리고 높이 세워진 건물들."

    nvl clear

    n "나는 그 사이를──────────냅다 질주한다."
    n "뒤를 돌아보자, 녀석들이 무시무시한 속도로 쫓아오기 시작했다."
    n "여기서 정신을 차리지 않으면 그대로 잡히고, 아마 아까보다 더 심한 강도로 구타당한다."
    n "살기 위해서라도, 지금은 잡히면 안 된다……!"
    n "─────────그리고, 머릿속을 채운 한 가지 생각."

    nvl clear

    n2 "(뚜르르르르……)"
    amphone "네, 아문 전화 받았습니다~!"
    l "…아문, 나 좀 도와줄 수 있어? 귀찮게 하는 녀석들이…"
    amphone "굉장하네~ 벌써 추적자가 붙은 거야? 체력도 좋아라!"
    l "한가하게 대답하지 말고!"
    amphone "아하하. 그래서 뭘 도와주면 돼?"
    l "삼천거리 근처 골목인데, 좌표를 보낼테니까, 근처에 적당히 싸울만한 곳을 알려줘."
    amphone "'싸울만한 곳?'"
    l "지금 ‘이 힘’의 정체가 네트워크로 퍼지면 엄청 곤란해지잖아……!"
    amphone "아~ 맞네. 잠깐만 기다려주세요~"
    amphone "쫓기는 중이지? 다리 부러지지 않게 조심하고!"

    n "곧이어 AI 비서의 목소리가 들려왔다. 잠깐만 기다리라는 것치곤, 꽤 빨랐다."
    n "{font=DungGeunMo.ttf}「잠시 뒤 우회전입니다.」{/font}"
    n "그 말을 들으며 계속 방향을 바꾸었다."
    n "왼쪽, 오른쪽, 가로지르고──────달린다."
    n "복잡한 미로 같은 C시의 거리를, 에우레카를 손에 쥔 채 달리고 있었다."
    n "녀석들 역시 계속해서 쫓아왔다."

    nvl clear

    n "{size=+20}탕! 탕!{/size}"
    n "──화기도 있었나? 이거, 안 좋은 걸."
    n "이 거리에서 총이라도 맞으면 곤란하다. 여기서 해치워야하나──"

    nvl clear

    n "………"
    n "……………"
    n "………………………………"
    n "「20m 직진 후 목적지 도착입니다.」"
    n "그리고 내비게이션이 종료된다. 나는 앞을 바라보았다."

    nvl clear
    # 배경바꾸기

    scene bg harlem
    with pixellate

    n "제격이다. 넓게 조성된 공터가 나타났다."
    n "공터, 라기에는 쓰레기장 근처지만."
    n "괜찮다. 어차피 C시에서는 다투는 게 일상이다."
    n "녀석들, 집행자들은 다가오고 있었다."
    n "손에는 온갖 무기들이 들려 있었다. {w}이거이거, 완전 깡패 집단이구만.{w}"
    n "나는 천천히 물러났다. 에우레카는 여전히 손에 들려 있다."
    n "기회만 있다면─ 선제공격을 해도 좋다."

    nvl clear

    hide Loui weapon01
    with dissolve

    mob1 "─────물러나."
    mob1 "………!!!!"
    mob1 "…………!!!!!!!"
    mob1 "대집행자님…………………!"

    n "기계로 변조한 목소리가 들려왔다. 나는 그쪽을 바라보았다."

    hide window

    show maskman
    with dissolve
    pause

    n "──어두운 골목에서, 누군가가 저벅저벅 걸어오고 있었다."
    n "가장 먼저 눈에 들어오는 것은, 무기."
    n "보름달을 형상화한 것 같은 차크람 형태다. 그러나, 무늬가 반달처럼 되어 있어 ‘반월’이라고 인식하게 된다."
    n "그 다음으로 목격하는 것은, 얼굴."
    n "그는 가면을 쓰고 있었다."
    n "입이 보이지 않는다. 눈도, 눈동자가 없어 공허한 검은색으로만 보인다."
    n "그리고─── 갓과, 천사 모양의 헤일로. 악마 뿔 모양의 머리장식."

    nvl clear

    n "다른 녀석들 보다는, 훨씬 더 '야차'스럽다."

    nvl clear

    nd "너희들 힘으로는 녀석들을 이기지 못해. 후퇴해서 정비하는 게 나을 거야."
    nd "알겠습니다……!"
    n "나는 그들을 바라본다. 온갖 가면을 쓴 집행자들은, 물러났다."
    n "그리고 그 ‘대집행자’라는 녀석만이 내 쪽으로 뚜벅뚜벅 걸어오고 있었다."
    n "그 녀석을 뚱하게 바라보았다."
    n "싸우자는 건가."

    nvl clear

    hide window
    show Loui at left
    with dissolve
    show maskman right at right
    with dissolve

    nd "────하나만 묻겠습니다, 불신자."
    n "존댓말을 하는 그 목소리에 고개를 기울였다."
    nd "뭐지."
    nd "그 힘은 연화님이 내린 신의 축복───에스페로(Espero). 그런 축복을 부여받고도 우리들에게 저항하고 싶은건가요?"
    n "나는 코웃음을 참기가 힘들었다. 하, 하고 비웃어주었다."
    nd "지금이라도 투항하면, 당신을 동료로서 받아들일 의향도 있습니다."

    nvl clear

    n "동료?"
    n "연화의 아이들이랑?"
    n "웃기지도 않는 소리다."
    nd "…나 참. 그쪽들이 준 힘이라고 꼭 그쪽 편에 붙어야하는 것도 아니고."
    nd "애초에 그쪽이 '사고로' 우리에게 준 힘 아니었던가?"
    nd "──────그러면 이쪽도 하나만 묻지, 광신도."

    nvl clear

    nd "────화이, 라고 하는 사람을 알고 있나?"

    n "나는 찔러보는 마음으로 그렇게 말했다."
    n "그렇지만 그 ‘집행자’는 확실히 동요했다."

    nvl clear

    nd "{size=+15}그 이름을 감히 입에...!{/size}"
    n "──────어이쿠, 화를 내는군."
    n "나는 그를 더 자극해보기로 했다."
    nd "화이. 지금 이름은 ‘연화’. ‘연화의 아이들’이라는 이름에서 알 수 있듯이 너희들의 수장이지."
    nd "몇 년 전, 원래 신으로 활동하던 '연화'는 죽었어."
    nd "그리고 그 대체재로 선출된게 '화이'지."
    nd "모른다고 생각하지 마. 너희들은 생각보다─────────허술한 집단이니까."

    nvl clear

    scene event11
    with dissolve
    pause

    play music "audio/battle01.mp3" loop

    nd "────────────방금 정했어요."
    nd "당신은───────────────최대한 고통스럽게 죽이겠다고."
    n "화를 내고 있다. 아무래도 역린인 모양이다."
    n "살기가 느껴진다. 누군가를 정말 죽일 기세로 이쪽을 노려보고 있다."
    n "텅 빈 눈동자가 그렇게 말하고 있었다."
    n "너는 이제 곧, 죽을 거라고."

    nvl clear

    scene bg harlem
    with dissolve
    n "하지만 괜찮다."
    n "감정적으로 동요하는 타입이니, 싸우면서 잘 자극한다면 빈틈을 노릴 수 있다는 뜻이다."
    nvl clear
    nd "아무튼 간에──────────"
    nd "어쨌든 그녀는 원래 인간이고, ‘화이’라는 본명을 가지고 있었지."
    nd "화이는─────나에게 있어서도 소중한 사람이야. 여신이 아니라."
    nd "알겠냐, 대집행자. {w}나는 그녀를 구할 거야.{w=1.0} 너희들이 이 힘을 부여해준 덕분에 자신이 붙었거든."

    nvl clear

    n "나는 그렇게 선언한다."
    n "그러자, 그는 무기를 무섭게 빼어 들었다."
    n "{cps=*0.1}──────그 두 개의 달에서, {b}스릉{/b}, 하며 칼날 같은 소리가 났다.{/cps}"
    n "순간 침을 꿀꺽 삼킨다."
    n "{cps=*0.8}베이면──────────죽는다.{/cps}"
    n "나는 그렇게 예감했다."
    n "진심을 다해서 싸워야한다. 설령 상대방을 죽이는 일이 있다 하더라도..."

    nvl clear

    with flash

    n "{i}{size=+15}스릉-{/size}{/i}"
    n "갑자기 눈 앞을 지나가는 그림자."
    n "저 멀리 있었던 대집행자였다. 어느새 이 틈에 온 것이다."
    n "빠르다. 그것도 나보다, 훨씬."
    n "뒤로 슬쩍 몸을 기울이고, 내빼는 반사신경이 없었다면 그대로 얼굴이 가로로 두쪽이 났으리라."
    n "이 녀석, 빠르다...!"

    nvl clear

    n "나는 그렇게 말하며 에우레카를 정방향으로 쥐었다."
    n "힘이 과하게 들어가 있다. 놀란 모양이다."
    n "그렇지만─────────맞고만 있을 수는 없다."

    nvl clear

#2

    nvl hide
    with dissolve

    scene event12
    with dissolve

    n "{i}{size=+15}-캉! 탕! 캉!{/size}{/i}" with vpunch
    with hpunch
    n "합(合)이 오간다."
    n "아까 녀석들과는 다르다."
    n "이 녀석은 에우레카의 움직임을 보고 있었다. 몸이 훨씬 가벼워진 지금으로는, 일반인의 눈이라면 내 움직임을 파악하지 못하리라 생각했지만."
    n "내 움직임, 그리고 다음에 이어질 동작까지 예측하고 있었다."
    n "버겁다."
    n "내가 간신히 따라가고 있다고 해도 좋을 정도로, 역부족이었다."
    n "이 싸움을 오래 해서는 안 된다는 예감이 든다."

    l "큭.......!"
    mob1 "입만 살아서는...! 연화님을 모독한 주제에.......!"

    nvl clear

    n "계속해서 공격이 몰아쳤다. 합이 맞들어가는 순간─────────"
    n "나는 그의 눈을 보았다. 가면 너머에서 살기가 느껴진다."
    n "대단한 기세다. 내가 순간적으로 겁을 먹을 정도로."

    nvl clear

    n "{i}{size=+15}─────────팍{/size}{/i}" with hpunch
    n "-순간 뒤로 내동댕이 쳐지는 몸. 몸동작 뿐만 아니라 힘도 강력했다."
    n "눈 앞에 그는 빠르게 다가오지 않았다. 대신 손을 뻗어 그 ‘달’을, 이쪽으로 늘였다."

    nvl clear

    n "{color=#f00}{i}{size=+25}-프슉{/size}{/i}{/color}" with redf

    nvl clear

    scene bg harlem

    show Loui attacked01
    with dissolve

    l "──────"
    l "흐으억──────!"
    mob1 "이대로 얌전히 죽여줄거라고 생각하지 마라!"

    hide Loui attacked01
    with dissolve

    n "와이어를 사용한 중거리 공격이다. 그대로 이쪽으로 검을 늘였다."
    n "무희와도 같은 몸동작. 그렇지만 빠르다."
    n "이 녀석은, 말도 안 된다."
    n "기계의 도움을 받지 않고서 저런 싸움 방식은 불가능하다. 그런데도 해내고 있었다."
    n "-배에 닿은 칼날이, 상처를 만들어냈다. 곧 피가 쏟아졌다."
    n "입에서 혈액의 맛이 느껴진다. 죽지는 않는다. 그렇지만 제법 심한 상처긴 하다."
    n "그렇지만 다음 공격을 속수무책으로 맞는다면───죽는다."

    nvl clear

    n "정말로──────────죽는다."

    nvl clear




    nd "{size=+25}별 것도 아닌게───!{/size}"
    n "──────────"

    show event13
    with Dissolve(0.3)

    n2 "──────────피융!"

    nvl clear

    n2 "방금 내가 들은 소리는───땅을 꿰뚫는 탄알이었다."
    n2 "미사일 같지만 그보다 훨씬 작고, 빨랐다. 나는 저 위를 바라보았다."

    scene bg harlem
    with dissolve

    n2 "근처 건물 창문에서 쏜 것이다."
    n2 "무엇인지 알 것 같아서────이마를 찌푸렸다."
    n2 "눈의 확대 프로그램을 개시해 그쪽을 바라보았다."

    nvl clear

    show Amun shoot02
    with dissolve

    am "이봐, 거기 가면쟁이!"
    am "내 친구한테 그럼 못 써! 법이 없다고 해서 남을 맘대로 패도 좋다곤 안했다?"

    show Amun shoot01

    am "걔는 나만 팰 수 있거든!"

    nvl clear
    n "────────────아문이다."
    n "베이지색 코트, 뿔테 안경, 그리고 자신만만한 금색 눈동자."
    n "멀리서 보아도, 그였다. 아마 화성에서 본다고 해도 그라고 알 수 있었을테지."

    nvl clear

    hide Amun shoot01
    with dissolve

    show maskman
    with dissolve

    nd "에스페로...?! 그렇다는 건..."
    n "그 ‘대집행자’라고 하는 녀석은 위와, 나를 번갈아보며 이를 뿌득 가는 소리를 내었다."
    n "그리고 순간 통신이 걸려온 건지, 허공을 보며 무어라 말하기 시작했다."
    nd "──복귀, 입니까?"
    nd "그렇지만...!"
    nd "...알겠습니다...."

    nvl clear

    n "그는 그렇게 말하고서, 이쪽을 바라보았다."
    n "증오에 가득찬, 기계로 변조된 목소리가 귀에 꽂혀왔다. {w}-아, 귀는 이제 없지만.{w=1.0}"
    nd "다음에 만날 때는... {p}살아 돌아가는 사람이 한 명 뿐일 줄 알아라.{p=1.0}"

    nvl clear

    hide maskman

    window hide
    show Loui bleed07 at left
    with dissolve
    pause

    stop music

    nd "네, 네. 용무 보러 가시죠."
    n "나는 그렇게 빈정댔고, 아문 역시 멀리서 크게 외쳤다."
    show amun02
    with dissolve
    pause
    nd "그쪽도 체포될 준비나 하시지 그래!"
    n "그 ‘대집행자’는 이윽고 모습을 감추었다. 답도 하지 않은 채였다."
    n "나는 그에게 위치 추적기 붙이지도 않았고, 미행도 하지 않았다."
    n "───그녀를 만나기 위해서라면, 언젠가는 만나게 된다. 그러니 다음을 기약했다."
    n "그나저나..."

    nvl clear

    show Loui bleed01
    with dissolve

    l "...아문. 내려와봐."

    hide amun02
    with dissolve
    show Amun right smile at right
    with dissolve

    am "네~!"
    n2 "그리고 그는 아래로 내려왔다."
    n2 "나는, 이제 아무도 없는 공터에서 그를 바라 보았다."
    n2 "몇 번을 봐도... 멀대같이 크다."
    n2 "그건 '저 모습'으로 변해버려도 마찬가지인 것 같았다."

    show Amun right hand at right

    am "조심 좀 하라니까. 혹시나 해봐서 왔는데 맞는 판단이었네."
    l "난 위치만 달라고 했거든."

    show Loui bleed04
    with dissolve

    l "그리고, 저 녀석들이 네 위치를 알았으면 어떻게 할 작정이었는데?"
    am "사이버웨어도 다 꺼놔서 그럴 일은 없어. 너무 걱정하지 말라니까~"
    l "(진짜, 생각이 있는 건지 없는 건지...)"

    show Loui bleed08
    with dissolve

    l "어쨌던... 고마워."

    show Loui bleed02
    with dissolve

    l "큭......"

    show Amun surprisedL at right
    with dissolve

    am "..뭐야, 왜 그래?"

    hide Loui bleed02
    with None

    show Loui injured01 at left
    with dissolve

    l "나 배가 좀 아파서... ...차 있냐?"

    show Amun smileL at right
    with dissolve

    am "뭐야, 그런 거야? 그거야 대령해놨습죠~!"

    show Amun surprisedL2 at right
    with dissolve

    am "아니, 잠깐. 뭐야 이게! 너, 배에 상처가...!"
    l "내가 배 아프다고 말 했잖아 새끼야..."
    am "멀리서 봐서 몰랐는데! 상처가 이렇게 심각할 줄은...?!"
    am "여기서 기다려! 금방 불러 올 게!"

    show Loui injured02
    with wipeleft

    l "(...사실 한계다.)"
    l "(상처가 너무 깊어서 현기증이 날 정도였으니까.)"
    l "(...안 돼, 점점 눈이 감겨 와...)"

    show Loui injured03

    l "...아문..."
    am "왜?! 뭐 필요한 거 있어?!"
    l "나 너 믿고 잘 게..."

    hide Loui injured03
    with fadehold

    n2 "털썩-"

    show Amun shout2 at center
    with dissolve

    am "잠깐, 야, 야!! 정신차려!"
    am "내가 널 들고 어떻게 가라고 멍청아!!!"

    hide Amun shout2
    with dissolve


    n "-그 뒤로의 일은, 일편적인 장면들만 기억난다."
    n "어지럼증 속에서 아문의 도움을 받아 응급처치를 한 것."
    n "차에 누워서, 본부로 돌아간 것."
    n "그리고 가디언즈 사람들에게 잔소리를 들은 것."
    n "이상하게도, 창문에 기대어 본 풍경만큼은 기억난다."

    nvl clear

    scene bg city
    with pixellate
    play music "audio/001.mp3" loop

    n "빽빽하게 밀집된 칠룡성채 거리."
    n "창문 너머로 보이는 건 C시의 어둠이라고 할 수 있는, 생생한 골목길의 풍경이다."
    n "네온사인이 공중을 현란하게 날아 다니며, 사람들의 시야를 유린했다. "
    n "이목을 이끄는 기업의 캐치프레이즈. 사람들의 뇌를 마비시키는 프로파간다."
    n "그리고 내가 태어나기 전부터 있었던, 오래된 간판이 비에 젖어 녹슬어 있었다."
    n "한자, 한국어, 일본어, 영어. 모든 것이 뒤섞인 채였다. "

    nvl clear

    n "그 수많은 광고들 속에서, 내가 차량 안에서 본 건, 오직 하나 뿐이었다."
    nd "-당신도 구원받을 수 있습니다."
    n "'구원'이라는 캐치프레이즈를 내세우며, 쓸데없이 평화로운 음악이 흐른다. "
    nd "'연화'님은 말씀하십니다. 이 혼탁한 세상에서, 오직 믿음과 유대만이 사람을 구원할 수 있다고!"
    nd "믿음만이 이 죄악의 세상에서 여러분을 구할 수 있습니다."
    nd "연화의 아이들, 근처의 예배당에서 말씀을 들어보세요."

    nvl clear

    n "───바보 같다."
    n "통증으로 정신이 흐릿한 와중에도 나는 그렇게 생각했다."
    n "화면은 곧 '연화님'이 기도하는 모습을 송출했다. 카메라로 찍은 것이 확실해보이는 영상이었다."
    n "영상 속의 그녀는, 몇 명의 신자에게 둘러싸여 종교적인 분위기를 연출하고 있었다."

    nvl clear

    n "물론, 그녀는 내가 알고 있는 사람이다."
    n "───화이."
    n "항상 꿈 속에 나오곤 하는 그녀."
    n "나는 창에 기댄 채로 화면 속의 화이를 바라 보았다."

    show Loui injured02
    with dissolve

    l "...화이....."
    l "기다, 려....."
    l "반드시......."

    scene bg black
    with pixellate

    stop music

    cen "1장 종료."

    # 이후 타이틀 오른다.
    #저장하시겠습니까?
    #챕터카드 뜨고..
    nvl clear

    scene bg bstreet
    with dissolve

    play music "audio/NonN.mp3" loop
    n "며칠 후."
    n "다른 말로 하면: 2112년, 9월 15일."

    nvl clear

    n "나는 후드를 덮어쓰고 혼천군(混川郡) 거리를 걷고 있었다."
    n "사천거리, 칠룡성채, 가디언즈 본부가 있는 하연동, 그 외에도 수많은 길거리 의사들과 해커..."
    n "혼천군은 C시의 주요 장기다. 개성 가득한 기업과 사람들이 오고 간다."
    n "목적도 분위기도 다양하다. 부자 기업가부터 사람 죽이는 데 특화된 요원까지."

    nvl clear

    n "'도시의 심장'이라는 호칭을 도심 지역인 썬로드(Sunroad)가 가져갔으니..."
    n "여기는 간 정도 되려나."
    n "혼천군 C시 남부의 행정 구역이었고, 한자를 공용어로 바꾼 '하이브리디안{size=-10}Hybridian{/size}'으로 자주 불렸다."
    n "혼합된 간? 웃기는 작명이다."
    n "그래도 도시의 독소를 빼주는 곳이니 간이 적당하리라."

    nvl clear

    n "----그 습격이 있은 이후로,'연화의 아이들'에서 습격이 온 적은 없었다."
    n "협박도 제안도 없다. 그들은 계속해서 전도나 홍보 활동만 하고 있었다."
    n "연화의 아이들이 주로 활동하는 사천거리 주변에 얼씬도 하지 않는 방법은 좋은 선택이었던 것 같다."

    nvl clear

    n "그동안은 가디언즈에서 마련해 은신처에서 지냈다."
    n "정말이지, 봉급은 짜도 이런 지원은 잘 해주는 직장이라니까."
    n "자원봉사단 활동도 직장이라고 할 수 있다면 말이지."
    n "아문이나 다른 가디언즈 사람들과는 꾸준히 연락했다."
    n "그렇지만 '눈에 띄는 행동'은 최대한 삼갔다."

    nvl clear

    n "한적한 교외 지역으로 향한다. 칠룡성채를 지나야 했어서 최대한 걸음을 빨리 옮겼다"
    n "다른 사람에게 폐를 끼치고 싶지 않아서 택시도 부르지 않았다."
    n "하이브리디안의 교외는 제법 한가하다."
    n "혼천군이 그 이름대로 온갖 잡다한 것들이 섞인 도시 구역인것과 대비되어,"
    n "조용한, 세계의 틈새 같은 느낌이다."
    n "적어지는 네온과 온라인 상의 소음을 뒤로 하고 나는 복잡한 골목길로 들어섰다."

    nvl clear

    n "작은 건물들이 즐비한 곳에 내가 가려는 곳이 있었다."
    n "홀로그램으로 폐허처럼 꾸며두었다. 지나가는 사람들은 여기를 전혀 신경쓰지 않는다."
    n "다들 각자의 사이버웨어에 빠져, 인터넷 안에 있는 정보들을 확인하기 바쁠 뿐."
    n "그렇지만 이곳은, 사실 깔끔하게 단장한 가디언즈 사무실이다."
    n "말하자면 잘 보면 알 수 있는 장소다."

    nvl clear

    n "정부라는 게 존재했던 옛날이라면, 가디언즈는 경찰 기관이었을 것이다."
    n "그렇지만 기업이 고도로 성장하고, 나라 전체를 집어삼킨 이후-"
    n "정치와 치안이 모두 민간 기업으로 넘어갔고, 모든 것에 값이 매겨졌다."
    n "경호원을 고용하는 건  20만 캐씨(KaeC), 과자 한 봉지는 4천 캐씨(KaeC), 그런 식으로."

    nvl clear
    n "그런 상황에 반발하여 세워진, 오직 공공을 위해 일하는 단체 - 자경단 가디언즈다."
    n "가디언즈는 도심 지역을 거점으로 삼고, 칠룡성채 부근으로 파견 나가는 방식으로 일하는 경우가 많다."
    n "그러니 이 사무실은 내 파견지인 셈이다."

    nvl clear


    scene bg office
    with dissolve

    n "연화의 아이들 수사를 시작하면서 추적자가 붙었다는 이유만으로, 가디언즈는 나에게 이곳을 내주었다."
    n "물론 아문과 내가 인간이 아니게 된 이후로부터는 은신처로도 요긴하게 사용하고 있다."

    n "창문 밖을 바라 보았다. 네온으로 만든 전광판이 모두 꺼져 있다."
    n "그만큼 혼천군은 C시의 포화한 기술로부터 동떨어진 곳이라고도 할 수 있다."
    n "경제적으로는 칠룡성채가 더 낙후된 지역이지만, C시의 모든 곳이 그렇듯이, 틈새가 가장 빈약한 법이었다."

    nvl clear

    n "-사무실 내부의 불은 꺼져 있었다. 나는 안으로 들어가 불을 킨 다음 일상적으로 행동했다."
    n "커피 두 잔을 내리고, TV를 킨 다음 소파에 앉아서 흘러 들어오는 소리에 의식을 맡겼다."
    n "나는 이 평온을 좋아한다."
    n "밖에서는 1초마다 정보가 몇 백, 몇 천, 몇 만개씩 흐른다."
    n "그걸 고르는 것도 일이고, 일은 사람을 피곤하게 만든다."

    nvl clear

    n "반면에 이곳은 전혀 그런 게 없다."
    n "이곳에서만큼은 인터넷, 가상현실, 약, 술, 담배, 모든 것이 없다."
    n "있다면 카페인 정도."

    nvl clear

    n "그렇게 잠시 기다리고 있으면, 문이 열리고, 발소리가 들려온다."
    show Amun right at right
    with dissolve
    pause
    n "아문이다."
    nvl clear
    show Loui at left
    with dissolve
    am "뭐야, 일찍 출근했네?"
    l "딱히 일찍 오려고 한 건 아닌데.. 어쩌다보니 그렇게 됐네."
    show Amun right smile
    am "역시 이달의 가디언즈 우수 요원~!"
    show Loui close eye
    l "지난 달에는 너였잖아. 이걸 놀려?"

    nvl clear

    show Amun right

    n "아문은 둥근 형태의 빵모자를 대충 눌러 쓴채로, 우산을 벽에 탁탁 털며 빗방울을 털어냈다."
    n "몸동작 하나하나에서 호쾌함과 시원함이 깃들어 있다."
    n "나에게서는 나올 수 없는 에너지가, 그에게는 있다. -해맑음, 그리고 강직함이라고 해야할까."
    n "그리고 그 역시, 나처럼 인간이 아닌 상태다."
    n "그에게 남은 것은 금빛 눈동자 뿐이다."

    nvl clear

    show Loui at left
    l "옷으로 가려도 결국 얼굴에서 위화감이 느껴지는데..."
    l "굳이 평소처럼 차려입는 이유가 있어?"
    am "벗고 다니면 당연히 더 눈에 띄겠지~? 가디언즈치고는 허술하네, 루이."
    l "……여전히 희망차구나."
    l "거의 재능 수준인데, 그 정도면."
    show Amun smileL at right
    am "그야 괜히 우중충해져 있을 이유도 없으니까."
    am "루이가 너무 매사에 심각해져 있는 거야~! 좀 웃고 살아야지."
    n "그것도 맞는 말이다."
    n "하지만 난 이 상태가 된 이후로, 계속 화이와 연화의 아이들에 대한 생각만 하느라 머리가 아플 지경이었다."
    n "그런데도 그는, 나와 비슷한 상태가 되었는데도 해맑아보였다."
    n "난 그런 지점을 신기하게 생각했다."

    hide Amun smile
    with dissolve
    hide Loui
    with dissolve

    nvl clear

    n "그는 내가 내린 아메리카노를 홀짝 마시고, 책상 위에 아무렇게나 놓여 있던 리모콘을 눌렀다."
    n "어제, 그가 정리해두었다고 한 프레젠테이션이 벽에 투사되었다."
#책갈피
    show Amun right at right
    show Loui at left
    with dissolve

    am "자, 그러면 어제 종합한 정보를 다시 되짚어보자고."
    am "재정리는 수사의 중요한 단계니까 말이야."
    l "솔직히 말해서, 너무 많이 해서 귀찮은데..."
    am "안 돼~! 제대로 집중해, 루이!"

    #2회차때 여기 선택지 추가...

    am "연화의 아이들’은 약 30년 전에 처음 발생한 사이비 종교야."
    am "기독교를 기반으로, 성경에 나온 구절을 마음대로 난도질하여 경전을 만든 종교 단체지."
    am "그리고 자신들의 입맛에 맞춰 내용을 추가하기도 했고."
    am "당연히 단체 생활도 해. 그들 생활에는 나름대로 규칙과 루틴이 있는 모양이야."

    show Loui02 at left

    l "...그러고보니, 이런 종교라고 할 만한 단체는 이제 거의 없지."
    l "다들 캐씨(KaeC)만 숭배하니까..."

    show Amun right hand
    am "그 점이 중요해."
    am "처음에 '연화의 아이들'은 단순한 소규모 그룹이었어. 어떤 그룹이었는지는 파악이 잘 안 되지만."
    am "몇 백년 전의 어떤 소설처럼 코뮌에서 시작한 것도 아니야. 내부 분열 같은 것도 없이 꽤 잘 성장했었어."
    am "그러나 그들은 어느 순간 모습을 드러냈어. 수십 명의, 독실한 신자들과 함께."

    am "그들은 '연화'라고 하는 여성 교주를 내세웠어."
    am "아이돌, 이라고 해야 할까. 젊은 미모, 확신에 찬 설교. 카리스마."
    am "'도시의 사람들과 달리 우리는 더럽지 않다'는 게 중요 홍보 포인트였어."
    am "루이, 너도 느끼겠지만 C시는 너무... 혼잡하고 이상하잖아."
    am "연화는 그런 '깨끗함'을 내세운 다음, 신자들을 모으기 시작했지."
    am "그게 성공적인 전략이었다고 봐, 나는."

    n "C시에는 죽는 사람도 많고 타락하는 사람들도 많다."
    n "그래서 수행에 빠지는 종교인들도 있고, 사이비도 적지 않지만..."
    n "연화의 아이들 같은 경우는 처음이었다."
    n "나는 아문의 설명에 답했다."

    #책갈피
    hide Loui02
    show Loui at left
    l "초대 교주인 '연화'를 필두로 마케팅에 가까운 '전도'를 시작했고..."
    l "그게 2100년대, 즉 지금으로부터 약 10년 전의 이야기였던 걸로 기억해."
    l "내가 다니던 학교에도 신자가 있었어."
    l "그렇지만 그때 당시에 '연화의 아이들'은 지금 수준으로 큰 집단은 아니었지."

    am "네 말 대로야."
    am "연화의 아이들은 어느 순간부터 폭발적으로 세력을 넓히기 시작했어."
    am "단순히 정신적인 구원만을 논하던 연화의 아이들이, 사회에도 침입하기 시작했지."
    am "C시 기업의 중요 인물들이 연화의 아이들의 상징인 연꽃 뱃지를 다는 일도 있었어."


    show Loui close eye
    l "..그리고 중요한 거."
    l "'섬광 현상' 같은 걸 일으키기도 했지."
    nvl clear

    n "아문은 고개를 끄덕이고, 관련 자료를 책상 위에 모으기 시작했다."
    n "이건 가디언즈가, 별 볼 일 없는 종교인 연화의 아이들을 주목하기 시작한 이유다."
    n "여러 기업들이, 그들을 주목하고 있는 이유도 여기에 있다."
    n "그는 신문을 올려 놓았고, 그곳에는 '섬광 사건'이라는 단어가 공통적으로 보였다."

    nvl clear

    n "최근 아무 이유도 없이 갑작스레 '섬광'을 보는 사람들이 늘었다."
    n "길을 지나가다가 시야가 빼앗기는 현상을 겪는다."
    n "그리고 불가사의한 사건이 곁들여진다."
    n "갑작스레 쓰러지거나."
    n "함께 있던 사람을 폭행하거나."
    n "...입에도 담기 힘든 성범죄를 일으키거나."

    nvl clear

    n "전자기파 폭탄도 아니고 매트릭스에 문제가 생긴 것도 아니다."
    n "사이버네틱 삽입물이 얼마나 구리건 좋던, 그 빛은 모두에게 공평하게 나타났다."
    n "그리고 그 사람을 결정적으로 바꿔버린다."
    n "원인은 아직 규명되지 않았다. 다만..."

    nvl clear

    am "몇 년 전, 연화의 아이들은 새로운 교주를 내세웠어. 확실히 다른 사람이야."
    am "그들은 '환생' 등의 단어를 사용해가며 그 사람 역시 연화님, 이라고 설명하는 모양이지만..."
    am "우리의 눈을 속일 순 없지. 교주는 바뀌었어. 환생이라고 해도, 다른 사람이야."

    show Loui

    l "그리고 그 이후로 대외적인 출현을 비롯해서... 여러 활동을 보이기 시작했다는 건가."
    am "바로 그거야."
    am "'섬광 현상'에 대한 신고도 이들이 활동을 벌인 시기와 일치해."
    am "우리가 이 녀석들이 범인이라고 생각한 것도, 연화의 아이들 신도들을 검거하려다가 겪게 된 거니까..."
    am "무슨 구체, 같은 걸 던졌었지?"
    l "...그렇지."
    hide Loui
    show Loui04 at left

    l "그 녀석들을 거기서 아예 죽여버렸어야됐는데..."
    am "루이, 예쁜 말!"
    hide Loui04
    show Loui close eye at left

    am "아무튼 간에."
    show Loui
    am "'섬광 사건'으로 인해 우리처럼 '인간이 아니게 된' 사람들이 점점 늘고 있어."
    am "그래서 '가디언즈'가 우리에게, '특별수사관'이라는 호칭을 주고 일을 맡겼다..만."
    l "세간에 이 모습이 알려지면 골치 아프니, 당분간은 조용히 지내야하는 신세지."

    n "나는, 그렇게 말하고 자리에 일어서서 내 컴퓨터가 있는 자리로 갔다."
    n "아문은 자신의 프레젠테이션을 껐고, 나는 내가 작업한 걸 띄웠다."
    n "그곳에 있는 건 그녀- 화이였다."
    n "내 기억 속에 있는 모습 그대로 박제되어 있다."
    n "당연하다. 옛날 사진이었으니까."

    nvl clear

    l "새롭게 교주로 선정된 사람은 ’화이‘라는 사람이야. 지금 물론 대외적인 이름은 '연화'님이지만."
    n2 "내가 이렇게 운을 띄우자, 아문은 고개를 기울였다."

    am "그걸 어떻게 알았어?"
    l "...눈이 닮았다고 생각했어."
    n2 "스스로 말하고도 어이 없지만, 그것만으로 연화가 화이라는 사실을 알아냈다."
    n2 "설마, 설마, 하면서 정보를 추적해낸 결과 얻은 정보다."
    am "단지 그것만으로?"
    l "물론 수사를 했어. 화이는 몇 년 전에, 학교를 중퇴하고 종적을 감추었거든."
    l "그리고 조사해보니, 이사도 하고 가족 전체가 각자 다니던 회사와의 연을 끊었어."

    show Loui close eye
    l "친구들과의 연도 전부 끊었지...."

    nvl clear

    show Loui
    n "나는 그렇게 말하고서 등을 뒤로 기댔다."
    n "화이의 목소리가 떠올랐다."
    n "어린 시절에, 내 마음을 빼앗은 건 그녀의 나긋하고 명랑한 목소리다."
    n "웃는 모습이 예쁘다고 생각했다."
    n "그런데 지금, 그녀는..."

    nvl clear
    nd "화이는 내 친구였어. 물론, 그 때도 연화의 아이들 신자긴 했지."
    n "그리고서, 화이에 대한 정보를 읊기 시작했다."

    hide Loui
    show Loui02 at left
    with Dissolve(0.50)
    pause

    nd "그녀는 5년 전, 2107년까지만 해도 멀쩡히 학교도 다니고 사회적인 활동도 하고 있었어."
    nd "최대한 자신의 종교 활동을 숨기고 있었고, 조용히 지내려고 했지."
    nd "그리고 내가 대화해보았을 때에도... 그렇게 열성적인 신자는 아니었어."
    nd "그러던 어느 날, '나는 중대한 결정을 해야만 해'라면서 상담을 걸어왔지."
    nd "화이는 주어나 목적어를 많이 생략해가면서 말했어."

    nvl clear

    nd "'나, 지금 정말 중요한 결정을 해야 해. 너라면 가족을 따를래, 아니면 네 스스로의 말을 믿을래?'"
    nd "그런 식이었지."
    nd "그때 나는 '네 주변 사람을 믿으라'고 말했지만 그녀 주변에는 연화의 아이들 신자 뿐이었겠지."
    nd "그래서 화이는 연화님이 되었다... ...그렇게 생각하는 거야, 루이?"
    n "아문이 그렇게 말하자 나는 눈을 감고 고개를 끄덕였다."

    nvl clear


    n "아문은 화이와 관련된 자료를 유심히 살펴보더니, 맹점이 하나 있다며 나에게 딴죽을 걸었다."
    nd "말도 안 되는 우연이긴 하네."
    nd "예전의 친구가 사이비 종교의 신도였다가 교주가 되었다..."
    nd "그것도 거의 살아 있는 신님 취급. 이상하네."
    nd "분명히 무언가 꿍꿍이가 있어."
    n "나는 이상하다는 아문의 말에 그렇게 덧붙였다."
    n "이건, 분명히 무슨 음모가 숨겨져 있다."

    nvl clear

    n "아문은 새로운 자료들을 펼치기 시작했다."
    n "그리고 나는 미간을 찌푸렸다."
    n "가디언즈가 연화의 아이들을 주시하고 있는 이유."
    n "C시에 돌고 있는 흉흉한 소문들, 그리고 연화의 아이들에 관련된 꿍꿍한 이야기들..."
    n "모두 한 가지를 가리키고 있다."
    #여기서는 adv모드로 할까

    nvl clear

    hide Loui02
    show Loui at left

    am "요컨대, C시에서 벌어지고 있는 '섬광 현상'은 연화의 아이들과 관련되어 있다고 보는 게 타당해."
    am "일단 우리가 경험했기도 하고?"
    l "...그렇지."
    l "길을 걷다가, 지하철이나 택시를 기다리다가, 혹은 집에 있다가. 우리처럼 일을 하다가."
    l "그 빛은 갑자기 찾아왔어. 대처할 틈도 없이."
    am "맞아."
    am "섬광 현상은 아직까지도, 잊을 만 하면 종종 발견되고 있고, 그 때마다 연화의 아이들은 포섭을 계속하고 있어."
    am "우리들이 구할 수 있다고, 구해주겠다고 나서고 있지."
    am "그리고 섬광 현상을 겪고 입교한 사람들 중에서, 실제로 '각성'을 한 경우도 있어."
    am "그게 한 몇 주 전이더라고."

    n "아문이 띄운 자료에, 한 인터넷 게시판의 글이 있었다."
    n "거친 어조다. 그렇지만 다들 고양되어 있었다."
    n "섬광 현상을 겪은 뒤에, 누군가의 목소리가 들리는 등 이상 현상을 겪었다."
    n "그래서 약도 먹고, 운동도 해보고 했지만 그 목소리는 계속해서 들려왔다."
    n "그런 와중에 연화의 아이들, 이라는 사람들을 만났다."
    n "그리고 그 글은 연화의 아이들을 홍보하는 게시자의 격앙된 메시지로 끝이 난다."
    n "당연히 모두는 두려워하듯이 놀라워했다. 광신이라는 게 늘 그렇듯이."

    nvl clear

    am "우리의 경우는 어땠더라?"
    am "...다시 떠올리기 싫은 기억이지만."
    am "지하철역에서 수상쩍은 행동을 하던... 그러니까, 아마 섬광 현상을 일으키려던 녀석들이 있었지."
    am "그리고 그들을 쫓다가? 그 정체불명의 구체를 맞고 이렇게 됐지."
    l "....엄청 힘들었어. 그 녀석들, 달리기는 왜 이렇게 빠른지..."
    l "그래서 붙잡았다. 그런데 그 녀석들이 연막이라도 치듯이, 그 기계를 작동시켰고..."
    l "빛을 보았지."
    am "그리고... 짜잔! 둘 다 이런 모습이네."
    l "...그러게."
    l "...내가 화이에 대해 어떻게 대하던, 결국 지금 연화의 아이들을 조사해서 진상을 까발리고 싶다는 생각은 변하지 않아."
    am "뭐, 그렇겠지."
    am "연화의 아이들’은 수상쩍은 구석이 너무 많으니까. 네 성격으로는 가만 두지 못할 거야."
    am "게다가 이 능력이 마음에 걸려."

    n "아문은 그렇게 말하고 난 다음, 눈을 감고 집중했다."
    n "그리고 어렵지 않게, 자신의 손끝에서 하늘색 구체를 생성했다."
    n "이것이 아문의 ‘힘’이다. 섬광 현상 이후로, 모습이 변하고, 쓸 수 있게 된 능력."
    n "그가 가볍게 손가락을 튕기자, 구체는 곧 빠른 속도로 벽을 향해 발사되었다."
    n "그곳에 부딪힌 구체는 벽에 박히듯 명중했으며, 똑같이 둥근 모양으로 파인 자국을 생성했다."
    n "아주 약한 구체임에도 총알 수준의 파괴력을 지니고 있었다."
    n "물체가 필요한 것도 아니고, 무기가 필요한 것도 아니다."
    n "그냥 허공에서 ‘생성’한 것이었다."

    nvl clear

    am "너무 위험해. 어떻게 발동되는 지도 솔직히 파악이 안 돼."
    am "나도 그냥 감으로 쏘고 있는 거란 말이야."
    am "만들어서, 쏜다. 이 생각만으로 탄환을 만들어 낼 수 있어."
    am "그리고 그 위력은 상상을 초월해."

    n "나는 그의 말에 동의했다."
    n "내가 매번, 에우레카를 꺼낼 때마다 마주하는 풍경."
    n "그것은 상당한 정신력을 요한다."
    n "그렇지만 그만큼 에우레카의 위력은 막강하다."
    n "무장한 요원 몇 명을 가볍게 제압할 수 있다."

    nvl clear

    nd "너도 경험했잖아, 루이. 이 힘으로 불러내는 무기, 마법, 기적...."
    nd "이름이 뭐가 됐던, 너무 강력한 힘을 지니고 있어."
    n "나는 그것에 동의했다. 그리고 덤덤하게 말했다."
    nd "연화의 아이들은 아마, 이 ‘힘’을 미끼로 신자를 모으고 있는 거겠지."
    nd "루이, 이건 심각한 문제야."
    nd "난 말이야. 그 양성된 신자들이 이런 능력을 모두 갖게 된다면, 이 도시가 어떻게 될지 잘 상상이 안 가."
    nd "그게 난 두려워."

    nvl clear

    n "우리는 아무 말도 하지 않았다."
    n "아문은 심각성을 이미 깨닫고 있었고, 나도 그제야 알 것 같았다."
    n "섬광 현상 - 그것이 우리를 인간이 아닌 것으로 만들었다. 가까스로 살아남긴 했다."
    n "문제는, 이것이 불특정 다수에게 퍼진다면──────"

    nvl clear

    n "무언가 끔찍한 일이 일어나리라는 예감이 있었다. 그리고 아문 역시 그걸 알아차리고 있었다."
    n "나 역시 켕기는 점이 하나 있었다."
    n "내가 에우레카를 불러낼 때마다 보이는 그 풍경."
    n "악마처럼 속삭이는 그 존재──────────제로."
    n "그것이 아문에게도 보일지도 궁금했다."
    n "그렇지만──그것은 짐작컨대, 내 마음 그 자체다."
    n "나는 그것을 알고 있었다. 그는 어떤 의미에서는 나이기도 하다는 것을."
    n "에우레카는 그가 주는 보상이자, 그의 힘이라는 걸."
    n "그렇다면 아문도 알고 있을까."

    nvl clear

    l "아문."
    am "응? 왜?"

menu:
    "아무것도 아니야.":
        jump nothing1
    "난 능력을 쓸 때마다 어떤 사람이 보여.":
        jump someguy

        label nothing1:

        l "아무것도 아니야."
        am "뭐야, 불러놓고."
        am "뭔가 비밀을 숨기고 있는 거야?"
        am "너무 숨기고 있지만 말고 나한테도 좀 알려주지."
        am "넌 항상 모든 걸 자기 혼자서 감당하려고 하니까 말이야."

        label someguy:
        l "난 능력을 쓸 때마다 어떤 사람이 보여."
        am "사람? 어떻게 생겼는데?"
        l "그러니까.."
        show event02
        with flash
        pause 1
        hide event02
        with flash

        l "눈 코가 없고 입만 보여."
        l "그리고 계속 나한테 무언가를 부추기는 것처럼... 속삭이곤 해."
        l "대화할 때마다 기분도 별로 좋지도 않고..."
        am "흠."
        am "‘에스페로’는 ‘연화의 아이들’사이에서 ‘마음의 힘’이라고 불린다고 해."
        am "그러니까 그런 거 아닐까."
        am "네 마음 속의.. 어두운 면?"
        am "뭔가 중2병 만화 같지만, 지금으로선 그것밖에 생각이 안나네. 하하."

        jump scene3

label scene3:

    am "어쨌던, 우리의 수사 방향은 그런게 되겠네."
    am "첫째. 연화의 아이들의 동향."
    am "둘째. 화이가 지금 연화님이 맞는지, 그리고 어떻게 해서 납치되었는지."
    am "셋째. '에스페로'에 대한 조사."
    l "좋아."
    l "그럼 나는..."
    l "...화이를 직접 조사하러 가겠어."
    l "그녀가 아무리 충실한 신자라고 하더라도, 갑작스레 교주가 된 건 이상해."
    l "분명... 무슨 사정이 있을 거야. 그렇게 믿고 싶어."
    am "...그렇구나."
    am "그렇게나 루이에게 소중한 사람이라면, 뭐, 난 말릴 수가 없겠네."
    am "하지만 아무리 생각해도 너무 위험해. 괜찮겠어?"
    n "나는 생각했다."
    n "이럴 때, 평소라면 아문과 함께 했을 것이라고. 그렇지만 지금은 다르다."
    n "계속해서, 나 혼자 가지 않으면 안 된다는 생각에 사로잡혀 있었다."
    n "옛날 이야기에 나오는 광인처럼 자꾸 무언가에 집착하고 있었다."
    n "그녀의 미소를 떠올릴 때마다──────"

    nvl clear

    n "그녀에게 답을 듣고 싶었다."
    n "직접, 화이의 목소리로 말을 해주길 원했다."
    n "어째서 나를 떠나가야 했냐고, 왜 그런 곳에 몸을 담아야만 했냐고──"
    nd "혼자 갈 거야. 그리고, 괜찮아."
    nd "지금은 좀 이상한 힘도 있으니까."
    n "내가 그렇게 말하니, 아문은 픽 웃었다."

    nvl clear

    nd "도울 게 있으면 언제든지 말해. 나랑, 가디언즈는 언제나 네 편이니까."
    nd "그러니까─── 우리는, 예전에도 함께였었잖아."
    nd "그때 했던 것처럼, 다시 힘을 모을 수 있을 거야!"
    n "그는 항상 그 때를 언급한다."
    n "나는 좀처럼 떠올리고 싶지 않은 기억이지만────그건 우리 둘을 잇는 인연, 같은 것이었으니까."

    nvl clear

    nd "알았어, 알았어. 거 참. 걱정도 많으셔."
    n "나는 그렇게 말하고 아문의 어깨를 두드렸다."
    n "그는 항상 과잉으로 걱정하는 경향이 있으니까."
    n "아문은 항상 날 보고 마음의 짐이 많다고 말하지만, 나는 그 반대라고 생각한다."
    n "남을 생각하는 저 이타심이 어디서 나오는지 궁금할 정도로──────그는 상냥하다."

    nd "조심해서 수사할 게. 에우레카도 꼭, 위험할 때만 꺼내기로."
    n "아문은 그 말을 듣고 나서야, 안심한 듯 미소를 지어 보였다."

    am "그럼 조심해. 무슨 일 있으면 연락하고."
    l "알았어."

    nvl clear

    n "나는 사무실을 나서, 정보를 모으러 가기로 했다."
    nvl clear

    scene bg market
    with dissolve

    play music "audio/techno.mp3" loop
    n "아문과 헤어지고, 사무실에서 나와 계속해서 걸었다. 그러자 칠룡성채가 나왔다."
    n "밀집된 도시의 근처에 사람들이 많은 시장이 있다. 모두 전자되어, 홀로그램 화면이 많다."
    n "그래서 너무 시끄럽고 혼잡한 느낌이다. 옛날의 시장은 이러지 않았겠지."
    n "주목받기 싫고, 눈에 띄는 것이 싫어 이번에도 후드를 눌러 썼다."
    n "어차피 경찰이 없는 도시다. '가디언즈'는 나의 아군이고, 피해야 할 사람이 있다면 언론이나 기업들의 하수인들뿐."
    n "그러니 거리를 걷는 것 정도는 괜찮다. 너무 눈에 띄게 행동하지만 않으면 걸릴 일도 없다."
    n "'연화의 아이들' 신도들은 조금 조심해야겠지만."

    nvl clear

    n "{i}꼬르륵...{/i}"
    n "....제길. 그리고 배가 고팠다."
    n "생각해보니 일어난지 몇 시간이나 됐는데 아무것도 먹고 있지 않았다. 게다가 전투를 한 뒤였다."
    n "몸이 가벼워지고, 맨 몸에서 무기를 불러낼 수 있는 몸이지만 소화 기관은 정상적으로 작동하는 모양이었다."
    n "주위를 적당하게 둘러보니 무인 국수 가게가 보였다."
    n "최대한 사람과의 접촉을 피해야했기 때문에 그곳에서 식사하기로 했다."

    #묘사추가

    nvl clear

    n "잠시 뒤 연락이 왔다."
    n "나는 새끼손가락을 까딱, 움직여서 사이버웨어를 작동시켜 눈 앞에 스크린을 띄웠다."
    n "몸이 변했다고 해도 이식물은 그대로다. 똑같이 배가 고픈 것처럼, 사이버웨어를 통해 네트에 접속하는 건 변하지 않는다."
    n "자신이 편한 몸동작과, 네트워크에서의 행동을 일치시켜둔다. 내 경우에는 새끼 손가락을 움직이는 게 온라인/오프라인 전환, 혀로 이식한 인조-어금니를 만지는 것이 연락 받기, 등등."
    n "그리고 내가 말한 행동을 전부 행했다. 화면을 열고 연락을 받았다."

    l "...여보세요."
    mob1 "선배! 뒤를 보세요!"

    nvl clear

    n "밝고 들뜬 목소리. 언제든지 지치지 않을 것 같은, 비타민 같은 톤이다. "
    n "뒤를 돌아보니 아카리가 그곳에 서 있었다."
    n "평소처럼 펑키한 패션이다. 그리고, 당연하지만 인간이다."
    n "최근에는 아문과, 조사에 나오는 연화의 아이들 사람들만 마주치다보니 오래간만에 보는 인간이라고 생각했다."
    n "그리고.. 그녀를 보니, 역시 내 자신이 이상하다는 생각이 먼저 들었다."
    n "그래, 인간은 원래 이렇게 생겼었지."

    nvl clear

    n "아카리는 갈색 단발 머리에, 키는 165cm 정도 된다. 수사관으로서 불리한 신체 조건이다. 게다가 체구도 작았다."
    n "그런데도 그녀는 현재, 가디언즈에서 가장 유능한 사람으로 손꼽힌다."
    n "그것이 아카리의 재능과 노력을 설명해준다."
    n "머리칼이 조금 젖어 있었다. 아까까지 계속 밖에 있었던 모양이다."

    nvl clear

    nd "...아카리...! 오랜만이야. 아니, 그것보다, 여긴 어떻게..."
    nd "루이 선배도 참~! 위치 기능을 켜놓고 어떻게 알았냐고 하면 어떡해요~!"
    nd "선배님이 저한테 가디언즈 앱 기본 기능도 모르냐고 쓴 소리 했던게 전 선명한데!"

    nvl clear

    n "아카리는 사람 좋게 웃어보이며 내 옆에 앉았다. 그 와중에 내가 시킨 간장 라멘이 나왔다."
    n "그녀는 잔치국수를 특 사이즈로 시킨 모양이었다. 여기 오기 전에부터 원격으로 주문한 건지, 바로 메뉴가 나왔다."
    n "몇 번을 봐도 어마어마한 대식가다."
    nd "이런 모습... 보여주고 싶진 않았는데. 부끄럽네."
    nd "에이, 괜찮아요. 아문 선배한 얘기 들어서 이미 알고 있었어요."
    n "그렇게 말하고서 내 모습을 살폈다. 신경을 쓰지 않으니 후드가 올라가 있었다."
    n "나는 그녀에게 이 꼴을 보이고 싶지 않았다. 평범한 사람에게 이런... 대충 생긴 모습으로 변해버린 걸 보이고 싶은 사람은 아무도 없을 거다."

    nvl clear

    nd "헤에~ 인간이 아니어도 제법 더러운 눈이에요."
    nd "그리고 진짜, 많은 게 생략되네요! 완전 가래떡처럼 생겼어."
    nd "볼 늘려도 되나요?"
    n "...그리고 여전히 묘하게 선을 넘는 말투."
    nd "선배한테 못 하는 말이 없어, 이게."

    nvl clear

    n "그녀는 내 핀잔에도 굴하지 않았다. 아카리의 장점이었다. 누가 뭐라고 해도 그녀는 그녀 페이스대로 산다."
    n "어쨌던 가디언즈도 회사임과 동시에 경력에 따라 선배 후배를 따지는 집단이다."
    n "그런 가디언즈에 '핵폭탄'이 들어왔다는 소문이 돌았고 주역은 아카리였다."
    n "지금은 그 모두가 핵폭탄에 져버렸다. 모두가 이 자기 멋대로인 페이스에 적응해버렸다."

    nvl clear

    nd "그래서, 왜 왔어?"
    n "내가 그렇게 말하자, 아카리는 서로 연결한 통신을 끊었다."
    n "순간 거리의 소음이 흘러 들어왔다."
    n "아카리는 내게 가까이 다가가 속삭였다."
    nd "아문 오빠가 전해주라고 한 정보가 있어서 왔어요."
    nd "그리고 한{size=-5}Han{/size} 선배가 물건도 전해달라고 해서요."
    nvl clear

    n "나는 고개를 끄덕였다."
    n "굳이 직접 찾아 온 이유는, 무선 메시지는 해킹이나 감시의 위험이 있어서라고 생각한다."
    n "이렇게 시끄러운 곳에서는 정보가 단발적으로, 수없이 쏟아지기 때문에 오히려 숨기기 쉽다."
    n "게다가 이렇게 오프라인으로 말하는 거라면 더욱 그렇다."
    n "아카리가 내게 넘겨준 것은 작은 칩이었다."

    nvl clear

    nd "목 뒤에다가 넣으시면 돼요, 선배."
    nd "한 선배가 만든 거래요. 선배의 상태를 확인해주는 확장 프로그램이랬는데..."
    n "나는 그가, 한이 무엇을 만들었는지 감이 잡히지 않았다. 그 자리에서 바로 삽입해버렸다."
    n "순간- 시야가 흔들렸다."
    n "그리고 새로운 창이 떠올랐다."

    nvl clear

    nvlphone "Espero ── 평화 상태."
    nd "...정말 만들었잖아. 한이 실력은 알아줘야 한다니까."
    nd "이게 대체 뭐예요, 선배? 저는 전달해준 것이기만 해서요!"
    n "한이 내 상태를 보고 나서 만들어준 프로그램이다."
    n "그는 나와 아문의 증언을 듣고서, 잠시 흥미가 생긴다며 우리의 신체 데이터를 빼갔다."
    n "그러니까, 수술대에 누워서 그에게 점검을 받았다는 뜻이다."
    n "그는 그곳에서 유전자 정보를 추출하여 자신의 원래 기술과 결합시켜 어떤 것을 만들어냈다."

    nvl clear
    nd "에스페로 관측 프로그램이야."
    n "나는 그녀에게, 일전에 한이 설명해준 대로 말하기 시작했다."
    nd "이걸로 내 몸에 깃들어 있는 에스페로가 어떤 상태인지 알 수 있어."
    nd "...정말 그런지 나는 잘 모르겠지만. 한의 말대로는 그래."
    nd "뭐, 앞으로 시험해봐야겠지..."

    nvl clear

    nd "그리고 이건... 화이라고 하는 사람의 위치에요."
    n "나는 그 말을 듣고 그녀를 바라 보았다."
    nd "아문 선배랑 제가 협력해서 알아낸 거예요! 나중에 밥이라도 쏴주세요?"
    n "아카리는 국수를 맛깔나게 먹다가, 자신의 목 뒤에 잭을 연결해 나에게 건넸다."
    n "나는 내 목 뒤를 더듬었다. 매끈한 피부 -피부라고도 할 수 없겠지만- 를 만지던 손이, 이윽고 딱딱한 연결부를 찾아냈다."
    n "인간이었던 시절에 개조해둔 신체는, 네트워크에 직접 접속할 수 있었다. '가디언즈'에 들어온 이후로는, 정보를 직접 읽는 데에만 사용하지만."
    n "예전에는 해킹을 하며 네트워크의 바다를 떠돌던 때도 있었지..."
    n "그런 감상에 젖으며 잭을 연결했다."

    nvl clear

    n "{font=DungGeunMo.ttf}-신원자 '아카리' 확인. 정보를 확인하시겠습니까?{/font}"
    n "나는 그렇게 했다."
    n "닫아둔 스크린이 다시 새롭게 떠올랐다."
    n "새로운 스크린은 C시의 지도를 펼쳤고, '여기에요!' 라고 빨간색 펜으로 요란하게 표시해둔, 아카리가 쓴 게 분명한 낙서가 보였다."
    n "화이는 도심부 중심에 있고, 칠룡성채와는 거리가 멀다."

    nvl clear

    nd "화이는 연화의 아이들이 본부로 삼고 있는, 거대한 예배당 내부에 있는 것 같아요."
    nd "보안 단계가 알파 3이라서, 외부에서는 사이버적으로 접근이 거의 불가능해요."
    nd "그러니까 선배가 직접 가셔서, 물리적으로 접촉해야하지 않을까 싶어요."
    n "괜찮은 정보다. 이걸 어디서 입수했는지 궁금해질 정도로."
    nd "고마워, 아카리. 덕분에 살았다."
    nd "헤헤~ 나중에 꼭 밥 사주시기에요?"
    nd "밥에 집착하는 거냐고."
    nd "먹는 것보다 중요한 일은 없으니까요!"

    nvl clear

    nd "-그런데, 선배. 그 사람이 옛날 친구라면서요?"
    nd "다 알아요. 아문 선배가 말하더라고요."
    nd "엄청 걱정하시던데요? 아문 선배가."
    nd "친구가 그런 상태가 되었으니까 분명 심란할 거라면서... 저보고 얘기 잘 해달래요."
    nd "그런데 정말, 그렇게 소중한 사이였었나요? 화이라는 사람은."
    n "그녀는 그렇게 말하면서 국수를 입에 우물댔다."
    n "다 먹고 말이나 하지 좀. 그렇지만 나는 그걸 굳이 말하지 않고, 조용히 먹으면서 들었다."
    n "입에 있는 걸 다 삼킨 아카리는 이어서 말했다."

    nvl clear

    nd "아문 선배가 루이 선배가 그렇게 된 이후로 가디언즈 본부에서도 조사를 하고 있어요."
    nd "선배님들이 현장직이시니까 저희는 사이버 상으로 조사했죠."
    nd "저랑 제 동기... 케인{size=-10}Kane{/size}이라고 아세요? 해커인 친구요."
    nd "걔가 물어준 정보에 따르면, 신자들은 화이를 좋아하나봐요."
    nd "옛날에 연화님은 범접할 수 없는 대상이었는데 지금은 친근하다고요."

    nvl clear

    nd "역시 기존의 다른 사람이겠죠?"
    n "아카리는 젓가락을 들고, 공중에 콕콕 집어가며 추리하는 탐정처럼 말했다."
    n "하지만 이건 그렇게 복잡한 사고를 요하는 일이 아니다. -나는 그녀에게 답하기 시작했다."
    nd "'연화'를 둘러싼 이런저런 가십 중에는 '환생'이 있어."
    nd "어느 순간부터 연화의 아이들의 경전에 '환생'과 관련된 이야기가 추가됐지."
    nd "기독교를 기반으로 하는 사이비치고는 꽤 뜬금 없는 요소야."

    nvl clear

    nd "조용히 지내던 종교 단체인 '연화'가 새로운 사람을 내놨어."
    nd "이런 종류의 종교는, 교주의 존재감이 상당히 크지."
    nd "그렇다는 건 그 단체 내부에서도 무언가 바람이 불었다는 걸 의미해."
    n "아카리는 신기하다는 듯한 나의 결론을 잠자코 듣고 있었다."
    nd "바람, 인가요?"

    nvl clear

    n "나는 의자 뒤로 자세를 기울였다. 그녀의 모습이 떠오르기 시작했다."
    nd "그렇지 않았다면 화이가 떠날 이유가 없었겠지..."
    n "아카리는 날 빤히 쳐다보니, 이윽고 한 마디를 던졌다."
    nd "화이 씨가 그렇게 중요한가요? 루이 선배에게 있어서."

    nvl clear
    play music "audio/morning.mp3" loop

    n "물론, 나는 이렇게 답한다."
    nd "소중해."
    nd "...그런 것도 있지만, 나는 확인하고 싶어."
    nd "대체 왜 그녀가 그곳에 머물러야만 했던 건지."
    nd "적어도 이유라도 듣고 싶은 심정이야."

    nvl clear

    cen "나는 그렇게 말하고 잠시 눈을 감았다."

    scene bg black
    with dissolve

    n "화이는, 인간이었다. 그것은 확실하다."
    n "기억 속의 화이는, '연화'의 신자였으며 종교 측면에서는 조금 불성실한 구석이 있었다."
    nd "루이- 나 예배 드리러 가기 싫어... 땡땡이 칠까?"
    n "교회를 가기 싫다고 투정부리는 일도 잦았고, 실제로 친구들과 논다면서 빠진 적도 있었다."
    n "그렇지만 매번 후회한다고 했다."
    n "그리고- 그녀는 사라졌다. '나에게는 종교의 의무가 있다'면서."

    nvl clear

    n "아카리의 말에 자연스레 나는 과거를 떠올리기 시작했다."
    n "아니, 떠올랐다기보다는.. 재생되었다."
    n "마들렌을 홍차에 적셔 먹자 눈 앞에 대서사시가 떠올랐다던 소설처럼."
    n "그녀의 목소리가────────들리기 시작했다."
    n "기계가 뇌의 기억을 불러오는 것처럼, 현실이 편집된다."
    nd "{color=#FF3399}루이!{/color}"

    nvl clear

    n "이것은──────────머나먼 기억 속에 있는 꿈이다."
    n "그러나──────────너무나도 오래되어, 이제는 잘 기억나지 않는다."
    n "그래도──────────변하지 않는다."

    nvl clear

    n "4월이었다."
    n "기계가 가득한 이 세계에서는 꽃을 찾아볼 수 없다. 오직 보존된 기록에서만 볼 수 있다."
    n "그래도 눈부신 한낮의 봄이었다."
    n "한산하고, 여유롭다. C시에서는 찾아보기 힘든 여유다."
    n "{b}이 학교{/b}의 장점이라고도 할 수 있겠지."

    nvl clear

    n "나는 그녀가 부른 그곳으로 향하고 있었다."
    n "근처에 있는 청소 로봇이 휘청이는 걸 세워주기도 하고."
    n "하늘을 바라보며, 오늘은 정말 맑구나, 산책을 가고 싶은 걸,"
    n "그런 생각을 하기도 했다."
    n "이건 전부 기술로 만든 가짜지만, 진짜라고 여겨도 될 정도로,"
    n "행복했다."

    nvl clear

    scene bg garden
    with dissolve

    n "시선이 닿는 곳은, 멋드러진 정원이었다."
    n "기계가 만든 가짜 하늘 아래에서, 꽃과 함께,"
    n "그녀가 웃고 있다."
    n "교복 블라우스가 잘 어울리는 모습이었다. 모두가 불평하는, 지나치게 긴 스커트도 완벽하게 어우러진다."
    n "나는 언제나 그녀를 추억할 때마다, ‘꽃'이라는 단어로 기억한다."
    n "그녀의 이름은 화이."
    n "꽃 두 송이. 혹은, 두 개의 찬란한 빛."
    n "그렇게 기억하면 잊어버릴 일이 거의 없다."

    nvl clear

    nd "왔어?"
    n "그녀는 천진난만한 미소를 지었다. 그쪽을 보며, 어색하게 웃는다."
    nd "왔어. 애초에 네가 부른 거잖아."
    n "잠시 가벼운 대화가 오간다. 나는 그녀의 옆자리에 앉는다."
    nd "점심 먹었어?"
    nd "그냥 걸렀어. 맛 없길래."
    nd "맨날 편의점 밥만 먹으면 건강 안 좋아질텐데."
    nd "어차피 도심 지역으로 가면 건강은 빨리 나빠져."

    nvl clear

    n "C시 외곽에 위치하고 있는 이 학원은, 독립적이다. 어른이 되면 도심으로 향해 일을 한다."
    n "그렇기에 원래라면 만나지 못할 사람들이 만나기도 한다."
    n "돈 있는 아이들과 돈 없는 아이들이 만나는, 유일한 교차점."
    n "순응하는 착한 아이와 반항하는 나쁜 아이가 갈등하는 혼란의 장소."
    n "그곳이 이 학원이었다."

    nvl clear
    n "화이와 나의 관계 역시 그렇다."
    n "그녀는 원래, 닫힌 사회에서 살아갈 운명이었다."
    n "말할 것도 없이, 연화의 아이들 얘기다."
    n "그렇기 때문에 난 그녀가 어느 순간 사라질까봐, 전전긍긍하며 생활을 보냈다."
    n "그리고 오늘은────────────"

    nvl clear

    nd "이제 학원 그만두래."
    nd "누가?"
    nd "엄마가. 가족들이 전부 그렇게 말하는 걸."
    nd "그러니까────이제 작별이야, 루이."
    nd "너에게는 꼭... 마지막 인사를 해야 할 것 같았어."

    nvl clear
    n "나는 그 말을 청천벽력처럼 받아 들인다."
    n "사실은 알고 있었다."
    n "그녀와의 만남은 오래 가지 못할 것이라는 걸."
    n "미리 들었기 때문에 각오했다고 생각했다."
    n "그러나 이별은 생각보다 빨리 찾아왔다."
    n "무심코 나는 그런 말을 뱉어 버린다."

    nvl clear
    nd "안 가면 안 되는 거야?"
    n "-아마, 인생에서 가장 처음으로 억지를 부린 때."
    n "그렇기에 진심이었다."
    n "그렇기에 거짓말이 아니었다."
    n "그렇기에, 그녀가 가지 않았으면 했다."

    nvl clear

    n "하지만 화이는 이미 마음을 정한 것 같았다."
    n "저 먼 허공을 바라보았다."
    n "나는 오직 화이만을 바라보았다."
    n "잠시 이어지는 침묵."
    n "그러다 그녀는조곤조곤 말을 꺼낸다."

    nvl clear

    nd "루이는 이해하지 못할 거야."
    nd "이 세상에는 절대로 어길 수 없는 규칙이 있어."
    nd "돈, 이해관계 같은 걸로 설명할 순 없어."
    nd "그건 절대적인 거야. 그러니까 따를 수밖에 없어."
    nd "그게 좋던 싫던..."

    nvl clear

    n "그러니까 그게 뭐 어쨌단 말인가."
    n "나는 그녀에게 이런 저런 말로, 억지를 부려가며 항변을 하고 싶었다."
    n "그렇게 싫으면 도망치라고."
    n "맞서 싸우는 것도 정도가 있다고, 말하려고 했다."
    n "사람은 태어날 때부터 자유로우니까."

    nvl clear

    nd "연화님을 모시기 위해서 일하는 거라면, 난 불행하지 않아."
    nd "그리고... 우린 언젠가 만날 수 있을 거야."
    nd "이 하늘 아래에서 살아가는 한──────────"

    nvl clear

    n "나는 이해하지 못했다."
    n "그녀의 행복은 곧 나의 행복일텐데."
    n "멀어지는 것이 너무나도 슬퍼, 미소 짓고 있는 그녀 앞에서 좋은 표정을 보일 수 없었다."
    n "예배에 가기 싫다고, 목사님이 너무 싫다고 말했던 그녀가."
    n "연화님이 우릴 사랑한다면 이렇게 답답하게 속박하지 않았으면 했다고 한 그녀가."
    n "어째서 그곳으로 간다고 말하며, 이렇게 찬란히 웃고 있는지."
    n "나는 이해하지 못했다. 이해할 수, 없었다. "
    n "내 작은 머리로는 도저히 받아들일 수 없었다."

    nvl clear

    nd "루이가 어디에서든 행복하면 좋겠어. 내 나름대로 계속, 응원하고 있을 거야!"
    n "─────────그러나 나는 화이를 도저히 막을 생각은 들지 않았다."
    n "그녀가 슬픈 표정을 지을까봐 두려웠다."
    n "그렇기에 아무 말도 하지 않았다."
    n "그냥 죄를 지은 사람처럼 그곳에, 입을 꾹 다문채로 서 있었다."
    n "좋아해. 그러니까 가지 마."
    n "그런 이야기는 꺼내지 않았다."
    n "손을 모으고, 나에게 무릎 꿇으며, 기도하는 그녀를 바라보기만 했다."
    n "내용은 잘 기억나지 않지만, 마지막 말만은 기억하고 있었다."

    nvl clear

    nd "나 있잖아. 여기서 겪은 모든 걸 다 잊어버려도, 루이만큼은 잊지 않을 게."
    n "나는──────────── 잘 모르겠다."
    n "화이가 모시는 ‘연화님’이 누구인지."
    n "왜 그렇게 그녀가 자유를 빼앗겨가며, 일상의 모든 것에 침범해야하는지."

    nvl clear

    n "그렇지만 그때 기억하는 것은,"
    n "내가 맞잡은 화이의 손이 아주 예뻤다는 것."
    n "나를 위해 그런 말을 해주는 그 마음이, 감당할 수 없을 정도로 벅찼다는 것."

    nvl clear

    n "이별은 결국 재회를 약속하는 행동이라고, 스스로 생각했다."
    n "이 세상에 단 하나 남은 아름다움일 것 같은 화이를."
    n "나는 언젠가 다시 볼 수 있으리라 생각했다."
    n "그렇지만─────그녀에게 편지가 오는 일은 없었다."
    n "내가 화이를 찾아가지도 않았다."
    n "화이가 다닌다는 그 교회들을 수소문하지도 않았다."

    nvl clear

    n "멀리서, 그저 멀리서."
    n "화이가 행복하기를 바랬을 뿐이었다."
    n "나는 다만 그녀가 기도를 올리거나, 멀쩡하게 예배를 드리는 모습을 이따금씩 생각했다."
    n "그렇지만, 화이는────────────"

    nvl clear

    scene bg market
    with flash
    play music "audio/techno.mp3"

    nd "선배?"
    n "나는 갑작스레 정신을 차렸다."
    n "아카리는 잔치국수(특)에 추가로 수육까지 깔끔하게 해치운 상태였다."
    n "...얘는 나한테 정보를 전해주러 온 거야 먹으러 온 거야?"
    n "그건 그렇고, 너무 과거에 사로잡혀 있었다. 상당히 오랫동안 멍때린 모양이었다."

    nvl clear

    nd "아까부터 제 말 계속 무시하고 라멘만 드시고.. 그렇게 배고프셨어요?"
    nd "...너도 계속 먹었잖아."
    nd "그거야 먹는것보다 중요한 건 없으니까!"
    nd "두 번 말하지 마."

    nvl clear

    n "하여간, 내가 '먹고 있다'는 행위를 하는 것조차 실감나지 않았다."
    n "사이버네틱 삽입물을 몸에 이식한 것과, 인간이 아니게 된 것. 그런 것들이 내 인지 능력에 영향을 끼치고 있는 모양이었다."
    n "그러니까 호접지몽 같다는 이야기다."
    n "내가 나비의 꿈을 꾸고 있는지 나비가 내 꿈을 꾸고 있는지, 명백하게는 알 수 없는 상태였다."
    n "나는 손을 몇 번 쥐었다 폈다."
    n "지금 이곳이 현실이다."
    n "그러니 지금은 움직여야 한다."

    nvl clear

    nd "정보 고마워. 나중에 밥 살 게."
    nd "그렇잖아도 이미 이 국수들, 선배 카드로 계산했어요!"
    n "어느 틈에...?"
    n "나는 문득 공용사무실 세 번째 서랍에, 내 명의의 카드를 하나 두고 왔다는 사실을 떠올렸다."
    nd "그럼 전 이만~!~!~!!!"

    nvl clear

    n "......."
    n "아카리는 빠른 속도로 사라졌다."
    n "그러면 뭐.. 이쪽도 움직이는 수밖에 없다."

    nvl clear

    n "가디언즈가 되어서 좋은 점은 여러가지가 있지만, 필요할 때에 차량을 불러 낼 수 있다는 점이었다."
    n "거기에 운전사도 없기 때문에, 해킹 방어와 실제로 습격당했을 때만 대비한다면 아주 편리했다."
    n "나는 그 차량 안에서, 창문에 팔을 걸친 채로 도시 야경을 바라보았다."
    n "내게 있어서 화이와의 추억은 소중하다."

    nvl clear
    n "아름다운 추억이라고 회상할 만큼, 좋았던 시절이다."
    n "그렇기에 그녀를 지키고 싶었다."
    n "원래 살던 삶으로 되돌리고 싶었다."
    n "'연화의 아이들'에서 신 노릇을 하는 건, 분명 불행하리라 생각했다."
    n "이건 내 맹목적인 생각이 아니라 그녀의 발언에서 기인한 추측이다."

    nvl clear

    n "그녀는 언제나, 자신의 종교에 대해 애매하게 말했기 때문에."
    n "...구하는 것은 못해도, 적어도 확인은 하고 싶다."
    n "화이가 지금 행복한지."
    n "그 믿음이란 건, 옳은 것인지."
    n "...화이가 하는 행동들이, 선한 의도라고 해도 누군가에게 상처를 주고 있다는 걸."
    n "알고 있기는 한지."

    nvl clear

    scene bg city2
    with pixellate
    play music "audio/NonN.mp3"

    n "────'예배당'이라고 하는 곳은 상당히 화려한 도심에 있었다."
    n "C시 북부로 가야하는 만큼 오래동안 차를 타야 했다."
    n "이곳이 바로 도시의 심장, 썬로드(Sunroad) 지역이다."

    nvl clear

    n "돌아다니는 인간들 모두, 말끔하고 멋진 차림이었다. 칠룡성채의 눈 아픈 패션은 온데간데 없다."
    n "그렇지만 그만큼 이질적이다. 이렇게 포화된 도시에서, 이런 깔끔함이라니."
    n "그리고 나는 보았다."
    n "지나치게 깔끔히 차려입은 사람들이, 서로를 보며 부자연스러운 미소를 지으면서 예배당 안으로 들어가는 모습을."

    nvl clear

    n "그 사람들은 대체로 모습을 가리고 있었다."
    n "이런 모습이니까──스틱맨임을 숨기는 건가."
    n "나는 바로 통신을 걸었다."
    nvl clear

    nd "여기는 하운드-3. 가디언즈 본부?"
    nvlphone "본부 등장, 수신자 케인{size=-10}Kane{/size}."
    n "그 광경을 본 나는 본부와의 교신을 시도하였고, 대기하고 있던 케인이 응답했다."
    n "그 특유의 낮고 시니컬한, 소년미가 느껴지는 목소리가 들려왔다."

    nvl clear

    nd "연화의 아이들 예배당 근처에 도착. 조사를 시작하려고 하는데."
    nvlphone "확인. 시야를 공유해주시길 바랍니다."
    n "그 특유의 딱딱한 목소리가 들려왔다."

    nvl clear

    n "나는 가디언즈 본부로 내 시야 정보를 전송했다."
    nvlphone "확인. 보유중인 자료와 네트워크 자료를 참고하여 브리핑하겠습니다."
    nvlphone "...그런데요, 루이 선배."
    nvlphone "...아문 수사관에게도 공유할까요?"
    n "케인이 그렇게 묻자, 나는 그러라고 답했다."

    nvl clear

    nd "본부에게 하운드-3이 전송."
    nd "지금부터 '연화의 아이들' 본부로 잠입수사를 시작한다."
    n "나는 짧게 통신한 다음 차에서 내렸다."
    n "잠시 뒤 응답이 왔다."

    nvl clear

    nvlphone "수사 허가 요청중... 승인되었습니다. 특이사항이 있을 경우 즉각 보고해주시길 바랍니다."
    n "수사반장님이 허가를 내려주셨다."
    n "이제 내 스타일대로 일을 하면 된다."

    nvl clear

    nd "케인, 말해두지만 나는 브리핑을 즉각즉각 하는 성격은 아니라서."
    nd "선언하고 난 다음에 바로 뛰쳐나가는 경우도 있어."
    nd "그때는 확실히 보조해주길 바란다."
    n "내가 그렇게 말하자 케인은 알겠다는 이모지를 보냈다."
    n "과묵한 성격인 것 같다."

    nvl clear

    n "────나는 전선을 목 뒤에 꽂고, 네트워크에 접속했다."
    n "목 뒤에서 전극이 자극되는 느낌이 들었다."
    n "이 정도의 약한 스파크는 일상이다."

    n "곧 시야를 메우는, 형형색색의 디지털 신호들. 현실세계의 풍경이 없어진다."
    n "수많은 창들이 떠오르고 네트워크 세계로 빠져든다."

    scene bg cyberspace
    with squares

    n "여러 가지 건물들이 보인다."
    n "C시의 매트릭스는 다른 곳과 다르다. 여러 가지 비유적인 요소를 사용하는 곳이 많다."
    n "판타지 세계를 인용하는 경우도 있고, 서브컬처 애니메이션에 등장하는 것들을 끌어온 사례도 많다."
    n "하지만 C시의 전자세계는 대부분 건물 그대로 이루어져 있다."

    nvl clear

    n "연화의 아이들 본부로 추정되는 저 건물의 견고한 방어 매트릭스는 성 같은 모양이었다."
    n "격자 모양의 그 가짜 건물로, 나는 들어가야한다."
    n "그렇지만 이대로 가다간 불에 타 죽고 말겠지."
    nd "케인, 지금부터 들어갈 거야. 보안 프로그램 확인 좀 해줘."

    nvl clear

    n "케인은 그 말을 듣고, 타이핑 소리를 몇 번 내더니 쯧, 하고 혀를 차는 소리를 냈다."
    nvlphone "...이상하네요. 없습니다. "
    nvlphone " 딱히 대응 해커는 없나봐요. 기본적인 프로그램만 있어서, 개시하시면 맞춰서 끌게요."
    n "의외다."
    n "아니면 함정일지도 모른다. 두 생각이 양립해서, 미간이 찌푸려졌다."

    nvl clear

    nd "수상쩍네... ...알았어, 계속 주시해줘."
    n "나는 그렇게 말하고서 저 앞을 바라 보았다."
    n "방어벽이 기초적으로만 있다면, 매복하고 있는 실력 좋은 녀석이 있을 수도 있다. "
    n "그렇지만 케인은 그런 '그림자의 사람'도 찾아낼 수 있는 실력자였다."
    n "사이비 종교라더니, 정말 이런 사이버 보안은 신경 안 쓰는 건지...."

    nvl clear

    n "그렇지만 보안이 없다면 꾸물거릴 이유는 없다."
    n "어떻게든 부딪혀보자."
    n "나는 팔을 들어, 그곳 벽에 손을 갖다 댔다."
    n "시야에 화면이 하나 떠오르고, 여러 문자들이 떠오른다."
    n "그것들을 그대로 복사한다. 그리고 전송한다."

    nvl clear

    nd "좌표 전송하였음. 침투 프로그램 요청."
    nvlphone "확인 '카프카'를 그쪽으로 보냅니다."
    n "개발자 녀석이 책을 좋아해서 그런 이름이 붙었다."
    n "뭐였더라, 이 시대의 영혼을 깨는 녀석이 될테니 그런 이름이 어울리겠다고 했었다."
    n "곧이어, 나는 푸른색 바다를 뚫고 기어오는 벌레들을 보았다."

    nvl clear

    n "그것들은 천천히 그 성벽- '연화'의 건물로 진입했다. 실제로는 프로그램이 움직이는 거겠지만."
    n "곧, 암호화된 연화 녀석들의 방화벽을 뚫고 우리에게 카메라 권한을 가져 올 것이다."
    n "─────잠시 뒤, 내 눈 앞에 여러 개의 화면이 떠오른다."
    n "나는 그 즉시 접속을 종료했다."

    nvl clear

    scene bg city2
    with pixellate

    n "카프카가 안쪽에서 활동하고 있다면, 굳이 유저인 나까지 매트릭스에 있을 필요가 없다. "
    n "혹시나, 저쪽이 방어 해커를 비밀리에 운용하고 있다면 잡힐 위험이 있고, 잡힌다면 골치 아파진다."
    n "그리고 눈 앞에 있는 화면들에 집중했다."
    n "조금 지루할지도 모르는 시간이다."

    nvl clear

    n "카프카가 취득한 화면들은 CCTV, 그리고 내부를 돌아다니는 청소 드론들이다. "
    n "사실상 '연화'에서 얻을 수 있는 시각은 다 얻은 것이다."
    nvlphone "아예 그냥 다른 사람 시각 인터페이스를 해킹해버리는 것도 괜찮을 것 같지 않아요?"
    n "-케인이 그렇게 말하자 나는 화들짝 놀랐다."

    nvl clear

    n "안 돼, 그건 너무 위험해."
    n "내가 그렇게 말하자 케인은 한숨을 쉬었다."
    nvlphone "-선배는 신중하시네요. 아문 선배랑 다르게."
    nd "이건 내게 있어서 중요한 문제야."
    n "나는 그렇게 답하고 등을 기댔다."

    nvl clear

    n "한 사람을 위해 마음을 쓰는  그렇게 쉬운 일이 아니다."

    nvl clear

    n "난 차에 앉아서 화면들을 돌려 보았다. '연화' 내부의 풍경이 즉시 내게로 송출되었다."
    n "내부는 평범...하다기 보다는, 꽤 독특했다. 예배당의 CCTV는 총 수십 여개. 이것만으로 규모가 꽤 되는 건물이라고 짐작할 수 있다."
    n "CCTV마다 방의 이름이 붙어 있었는데, '예배 본당' 같이 평범한 이름이 있는가 하면 '수행의 방' 같이 목적을 짐작하기 어려운 방들이 있었다."
    n "사이비 종교답다고 해야 할지, 수상쩍고 불쾌해지는 이름들이다."



    nvl clear

    n "케인은 나와 같이 화면을 보고 있었다."
    n "나는 잠자코 있었던 것과 대조적으로 그는 계속 불평을 해댔다."
    nvlphone "'연화님'이 안 보이네요..."
    nd "화면 갯수가 많아서 그래. 잘 찾으면 나올 거야."
    nd "그리고, 항상 그녀가 카메라가 있는 곳에 있으리라는 법도 없잖아."

    nvl clear

    n "그는 이후 아무 말도 하지 않았다."
    n "그러다 또 다른 말이 들려왔다."
    nvlphone "선배는 그거 아세요? 선배처럼 변한 사람들이 언젠가 괴물로 변해버린다는 거."

    nvl clear

    nd "뭐?"
    n "처음 듣는 이야기였다."
    nvlphone "순찰 도는 녀석한테서 들은 소식인데요."
    nvlphone "그런 모습으로 변해버리면 능력을 쓸 수 있잖아요?"
    nvlphone "그렇게 남발하다가 어느 순간 자제력을 잃는대요."

    nvl clear

    nvlphone "하연동 델타 구역 쪽의 사정이 요즘 흉흉한 건 아시죠?"
    nvlphone "거기에서 또 사상자가 발생했는데, 피의자이자 피해자였던 사람이 선배 같은 스틱맨이었대요."
    n "나는 멍해졌다."
    n "피의자이자 피해자였던 사람?"

    nvl clear

    nd "좀 더 자세히 설명해봐."
    nvlphone "그 능력.. 뭐라고 했더라. 에스페로? 그걸 사용해서 싸움을 벌이던 청소년 무리들이,"
    nvlphone "어느 순간 폭주해서 서로 죽고 죽였대요."
    nvlphone "그렇게 해서 세 명이 죽었고 목격자였던 한 명은 정신이 이상해졌다⋯ 뭐 그런 이야기에요."

    nvl clear

    nvlphone "아직 언론까지는 안 퍼졌어요."
    nvlphone "그러니까 선배가 조사하는 것에서 좋은 결과가 나와야 그 쪽의 사건도 해결할 수 있다는 뜻이에요."
    n "갑자기 생각에 잠겼다."
    n "제로의 모습이 계속해서 일렁이는 건- 어쩔 수 없겠지."
    n "그렇지만 수사에 있어서는 자아를 키우면 안 된다."

    nvl clear

    n "그런 현상이 실제로 일어난다면, 다른 사람들은 어떻게 되는 건가."
    n "섬광 현상을 겪은 모두가 그렇게 된다면?"
    n "⋯생각하고 싶지도 않다."
    nvlphone "선배도 언젠가 그렇게 되나요?"

    nvl clear

    nd "불길한 소리 하지 마. 내가 무슨⋯"
    nvlphone "그렇다면 다행이고요."
    n "그렇게 대화가 일단락 될 즈음-"
    nvlphone "⋯저 사람 아니에요?"

    nvl clear

    n "그 많고 많은 화면들 속에서 발견하고 말았다."
    n "그녀가 있는 곳은 어떤 방이었다. 개인이 생활하는 공간인 듯, 꽤 널찍한 침대도 있고 옷장이며, 화장대며 평범한 방에 있을 건 다 있었다."
    n "아주 잘 꾸며놨다. 이곳이 바로 '연화님'의 방인가. 방 이름을 슬쩍 살펴보니, '개인실'이라는 이름만 있고 별다른 고유명사는 없었다."
    n "나는  화면만을 확대했다."

    nvl clear

    n "거울 앞에서, 머리 장식을 고쳐 쓰는 그녀가 있었다. "
    n " 다만 - 역시 인간의 모습은 아니다. 그 이질적인 모습으로 얼굴을 꾸미고 있으니, 제법 이질감이 들었다."
    n "그러나- 확실히 내가 알고 있는 모습이다."
    n "둥그런 눈. 분홍색 눈동자."

    nvl clear

    n "그녀는 지금, 머리에 꽃장식을 달고 옷을 입고 있었다."
    n "한복이다. 지금에야 국가의 구분은 없어진지 오래지만,"
    n "옛 한국 옷을 그녀는 입고 있었다."
    n "상의는 짧지만 치마는 길다. 전체적으로 하얀색이지만, 아래로 갈수록 그녀의 눈동자처럼 분홍빛으로 물든다."
    n "아름다운 의상이다."

    nvl clear

    n "그렇지만 나는 곧 그 옷의 의미를 깨닫고 불쾌해진다."
    n "저렇게 잘 치장해둔 모습이라면, 분명히 그녀가 숭배받고 있다는 것을 의미하리라."
    nd "소리는 취득 안 되나?"
    n "내가 그렇게 말하자 케인이 부정적인 답을 보냈다."
    nd "잠시만 기다려주시면⋯"

    nvl clear

    nvlphone "⋯네, 연결 됐어요. 근처의 로봇 청소기 권한을 빼냈어요."
    nvlphone "그걸로 직접 보시겠어요?"
    nd "좋아."
    n "화면에 창이 떠올랐다. 다이브를 하겠냐는 물음이었다."
    n "나는 의자에 등을 기댔다. 전극이 맞닿아 파직거리는 느낌이 들었다."

    nvl clear
    n "순간- 시야가 암전되고, 푸른색 사각형 격자가 들어섰다."
    n "그리고-"
    nvl clear

    scene bg hwairoom
    with dissolve
    play music "audio/001.mp3" loop

    nd "이채야."
    nd "네, 연화님."
    nvl clear

    n "-소녀는, 그 방 안에서 앉으며 자신의 가장 친한 친구를 부른다."
    n "그녀의 이름은 이채."
    n "연보라색 원피스가 잘 어울리는 연약한 존재다."

    nvl clear

    nd "나가야만 하겠지?"
    nd "⋯⋯"
    n "이채는 대답하지 않는다."
    n "이 순간만을 위해, '연화님'은 단장된다. 자신은 그를 위한 일꾼이다. 시녀, 라고도 볼 수 있다."
    n "그렇게 선을 긋는 능력이 필요했다."

    nvl clear

    nd "네."
    n "이채는 란티모 님, 에게 지시받은 대로 조금 기계적으로 답한다."
    n "그녀는 지금 연화님을 감시해야만 한다. 친하게 굴어서는 안 된다."
    n "그럼에도 마음이 쓰이는 건 어쩔 수 없나 보다."
    nd "갔다 와서는 푹 쉬실 수 있어요, 연화님. 그때 말동무를 해 드릴게요."

    nvl clear

    nd "⋯.이채야."
    n "그녀는 자꾸 이채에게 말을 걸어왔다."
    nd "네."
    nd "언니, 라고 해봐. 저번에는 잘했잖아."
    nd "안 돼요."
    nd "어째서?"
    nd "지금은 안 되어요, 연화님. 적어도 예배가 끝난 후에 해주세요."

    nvl clear

    n "이채의 목소리는 연민이 들어서 있었지만, 결국에는 차가웠다."
    n "연화는 거울을 바라보며 한숨을 깊게 내쉬었다."
    n "이번 집회도 쓸데없이 화려하고 바보 같으리라. 자신이 예전 연화님의 예배를 보았던 것처럼."
    n "차이점이 있다면 자신이 주인공이라는 점이었다. 이제는 그녀가 연화님이다."

    nvl clear

    nd "그래, 안 되겠지⋯ ⋯그럼 나가자. 사람들이 기다리겠어."
    nd "네, 연화님."

    nvl clear

    scene bg city2
    with flash

    play music "audio/NonN.mp3"
    nvlphone "타겟, 움직입니다. 몇 명의 일행이 있는 것 같습니다. 전부- 스틱맨처럼 보여요."
    n "케인은 그렇게 브리핑했고 나는 영상과의 교신을 끊었다."
    n "예배가 곧 시작되는 것 같았다. 나는 창문 바깥으로 사람들의 동향을 살폈다."
    n "경호원은 출입을 통제하기 시작했고, 그곳으로 들어가던 다양한 사람들은 발자국이 끊겼다."
    n "신자를 수용한 예배당은 더 이상 사람을 받지 않고 있다."
    nvl clear
    n "아까 들은 대화가 얼마나 마음을 짓누른다고 해도 지금은 집중해야 한다."
    n "여기서 들어가야 한다. 지금이, 바로 그 기회다."
    nd "케인, 지금 들어갈 게. 시야를 공유할테니까 계속 지켜보고 있어줘."
    nvlphone "..너무 무모한 선택 아니신가요?"
    nd "그렇지만 지금이 들어가야 할 때야."

    nvl clear

    n "난 그렇게 말하고서 차량에서 나왔다."
    n "케인이 아무 말도 하지 않자, 말을 덧붙여서 통신을 이었다."
    nd "말리지 않을 셈이야?"
    nvlphone "저는 방임주의라서요."
    n "케인은 그렇게 하고서 잠시 동안 말을 하지 않았다."

    nvl clear
    nvlphone "그렇지만⋯ 루이 선배가 이렇게까지 집착하는 일이라면 저는 말릴 수 없을 것 같아요."
    nvlphone "이해할 수 있을 것 같기도 하고요."
    nvlphone "사람이라면 다 그런 거, 가지고 있잖아요."
    nvlphone "브리핑은 계속 보고 있을 게요. 필요하시면 콜사인."

    nvl clear

    n "그는 그렇게 말한 뒤 잠시 통신을 끊었다."
    n "나는 이 정도 말할테니 뒤는 네가 알아서 해라- 그런 신호처럼 들린다."
    n "그런 것으로 인해 결심할 수 있었다."
    n "앞으로 나아가기로."

    nvl clear

    n "차에서 나서서 그곳으로 천천히 걸어가고 있었다."
    n "주변에는 아무도 없다."
    n "썬로드의 평범한 거리지만, 차량이 거의 다니지 않았다."
    n "공중에도, 지상에도."

    nvl clear

    n "이상하다는 생각이 든다. 마치- 혼자 남겨진 것 같다."
    n "이 주변, 이 거리, 이 도시에서 홀로 서 있는 듯한."
    n "낯설고도 불안한 감각."
    n "앞으로 나서고 있다. 왜냐하면─── 그곳에 가야 할 길이 있으니까."
    n "그런데도 이상하다."

# 연출 수정 해야하는데 SSIBAL

    cen "이런 곳에 홀로 서 있는 건 어쩐지-"

    scene bg black
    with change
    stop music
    play sound "audio/hit.mp3"

    cen "{size=+50}빠각!{/size}" with vpunch

    scene bg white
    with dissolve


    nvl clear

    n "순간────시야가 가려진다."
    n "후두부를 맞은 충격."
    n "누군가에게 습격당했다. 알기도 전에 감각하고 만다."
    n "쿵, 하고 쓰러진다." with hpunch

    nvl clear

    cen "{color=#000}멀리서 목소리가 들려왔다. 그게 누구인지는 알 수 없었다.{/color}"
    cen "{color=#000}몸이 옮겨진다.{/color}"
    cen "{color=#000}시야가──────────────멀어진다───────────────────{/color}"

    scene black
    with fade

    pause

    # 씬전환
    nvl clear

##############################################################################################################################


    scene bg whiteroom1
    with Dissolve(3.0)
    pause

    play music "audio/horror_celesta.mp3" loop

    n "──────────"
    n "눈을 떴다."
    n "이곳도 저곳도 흰색인 곳에, 나는 누워 있었다."
    n "아까까지 무엇을 했는지 잘 기억이 나지 않는다."
    n "아니────"
    n "기억은 나는데 '실감이 나지 않는다'."
    n "잠결에 보았던 실루엣, 혹은 깊은 잠에서 본 꿈처럼 아득했다."

    nvl clear

    n "{p=1.0}머리가 욱씬거렸다." with redf

    n "순간 아까 뒤통수를 얻어 맞은 장면이 떠올랐다."
    n "소리도 들리지 않을 정도로 은밀했고, 감지되지 않을 정도로 빨랐다."
    n "아니면 감지 장치를 속일 만한, 다른 기계를 부착했던가."

    show Loui injured01
    with dissolve
    pause

    l "⋯⋯윽⋯."
    l "⋯⋯⋯⋯무슨 일이지, 이게⋯?"
    l "분명 누구한테 맞은 건 기억나는데⋯⋯."

    nvl clear

    n "나는 주변을 둘러보았다."

    nvl clear

    n "여기도 저기도 하얗고, 벽과 바닥을 구분하는 것은 가는 선밖에는 없다."
    n "누군가가 주기적으로 관리해주고 있는 것인지, 얼룩 하나도 남아 있지 않다. 너무 깨끗해서 이상했다."
    n "외부의 혼잡함과는 너무나도 구별된다."
    n "애초에⋯"

    l "여긴⋯"
    l "어디지⋯?"

    nvl clear

    n "나는 빠르게 주변으로 시야를 돌렸다. 그런데-"
    define whitedissolve = ImageDissolve('bg/whiteroom2.jpg', time = .5, ramplen = 256)

    scene bg whiteroom2
    with whitedissolve
    pause 1.0

    n "몇 군데에 길이 나 있을 뿐, 어떤 표지판도 없다."
    n "흰색은 물론 안정감이 든다. 게다가 잘 만든 건축물처럼 보였다."
    n "어느 곳의 벽이든 미감 처리가 잘 되어 있다."

    nvl clear
    n "그렇지만 이건 너무나도, 달랐다."
    n "창문도 없고 표시도 없으며, 사이버네틱으로 만들어진 것들은 하나도 없다."
    n "C시에서 이런 게 가능하다고?"
    n "애초에 여기가 C시가 맞긴 한가?"

    nvl clear

    n "두근, 두근."
    n "점점 진정하기가 힘들어졌지만, 심호흡을 하기로 했다."
    nd "가디언즈 본부?"
    nd "습격을 받았다. 후두부를 맞은 다음에 정신을 잃었는데⋯"

    nvl clear

    n "────────"
    n "──────────────"

    n "연락이── 되지 않았다."
    nd "본부, 응답하라. 하운드-3이 통신 요청...!"
    n "조금 급해졌다."
    n "이상했다. 분명 네트워크와 항시 연결되어 있을 터인데⋯"
    n "나는 추가로 화면을 열어 상태를 점검했다."

    nvl clear

    n "구시대와 다르게, 지금은 몸을 어느 정도 개조하면 24시간 동안 온라인에 접속해 있을 수 있다."
    n "서버들이 대체로 로컬(Local)로 바뀌긴 했지만, 그래도 공용 네트워크나 권한이 있는 서버에는 들어갈 수 있다."

    nvl clear

    n "그런데 들어갈 수 없었다."
    n "이건 단 하나만을 뜻한다."
    n "주변에 재머(Jammer)가 있다. 통신을 방해하는 장치가 나를 방해하고 있었다."

    nvl clear

    l "(그렇다 해도 설명이 안 돼⋯⋯.)"
    l "(방해 장치가 있다면 시야에도 영향을 미치는 게 맞아.)"
    l "(증강현실 화면을 실시간으로 눈에 떠오르게 해놨으니까.)"
    l "(나 같은 경우에는, 딥 다이브(Deep dive)도 어느 정도 가능한 신체기도 하지.)"
    l "(그러니까 정신에도 영향을 미칠 수 있다.)"
    l "(그런데 지금은- 멀쩡하리만큼 제정신이란 말이야.)"

    nvl clear

    n "시야도 또렷하고 몸도 제대로 움직일 수 있다."
    n "오직 외부로만 단절된 상태였다."
    n "이건 마치- 누군가를 격리하고 있는 감옥과도 같지 않은가. 이런 곳에서 정을 어떻게 찾는 거지?"
    n "그런 생각이 들 즈음-"

    nvl clear

    scene bg black
    with wiperight
    pause 0.2
    scene whitestair
    with wiperight

    n "계단이 눈에 들어왔다."
    n "온통 하얗고, 지표라곤 아무것도 없는 곳인데."
    n "그것만이 눈에 들어왔다."
    n "저 곳으로 올라가면 무언가가 있을지도 몰라."
    n "어차피 나가는 문도 보이지 않으니까."
    n "그런 생각이 들어서, 발걸음을 옮기기 시작했다."

    nvl clear

    nd "여보세요?"
    nd "누구 없어요?"

    nvl clear

    n "그렇게 말해도 아무도 듣지 않았다."
    n "내 목소리만 계속해서 반사되어 들릴 뿐이었다."
    n "그때-"
    n "목소리가- 들려오기 시작했다."

    nvl clear

    cen "{size=+25}{color=#000}어서오세요.{/color}{/size}"
    cen "{size=+25}{color=#000}그대로 위층으로 올라오시면 됩니다.{/color}{/size}"

    n "그 목소리는 직접적으로 들려왔다."
    n "누군가가 통신을 걸거나 옆에서 말을 거는 게 아니라,"
    n "머릿속에서 집접 웅웅 울려퍼졌다."

    cen "{size=+25}{color=#000}저희는 당신을 기다리고 있었습니다.{/color}{/size}"
    cen "{size=+25}{color=#000}예언자님께서 당신을 기다립니다.{/color}{/size}"

    nvl clear
    n "⋯저런다고 해서 찾아갈 줄 아나."
    n "그렇지만 딱히 방법도 없었다."
    n "1층에 나 있는 수많은 길을 헤맬 바에는 일직선으로 올라가는 게 낫다."
    n "나는 그렇게 판단하고, 천천히 위로 올라가기 시작했다."

    nvl clear

    n "계단을 올라갈 때마다 불안감이 엄습했다."
    n "무서운 괴물이 나올 것 같지도 않다."
    n "갑작스레 습격이 찾아올 것 같지도 않다."


    nvl clear

    n "2층으로 올라오자마자 열려있는 문이 보였다."
    n "안쪽의 풍경은 보이지 않는다. 다만 소리만이 들려올 뿐이었다."
    n "어딘가 그리운 느낌이 드는 피아노 소리, 그리고 사람들의 합창."
    n "찬양이다."
    n "신에 대한 찬미를 올리고 멜로디를 모으고 모아 하늘로 보내는 작업을 하는 것 같았다."

    nvl clear

    n "그래, 여기는 예배당이었지."
    n "그런 생각이 들자 문득 이방인이 된 것 같았다."
    n "그렇지만 나는 나아가야 한다."
    n "아까 화이는 예배당으로 향한다고 했다. 그러니-"

    nvl clear

    n "이 너머에는, 필시 그녀가 있다."

    nvl clear

    n "그 안으로 들어가자 기묘한 광경이 펼쳐졌다."

#################################################################################
#여기서부터 작업시작하세요
#어떻게이틀이지났는데여기스크립트가 그대로야

    nvl clear

    scene bg church
    with dissolve

    #이거대사창안에서가운데정렬해야할듯
    nd "그런고로 이 자는 죄인입니다."
    nd "여기서 죄 없는 자만이 이 자에게 돌을 던지십시오."
    nd "그렇지만, 우리 모두 그럴 수는 없는 걸 잘 아시지 않습니까, 여러분?"
    nd "우리도 똑같습니다."

    n "누군가가 사람들에게 그렇게 고하고 있었다."
    n "남자의 목소리, 그렇지만 하늘을 걷듯이 가볍고 얇다."
    n "목소리에 힘이 실려 있지만 톤 자체는 무겁지 않았다."
    n "그렇기에 이상한 매력이 있는, 소리였다."

    nvl clear

    n "나는 안쪽으로 걸어갔다."
    n "그리고- 그 광경을 보았다."

    nvl clear

    n "수많은 사람들이 의자에 앉아서, 고개를 숙인 채로 예배를 듣고 있었다."
    n "교회 의자가 양쪽에 나 있었고, 그 중앙으로 카페트가 깔려 있는 것처럼 길이 나 있었다."
    n "마치 지옥으로 향하는 아가리처럼 벌려져 있었다."
    n "대략 150명 정도 되어 있는 사람이, 정갈하게 거대한 예배당에 앉아 있었다."
    n "교회는 아주 커다래서, 거대한 홀처럼 보이기도 했다. 지금 이렇게 많은 사람들이 있는데, 더 많은 사람들을 수용할 수 있으리라는 생각이 들었다."

    nvl clear

    n "나는 그것을 아주 멀리서 보았다. 입구에서. 그리고 그곳에서는 두 사람이 보인다."
    n "저 멀리, 무대 위에 있는 자들이."
    n "그곳에는 두 존재가 있었다."
    n "한 명은- 흰색과 금색 조합의 옷이 돋보이는 인물이다."
    n "청녹색 눈동자에,나와 비슷한 모습- 저 사람도 분명, '그런 현상'을 겪은 사람이리라."
    n "그리고 예배당에서 저런 위치에 있는 사람은 필연적으로, 이 종교의 높은 사람이라는 뜻이다."

    nvl clear

    n "안 좋은 예감이 든다."
    n "특히 그의 웃는 표정에서 - 온갖 종류의 불길함이 느껴졌다."
    nd "죄인은 미워해서는 안되지만 회개하지 않는 죄인은 쳐야 마땅합니다."
    nd "우리의 반면교사로 삼아 마땅합니다."
    nd "이 자는- 우리처럼 선택받았지만 연화님의 은총을 거부했습니다."
    nd "게다가 저희를 속이고, 불신자들에게 저희의 정보를 팔아 넘기려고 했죠."

    nvl clear

    n "나는 그 대목에서 짐작할 수 있었다."
    n "그가 누구를 말하는 지를."
    n "순간, 불안감이 엄습해와 온몸을 덮는다."
    n "불안감은 곧 현실이 되어 공포로 변했다."
    n "그렇게 해서 온 몸이 저릿거리는, 이상한 감각이 들었다. 이전에는 느껴보지 못한."
    n "나는 그 중앙 통로로 저벅, 저벅, 계속 걸어갔다."
    n "몇몇 사람들은 나를 쳐다보았지만 - 상관 없다."

    nvl clear

    nd "다행스럽게도 예언의 서에 나와 있는 저주받은 남자는 아니었습니다."
    nd "그렇지만 거짓된 신앙, 가짜 뜻을 가지고 이곳에 숨어 기어 들어왔습니다."
    nd "그렇게 계속해서 능력을 쓰고, 저희의 신앙을 애매하게 거부하면서,"
    nd "저항하다, 결국은 자신의 죄를 견디지 못했습니다."

    nvl clear

    n "누구도 답하지 않았다."
    n "누군가가 선창할 법도 한데 모두가 침묵했다."
    n "나는 그것에서 그 남자의 카리스마를 실감했다. 종교인데도 누군가가 답하지 못한다는 것은, 그만큼 이 사람의 힘이 강하다는 뜻이다."
    n "힘이라고 해야할까. 어쩌면 그들은 압제당하고 있는 게 아닐지도 모른다."
    n "자의로 독재에 따르는 사람들이 가장 무서운 법이다."

    nvl clear

    n "나는 그들 사이에서 - 그냥 서 있기만 했다."
    n "그들에게 압도되고 있었다."
    n "이상한 세계에 빨려 들어온 것처럼, 아무런 말도 할 수 없었다."
    n "구멍 속으로 빠져 든 앨리스처럼."

    nvl clear

    n "-남자는, 손을 들어 자신의 소매를 쥐었다. 다짐하는 것처럼 보이기도 했다."
    n "나는 계속해서 그를 보았다."
    n "그가 '죄인'이라고 하는 사람을 보고 싶지 않았다."
    n "왜냐하면 그는-"

    nvl clear

    scene 16
    with dissolve
    pause

    nd "연화님은 죄인 역시 사랑하라는 말씀을 베푸셨었습니다. 그에게는 다행스러운 일이죠."
    nd "세상을 구원하는 구세주로서 그분은 죄인 역시 사랑하십니다."
    nd "여러분이 연화님을 사랑하신다면 연화님 역시 여러분을 사랑하십니다."
    nd "그렇지만 계속해서 죄를 짓는다면 연화님은 하늘에 계신 그분과 함께, 그 죄인을 치십니다."
    nd "그리고 여기 있는 이 죄인은 - 쳐야 마땅할 죄인이지 않겠습니까?"

    nvl clear

    n "대답이 여기 저기서 들려왔다."
    n "그렇다, 옳다, 기독교처럼 아멘, 같은 단어를 외치는 사람도 있었다. 다른 단어이긴 했지만."
    n "알아들을 수 없는 걸 보니 독창적인 언어겠지."
    n "이윽고 그 남자는 말을 이었다."
    nd "그는 그 은총-에스페로를 남발하다가.. 결국 자신의 죄에 짓눌리고 말았습니다."
    nd "당신께서, 우리에게 그런 벌을 주지 않으심에 감사드립시다. 오늘도 무사히 하루를 넘길 수 있음을 찬미합시다."
    nd "그분께 경배 바친 우리가, 이곳에서 기적을 행사하는 대리인으로서 있는 것에 감사드립시다."

    nvl clear

    nd "그나저나-"
    n "그는 그렇게 말하다, 나와 눈이 마주쳤다."
    n "나는 그를 올려다 보았다."
    n "초점이 되려 확실해서 불길한 사람이 있다. 각성 상태거나 무언가를 깊게 신뢰하고 있어서 희번득한 눈빛."
    n "이쪽은 후자다."
    n "무서운──────광신도다."

    nvl clear

    nd "죄를 지으면 벌을 받아야합니다."
    nd "{size=+30}죄를 지으면 벌을 받아야합니다!{/size}"
    nd "벌을 받으면 구원받지 못합니다."
    nd "{size=+30}구원받지 못합니다!{/size}"
    nd "구원받지 못하면-"

    nvl clear

    nd "여러분은 살아남지 못합니다."
    nd "이 더럽고 위험한 세상에서 살아남기가 얼마나 어려운지는 여러분들이 아시지 않습니까."
    nd "C시에는 어둠이 가득 도사리고 있습니다, 우리 연화의 아이들이여."
    nd "우리에게는 우리밖에 없고, 더러운 기술 외에 사용할 힘은 에스페로 뿐입니다."
    nd "우리는 단합하여 서로를 지켜야하고, 저 바깥의 죄인과 불신자들과 맞서야합니다."
    nd "그리고 순진한 어린양들을 더 많이 그분의 길로 인도해야합니다. 연화님의 이름 아래에───"

    nvl clear

    nd "그리고 여기, 죄인이 한 명 있습니다."

    nvl clear

    n "'죄인'은 내가 알고 있는 사람이었다."
    n "많은 이야기를 나눠보지 못했지만 그는 '가디언즈' 요원이었다."
    n "연화의 아이들을 예전부터 계속해서 추적하던 일원이었고, 그 역시 스틱맨이었다."
    n "그는 앞쪽을 보고 있었다."
    n "정확히는 보지는 못했다. 안대에 눈이 가려져 있었기 때문이다. 그렇기 내가 온 것도 모른다."

    nvl clear

    n "아─────────────"
    n "저 친구도 내가 구할 수 있었을지도───모른다. 그런데 너무 늦어버렸다. 이미 그는 이곳의 포로─"
    n "손은 묶여 있다."
    n "입은 멍하니 벌려져, 마치 무대에 올라온, 동화 속의 바보 같다. 그렇기에 끔찍하다."

    nvl clear

    scene 17
    with dissolve

    nd "자─"
    nd "당신은, 하늘에 계신 그분께 자신의 죄를 인정하고 용서를 구하십니까?"
    nd "⋯⋯."
    nd "그분의 은총을, 이제라도 그분을 위해 사용하고 연화의 아이들에게 베풀 것을 약속하십니까?"
    nd "⋯모⋯."
    nd "더 크게."
    nvl clear

    nd "⋯⋯⋯⋯⋯⋯⋯⋯. ⋯⋯⋯⋯⋯⋯⋯."
    nd "⋯⋯모르겠⋯⋯"
    nd "잘⋯⋯모르겠어⋯⋯⋯⋯."
    nd "나는⋯ 당신들을 조사하러 왔을 뿐이야⋯⋯."
    nd "당신들과 한패가 되기 위해서가 아니라⋯⋯⋯⋯⋯."
    nd "너희들은 왜 이러는 거야⋯⋯⋯? 왜 형체도 없는 그 사람 따위를⋯⋯⋯⋯."

    nvl clear

    #어휴 퇴고 많이했다
    n "이후 아무런 소리도 들리지 않았다."
    n "군중들의 웅성임을 제외하면 아무도 말하지 않았다."
    nd "바깥 사람들에게는 저희가 바보처럼 보이겠죠."
    nd "네트워크 반대주의자, 오래된 종교인들, 근본주의자, 그리고 이단."
    nd "하지만 우리는 다른 사람들이 추구하지 않는 걸 추구합니다. 더러운 것을 혐오하고 깨끗한 걸 추구합니다."
    nd "그것이 누군가에게 구원이 된다면!"
    nd "저희는 당연히도 이단이고 광신도가 될 것입니다. 그렇지 않습니까?"

    nvl clear


    n "남자는 계속해서 말을 이어갔다."
    n "앞이 보이지 않는 그에게 계속 공격적으로 쏘아 붙인다."
    nd "그렇다면 당신은 무엇을 믿습니까?"
    nd "무언가를 믿지 않는다고 해서 당신의 삶에서 무언가가 바뀌었습니까?"
    nd "하지만 반대로 저희는, 바뀌었습니다."
    nd "연화님을 믿고 나서 힘을 얻었습니다. 살아갈 의지를,"

    nvl clear

    n "그는 그렇게 말하고, 머리에 손을 얹었다. 마치 세례하는 것처럼."
    n "그리고 속삭였다."
    n "그렇지만 그 목소리는 그 현장에 있는 모두에게 들렸다. - 그러리라, 생각한다."
    nd "이제 우리의 지도자인 그분이 당신께 내려옵니다."
    nd "그때까지 당신이 죄를 뉘우치지 않는다면."
    nd "이제 당신이 마지막으로, 구원을 받지 못한다면,"
    nd "당신은 정말로 집행당합니다."

    nvl clear

    nd "안타깝게 생각합니다. 그분의 음성을 듣지 못하다니."
    nd "그렇지만 저희가 집행하지 않아도 당신은, 타락한 죄인이 되어 이성을 잃고 말겠죠."
    nd "그러니까 최대한 덜 고통스럽게 해드리겠습니다."
    nd "축복이 있기를. 다 같이 이 죄인을 축복합시다!"

    nvl clear

    nd "{size=+30}축복이 있기를!{/size}"

    nvl clear

    scene bg church
    with dissolve

    nd "⋯⋯."
    n "근처에서 집행자가 다가오고 있었다. 가면을 쓴 사람들이다."
    n "며칠 전에 보았던 그들과 똑같다. 손에는 얼굴을 가리는 천과, 거대한 도끼가 있었다."
    n "저것도 에스페로일까? 아니- 이제 그건 사실 별로 중요하지 않다."

    nvl clear

    nd "그쯤하지 그래."
    n "나는 거기서 참을 수 없었다."
    n "더 이상은 그가 행패를 부리는 걸 볼 수 없었다."

    nvl clear

    nd "아────."
    nd "초대받지 않은 손님이 왔군요."
    nd "안녕하십니까, 또 다른 불신자여."
    nd "기다리고 있었습니다."

    nvl clear

    n "그가 그 말을 하자 신자들이 일제히 나를 쳐다보았다."
    n "무서운 광경이다. 모든 사람이 나에게로 시선을 집중하고 있다."
    n "구토감이 몰려올 정도의 압박감이다."
    n "그리고 그것은 비단 수많은 사람의 시선뿐만 아니라,"
    n "저 사람- 교주, 로 추측되는 남자의 기운 때문도 있다."

    nvl clear

    nd "보세요, 당신의 동료였던 자도 저주받았습니다. 회개하지 못하여 죄인이 된 모습을 보시니 어떻습니까?"
    nd "나는 당신을 알고 있어요, 저주받은 남자. 가엾은 수사관."
    nd "루이."

    nvl clear

    n "이름은 어떻게 알았지, 같은 대사 따위는 하지 않는다."
    n "저 녀석도 저 녀석만의 첩보망이라는 게 있을 테니까."
    nd "화이는─────어디에 있지?"
    nd "지금 당장 내 앞으로 데려오지 않으면 좋은 꼴은 못 볼거야."

    nvl clear

    n "그 이름이 나오자, 남자는 픽 하고 웃었다. 우스운 불나방 취급을 당했다."
    nd "그 사람이 누구도 모르는 데다가, 초대에 이렇게 응하는 사람의 말을 들을 필요는 없다고 생각해요."
    nd "집행을 계속합시다! 동요하지 마시길! 저 자는 그저 정욕에 빠져 여자에 미친 사람일 뿐입니다."

    nvl clear

    n "-나는 순간 화가 치밀어 올랐다."
    n "그는 넌지시, 알고 있는 것 같았다."
    n "내가 '연화님'이 아니라 화이를 데리고 가려 하는 것을. 그렇기에- 분노가 감싸기 시작했다."
    n "시야가 깜빡거리는 것과 동시에 현기증이 일었다."

    nvl clear

    n "며칠 전에 경험했던 바로 그 감각이었다."
    n "정신을 집중한다면───바로 그것을 불러낼 수도 있을 것이었다."
    n "나는..."

    menu:
        "에우레카를 꺼내어 달려든다":
            jump scene01A

            label scene01A:

                n "───────────"
                n "【에우레카(Eureka)──── 지금 네 힘이 필요해.】"
                n "【한 번만 더 힘을 빌려줘.】"
                n "【저 녀석의 심장을⋯⋯⋯ 가져다 줘.】"
                nvl clear
                n "생각이 끝나고──눈을 깜빡이자, 순식간에 손에 에우레카가 쥐어졌다."
                n "마음이 외친 후로 그것이 응답했다. 제로와의 대화가 없어도 이것을 불러낼 수 있게 되었다."
                n "손에 쥐어진 에우레카. 탄성을 내지르는 사람들."
                n "가면을 쓴 '집행자'들이 일제히 일어서서 나를 쳐다보았다. 표정은 보이지 않았다."
                n "하지만 그들은 끔찍한 표정을 짓고 있으리라."
                nvl clear

                n "-그 예언자라고 하는 남자는, 날 보며 알 수 없는 미소만 띄워 올리고 있었다."
                nd "그대로 달려오실 건가요? 그래도 좋죠. 저희라고 에스페로가 없는 것도 아니니까."
                nd "보십시오, 여러분!"
                nd "이 자는 여인을 탐하는 욕망에 허덕여 끝내 구원받지 못하고,"
                nd "죄인으로 향하는 주로를 달리고 있군요."
                nd "이곳에서 당신의 죄를 증명하실 겁니까? 저희야 좋죠! 하하. 아하하하!"
                nvl clear


                nvl clear
                n "달려 나간다."
                n "손에서 꽉 쥔 에우레카를 놓지 않는다. 남자는 웃고 있었다. 여러 명의 신도들과 함께."
                n "그렇다면 지금이 기회이지 않은가!"
                n "지금, 일격에 저 녀석을──────"

                nvl clear


        "지금은 참도록 한다":
            jump scene01B
            label scene01B:
                n "지금은 참아야 한다."
                n "나는 마음 속에 끓어오르는 충동을──억눌렀다. 지금은 날뛰어서는 안 된다. 훨씬 불리하다."
                n "연화의 아이들이 요원을 얼마나 운용하고 있을지도 모르고 전투력도 파악이 안 된다."
                n "이성을 신용해야 한다. 여기서는 침착해야 해."

                nvl clear

                n "그렇다면 어떡하지? 이 상황을 타개할 방법이 있나?"
                nd "하하, 이것 보십시오! 수행하지 못한 사람은 이렇게 됩니다."
                nd "축복을 받고서도 제 몸 하나 가누지 못하지 않습니까. 이토록 신은 공평합니다."
                nd "오직 믿는 사람에게만 힘을 주시지요."
                nd "저주받은 남자여── 그대로 굴복하시죠."
                nd "당신도 이 자와 함께 집행해드리겠습니다."

                nvl clear

                n "죽는 건가?"
                n "또 다른 방법이 정말로 없는 건가?"
                n "네트워크 접속을 다시 시도해보려고 했지만────무리다."
                n "이젠 어떻게 해야..."





    nvl clear




    stop music
    nd "{size=+40}그만!{/size}"

    nvl clear
    play music "audio/001.mp3" loop

    n "어디선가──── 들려오는 목소리."
    n "순간 심장이 멎는 것 같은 착각이 들었다."
    n "그 목소리다."
    n "내가 알고 있는 바로 그 톤, 어조, 뉘앙스, 모든 것들이 그대로였다."
    n "조금 성숙해진 목소리지만 거의 차이가 없다."

    nvl clear

    n "정확하고 강단있다. 그리고 조금 높다."
    n "그런 여성의 목소리는- 누구도 따라할 수 없다."
    n "누구도 따라해서는 안 된다."
    n "왜냐하면 그 목소리는 온전히 그녀만의 것일 테니까─────"

    nvl clear

    nd  "란티모, 그 정도면 됐어요. 다른 사람들도 다 앉아요."
    n "남자는 그제야 설교를 멈추었다. 이름이 란티모인 모양이군."
    n "흥분해서 일어서거나, 나에게 고함을 치던 몇몇 신도들도 순순히 자리에 앉았다. 예배당은 금세 조용해져 침묵으로 가득했다."
    n "나는─ 란티모가 아무 반응도 보이지 않자, 자연스레 목소리가 들려 온 곳을 바라보았다."
    n "사실 그가 있던 없던 그쪽을 보았을 것이다."
    n "그 이유는───"

    #책갈피

    scene 14
    with dissolve
    pause

    nvl clear

    n "열린 문 사이로 두 명의 사람이 보였다."
    n "한 사람은 키가 작다. 그리고 보라색  원피스를 입었다."
    n "무릎까지 오는 길이, 하늘하늘하다기보다는 몸에 딱 맞춘 사이즈."
    n "자세히 보니 상의와 한 옷이다. 저고리와 치마로 이루어진 종류다. 이것도 연화의 아이들에서 사용한, 어느 나라의 전통복에서 따온 디자인인 것 같다."
    n "인간이었다면 뒷머리를 묶었을 꽃장식이 인장식이었다."
    nvl clear
    n "전체적으로 연보라색, 이라는 인상이 강했다. 그렇지만 그녀의 눈동자는 검은색이었다."
    n "옆에 있는 사람을 보좌하는 것인지 뒤에 서 있다."
    n "그리고 그녀 옆에 있는 사람은-"
    nvl clear

    scene 15
    with dissolve
    pause

    nd "초대해놓는다고 말하고서 이렇게 공개적으로 면박을 주는 건 대체 뭔 예의인지 모르겠네."
    nd " 손님은 제가 데려갈테니 예배를 계속해요, 란티모."
    n "그녀는 그렇게 말하며 란티모를 노려보았다. 제법 날카로운 눈빛을 하고 있었다."
    n "예전부터 저런 얼굴을 하곤 했었지. 불의를 참지 못하는 성격이니까."
    nd "⋯⋯⋯."

    nvl clear

    n "순간 침묵이 일었다."
    n "왜냐면 '연화의 아이들' 예배 현장에- 그 본인이 나타난 셈이었으니까."
    n "누군가는 두 손을 모으고 경배하기 시작했다. 존재 자체를 놀라워하는 걸까. 잘 이해되지는 않았다."
    n "시선을 두지 않으려고 하는 사람도 있었다. 그 정도로 그녀는 지금 이 사람들에게, 그런 의미를 갖고 있는 존재다."
    n "그렇지만 그 아름다움과 카리스마에 압도되어 있는 사람이 대부분이었다. 모두 경이로워 하고 있었다."
    n "그들은 '연화'라는 이름에 놀랐겠지만 나는 다르다."

    nvl clear
    n "화이."
    n "그녀의 등장은, 신도들에게도 뜻밖이었던 듯───────모두가 침묵했다."
    n "예전과 전혀 다르지 않지만, 어떤 의미로는 모든 게 변해버린 모습이었다."
    n "화이는──단아한 옷차림을 하고 있었다. 발을 전부 가리는 펑퍼짐한 치마, 가는 선의 저고리, 꽃 모양 노리개."
    n "그리고─ 인간에서 벗어났다 해도, 여전한 분홍빛 눈동자."
    n "나는 그녀를 얼빠진 표정으로 바라보고 있었다."
    n "신이라는 맥락 없이도 아름다운 자태다."

    nvl clear
    nd "네, 분부대로 하죠."
    n "그는 여전히 능글능글 웃는 표정으로 그렇게 말했다. 꾸벅, 하고 허리를 숙이는 모습이 가증스럽다."
    nd "가셔도 좋습니다."
    n "나는 그에게 등을 돌렸다. 란티모는 나를──여전히 비웃고 있는 것 같았다."
    n "저런 사람은 오래 봐줄 이유가 없으니까, 그냥 더러우니까, 같은 이유로 생각했다.."

    nvl clear

    n "──────문득 란티모가 뒤에서 말을 걸어왔다."
    nd "그래도 조심하시길, 수사관이여."
    nd "더러운 세상에서 오신 분이니, 깨끗한 곳을 더럽히진 않았으면 좋겠습니다."
    nd "특히 연화님은 더욱 더."
    nd "저희 모두에게 소중한 분이니까요. 구세주이자 신인 그분을 욕보이지 않으셨으면 합니다."


    nvl clear

    n "속으로 욕해주고 싶은 마음을 꾹 참았다. 여기서 화를 냈다가는 모든 일을 망치는 셈이 된다."
    n "그러니까 인내해야만 한다."

    nvl clear

    nd "자, 가시죠. 손님..."
    n "화이가 그렇게 말하는 소리가 들려왔다. 나는 그녀의 옆으로, 천천히 다가갔다."
    n "입으로 심장이 튀어 나오는 것 같아서 긴장되었다."
    n "그녀는 알아챘을까? 내가 누군지?"
    n "아니면───단순한 손님이라서?"
    n "어쨌거나 우리는 문을 나섰다. 천천히, 걸어나가듯이."

    nvl clear

    scene bg black
    with dissolve

    n "닫힌 문으로는 아무런 소리도 들리지 않다가 이내 찬송가가 들려오기 시작했다."
    n "귀를 막고 싶을 정도다. 화이가 옆에 오니 그 맥락들이 더 끔찍하게 느껴지는 것 같았다."
    n "맹목적인 추종과 개인을 구원의 대상으로 삼는 추악함."
    n "더는 가만 두고 볼 수 없지만 내가 어떻게 할 수 있는 것도 아니었다."
    n "그러니 침착해야 해."
    nvl clear
    n "나는 화이를 말 없이 따라갔다."
    n "사람들이 많은 예배당을 등지고 나오는 기분은 낯설었다."
    n "수업 시간에 땡땡이를 치는 기분이라고 해야 할까, 학교생활을 같이 했던 그녀와 함께라서 그런 걸까."
    n "우리는 계속해서 끝없는 복도를 걸었다. 그동안 아무런 말도 하지 않았다."
    n "그녀에게 묻고 싶은 말은 많았지만 - 지금은 참기로 했다."
    n "무엇보다 그녀 옆에 있는 소녀가 신경 쓰이기도 했다."
#책갈피

    nvl clear
    n "나는 오로지 화이만을 믿을 수 있었다."
    n "그 외의 사람은 아직- 잘 모르겠다."
    n "이윽고 우리는 어떤 문 앞에 도착했다. 그곳에는 구식 자물쇠가 있었다."
    n "화이는 아무렇지 않게, 저고리 사이에서 키를 꺼내 잠금을 풀었다."

    nvl clear

    n "방 안으로 들어서자, 은은한 분홍색 벽지의 방이 나타났다."
    n "분홍, 보다는 흰색의 비중이 더 가깝다. 마치 연꽃 같다."
    n "침대 하나와 넓은 공간, 화장대, 등등. 영락없이 평범한 방이다."
    n "벽에는 구시대의 영화 포스터 같은 것이 붙어 있었다. 카사블랑카, 로마의 휴일, 멋진 인생, 사랑은 비를 타고..."
    n "최소 150년은 지난 영화들이다. 내가 평범한 C시의 주민이었다면 절대 몰랐을 작품들이다."
    n "전부 화이의 취향이다. 학교에서도 자주 언급했던 영화들."

    nvl clear
    n "창문 밖으로는 C시의 풍경이 보였다. 내 아파트에 비하면 훨씬 더 쾌적하다."
    n "혼잡한 광고들은 전혀 보이지 않고 반듯이 정리된 네온만 보인다."
    n "설사 기업의 홍보 문구가 보인다고 해도 굉장히 세련되었다."
    n "이곳에서 높이와 시선의 차이를 느낀다. 새삼스러웠다."
    nvl clear
    n "화이는 침대 근처로 가서, 잠시 허공을 바라보았다."
    n " 그 여자는 그녀의 앞에 서 있었다."
    n "나는 문 앞에 멀뚱히 서 있었고 그들은 나를 바라보았다."

    nvl clear
    nd "⋯⋯"
    n "우리는 잠시 동안 아무 말도 하지 않았다."
    n "보라색 원피스를 입은 여자는, 자신이 시종이라는 걸 과시하기라도 하는 것처럼 눈을 감고 있었다."
    n "화이는 나를- 계속해서 보고 있었다."
    n "나의 눈을 보고 있었다. 나 역시 그녀의 눈동자를 보았다."
    nvl clear

    nd "⋯⋯⋯⋯"
    n "무슨 말이라도 하고 싶었다."
    n "그녀에게 쏟아내고 싶은 감상이 많아서, 그만 섣불리 입을 열었다."
    nd "저기⋯."

    #트랜지션안넣으면사망함

    nvl clear

    n "-순간,"
    n "눈 앞에 칼날이 스쳐지나가는,"
    n "그 날 선 감각이 느껴졌다."

    nvl clear
    n "동공 바로 앞에 날카로운 쇳덩어리가 있었다."
    n "반달 모양으로 둥글게 휘어져 있는데, 눈동자를 오른쪽으로 돌리니 그 모양을 짐작할 수 있었다."
    n "휘어진 칼날. 긴 손잡이. 사용자로부터 긴 리치."
    n "낫이다."
    nvl clear
    n "그리고 나는 짐작할 수 있었다."
    n "이건 필시 화이의 에스페로다."
    n "그녀의 가녀린 손 끝에 쥐어진 낫의 손잡이."
    n "곳곳마다 꽃으로 물들어 있었다, 고 해도 좋을 정도로 아름답다."
    n "칼날이 앞에 있는데도 그런 착각이 들었다. 그 정도로 그녀 앞에서는 사리분별이 되지 않는다."

    nvl clear
    nd "지금부터."
    nd "묻는 말에만 대답하도록 하세요."
    n "딱딱한 경어. 화이의 말투가 아니었다."
    n "나는 지금 그녀가 그녀 본연의 모습으로 말하고 있지 않음을, 깨달았다."
    nvl clear
    nd "하나. 당신은 대체 누구죠?"
    nd "⋯⋯물론 난 알고 있어. 네가 누군지, 조금은 알 것 같아."
    nd "그렇지만 이 질문에는 현명하게 답해야 할 거에요."
    nvl clear
    nd "둘. 여기에 뭐하러 왔죠?"
    nd "여기가 연화의 아이들 본부라는 건 누구나 다 아는 사실이고,"
    nd "예배 시간이라서 일반적인 사람은 들어올 수 없을텐데⋯"
    nd "게다가 그 모습."
    nd "⋯길게 말하진 않겠어요."

    nvl clear

    nd "마지막으로 셋."
    nvl clear

    n "그 대목에서- 그녀의 눈동자는 조금씩 떨려오기 시작했다."
    n "나는 그 변화를 눈치챌 수 있었다.-애초에, 화이는 거짓말을 하지 못한다."
    n "그 때, 아주 많이 연습한 '그 말'을 제외하고선 항상 그랬다."
    n "거짓말을 할 때마다 입이 미세하게 떨린다."
    n "그리고 눈동자가 갈 곳을 잃는다."
    n "지금 그녀는 그 모습을 하고 있었다."

    nvl clear

    nd "왜⋯ 지금 온 거죠?"

    nvl clear
    n "정적이---감돈다."
    n "이 방은 우리가 지내보지 못한, 외로움의 시간으로 이루어져 있다."
    n "나는 그녀를 보고서 동정하지 않으려고 했다."
    n "화이가 불쌍하다고 생각하지 않았으면 했다."
    n "그녀는 지금 너무나도 올곧게 서 있다."
    n "그 시간을 어떤 마음으로 보내왔을지-"
    n "나로서는 감히 짐작조차도 할 수 없었다."

    nvl clear

    menu:
        "⋯지금이라도 오고 싶었어. 널 구하러 왔어.":
            nd "⋯지금이라도 와야 할 것 같았어."
            nd "아무리 생각해도 네가 이곳을 좋아하지는 않는 것 같았으니까."
            nd "널 구하러 왔어, 화이."
            nvl clear
            nd "⋯.!"
            nd "⋯⋯⋯⋯."
            nvl clear
            n "그녀는 아무 말도 하지 않았다."
            n "순간 내 말에 어떤 감정을 느꼈는지, 경계를 풀고 당황함을 감추려는 것밖에는."
            n "다른 건 아무것도 하지 않았다."
            n "그것만으로 알 수 있었다."
            nd "우리는 같은 것을 생각하고 있었다고----"

        "아무 말도 하지 않는다":
            nd "⋯⋯⋯⋯"
            n "나는 아무 말도 하지 않았다."
            n "그녀 앞에 더 빨리 나타나지 않았음에 사죄하는 시간이었다."
            n "화이의 시선이 느껴졌다."
            n "무언가를 말하라는, 어떤 원망 같은 게 느껴지기도 했다."


    nvl clear

    nd "⋯⋯⋯정말이야, 루이? 내가 알고 있는 그 사람이 맞아?"

    n "나는 화이의 그 말에, 조금 웃었다."
    n "점점 낯설었던 그녀의 모습에서, 내가 알고 있는 모습으로 돌아오고 있었다."
    n "사소한 것에도 잘 놀라고 감정 변화가 큰."
    n "화이다."

    nvl clear

    nd "꽤나 영화 히로인 같은 소리를 하네."
    nd " 그렇지만⋯! 그런 말이 나올 수밖에 없잖아⋯!"
    nd "⋯하하."
    n "나는 실소를 흘렸다."

    nvl clear

    nd "네가 알고 있는 루이가 맞아."
    nd "⋯24세, 현재 가디언즈 소속의 수사관."
    nd "그리고 네가 있는 연화의 아이들을 조사 중이지."
    nvl clear
    nd "잠깐, 루이. 수사관이 됐다고?"
    nd "응."
    n "그녀는 한층 더 놀라며 기쁜 표정을 보였다."
    nd "약속한 거, 지켰어. 그러니까 내가 한 약속도 지켜줄 수 있겠어?"
    n "조금 마음이 조급해져서, 그렇게 말했다."

    nvl clear
    nd "그러니까, 화이."
    nd "더는 여기 있을 필요가-"

    nvl clear

    ich "⋯저⋯. 실례가 안된다면.."
    n2 "문득 낯선 목소리가 들려왔다."
    n2 "구름 위를 사뿐사뿐 걷는 것처럼 몽환적인 목소리. 그렇지만 어느 정도는 강단이 있다."
    n2 "단순히 헤매는 톤만은 아니었다."
    ich "두 분은 어떤 사이..이신가요..?"

    nvl clear

    n "나는 목소리가 들려온 쪽을 보았다."
    n "연보라색 꽃무늬 원피스, 작은 키."
    n "화이와 비슷하지만 전혀 다르다. "
    n "똑같이 '인간이 아닌 상태'- 스틱맨이지만,"
    n "검은색 눈동자나 분위기 같은 것이 차별점이다."

    nvl clear

    nd "⋯화이 언니가 특별하게 여기는 분이시라면 저도 경계하진 않을 게요."
    nd "언니⋯ 이 사람은 누구에요?"
    nvl clear

    n "나는 화이와 눈이 마주쳤다."
    n "서로 추억을 나눌 시간도 없이 새로운 사람과 인사라니."
    n "그리고 실수, 를 조금 한 것일지도 모르겠다."
    n "이 사람은 연화의 아이들 소속의 사람일텐데⋯"
    n "화이 외의 사람에게 '구출'이라는 단어를 흘린 것부터가 실수였다."

    h "루이야. 내 학교 다닐 때의 친구."
    l "⋯그 정도로만 정리되는 거야?"
    h "어쩔 수 없잖아. 달리 우리 관계를 설명할 말도 없고⋯"
    n2 "화이는 그렇게 말하고서 상황을 설명하기 시작했다."

    h "루이, 이쪽은⋯. 이채라고 해."
    h "나랑 굉장히 오래 알던 사이야."
    h "똑같이 '연화'님을 믿고 있지만, 오해는 하지 않아줬으면 해."
    h "나를 많이 도와주고 지지해준 애니까."
    h "우리보다 한 살 동생이야!"
    h "이채, 이쪽은 루이."
    h "역시 나랑 굉장히 오래된 친구고⋯. ⋯지금은 가디언즈의 경찰이라고?"
    l "응."
    l "정확히는 '수사관'이라고 하는 현장직이야."
    l "도시를 직접 누비면서 범죄자들이랑 싸워."
    l "해커들이랑은 다르지."

    n2 "이채, 라고 하는 사람은 나를 계속해서 보고 있었다."
    n2 "눈매가 동그랗기 때문에 겉으로 보기에는 전혀 위험해보이지 않는다."
    n2 "그렇지만 경계 태세는 걷히지 않았다. 살갑게 대하고 싶어도- 이래서야 친해질 순 없잖아."

    h "둘이 친하게 지내면 좋겠네!"
    n "화이가 그렇게 말하자, 그제야 그녀는 경계를 풀었다."
    ich "이채⋯라고 해요."
    ich "만나서 반가워요⋯."
    ich "⋯."
    ich "언니한테 나쁜 짓 하면 화낼 거예요."
    ich "그리고.. 잘 부탁해요."
    n2 "그녀는 그렇게 말하고서, 조금 웃어보였다."
    n2 "자연스러운 미소다. "
    l "아, 응. 잘 부탁해."
    l "화이랑은 동갑이지만⋯. 편하게 불러."
    l "굳이 오빠니 그런 호칭 쓸 필요도 없어."
    ich "⋯네."
    l "(⋯전혀 염두도 안한 것 같네.)"
    l "(부끄럽게 시리.)"
    ich "⋯그러면 언니, 이제⋯"
    ich "아예 가버리시게요?"
    nvl clear
    n "이채가 그렇게 말하자 긴장하는 분위기가 감돌기 시작했다."
    n "나만 그렇게 느끼는 걸지도 모르겠지만."
    n "그래, 이렇게 될 것이라고 예상을 못했던 건 아니다."
    n "그렇지만 현실로 다가오니 실제보다, 무겁다."

    nvl clear
    n "이채의 말에서 무게가 느껴졌다."
    n "그녀는 이미 이곳에서 중요한 존재라도 되는 걸까."
    n "물론 그들의 입장에서는 그렇겠지."
    n "그걸 증명하기라도 하는 것처, 화이는 허공을 바라보고 있었다."
    n "깊게 사색하는 학자처럼⋯"

    nvl clear

    h "⋯그것까지는 아직 몰라."
    h "하지만 돌파구가 생겼다면⋯ ⋯.빠져나가지 않을 이유는 없겠지?"
    n "그녀는 나를 보며 웃었다."
    n "나만 기다리고 있었던 건가, 하는 생각이 드는 건 어쩔 수 없나보다."
    n "하지만 실상 그렇지만은 않겠지."

    nvl clear

    l "화이."
    l "⋯그러니까 넌, 연화님이 아닌 거잖아."
    l "살아있는 신 따위가 아니지?"
    l "그렇다면 더 있을 이유가 어디 있어."
    l "같이 도망치자. 여기서 꺼내줄 게."

    h "그게⋯"
    h "복잡한 사정이 얽혀 있어, 루이."
    h "우리는.. '연화의 아이들'은 단순한 사이비 종교가 아니야."
    h "간단하게 설명할 수 없는 이해 관계가 얽혀 있어."
    h "너도- 알고 있는 거 아니야? 그 모습이면.."
    h "마음이 힘이 되는 능력- 에스페로(Espero)를⋯?"

    n2 "화이는 그렇게 말하고서 이채를 보았다."

    ich "화이 언니는 혼자 도망치고 싶어하지 않아요."
    ich "당신이, 흑기사건 구원자건 뭐건⋯."
    ich "맹목적으로 군다면,"
    ich "그렇게 쉽게 되진 않을 거예요."

    n "나는 이채의 말을 듣고 조금 화가 났다."
    n "이제 거의 다 된 계획인데 누가 재를 뿌린 것 같은 기분이 들었다."
    n "그냥 여기서 화이를 데려 나가면 안되는 건가?"
    n "그녀를 지키는 건 가디언즈던, 아니면 나 혼자서든 할 수 있는데-"
    n "왜 안 된다는 거야?"

    nd "그 교주 같은 녀석 때문에 그래? 란티모라고 했었나?"
    nd "그런 녀석은 그냥 해치우면 되는 거 아니야?"
    nd "혼자서 되지 않는다면 도와줄 게."
    nd "나도 네가 쓰는, 그 '에스페로'라는 힘을 가지고 있어! 그러니까-"

    nvl clear

    nd "바보 같은 소리 하지마, 루이!"
    n "화이가 그렇게 말했다."
    n "화이가, 그렇게 외쳤다."
    n "나는 거기서 어떤 종류의 절망감을 느꼈다."
    n "왜 지금 그녀를 구할 수 없는지."
    n "이해할 수가 없었다."

    nvl clear
    nd "나는 있지, 동화 속에 나오는 공주님 같은 게 아니야."
    nd "네가 좋다고 해서 내가 이곳에서 빠져나갈 수 있는 게 아니란 말이야."
    nd "⋯⋯."

    nvl clear
    n "화이는 그 말을 한 뒤, 괜히 한 말이었다 싶었는지 표정을 바꾸었다."
    n "강단 있던 표정이 금방 누그러졌다."
    n "여전히 감정적인 모습이었다."
    nd "미안, 괜히 화를 내 버렸네⋯"

    menu:
        "아무 말도 하지 않는다":
            nd "⋯"
            n "화이는 나를 보았다."
            n "곧 다시, 미소 짓는 표정으로 바꾸었다."
            nd "옛날처럼 꼭 이럴 때는 아무 말도 안한단 말이야, 루이."

        "괜찮아, 이해해.":
            nd "괜찮아, 이해해."
            nd "오히려 내가 미안해. 이기적으로 굴었네."
            n "내가 그렇게 말하자, 화이는 안심했다는 듯이 웃어보였다."



    nd "..내가 지금 널 따라갈 수 없는 이유는 여러 개가 있지만, 우선."
    nd "란티모가 계획을 세우고 있다는 것만 말해줄 게."
    n "화이가 그렇게 말하자 나는 호기심이 들었다."
    nd "계획?"

    nvl clear

    nd "란티모는 지금 계속해서 '빛의 도래'를 벌여서, 에스페란토들을 만들어서 신도들을 늘리려 하고 있어."
    nd "내가 극구 반대해도 이제는 소용이 없어."
    nd "초대 '연화'랑은 다르게 나는 발언권이 그렇게 많진 않거든⋯"
    nd "그걸 막을 사람이 필요했어."

    nvl clear

    nd "그리고 루이, 네가 지금 여기에 나타난 거야."
    nd "이상하게 생각할 수도 있을 거야."
    nd "내가 널 이용하는 거라고 생각하는 것도 당연해."
    nd "그렇지만⋯"

    nvl clear

    nd "나에게는 지금 네가 필요해."
    nd "⋯도와줄 수 있어?"

    menu:
        "당연하지":
            nd "⋯물론."
            nd "무슨 일이든지 말만 해. 뭐든 해줄 게."
            jump hwai

        "가디언즈 사람도 있고, 돌아가서 이야기를 해 봐야한다":
            nd "⋯무리야."
            nd "지금 나도, 혼자 행동할 수 있는 신분이 아니야."
            nd "너를 구하러 온 건 맞아."
            nd "하지만 난 결국 연화의 아이들 전체를 조사하러 온 수사관이야."
            nd "네 편을 들어가면서 동료들을 배신할 순 없어."
            nvl clear
            nd "⋯그래?"
            nd "⋯. ⋯⋯알았어."
            n "화이는 그렇게 말하고서, 조금 실망한 표정을 지었다."
            nd "... ...내가 꿈을 꾸고 있었나봐."
            nd "그렇게 오랜 시간이 지났는데, 여전히 네가 나를⋯"
            nd "무조건 따를 이유는 없지."
            nvl clear
            n "씁쓸하지만 그게 현실이었다."
            n "이제 나는 혼자가 아니다."
            n "아문도 있고, 아카리나 한, 케인 같은 가디언즈 동료들이 있다."
            n "그러니⋯ 지금 당장 합류하는 건 무리다."
            jump amun

            nvl clear


label amun:
    n "여기에 아문 루트 입력"
    n "플레이해주셔서 감사합니다."
    return

label hwai:
    h "⋯⋯⋯!"
    n2 "화이는 놀란 눈으로 나를 쳐다보았다."
    n2 "기대를 별로 하지 않은 것인지, 감정의 편차가 제법 크다. 나는 실소를 흘렸다."
    l "왜 그래? 안 그럴 것 같았어?"
    h "아니, 그야⋯⋯⋯."
    h "내가 너랑 친했다고 해서, 네가 모든 말을 다 들어줄 의무도 없고⋯⋯."
    h "⋯⋯⋯내 특이한 점도 있고."
    h "솔직히⋯⋯⋯ 거절당할 거라고 생각했어."
    n2 "하지만 그렇지 않다."
    n2 "지금 이곳에 온 건 다 이유가 있었다."
    l "(⋯⋯화이도 여전히 같은 마음일까?)"
    n2 "이채는 우리 둘을 잠시 번갈아 보았다."
    n2 "간단한 소개는 했다지만 그녀는 우리를 어색해하는 것 같았다. 그렇지만 아까처럼 당돌하게 이야기하지도 못했다."
    n2 "화이는 이채를 보더니, 미안하다는 표정을 지으며 사정하기 시작했다."
    h "저, 미안해, 이채야! 영문 모를 이야기를 많이 했지?"
    ich "괜찮아요⋯! 전 괜찮으니까⋯."
    ich "화이 언니가 하고 싶은대로 하면, 전 그걸로 좋아요!"


    n "플레이해주셔서 감사합니다."
    return



 #씬전환

    #여

    return
