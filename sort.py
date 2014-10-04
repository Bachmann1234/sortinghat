import os
import random
import wave
import time
import pyaudio

CHUNK = 1024

BASE_AUDIO_DIR = "audio"

WAIT_TIME = .25


def list_all_sound_files(subdir):
    """
    Get all the sound files from a subdir in the audio
    folder
    :param subdir:
        Subdir to list
    :return:
        all sound files in subdir
    """
    return [f for f in os.listdir(
        os.path.join(BASE_AUDIO_DIR, subdir)
    ) if f[-4:] == '.wav']


def get_full_path(subdir, audio_filename):
    """
    given an audio file and the subdir give a full path
    from the base sound dir
    :param audio_filename:
        string, filename
    :return:
        full path from audio dir
    """
    return os.path.join(
        BASE_AUDIO_DIR,
        subdir,
        audio_filename
    )


def get_random_wav_file(subdir):
    """
    Used to play a sound matching a category
    :param subdir:
        Which subdir to pull the file out of. Base dir is audio
    :return:
        A full path to the sound file chosen.
    """
    return get_full_path(
        subdir,
        random.choice(
            list_all_sound_files(subdir)
        )
    )


def play_sound(sound_file_path):
    """
    Play the sound at a given path
    :param sound_file_path:
        string path
    """
    with wave.open(sound_file_path, 'rb') as wf:
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(CHUNK)
        while data:
            stream.write(data)
            data = wf.readframes(CHUNK)
        stream.stop_stream()
        p.terminate()

if __name__ == '__main__':

    # Consider some stalling lines
    script = list_all_sound_files('stalling')
    random.shuffle(script)
    script = [get_full_path('stalling', f)
              for f in script
              if random.random() < .2]

    # Consider shouting I know!
    if random.random() < .5:
        script.append(get_random_wav_file('know'))

    # Pick a house
    script.append(get_random_wav_file('houses'))

    for sound in script:
        play_sound(sound)
        time.sleep(WAIT_TIME)
