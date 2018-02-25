from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader

class TouchInput(FloatLayout):
	def onTouchDown(self, soundFileName):
		soundFileName.play()

#sourceSounds/Clap2.wav


class drumPad(App):
	eight081 = SoundLoader.load("sourceSounds/808-1.wav")
	eight082 = SoundLoader.load("sourceSounds/808-2.wav")
	clap1 = SoundLoader.load("sourceSounds/Clap1.wav")
	clap2 = SoundLoader.load("sourceSounds/Clap2.wav")
	clap3 = SoundLoader.load("sourceSounds/Clap3.wav")
	clap4 = SoundLoader.load("sourceSounds/Clap4.wav")
	hat1 = SoundLoader.load("sourceSounds/Hat1.wav")
	hat2 = SoundLoader.load("sourceSounds/Hat2.wav")
	kick1 = SoundLoader.load("sourceSounds/Kick1.wav")
	kick2 = SoundLoader.load("sourceSounds/Kick2.wav")
	kick3 = SoundLoader.load("sourceSounds/Kick3.wav")
	kick4 = SoundLoader.load("sourceSounds/Kick4.wav")
	snare1 = SoundLoader.load("sourceSounds/Snare1.wav")
	snare2 = SoundLoader.load("sourceSounds/Snare2.wav")
	snare3 = SoundLoader.load("sourceSounds/Snare3.wav")
	snare4 = SoundLoader.load("sourceSounds/Snare4.wav")

	def build(self):
		return TouchInput()


if __name__ == "__main__":
    drumPad().run()
