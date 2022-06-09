import gtts as gt
import os

TamilText = "இந்திய அரசியலமைப்புச் சட்டத்தின் 226வது பிரிவின் கீழ் தாக்கல் செய்யப்பட்ட ரிட் மனு,"
tts = gt.gTTS(text=TamilText, lang='ta')
tts.save("Tamil-Audio.mp3")
os.system("Tamil-Audio.mp3")