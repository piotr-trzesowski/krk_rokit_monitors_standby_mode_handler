import numpy as np
import sounddevice as sd
import time


class KRKMonitorStandbyModeHandler:

    @staticmethod
    def generate_and_play_wave(frequency=60, duration=5, amplitude=0.05, sample_rate=44100):
        """
        Generate a low-frequency sine wave and play it.
        """
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)
        sd.play(sine_wave, samplerate=sample_rate)
        sd.wait()  # Wait until the sound is done playing

    def keep_monitors_active(self, interval_minutes=10):
        """
        Periodically play a low-frequency sound to keep KRK monitors active.
        """
        while True:
            print("Generating and playing sound to prevent standby...")
            self.generate_and_play_wave()
            print(f"Waiting for {interval_minutes} minutes before the next signal...")
            time.sleep(interval_minutes * 60)  # Convert minutes to seconds


if __name__ == "__main__":
    x = KRKMonitorStandbyModeHandler()
    x.keep_monitors_active()
