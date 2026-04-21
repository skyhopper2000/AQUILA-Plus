import numpy
import sounddevice

class Buzzer():

    def __init__(self,
                frequency : float, 
                duration : float,
                volume : float, 
                sample_rate=44100):
        
        self.frequency = frequency
        self.duration = duration
        self.volume = volume
        self.sample_rate = sample_rate

    def play_buzz(self):
        """
        Play a pure sine wave tone.

        :param frequency: Frequency in Hz (e.g., 440 = A4 note)
        :param duration: Duration in seconds
        :param volume: Volume (0.0 to 1.0)
        :param sample_rate: Samples per second
        """
        try:
            # Validate inputs
            if not (0 < self.frequency <= 20000):
                raise ValueError("Frequency must be between 1 and 20,000 Hz.")
            if not (0 < self.duration <= 10):
                raise ValueError("Duration must be between 0 and 10 seconds.")
            if not (0.0 <= self.volume <= 1.0):
                raise ValueError("Volume must be between 0.0 and 1.0.")

            # Generate time values
            t = numpy.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)

            # Generate sine wave
            waveform = self.volume * numpy.sin(2 * numpy.pi * self.frequency * t)

            # Play sound
            sounddevice.play(waveform, samplerate=self.sample_rate)

        except Exception as e:
            print(f"Error: {e}")