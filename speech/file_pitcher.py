
def file_pitcher(octave_modifier):
    from pydub import AudioSegment

    filename = 'speech/voiceline.wav'
    sound = AudioSegment.from_file(filename, format=filename[-3:])
    new_sample_rate = int(sound.frame_rate * (octave_modifier ** 1))
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    hipitch_sound = hipitch_sound.set_frame_rate(44100)
    hipitch_sound.export("speech/voiceline_pitched.wav", format="wav")