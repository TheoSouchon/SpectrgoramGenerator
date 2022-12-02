from opensoundscape.audio import Audio
from opensoundscape.spectrogram import Spectrogram

from pathlib import Path

# Settings
image_shape = (600, 600) #(height, width) not (width, height)
image_save_path = Path('./saved_spectrogram.png')

# Load audio file as Audio object
audio = Audio.from_file("okay-3.wav")

# Create Spectrogram object from Audio object
spectrogram = Spectrogram.from_audio(audio)

# Convert Spectrogram object to Python Imaging Library (PIL) Image
image = spectrogram.to_image(shape=image_shape,invert=True)

# Save image to file
image.save(image_save_path)