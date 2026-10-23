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
### commandes/coach_v_stafford.json
    voix générée : 773 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_stafford.mp4 {"voix_brute_s": 60.0, "tempo": 1.154, "video_s": 52.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 132}
### commandes/coach_v_tarrasch.json
## 2026-10-21 21:21 UTC · run 39678015241
### commandes/v2_v_siberien.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_siberien.mp4 {"voix_brute_s": 56.0, "tempo": 1.072, "video_s": 55.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 115}
### commandes/v2_v_stafford.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_stafford.mp4 {"voix_brute_s": 60.0, "tempo": 1.146, "video_s": 55.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 149}
## 2026-10-21 21:25 UTC · run 39678398757
### commandes/coach_v_englund.json
    voix générée : 645 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_englund.mp4 {"voix_brute_s": 54.7, "tempo": 1.049, "video_s": 55.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 102}
### commandes/coach_v_foiefrit.json
    voix générée : 694 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_foiefrit.mp4 {"voix_brute_s": 51.6, "tempo": 1.0, "video_s": 54.6, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 111}
### commandes/coach_v_halosar.json
    voix générée : 636 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_halosar.mp4 {"voix_brute_s": 61.6, "tempo": 1.174, "video_s": 55.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 116}
### commandes/coach_v_kieninger.json
    voix générée : 616 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_kieninger.mp4 {"voix_brute_s": 51.5, "tempo": 1.0, "video_s": 54.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 94}
### commandes/coach_v_noe.json
    voix générée : 790 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_noe.mp4 {"voix_brute_s": 75.2, "tempo": 1.18, "video_s": 66.3, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 124}
### commandes/coach_v_tarrasch.json
    voix générée : 537 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_tarrasch.mp4 {"voix_brute_s": 40.8, "tempo": 1.0, "video_s": 43.8, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 93}
### commandes/coach_v_tennison.json
    voix générée : 587 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_tennison.mp4 {"voix_brute_s": 42.9, "tempo": 1.0, "video_s": 45.9, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 96}
### commandes/perso_lasker.json
    voix générée : 895 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/perso_lasker.mp4 {"voix_brute_s": 64.1, "tempo": 1.166, "video_s": 55.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 152}
## 2026-10-21 21:38 UTC · run 39679534038
### commandes/ab_v_siberien_hookB.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_siberien_hookB.mp4 {"voix_brute_s": 56.0, "tempo": 1.072, "video_s": 55.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 115}
## 2026-10-21 21:41 UTC · run 39680711782
### commandes/gaffe_demo.json
    OK /home/runner/work/blundercheck/blundercheck/sorties/gaffe_Jwt6l2NL.mp4 {"partie": "Jwt6l2NL", "coup": "25. Rxc1", "camp": "Blancs", "solution": ["Rxc1+", "Bf1", "Rxf1+"], "classement": 1976, "controle": {"meilleur": "Bf1", "eval_meilleur": 72, "eval_gaffe": -9995, "perte": 10067}, "video_s": 16.3}
## 2026-10-21 21:52 UTC · run 39682133461
### commandes/v3_v_siberien.json
    voix générée : 767 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/v_siberien_v3.mp4 {"voix_brute_s": 55.0, "tempo": 1.054, "video_s": 55.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 128}
## 2026-10-22 14:54 UTC · run 39798794701
### commandes/perso_legal.json
    voix générée : 742 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/perso_legal.mp4 {"voix_brute_s": 56.6, "tempo": 1.029, "video_s": 55.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 133}
### commandes/test_voix_cases.json
    version 4 : Version quatre. Tu joues fou sé quatre, puis pion eu quatre, et cavalier èf sept.
    version 5 : Version cinq. Tu joues le fou en C4, puis le pion en E4, et le cavalier en F7.
    OK /home/runner/work/blundercheck/blundercheck/sorties/echantillons {"versions": 5}
## 2026-10-22 14:58 UTC · run 39800012297
## 2026-10-22 23:04 UTC · run 39869295076
### commandes/perso_pigeon_jour_1.json
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    minutage : 18 phrases, 11 coups, 0 pauses
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_1.mp4 {"voix_brute_s": 39.6, "tempo": 1.0, "video_s": 40.1, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 99}
## 2026-10-22 23:08 UTC · run 39869696900
### commandes/perso_analyse_celebre_1.json
    voix générée : 416 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/analyse_celebre_1.mp4 {"voix_brute_s": 28.7, "tempo": 1.0, "video_s": 28.7, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 84, "minutage": "11 phrases, 2 coups, 0 pauses"}
### commandes/perso_pigeon_jour_2.json
    voix générée : 538 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_2.mp4 {"voix_brute_s": 36.5, "tempo": 1.0, "video_s": 37.2, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 102, "minutage": "18 phrases, 9 coups, 0 pauses"}
### commandes/perso_quiz_legal_2.json
    voix générée : 590 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_2.mp4 {"voix_brute_s": 44.8, "tempo": 1.0, "video_s": 47.7, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 112, "minutage": "20 phrases, 1 coups, 1 pauses"}
## 2026-10-23 23:15 UTC · run 40037729270
### commandes/perso_pigeon_jour_3.json
    voix générée : 297 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_3.mp4 {"voix_brute_s": 27.1, "tempo": 1.0, "video_s": 25.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 56, "minutage": "12 phrases, 5 coups, 0 pauses"}
## 2026-10-23 23:18 UTC · run 40038815178
### commandes/perso_pigeon_en_1.json
    voix générée : 282 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_1.mp4 {"voix_brute_s": 22.4, "tempo": 1.0, "video_s": 23.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 51, "minutage": "10 phrases, 9 coups, 0 pauses"}
