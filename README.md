# シュレーディンガーのねこふんじゃった
有名なシュレーディンガーのねこをふんづけちゃったらどうなるのか、という思考実験の結果、生まれた曲です。<br>
それぞれの音を鳴らすたびに判定(観測)が行われ、1/2 の確率で~~死ぬ~~鳴るしかけとなっています。<br>

### 実装について
ググった結果なんとなくpythonが楽そうだったので採用しました。<br>
```
Python 3.12.3
numpy 2.0.0
PyAudio 0.2.14
```

### 演奏を聴く
サンプルとして3つのmp3ファイルを格納しました。<br>
これらを聴き比べることで、演奏ごとにメロディが異なることがわかるでしょう。<br>
pyファイルを実行して演奏する場合は、上記に書いたとおりnumpy、PyAudioのインストールが必要となります。<br>

### 参考にしたサイト
Pythonで音楽 - PyAudioとNumPyで楽器を作ろう<br>
https://news.mynavi.jp/techplus/article/zeropython-55/<br>

音階の周波数<br>
https://tomari.org/main/java/oto.html<br>

### 使用した楽譜
ピアノ塾　『ねこふんじゃった』<br>
https://pianojuku.info/wp-content/uploads/2022/09/2b3dc83b35ddae17c30b3951060f947b.pdf<br>
