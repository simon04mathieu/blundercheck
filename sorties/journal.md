## 2026-10-21 20:43 UTC · run 39672696817
### commandes/boucle_lasker.json
    OK /home/runner/work/blundercheck/blundercheck/sorties/boucle_lasker.mp4 {"video_s": 10.0}
### commandes/echantillons.json
ÉCHEC :
    ElevenLabs POST /voices/add/08cb726069be6a0fae454156fe8898ed6fc29841598070e2ebbb516a219efc8a/ecxPjiGTvAfpGEams6ec -> 401 : {"detail":{"type":"authentication_error","code":"unauthorized","message":"The API key you used is missing the permission voices_write to execute this operation.","status":"missing_permissions","request_id":"f527d5fad4e7c2caeeb6221b4cd1d413"}}
### commandes/perso_lasker.json
ÉCHEC :
    ElevenLabs POST /voices/add/08cb726069be6a0fae454156fe8898ed6fc29841598070e2ebbb516a219efc8a/ecxPjiGTvAfpGEams6ec -> 401 : {"detail":{"type":"authentication_error","code":"unauthorized","message":"The API key you used is missing the permission voices_write to execute this operation.","status":"missing_permissions","request_id":"02b5b6926e4b4deda730e25f620c6caa"}}
## 2026-10-21 21:09 UTC · run 39676346747
### commandes/coach_v_englund.json
ÉCHEC :
    Traceback (most recent call last):
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 119, in <module>
        res = {"echantillons": lambda c: (echantillons(c), {}), "perso": video_voix, "coach": video_voix, "boucle": boucle}[cmd["type"]](cmd)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 84, in video_voix
        mots = transcrire(wav)
               ^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 35, in transcrire
        segs, _ = m.transcribe(audio, language="fr", word_timestamps=True)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/transcribe.py", line 876, in transcribe
        audio = decode_audio(audio, sampling_rate=sampling_rate)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/audio.py", line 46, in decode_audio
        with av.open(input_file, mode="r", metadata_errors="ignore") as container:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "av/container/core.py", line 479, in av.container.core.open
    TypeError: open() got an unexpected keyword argument 'metadata_errors'
### commandes/coach_v_foiefrit.json
ÉCHEC :
    Traceback (most recent call last):
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 119, in <module>
        res = {"echantillons": lambda c: (echantillons(c), {}), "perso": video_voix, "coach": video_voix, "boucle": boucle}[cmd["type"]](cmd)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 84, in video_voix
        mots = transcrire(wav)
               ^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 35, in transcrire
        segs, _ = m.transcribe(audio, language="fr", word_timestamps=True)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/transcribe.py", line 876, in transcribe
        audio = decode_audio(audio, sampling_rate=sampling_rate)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/audio.py", line 46, in decode_audio
        with av.open(input_file, mode="r", metadata_errors="ignore") as container:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "av/container/core.py", line 479, in av.container.core.open
    TypeError: open() got an unexpected keyword argument 'metadata_errors'
### commandes/coach_v_halosar.json
ÉCHEC :
    Traceback (most recent call last):
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 119, in <module>
        res = {"echantillons": lambda c: (echantillons(c), {}), "perso": video_voix, "coach": video_voix, "boucle": boucle}[cmd["type"]](cmd)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 84, in video_voix
        mots = transcrire(wav)
               ^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 35, in transcrire
        segs, _ = m.transcribe(audio, language="fr", word_timestamps=True)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/transcribe.py", line 876, in transcribe
        audio = decode_audio(audio, sampling_rate=sampling_rate)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/audio.py", line 46, in decode_audio
        with av.open(input_file, mode="r", metadata_errors="ignore") as container:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "av/container/core.py", line 479, in av.container.core.open
    TypeError: open() got an unexpected keyword argument 'metadata_errors'
### commandes/coach_v_kieninger.json
ÉCHEC :
    Traceback (most recent call last):
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 119, in <module>
        res = {"echantillons": lambda c: (echantillons(c), {}), "perso": video_voix, "coach": video_voix, "boucle": boucle}[cmd["type"]](cmd)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 84, in video_voix
        mots = transcrire(wav)
               ^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 35, in transcrire
        segs, _ = m.transcribe(audio, language="fr", word_timestamps=True)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/transcribe.py", line 876, in transcribe
        audio = decode_audio(audio, sampling_rate=sampling_rate)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/audio.py", line 46, in decode_audio
        with av.open(input_file, mode="r", metadata_errors="ignore") as container:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "av/container/core.py", line 479, in av.container.core.open
    TypeError: open() got an unexpected keyword argument 'metadata_errors'
### commandes/coach_v_noe.json
ÉCHEC :
    Traceback (most recent call last):
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 119, in <module>
        res = {"echantillons": lambda c: (echantillons(c), {}), "perso": video_voix, "coach": video_voix, "boucle": boucle}[cmd["type"]](cmd)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 84, in video_voix
        mots = transcrire(wav)
               ^^^^^^^^^^^^^^^
      File "/home/runner/work/blundercheck/blundercheck/outils/fabrique.py", line 35, in transcrire
        segs, _ = m.transcribe(audio, language="fr", word_timestamps=True)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/transcribe.py", line 876, in transcribe
        audio = decode_audio(audio, sampling_rate=sampling_rate)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/faster_whisper/audio.py", line 46, in decode_audio
        with av.open(input_file, mode="r", metadata_errors="ignore") as container:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "av/container/core.py", line 479, in av.container.core.open
    TypeError: open() got an unexpected keyword argument 'metadata_errors'
### commandes/coach_v_siberien.json
    voix générée : 732 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_siberien.mp4 {"voix_brute_s": 56.0, "tempo": 1.076, "video_s": 52.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 115}
