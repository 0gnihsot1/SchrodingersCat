import pyaudio
import numpy as np
import asyncio
import random

# サンプリングレートを定義
RATE = 44100

# BPMや音長を定義
BPM = 100
L1 = (60 / BPM * 4)
L2,L4,L8,L16 = (L1/2,L1/4,L1/8,L1/16)

# ドレミ...の周波数を定義
C0,C0_,D0,D0_,E0,F0,F0_,G0,G0_,A0,A0_,B0 = (
        130.813, 138.591, 146.832, 155.563, 164.814,
        174.614, 184.997, 195.998, 207.652, 220.000,
        233.082, 246.942)
C1,C1_,D1,D1_,E1,F1,F1_,G1,G1_,A1,A1_,B1 = (
        261.626, 277.183, 293.665, 311.127, 329.628,
        349.228, 369.994, 391.995, 415.305, 440.000,
        466.164, 493.883)
C2,C2_,D2,D2_,E2,F2,F2_,G2,G2_,A2,A2_,B2 = (
        523.251, 554.365, 587.330, 622.254, 659.255,
        698.456, 739.989, 783.991, 830.609, 880.000,
        932.328, 987.767)
C3,C3_,D3,D3_,E3,F3,F3_,G3,G3_,A3,A3_,B3 = (
        1046.502, 1108.731, 1174.659, 1244.508, 1318.510,
        1396.913, 1479.978, 1567.982, 1661.219, 1760.000,
        1864.655, 1975.533)

# 音の数
aliveNote = 0
deadNote = 0

# サイン波を生成
def tone(freq, length, gain):
    slen = int(length * RATE)
    t = float(freq) * np.pi * 2 / RATE
    return np.sin(np.arange(slen) * t) * gain

# 和音を生成
def chord(freqs, length, gain):
    slen = int(length * RATE)
    chord_wave = np.zeros(slen)
    for freq in freqs:
        t = float(freq) * np.pi * 2 / RATE
        chord_wave += np.sin(np.arange(slen) * t) * gain / len(freqs)
    return chord_wave

# 50%の確率で音を鳴らす
def observe(sound):
    global aliveNote
    global deadNote
    if random.random() < 0.5:
      aliveNote += 1
      return sound
    else:
      deadNote += 1
      return 0

# 再生
def play_wave(stream, samples):
    stream.write(samples.astype(np.float32).tobytes())

# 出力用のストリームを開く
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=RATE,
                frames_per_buffer=1024,
                output=True)

def main():
  global aliveNote
  global deadNote
  
  # 『ねこふんじゃった』
  print("『シュレーディンガーのねこ○んじゃった』")
  
  # ねこ　ふんじゃった　ねこ　ふんじゃった
  play_wave(stream, tone(0, L4+L8, 1.0))
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # ねこ　ふんずけちゃったら　ひっかいた
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # ねこ　ひっかいた　ねこ　ひっかいた
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # ねこ　びっくりして　ひっかいた
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # わるいねこめ　つめをきれ
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(A2_), L8, 0.3))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(A2_), L8, 0.3))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(A2_), L8, 0.3))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(C3_), L8, 0.3))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D3_), L8, 0.3))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # やねをおりて　ひげをそれ
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(D3_), L8, 0.3))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(D3_), L8, 0.3))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(D3_), L8, 0.3))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(C3_), L8, 0.3))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(A2_), L8, 0.3))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # ねこ　にゃーご　にゃーご　ねこかぶり
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  play_wave(stream, tone(observe(F1), L8, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  play_wave(stream, tone(observe(G1), L8, 1.0))
  play_wave(stream, tone(observe(G1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # ねこ　なでごえ　あまえてる
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(G1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(G1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(G1_), L8, 1.0))
  play_wave(stream, tone(observe(G1), L8, 1.0))
  play_wave(stream, tone(observe(G1_), L8, 1.0))
  play_wave(stream, tone(observe(A1), L8, 1.0))
  play_wave(stream, tone(observe(A1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # ねこ　ごめんなさい　ねこ　ごめんなさい
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes1 = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes1, L8, 1.0))
  chord_notes1 = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes1, L8, 1.0))
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes1 = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # ねこ　おどかしちゃって　ごめんなさい
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # ねこ　よっといで　ねこ　よっといで
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # ねこ　かつぶしやるから　よっといで
  play_wave(stream, tone(observe(D2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(C1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(D1_), L8, 1.0))
  chord_notes = [observe(F2), observe(B1)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(F1_), L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  
  # 終奏
  play_wave(stream, tone(0, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_), observe(C1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(C2_), L16, 1.0))
  play_wave(stream, tone(observe(D2), L8, 1.0))
  play_wave(stream, tone(observe(C2_), L8, 1.0))
  play_wave(stream, tone(0, L8, 1.0))
  chord_notes = [observe(F2), observe(B1), observe(C1_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  chord_notes = [observe(F2_), observe(A1_), observe(F0_)]
  play_wave(stream, chord(chord_notes, L8, 1.0))
  play_wave(stream, tone(0, L8, 1.0))
  
  stream.close()
  p.terminate()
  
  print("鳴った音は "+str(aliveNote)+" 個")
  print("鳴らなかった音は "+str(deadNote)+" 個")
  probability = aliveNote / (aliveNote + deadNote) * 100
  print(f"およそ {probability:.2f} %の確率で音がなりました。")

if __name__ == "__main__":
    main()
