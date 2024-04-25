import pvporcupine
from pvrecorder import PvRecorder

KEYWORD_FILE_PATH = './model-pi/jarvis_en_raspberry-pi_v3_0_0.ppn'

porcupine = pvporcupine.create(
    access_key="u/kod4bBbp87SvR+HnfTE8jalPhs9pO6BKHgURpX0hcZv09roVGPZQ==", keyword_paths=[f'{KEYWORD_FILE_PATH}'])

recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)


def wake_word(function):
    try:
        recorder.start()
        while True:
            pcm = recorder.read()
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                function()
    except KeyboardInterrupt:
        recorder.stop()
    finally:
        porcupine.delete()
        recorder.delete()
