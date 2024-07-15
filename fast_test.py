import wave
from play_speech_content import play_speech


def concatenate_audio_wave(audio_clip_paths, output_path):
    """Concatenates several audio files into one audio file using Python's built-in wav module
    and save it to `output_path`. Note that extension (wav) must be added to `output_path`"""
    data = []
    for clip in audio_clip_paths:
        w = wave.open(clip, "rb")
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    output = wave.open(output_path, "wb")
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()


#concatenate_audio_wave("files/audio_books/audio.wav", "audio.wav")

play_speech("files/audio_books/")