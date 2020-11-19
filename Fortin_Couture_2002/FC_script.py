#!/usr/bin/env python
# coding: utf-8

from psychopy import visual,core,event,gui
import random as rd
import pandas as pd

myDlg = gui.Dlg(title="KJ_PsyTime")
myDlg.addText('Subject info')
myDlg.addField('ID:')
myDlg.addField('Sex:', choices = ["m","f"])
myDlg.addField('Age:')
meta = myDlg.show()

if myDlg.OK:
    print("Proseed")
else:
    print('user cancelled')
    core.quit()

win = visual.Window(fullscr=True)
text = visual.TextStim(win);
text2 = visual.TextStim(win,pos=(-0.6,-0.8))
text3 = visual.TextStim(win,pos=(0.6,-0.8))
img = visual.ImageStim(win,image="mozaic.jpg",size=0.15)
event.Mouse(visible=False)

Condition = ["Control","Moderate","Difficult"]
plus = visual.TextStim(win,"+")
ISI = core.StaticPeriod(screenHz=60)

Ntrial = 10;Nserial = 8;
cnd = [];trial = [];stimli = [];btn = [];
ObjTime = [];SubTime = [];trial4TE = [];cnd4TE = []

inst = [["""実験者から説明を受けたら，実験を開始してください．
            <スペースキーを押して実験を開始>"""],
            ["""今から，１つ目の課題を行います．
            課題は複数の試行から成り立ちます．
            それぞれの試行は２つのパートに分かれます．""",
             """【パート１】
            ０から９までの整数が，モザイクを挟み次々と呈示されていきます．
            この課題では，これらが呈示される様子を見ておいてください
            （反応する必要はありません）　　　　　　　　　　　　""",
            """【パート２】
            Fキーを押し，パート１全体の所要時間と感覚的に
            同じ長さの時間が経ったと思ったら，Jキーを押してください．
            Jキーを押すまでの間には，#が表示されます．
            所要時間とは，パート１で'Go!'と表示された直後から
            'Wait...'と表示される直前までの時間です""",
            """これらを1試行として，全部で15試行行います．
            各試行のパート１の時間の流れには気を配り，
            パート２での所要時間の再現がなるべく正確に
            なるように頑張ってください．　　　　　　　"""],
            ["""今から，２つ目の課題を行います．
            課題は複数の試行から成り立ちます．
            それぞれの試行は２つのパートに分かれます．""",
            """【パート１】
            ０から９までの整数が，モザイクを挟み次々と呈示されていきます．
            ここでは，呈示される整数に基づく判断を行います，""",
             """<「３」以外が呈示された時>
            直後のモザイクが呈示されている間にスペースキーを1度押してください．
            <「３」が呈示された時>　　　　　　　　　　　　　　　　　　
            何も押さないでください．　　　　　　　　　　　　　　　　　　""",
             """【パート２】
            Fキーを押し，パート１全体の所要時間と感覚的に
            同じ長さの時間が経ったと思ったら，Jキーを押してください．
            Jキーを押すまでの間には，#が表示されます．
            所要時間とは，パート１で'Go!'と表示された直後から
            'Wait...'と表示される直前までの時間です""",
            """これらを1試行として，全部で15試行行います．
            各試行のパート１の時間の流れには気を配り，
            パート２での所要時間の再現がなるべく正確に
            なるように頑張ってください．　　　　　　　　"""],
            ["""今から，３つ目の課題を行います．
            課題は複数の試行から成り立ちます．
            それぞれの試行は２つのパートに分かれます．""",
            """【パート１】
            ０から９までの整数が，モザイクを挟み次々と呈示されていきます．
            この課題のルールは少しトリッキーです．
            ここでは"１つ前に呈示された整数"に基づく判断を行います．""",
            """<１つ前に「３」以外が呈示された時>
            直後のモザイクが呈示されている間にスペースキーを1度押してください．
            <１つ前に「３」が呈示された時>　　　　　　　　　　　　　　　　　
            今の整数の直後のモザイクが呈示されている間，何も押さないでください．
            ※１つ目の整数には反応する必要はありません　　　　　　　　　　　　""",
            """【パート２】
            Fキーを押し，パート１全体の所要時間と感覚的に
            同じ長さの時間が経ったと思ったら，Jキーを押してください．
            Jキーを押すまでの間には，#が表示されます．
            所要時間とは，パート１で'Go!'と表示された直後から
            'Wait...'と表示される直前までの時間です""",
            """これらを1試行として，全部で15試行行います．
            各試行のパート１の時間の流れには気を配り，
            パート２での所要時間の再現がなるべく正確に
            なるように頑張ってください．　　　　　　"""]]

text.setText(inst[0][0]);text.draw();win.flip()
event.waitKeys(keyList=["space"])

index = 0
for cond in Condition:

    index=index+1

    k=0;flag=0;

    while flag<0.5:

        if k>0 and k<len(inst[index])-1:
            text.setText(inst[index][k]);text.draw();
            text2.setText("Fキーで前へ戻る")
            text3.setText("Jキーで次に進む")
            text2.draw();text3.draw();win.flip()

            proseed = event.waitKeys(keyList=["f","j"])
            k = k+1 if proseed==["j"] else k-1
        elif k==0:
            text.setText(inst[index][k]);text.draw();
            text3.setText("Jキーで次に進む")
            text3.draw();win.flip()

            proseed = event.waitKeys(keyList=["j"])
            k = k+1
        elif k==len(inst[index])-1:
            text.setText(inst[index][k]);text.draw();
            text2.setText("Fキーで前に戻る")
            text3.setText("スペースキーで説明を終了")
            text2.draw();text3.draw();win.flip()

            proseed = event.waitKeys(keyList=["f","space"])
            if proseed==["f"]:
                k = k-1
            elif proseed==["space"]:
                break

    text.setText("スペースを押すと練習に入ります\n練習は5試行分行います");text.draw();win.flip()
    event.waitKeys(keyList=["space"])

    for tri in range(1,5+1):
        numlist = [rd.randint(0,9) for i in range(Nserial+1)]
        numlist = [(rd.choice([0,1,2,5,6,7,8,9]) if i==3 else i) for i in numlist]
        for i in rd.sample(range(1,9),rd.choice([1,2])):
            numlist[i] = 3

        plus.draw();win.flip()
        ISI.start(1);ISI.complete()

        text.setText("""【練習・パート１】
                        準備ができたらスペースを押し，試行を始めてください""");text.draw();win.flip()
        event.waitKeys(keyList=["space"])

        text.setText("Ready?");text.draw();win.flip()
        ISI.start(1);ISI.complete()

        text.setText("Go!");text.draw();win.flip()
        ISI.start(0.3);ISI.complete()

        for i in range(len(numlist)):
            ISI.start(0.3); #0.3
            text.setText(str(numlist[i]));
            text.draw();win.flip()
            ISI.complete()

            ISI.start(0.9) #0.9
            img.draw();win.flip()
            ISI.complete()

        #ここに時計状のアレをアレする

        text.setText("Wait...");text.draw();win.flip()
        ISI.start(2);ISI.complete()

        text.setText("""【練習・パート２】
                        準備ができたらFキーを押し，パート１の所要時間と
                        同じ長さの時間が経ったらJキーを押してください．""");
        text.draw();win.flip()

        event.waitKeys(keyList=["f"])
        text.setText("#");text.draw();win.flip()
        event.waitKeys(keyList=["j"])
#本番
    text.setText("""練習試行が終わったら，外で待機している
                    TAに声をかけ，ルールの確認を行ってください""");text.draw();
    win.flip()
    event.waitKeys(keyList=["a"])
    text.setText("スペースを押すと本番に入ります");text.draw();win.flip()
    event.waitKeys(keyList=["space"])

    for tri in range(1,Ntrial+1):
        numlist = [rd.randint(0,9) for i in range(Nserial+1)]
        numlist = [(rd.choice([0,1,2,5,6,7,8,9]) if i==3 else i) for i in numlist]
        for i in rd.sample(range(1,9),rd.choice([1,2])):
            numlist[i] = 3

        plus.draw();win.flip()
        ISI.start(1);ISI.complete()

        text.setText("""【パート１】
                        準備ができたらスペースを押し，試行を始めてください""");text.draw();win.flip()
        event.waitKeys(keyList=["space"])
        timer = core.MonotonicClock();

        text.setText("Ready?");text.draw();win.flip()
        ISI.start(1);ISI.complete()

        text.setText("Go!");text.draw();win.flip()
        ISI.start(0.3);ISI.complete()

        for i in range(len(numlist)):
            ISI.start(0.3); #0.3
            text.setText(str(numlist[i]));
            text.draw();win.flip()
            ISI.complete()

            ISI.start(0.9) #0.9
            img.draw();win.flip()#ここの処理速度より早く押してしまうと空判定される
            rsp = event.getKeys(keyList=["space"])
            ISI.complete()

            if cond !="Control" and i>=2:
                trial.append(tri);
                stm = numlist[i] if cond == "Moderate" else numlist[i-1]
                cnd.append(cond);

                if rsp == ["space"] and stm != 3:
                    btn.append(1);stimli.append(0);

                elif rsp == ["space"] and stm == 3:
                    btn.append(1);stimli.append(1);

                elif rsp == [] and stm != 3:
                    btn.append(0);stimli.append(0);

                elif rsp == [] and stm == 3:
                    btn.append(0);stimli.append(1);


        ObjTime.append(timer.getTime())
        trial4TE.append(tri);cnd4TE.append(cond)

        #ここに時計状のアレをアレする

        text.setText("Wait...");text.draw();win.flip()
        ISI.start(2);ISI.complete()

        text.setText("""【パート２】
                        準備ができたらFキーを押し，パート１の所要時間と
                        同じ長さの時間が経ったらJキーを押してください．""");
        text.draw();
        win.flip()

        event.waitKeys(keyList=["f"])

        timer = core.MonotonicClock()
        text.setText("#");text.draw();win.flip()
        event.waitKeys(keyList=["j"])
        SubTime.append(timer.getTime())

    plus.draw();win.flip()
    ISI.start(1.5);ISI.complete()

plus.setText("""実験はこれで終了です．お疲れさまでした！
                (スペースキーを押して画面を終了してください)""")
plus.draw();win.flip()
event.waitKeys(keyList=["space"])

record_Attention = pd.DataFrame({"subid":[meta[0] for i in range(len(cnd))],
                                 "sex":[meta[1] for i in range(len(cnd))],
                                 "age":[meta[2] for i in range(len(cnd))],
                                 "condition":cnd,
                                 "trial":trial,
                                 "signal":stimli,
                                 "response":btn
                                });#速い反応時間はだめ

record_Estimation = pd.DataFrame({"subid":[meta[0] for i in range(len(trial4TE))],
                                  "sex":[meta[1] for i in range(len(trial4TE))],
                                  "age":[meta[2] for i in range(len(trial4TE))],
                                  "Condition":cnd4TE,
                                  "Trial":trial4TE,
                                  "ObjTime":ObjTime,
                                  "SubTime":SubTime
                                });
win.close();

SART_name =  'SART_{}.csv';DE_name = 'DE_{}.csv'

#print(record_Attention)
#print(record_Estimation)

record_Attention.to_csv(SART_name.format(meta[0]),index=False,encoding="shift_jis")
record_Estimation.to_csv(DE_name.format(meta[0]),index=False,encoding="shift_jis")

core.quit();
