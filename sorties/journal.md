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
### commandes/perso_pigeon_en_2.json
    voix générée : 286 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_2.mp4 {"voix_brute_s": 24.5, "tempo": 1.0, "video_s": 25.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 53, "minutage": "12 phrases, 11 coups, 0 pauses"}
### commandes/perso_pigeon_jour_3_sansmusique.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_3.mp4 {"voix_brute_s": 27.1, "tempo": 1.0, "video_s": 25.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 56, "minutage": "12 phrases, 5 coups, 0 pauses"}
### commandes/perso_pigeon_jour_4.json
    voix générée : 290 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_4.mp4 {"voix_brute_s": 21.7, "tempo": 1.0, "video_s": 22.3, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 57, "minutage": "13 phrases, 13 coups, 0 pauses"}
### commandes/perso_quiz_legal_3_court.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_3_court.mp4 {"voix_brute_s": 34.4, "tempo": 1.0, "video_s": 37.5, "voice_id": "aucune", "musique": "fond1.mp3", "mots_transcrits": 40, "minutage": "9 phrases, 1 coups, 1 pauses"}
### commandes/perso_quiz_legal_3_long.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_3_long.mp4 {"voix_brute_s": 64.5, "tempo": 1.0, "video_s": 67.5, "voice_id": "aucune", "musique": "fond1.mp3", "mots_transcrits": 115, "minutage": "24 phrases, 3 coups, 1 pauses"}
## 2026-10-24 23:04 UTC · run 40141175568
### commandes/perso_pigeon_jour_5.json
    voix générée : 274 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_5.mp4 {"voix_brute_s": 20.9, "tempo": 1.0, "video_s": 20.9, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "fond1.mp3", "mots_transcrits": 57, "minutage": "10 phrases, 6 coups, 0 pauses"}
## 2026-10-24 23:07 UTC · run 40141386955
### commandes/perso_analyse_celebre_2_court.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/analyse_celebre_2_court.mp4 {"voix_brute_s": 35.5, "tempo": 1.0, "video_s": 35.5, "voice_id": "aucune", "musique": "fond1.mp3", "mots_transcrits": 39, "minutage": "11 phrases, 15 coups, 0 pauses"}
### commandes/perso_analyse_celebre_2_long.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/analyse_celebre_2_long.mp4 {"voix_brute_s": 64.4, "tempo": 1.0, "video_s": 64.5, "voice_id": "aucune", "musique": "fond1.mp3", "mots_transcrits": 116, "minutage": "32 phrases, 33 coups, 0 pauses"}
### commandes/perso_pigeon_en_3.json
    voix générée : 292 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_3.mp4 {"voix_brute_s": 22.5, "tempo": 1.0, "video_s": 23.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 53, "minutage": "10 phrases, 6 coups, 0 pauses"}
### commandes/perso_pigeon_en_4.json
    voix générée : 298 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_4.mp4 {"voix_brute_s": 21.0, "tempo": 1.0, "video_s": 21.6, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 52, "minutage": "10 phrases, 7 coups, 0 pauses"}
### commandes/perso_pigeon_jour_5_sansmusique.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_5.mp4 {"voix_brute_s": 20.9, "tempo": 1.0, "video_s": 21.4, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 57, "minutage": "10 phrases, 6 coups, 0 pauses"}
### commandes/perso_pigeon_jour_6.json
    voix générée : 281 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_6.mp4 {"voix_brute_s": 22.7, "tempo": 1.0, "video_s": 23.3, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 53, "minutage": "10 phrases, 7 coups, 0 pauses"}
## 2026-10-26 00:05 UTC · run 40247599012
### commandes/perso_quiz_legal_4_court.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_4_court.mp4 {"voix_brute_s": 36.5, "tempo": 1.0, "video_s": 39.5, "voice_id": "aucune", "musique": "fond1.mp3", "mots_transcrits": 51, "minutage": "12 phrases, 1 coups, 1 pauses"}
## 2026-10-26 00:17 UTC · run 40247817406
### commandes/perso_pigeon_en_5.json
    voix générée : 282 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_5.mp4 {"voix_brute_s": 20.8, "tempo": 1.0, "video_s": 21.5, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 50, "minutage": "8 phrases, 8 coups, 0 pauses"}
### commandes/perso_pigeon_en_6.json
    voix générée : 280 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_6.mp4 {"voix_brute_s": 22.0, "tempo": 1.0, "video_s": 22.6, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 50, "minutage": "10 phrases, 6 coups, 0 pauses"}
### commandes/perso_pigeon_jour_7.json
    voix générée : 315 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_7.mp4 {"voix_brute_s": 21.8, "tempo": 1.0, "video_s": 22.4, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 60, "minutage": "10 phrases, 8 coups, 0 pauses"}
### commandes/perso_pigeon_jour_8.json
    voix générée : 292 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_8.mp4 {"voix_brute_s": 23.9, "tempo": 1.0, "video_s": 24.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 55, "minutage": "10 phrases, 6 coups, 0 pauses"}
### commandes/perso_quiz_legal_4_long.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_4_long.mp4 {"voix_brute_s": 66.4, "tempo": 1.0, "video_s": 69.5, "voice_id": "aucune", "musique": "fond1.mp3", "mots_transcrits": 92, "minutage": "20 phrases, 1 coups, 1 pauses"}
## 2026-10-27 00:13 UTC · run 40423998653
### commandes/perso_pigeon_en_7.json
    voix générée : 292 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_7.mp4 {"voix_brute_s": 20.4, "tempo": 1.0, "video_s": 21.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 52, "minutage": "10 phrases, 9 coups, 0 pauses"}
## 2026-10-27 00:17 UTC · run 40425357818
### commandes/perso_analyse_celebre_3_court.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/analyse_celebre_3_court.mp4 {"voix_brute_s": 38.5, "tempo": 1.0, "video_s": 38.5, "voice_id": "aucune", "musique": "fond1.mp3", "mots_transcrits": 45, "minutage": "14 phrases, 17 coups, 0 pauses"}
### commandes/perso_analyse_celebre_3_long.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/analyse_celebre_3_long.mp4 {"voix_brute_s": 66.4, "tempo": 1.0, "video_s": 66.5, "voice_id": "aucune", "musique": "fond1.mp3", "mots_transcrits": 84, "minutage": "27 phrases, 49 coups, 0 pauses"}
### commandes/perso_pigeon_en_8.json
    voix générée : 268 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_8.mp4 {"voix_brute_s": 21.1, "tempo": 1.0, "video_s": 21.7, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 49, "minutage": "10 phrases, 8 coups, 0 pauses"}
### commandes/perso_pigeon_jour_10.json
    voix générée : 267 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_10.mp4 {"voix_brute_s": 24.0, "tempo": 1.0, "video_s": 22.7, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 50, "minutage": "10 phrases, 8 coups, 0 pauses"}
### commandes/perso_pigeon_jour_9.json
    voix générée : 282 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_9.mp4 {"voix_brute_s": 19.7, "tempo": 1.0, "video_s": 20.3, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 52, "minutage": "10 phrases, 9 coups, 0 pauses"}
## 2026-10-28 00:03 UTC · run 40606224095
### commandes/perso_pigeon_en_9.json
    voix générée : 255 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_9.mp4 {"voix_brute_s": 22.3, "tempo": 1.0, "video_s": 23.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 45, "minutage": "10 phrases, 4 coups, 0 pauses"}
## 2026-10-28 00:07 UTC · run 40606554508
### commandes/perso_pigeon_en_10.json
    voix générée : 294 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_10.mp4 {"voix_brute_s": 21.4, "tempo": 1.0, "video_s": 22.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 56, "minutage": "11 phrases, 5 coups, 0 pauses"}
### commandes/perso_pigeon_jour_11.json
    voix générée : 266 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_11.mp4 {"voix_brute_s": 22.0, "tempo": 1.0, "video_s": 22.8, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 50, "minutage": "10 phrases, 4 coups, 0 pauses"}
### commandes/perso_pigeon_jour_12.json
    voix générée : 291 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_12.mp4 {"voix_brute_s": 19.7, "tempo": 1.0, "video_s": 20.3, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 54, "minutage": "11 phrases, 5 coups, 0 pauses"}
### commandes/perso_quiz_legal_5_court.json
    voix générée : 266 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_5_court.mp4 {"voix_brute_s": 21.3, "tempo": 1.0, "video_s": 24.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 50, "minutage": "11 phrases, 1 coups, 1 pauses"}
### commandes/perso_quiz_legal_5_long.json
    voix générée : 722 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_5_long.mp4 {"voix_brute_s": 59.0, "tempo": 1.0, "video_s": 61.7, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 137, "minutage": "27 phrases, 1 coups, 1 pauses"}
## 2026-10-28 17:08 UTC · prof corrige · run 40732831561
### commandes/prof/essai_1.json
    
## 2026-10-29 00:04 UTC · run 40791525991
### commandes/perso_pigeon_en_11.json
    voix générée : 119 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_11.mp4 {"voix_brute_s": 9.8, "tempo": 1.0, "video_s": 10.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 19, "minutage": "6 phrases, 5 coups, 0 pauses"}
## 2026-10-29 00:07 UTC · run 40791799701
### commandes/perso_pigeon_en_12.json
    voix générée : 158 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_12.mp4 {"voix_brute_s": 12.1, "tempo": 1.0, "video_s": 12.8, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 27, "minutage": "8 phrases, 11 coups, 0 pauses"}
### commandes/perso_quiz_legal_6_en.json
    voix générée : 212 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_6_en.mp4 {"voix_brute_s": 18.2, "tempo": 1.0, "video_s": 20.8, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 38, "minutage": "9 phrases, 6 coups, 1 pauses"}
### commandes/perso_quiz_legal_6_fr.json
    voix générée : 179 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_6_fr.mp4 {"voix_brute_s": 13.3, "tempo": 1.0, "video_s": 16.1, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 41, "minutage": "8 phrases, 6 coups, 1 pauses"}
### commandes/perso_quiz_legal_7_en.json
    voix générée : 211 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_7_en.mp4 {"voix_brute_s": 17.2, "tempo": 1.0, "video_s": 19.9, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 37, "minutage": "8 phrases, 1 coups, 1 pauses"}
### commandes/perso_quiz_legal_7_fr.json
    voix générée : 184 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_7_fr.mp4 {"voix_brute_s": 16.4, "tempo": 1.0, "video_s": 18.6, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 49, "minutage": "9 phrases, 1 coups, 1 pauses"}
## 2026-10-29 11:14 UTC · run 40863448533
### commandes/prof_corrige_1.json
    voix générée : 374 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/prof_corrige_1.mp4 {"voix_brute_s": 26.1, "tempo": 1.0, "video_s": 26.3, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 65, "minutage": "5 phrases, 3 coups, 0 pauses", "ecrans": 3, "phrases_du_prof": 4}
## 2026-10-29 11:30 UTC · prof corrige · run 40865847881
### commandes/prof/partie_1.json
    OK : partie_1, 63 demi-coups, 3 moments, 36 commentaires du prof
## 2026-10-29 11:34 UTC · run 40866269896
### commandes/prof_partie_1.json
    voix générée : 86 caractères
    voix générée : 97 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/prof_partie_1.mp4 {"video_s": 57.5, "demi_coups": 63, "rythme_s": 0.39, "arrets": 3, "ecrans": 4, "voix": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune"}
## 2026-10-29 11:40 UTC · run 40867043136
### commandes/prof_partie_1.json
    voix réutilisée (0 crédit)
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/prof_partie_1.mp4 {"video_s": 57.5, "demi_coups": 63, "rythme_s": 0.39, "arrets": 3, "ecrans": 4, "voix": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune"}
## 2026-10-29 12:15 UTC · pièges · run 40871738753
### commandes/pieges/reserve_1.json
ÉCHEC :
      File "/home/runner/work/blundercheck/blundercheck/outils/coach2.py", line 7, in <module>
        import coach
      File "/home/runner/work/blundercheck/blundercheck/outils/coach.py", line 8, in <module>
        from PIL import Image, ImageDraw, ImageFilter
    ModuleNotFoundError: No module named 'PIL'
## 2026-10-29 12:17 UTC · pièges · run 40871952185
### commandes/pieges/reserve_2.json
ÉCHEC :
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/PIL/ImageFont.py", line 302, in __init__
        self.font = core.getfont(
                    ^^^^^^^^^^^^^
    OSError: cannot open resource
## 2026-10-29 12:19 UTC · pièges · run 40872209695
### commandes/pieges/reserve_3.json
    OK stock/pieges-candidats.md : 11 pièges, dont 11 jamais faits
## 2026-10-29 12:30 UTC · pièges · run 40873782548
### commandes/pieges/reserve_4.json
    OK stock/pieges-candidats.md : 11 pièges, dont 11 jamais faits
## 2026-10-29 12:40 UTC · pièges · run 40873832983
### commandes/pieges/reserve_5.json
    OK stock/pieges-candidats.md : 25 pièges, dont 25 jamais faits
## 2026-10-30 00:05 UTC · run 40977334977
### commandes/perso_pigeon_en_13.json
    voix générée : 262 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_13.mp4 {"voix_brute_s": 20.0, "tempo": 1.0, "video_s": 20.5, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 48, "minutage": "10 phrases, 4 coups, 0 pauses"}
### commandes/perso_pigeon_en_14.json
    voix générée : 252 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_14.mp4 {"voix_brute_s": 18.4, "tempo": 1.0, "video_s": 19.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 45, "minutage": "8 phrases, 4 coups, 0 pauses"}
### commandes/perso_pigeon_en_15.json
    voix générée : 266 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_15.mp4 {"voix_brute_s": 19.2, "tempo": 1.0, "video_s": 20.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 49, "minutage": "10 phrases, 4 coups, 0 pauses"}
### commandes/perso_pigeon_jour_13.json
    voix générée : 253 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_13.mp4 {"voix_brute_s": 19.8, "tempo": 1.0, "video_s": 20.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 46, "minutage": "8 phrases, 4 coups, 0 pauses"}
### commandes/perso_quiz_legal_8_fr.json
    voix générée : 255 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_8_fr.mp4 {"voix_brute_s": 20.5, "tempo": 1.0, "video_s": 23.3, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 58, "minutage": "8 phrases, 2 coups, 1 pauses"}
## 2026-10-30 00:11 UTC · run 40977991726
### commandes/perso_pigeon_en_14.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_14.mp4 {"voix_brute_s": 18.4, "tempo": 1.0, "video_s": 21.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 45, "minutage": "8 phrases, 4 coups, 1 pauses"}
## 2026-10-30 11:44 UTC · pièges · run 41050253354
### commandes/pieges/reserve_1300_2000.json
    OK stock/pieges-candidats.md : 10 pièges, dont 9 jamais faits
## 2026-10-31 00:06 UTC · prof corrige · run 41148243996
### commandes/prof/prof_2.json
    OK : prof_2, 135 demi-coups, 3 moments, 81 commentaires du prof
## 2026-10-31 00:18 UTC · run 41149289617
### commandes/perso_gourmande_en_1.json
    voix générée : 354 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/gourmande_en_1.mp4 {"voix_brute_s": 26.6, "tempo": 1.0, "video_s": 27.3, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 61, "minutage": "9 phrases, 6 coups, 0 pauses"}
### commandes/perso_gourmande_fr_1.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/gourmande_fr_1.mp4 {"voix_brute_s": 33.5, "tempo": 1.0, "video_s": 34.1, "voice_id": "aucune", "musique": "aucune", "mots_transcrits": 67, "minutage": "9 phrases, 6 coups, 0 pauses"}
### commandes/perso_pigeon_en_16.json
    voix générée : 405 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_16.mp4 {"voix_brute_s": 29.9, "tempo": 1.0, "video_s": 30.6, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 68, "minutage": "13 phrases, 10 coups, 0 pauses"}
### commandes/perso_quiz_legal_9_en.json
    voix générée : 266 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_9_en.mp4 {"voix_brute_s": 20.5, "tempo": 1.0, "video_s": 23.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 53, "minutage": "8 phrases, 2 coups, 1 pauses"}
### commandes/perso_quiz_legal_9_fr.json
    voix générée : 278 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_9_fr.mp4 {"voix_brute_s": 21.5, "tempo": 1.0, "video_s": 24.1, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 55, "minutage": "9 phrases, 2 coups, 1 pauses"}
## 2026-10-31 00:26 UTC · run 41150112987
### commandes/perso_quiz_legal_9_en_long.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_9_en_long.mp4 {"voix_brute_s": 20.5, "tempo": 1.0, "video_s": 27.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 53, "minutage": "8 phrases, 2 coups, 1 pauses"}
## 2026-10-31 00:30 UTC · pièges · run 41150474685
### commandes/pieges/2026-10-31b.json
    OK stock/pieges-candidats.md : 10 pièges, dont 7 jamais faits
## 2026-10-31 10:41 UTC · run 41193698239
## 2026-10-31 10:55 UTC · pièges · run 41194697275
### commandes/pieges/2026-10-31-varies.json
    OK stock/pieges-candidats.md : 8 pièges, dont 7 jamais faits
## 2026-11-01 00:06 UTC · run 41255076981
### commandes/perso_pigeon_en_17.json
    voix générée : 238 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_17.mp4 {"voix_brute_s": 17.3, "tempo": 1.0, "video_s": 18.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 42, "minutage": "6 phrases, 4 coups, 0 pauses"}
### commandes/perso_pigeon_jour_14.json
    voix générée : 276 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_jour_14.mp4 {"voix_brute_s": 19.1, "tempo": 1.0, "video_s": 20.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 49, "minutage": "6 phrases, 6 coups, 0 pauses"}
### commandes/perso_quiz_legal_10_en.json
    voix générée : 232 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_10_en.mp4 {"voix_brute_s": 18.5, "tempo": 1.0, "video_s": 21.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 46, "minutage": "8 phrases, 4 coups, 1 pauses"}
### commandes/perso_quiz_legal_10_fr.json
    voix générée : 256 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_10_fr.mp4 {"voix_brute_s": 19.1, "tempo": 1.0, "video_s": 21.8, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 54, "minutage": "7 phrases, 4 coups, 1 pauses"}
### commandes/perso_quiz_legal_11_en.json
    voix générée : 234 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/quiz_legal_11_en.mp4 {"voix_brute_s": 17.9, "tempo": 1.0, "video_s": 20.6, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 43, "minutage": "7 phrases, 1 coups, 1 pauses"}
### commandes/prof_corrige_2.json
    voix générée : 283 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/prof_corrige_2.mp4 {"voix_brute_s": 20.0, "tempo": 1.0, "video_s": 20.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 49, "minutage": "4 phrases, 2 coups, 0 pauses", "ecrans": 2, "phrases_du_prof": 3}
## 2026-11-01 00:13 UTC · run 41255410772
### commandes/perso_pigeon_en_17.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_17.mp4 {"voix_brute_s": 17.3, "tempo": 1.0, "video_s": 21.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 42, "minutage": "6 phrases, 4 coups, 1 pauses"}
## 2026-11-01 00:16 UTC · prof corrige · run 41255957787
### commandes/prof/prof_3.json
    OK : prof_3, 41 demi-coups, 3 moments, 25 commentaires du prof
## 2026-11-02 00:06 UTC · run 41365293945
### commandes/perso_finale_carre_1.json
    voix générée : 258 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_carre_1.mp4 {"voix_brute_s": 21.0, "tempo": 1.0, "video_s": 23.8, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 50, "minutage": "8 phrases, 7 coups, 1 pauses"}
### commandes/perso_finale_carre_1_fr.json
    voix générée : 242 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_carre_1_fr.mp4 {"voix_brute_s": 19.8, "tempo": 1.0, "video_s": 22.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 52, "minutage": "8 phrases, 7 coups, 1 pauses"}
### commandes/perso_nb_coups_1.json
    voix générée : 172 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/nb_coups_1.mp4 {"voix_brute_s": 15.0, "tempo": 1.0, "video_s": 18.7, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 27, "minutage": "7 phrases, 0 coups, 1 pauses"}
### commandes/perso_nb_coups_1_fr.json
    voix générée : 199 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/nb_coups_1_fr.mp4 {"voix_brute_s": 14.4, "tempo": 1.0, "video_s": 18.1, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 33, "minutage": "8 phrases, 0 coups, 1 pauses"}
### commandes/perso_pigeon_en_18.json
    voix générée : 257 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_18.mp4 {"voix_brute_s": 23.2, "tempo": 1.0, "video_s": 23.9, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 49, "minutage": "11 phrases, 6 coups, 0 pauses"}
### commandes/perso_tactique_clouage_1.json
    voix générée : 234 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/tactique_clouage_1.mp4 {"voix_brute_s": 19.6, "tempo": 1.0, "video_s": 20.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 43, "minutage": "9 phrases, 7 coups, 0 pauses"}
## 2026-11-02 00:13 UTC · run 41365900434
### commandes/perso_finale_carre_1.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_carre_1.mp4 {"voix_brute_s": 21.0, "tempo": 1.0, "video_s": 23.8, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 50, "minutage": "8 phrases, 5 coups, 1 pauses"}
### commandes/perso_finale_carre_1_fr.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_carre_1_fr.mp4 {"voix_brute_s": 19.8, "tempo": 1.0, "video_s": 22.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 52, "minutage": "8 phrases, 4 coups, 1 pauses"}
## 2026-11-02 17:19 UTC · run 41489953573
### commandes/perso_pigeon_en_18.json
    voix générée : 307 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_18.mp4 {"voix_brute_s": 28.8, "tempo": 1.0, "video_s": 30.3, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 56, "minutage": "11 phrases, 7 coups, 1 pauses"}
## 2026-11-03 00:06 UTC · run 41550244444
### commandes/perso_finale_saavedra_1.json
    voix générée : 468 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_saavedra_1.mp4 {"voix_brute_s": 35.6, "tempo": 1.0, "video_s": 36.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 91, "minutage": "13 phrases, 11 coups, 0 pauses"}
### commandes/perso_legende_miniature_1.json
    voix générée : 395 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/legende_miniature_1.mp4 {"voix_brute_s": 28.8, "tempo": 1.0, "video_s": 30.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 73, "minutage": "12 phrases, 6 coups, 1 pauses"}
### commandes/perso_legende_miniature_1_fr.json
    voix générée : 483 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/legende_miniature_1_fr.mp4 {"voix_brute_s": 34.8, "tempo": 1.0, "video_s": 36.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 95, "minutage": "12 phrases, 6 coups, 1 pauses"}
### commandes/perso_pigeon_en_19.json
    voix générée : 403 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pigeon_en_19.mp4 {"voix_brute_s": 30.5, "tempo": 1.0, "video_s": 32.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 76, "minutage": "12 phrases, 6 coups, 1 pauses"}
### commandes/perso_touch_move_1.json
    voix générée : 321 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/touch_move_1.mp4 {"voix_brute_s": 26.0, "tempo": 1.0, "video_s": 28.7, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 63, "minutage": "9 phrases, 1 coups, 1 pauses"}
### commandes/perso_touch_move_1_fr.json
    voix générée : 339 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/touch_move_1_fr.mp4 {"voix_brute_s": 25.2, "tempo": 1.0, "video_s": 28.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 69, "minutage": "9 phrases, 1 coups, 1 pauses"}
## 2026-11-03 00:13 UTC · run 41551143852
### commandes/perso_finale_saavedra_1.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_saavedra_1.mp4 {"voix_brute_s": 35.6, "tempo": 1.0, "video_s": 36.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 91, "minutage": "13 phrases, 11 coups, 0 pauses"}
## 2026-11-03 00:16 UTC · run 41551513547
### commandes/perso_finale_saavedra_1.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_saavedra_1.mp4 {"voix_brute_s": 35.6, "tempo": 1.0, "video_s": 36.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 91, "minutage": "13 phrases, 11 coups, 0 pauses"}
## 2026-11-03 00:18 UTC · pièges · run 41551824316
### commandes/pieges/2026-11-03.json
    OK stock/pieges-candidats.md : 0 pièges, dont 0 jamais faits
## 2026-11-03 08:44 UTC · pièges · run 41605495437
### commandes/pieges/2026-11-03b.json
    OK stock/pieges-candidats.md : 0 nouveaux pièges ajoutés, 9 en réserve ; écartés : {'export refusé': 220}
## 2026-11-03 09:03 UTC · pièges · run 41607859292
### commandes/pieges/2026-11-03c.json
    OK stock/pieges-candidats.md : 11 nouveaux pièges ajoutés, 20 en réserve ; écartés : {'export refusé': 3, 'variété': 178}
## 2026-11-03 09:22 UTC · run 41610421119
### commandes/perso_exemple_morra_1.json
    voix générée : 833 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/exemple_morra_1.mp4 {"voix_brute_s": 63.3, "tempo": 1.0, "video_s": 65.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 157, "minutage": "23 phrases, 16 coups, 1 pauses"}
## 2026-11-03 09:31 UTC · run 41611609498
### commandes/perso_exemple_morra_2.json
    voix générée : 383 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/exemple_morra_2.mp4 {"voix_brute_s": 30.4, "tempo": 1.0, "video_s": 32.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 74, "minutage": "12 phrases, 5 coups, 1 pauses"}
## 2026-11-03 10:41 UTC · run 41621065461
### commandes/perso_exemple_morra_2.json
    voix générée : 426 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/exemple_morra_2.mp4 {"voix_brute_s": 32.4, "tempo": 1.0, "video_s": 34.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 84, "minutage": "13 phrases, 5 coups, 1 pauses"}
## 2026-11-03 13:31 UTC · run 41644784712
### commandes/perso_exemple_morra_2.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/exemple_morra_2.mp4 {"voix_brute_s": 32.4, "tempo": 1.0, "video_s": 34.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 84, "minutage": "13 phrases, 5 coups, 1 pauses"}
## 2026-11-04 00:06 UTC · run 41744182318
### commandes/perso_decouverte_cavalier_1.json
    voix générée : 486 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/decouverte_cavalier_1.mp4 {"voix_brute_s": 37.1, "tempo": 1.0, "video_s": 38.8, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 90, "minutage": "14 phrases, 7 coups, 1 pauses"}
### commandes/perso_decouverte_cavalier_1_fr.json
    voix générée : 447 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/decouverte_cavalier_1_fr.mp4 {"voix_brute_s": 33.2, "tempo": 1.0, "video_s": 35.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 84, "minutage": "13 phrases, 7 coups, 1 pauses"}
### commandes/perso_evergreen_1.json
    voix générée : 537 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/evergreen_1.mp4 {"voix_brute_s": 43.8, "tempo": 1.0, "video_s": 45.5, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 97, "minutage": "17 phrases, 10 coups, 1 pauses"}
### commandes/perso_reti_etude_1.json
    voix générée : 534 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/reti_etude_1.mp4 {"voix_brute_s": 41.6, "tempo": 1.0, "video_s": 43.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 100, "minutage": "15 phrases, 9 coups, 1 pauses"}
### commandes/perso_reti_etude_1_fr.json
    voix générée : 548 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/reti_etude_1_fr.mp4 {"voix_brute_s": 41.3, "tempo": 1.0, "video_s": 43.1, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 107, "minutage": "15 phrases, 9 coups, 1 pauses"}
## 2026-11-04 00:13 UTC · pièges · run 41745117905
### commandes/pieges/2026-11-04.json
    OK stock/pieges-candidats.md : 15 nouveaux pièges ajoutés, 35 en réserve ; écartés : {'export refusé': 3, 'déjà en réserve': 8, 'variété': 196, 'pas une faute': 1}
## 2026-11-05 00:26 UTC · run 41941159609
### commandes/perso_dame_pion_1.json
    voix générée : 405 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/dame_pion_1.mp4 {"voix_brute_s": 34.8, "tempo": 1.0, "video_s": 36.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 76, "minutage": "15 phrases, 7 coups, 1 pauses"}
### commandes/perso_dame_pion_1_fr.json
    voix générée : 443 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/dame_pion_1_fr.mp4 {"voix_brute_s": 33.9, "tempo": 1.0, "video_s": 35.6, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 88, "minutage": "15 phrases, 7 coups, 1 pauses"}
### commandes/perso_echange_pions_1.json
    voix générée : 369 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/echange_pions_1.mp4 {"voix_brute_s": 31.2, "tempo": 1.0, "video_s": 32.7, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 71, "minutage": "14 phrases, 7 coups, 1 pauses"}
### commandes/perso_nimzo_intermezzo_1.json
    voix générée : 484 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/nimzo_intermezzo_1.mp4 {"voix_brute_s": 39.8, "tempo": 1.0, "video_s": 41.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 89, "minutage": "15 phrases, 9 coups, 1 pauses"}
### commandes/perso_nimzo_intermezzo_1_fr.json
    voix générée : 538 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/nimzo_intermezzo_1_fr.mp4 {"voix_brute_s": 42.8, "tempo": 1.0, "video_s": 44.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 97, "minutage": "15 phrases, 9 coups, 1 pauses"}
### commandes/perso_petrov_cavalier_mat3_1.json
    voix générée : 375 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/petrov_cavalier_mat3_1.mp4 {"voix_brute_s": 30.5, "tempo": 1.0, "video_s": 32.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 70, "minutage": "12 phrases, 5 coups, 1 pauses"}
## 2026-11-05 00:35 UTC · run 41942351016
### commandes/perso_dame_pion_1.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/dame_pion_1.mp4 {"voix_brute_s": 34.8, "tempo": 1.0, "video_s": 36.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 76, "minutage": "15 phrases, 7 coups, 1 pauses"}
### commandes/perso_dame_pion_1_fr.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/dame_pion_1_fr.mp4 {"voix_brute_s": 33.9, "tempo": 1.0, "video_s": 35.6, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 88, "minutage": "15 phrases, 7 coups, 1 pauses"}
### commandes/perso_nimzo_intermezzo_1.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/nimzo_intermezzo_1.mp4 {"voix_brute_s": 39.8, "tempo": 1.0, "video_s": 41.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 89, "minutage": "15 phrases, 9 coups, 1 pauses"}
### commandes/perso_nimzo_intermezzo_1_fr.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/nimzo_intermezzo_1_fr.mp4 {"voix_brute_s": 42.8, "tempo": 1.0, "video_s": 44.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 103, "minutage": "15 phrases, 9 coups, 1 pauses"}
## 2026-11-06 00:13 UTC · run 42135118167
### commandes/perso_deepblue_g6_1.json
    voix générée : 635 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/deepblue_g6_1.mp4 {"voix_brute_s": 55.1, "tempo": 1.0, "video_s": 56.5, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 112, "minutage": "23 phrases, 24 coups, 1 pauses"}
### commandes/perso_finale_lucena_1.json
    voix générée : 498 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_lucena_1.mp4 {"voix_brute_s": 41.1, "tempo": 1.0, "video_s": 42.7, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 95, "minutage": "15 phrases, 17 coups, 1 pauses"}
### commandes/perso_finale_lucena_1_fr.json
    voix générée : 521 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_lucena_1_fr.mp4 {"voix_brute_s": 42.1, "tempo": 1.0, "video_s": 43.8, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 98, "minutage": "15 phrases, 17 coups, 1 pauses"}
### commandes/perso_marshall_grec_1.json
    voix générée : 516 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/marshall_grec_1.mp4 {"voix_brute_s": 45.6, "tempo": 1.0, "video_s": 47.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 93, "minutage": "20 phrases, 17 coups, 1 pauses"}
### commandes/perso_scandi_degagement_1.json
    voix générée : 389 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/scandi_degagement_1.mp4 {"voix_brute_s": 29.2, "tempo": 1.0, "video_s": 30.9, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 73, "minutage": "10 phrases, 6 coups, 1 pauses"}
### commandes/perso_scandi_degagement_1_fr.json
    voix générée : 416 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/scandi_degagement_1_fr.mp4 {"voix_brute_s": 35.3, "tempo": 1.0, "video_s": 37.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 83, "minutage": "11 phrases, 6 coups, 1 pauses"}
## 2026-11-06 00:34 UTC · run 42137706432
### commandes/perso_deepblue_g6_1.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/deepblue_g6_1.mp4 {"voix_brute_s": 55.1, "tempo": 1.0, "video_s": 56.5, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 112, "minutage": "23 phrases, 24 coups, 1 pauses"}
### commandes/perso_finale_lucena_1.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/finale_lucena_1.mp4 {"voix_brute_s": 41.1, "tempo": 1.0, "video_s": 42.7, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 95, "minutage": "15 phrases, 17 coups, 1 pauses"}
### commandes/perso_marshall_grec_1.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/marshall_grec_1.mp4 {"voix_brute_s": 45.6, "tempo": 1.0, "video_s": 47.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 93, "minutage": "20 phrases, 17 coups, 1 pauses"}
### commandes/perso_scandi_degagement_1.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/scandi_degagement_1.mp4 {"voix_brute_s": 29.2, "tempo": 1.0, "video_s": 30.9, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 73, "minutage": "10 phrases, 6 coups, 1 pauses"}
### commandes/perso_scandi_degagement_1_fr.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/scandi_degagement_1_fr.mp4 {"voix_brute_s": 35.3, "tempo": 1.0, "video_s": 37.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 83, "minutage": "11 phrases, 6 coups, 1 pauses"}
## 2026-11-07 00:05 UTC · run 42315971505
### commandes/perso_fou_mauvaise_couleur_1.json
    voix générée : 479 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/fou_mauvaise_couleur_1.mp4 {"voix_brute_s": 37.3, "tempo": 1.0, "video_s": 39.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 89, "minutage": "14 phrases, 9 coups, 1 pauses"}
### commandes/perso_lasker_bauer_1.json
    voix générée : 604 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/lasker_bauer_1.mp4 {"voix_brute_s": 49.7, "tempo": 1.0, "video_s": 51.3, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 113, "minutage": "17 phrases, 18 coups, 1 pauses"}
### commandes/perso_lasker_bauer_1_fr.json
    voix générée : 601 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/lasker_bauer_1_fr.mp4 {"voix_brute_s": 53.2, "tempo": 1.0, "video_s": 54.9, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 118, "minutage": "17 phrases, 18 coups, 1 pauses"}
### commandes/perso_percee_3v3_1.json
    voix générée : 445 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/percee_3v3_1.mp4 {"voix_brute_s": 39.3, "tempo": 1.0, "video_s": 41.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 91, "minutage": "12 phrases, 9 coups, 1 pauses"}
### commandes/perso_percee_3v3_1_fr.json
    voix générée : 492 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/percee_3v3_1_fr.mp4 {"voix_brute_s": 39.2, "tempo": 1.0, "video_s": 41.0, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 98, "minutage": "12 phrases, 9 coups, 1 pauses"}
### commandes/perso_vienne_stanley_1.json
    voix générée : 322 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/vienne_stanley_1.mp4 {"voix_brute_s": 30.0, "tempo": 1.0, "video_s": 31.7, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 65, "minutage": "12 phrases, 6 coups, 1 pauses"}
## 2026-11-07 00:13 UTC · run 42316815803
### commandes/perso_lasker_bauer_1.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/lasker_bauer_1.mp4 {"voix_brute_s": 49.7, "tempo": 1.0, "video_s": 51.3, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 113, "minutage": "17 phrases, 18 coups, 1 pauses"}
### commandes/perso_lasker_bauer_1_fr.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/lasker_bauer_1_fr.mp4 {"voix_brute_s": 53.2, "tempo": 1.0, "video_s": 54.9, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 117, "minutage": "17 phrases, 18 coups, 1 pauses"}
## 2026-11-08 00:06 UTC · run 42428115133
### commandes/perso_passant_decouverte_1.json
    voix générée : 485 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/passant_decouverte_1.mp4 {"voix_brute_s": 38.3, "tempo": 1.0, "video_s": 39.9, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 95, "minutage": "14 phrases, 7 coups, 1 pauses"}
### commandes/perso_rotlewi_rubinstein_1.json
    voix générée : 434 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/rotlewi_rubinstein_1.mp4 {"voix_brute_s": 35.6, "tempo": 1.0, "video_s": 37.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 83, "minutage": "13 phrases, 8 coups, 1 pauses"}
### commandes/perso_rotlewi_rubinstein_1_fr.json
    voix générée : 457 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/rotlewi_rubinstein_1_fr.mp4 {"voix_brute_s": 37.9, "tempo": 1.0, "video_s": 39.5, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 94, "minutage": "13 phrases, 8 coups, 1 pauses"}
### commandes/perso_short_timman_1.json
    voix générée : 540 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/short_timman_1.mp4 {"voix_brute_s": 46.3, "tempo": 1.0, "video_s": 47.9, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 105, "minutage": "15 phrases, 11 coups, 1 pauses"}
### commandes/perso_short_timman_1_fr.json
    voix générée : 543 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/short_timman_1_fr.mp4 {"voix_brute_s": 42.3, "tempo": 1.0, "video_s": 44.1, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 112, "minutage": "14 phrases, 11 coups, 1 pauses"}
### commandes/perso_sicilienne_dame_1.json
    voix générée : 479 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/sicilienne_dame_1.mp4 {"voix_brute_s": 39.2, "tempo": 1.0, "video_s": 40.8, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 87, "minutage": "15 phrases, 8 coups, 1 pauses"}
## 2026-11-08 00:16 UTC · run 42428953654
### commandes/perso_rotlewi_rubinstein_1.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/rotlewi_rubinstein_1.mp4 {"voix_brute_s": 35.6, "tempo": 1.0, "video_s": 37.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 83, "minutage": "13 phrases, 8 coups, 1 pauses"}
### commandes/perso_short_timman_1.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/short_timman_1.mp4 {"voix_brute_s": 46.3, "tempo": 1.0, "video_s": 47.9, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 105, "minutage": "15 phrases, 11 coups, 1 pauses"}
### commandes/perso_short_timman_1_fr.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/short_timman_1_fr.mp4 {"voix_brute_s": 42.3, "tempo": 1.0, "video_s": 44.1, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 112, "minutage": "14 phrases, 11 coups, 1 pauses"}
## 2026-11-08 00:24 UTC · run 42429522134
### commandes/perso_short_timman_1_fr.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/short_timman_1_fr.mp4 {"voix_brute_s": 42.3, "tempo": 1.0, "video_s": 44.1, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 112, "minutage": "14 phrases, 11 coups, 1 pauses"}
## 2026-11-09 00:09 UTC · run 42538565602
### commandes/perso_deux_cavaliers_1.json
    voix générée : 460 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/deux_cavaliers_1.mp4 {"voix_brute_s": 37.6, "tempo": 1.0, "video_s": 41.3, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 89, "minutage": "14 phrases, 7 coups, 1 pauses"}
### commandes/perso_deux_cavaliers_1_fr.json
    voix générée : 499 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/deux_cavaliers_1_fr.mp4 {"voix_brute_s": 43.5, "tempo": 1.0, "video_s": 45.3, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 100, "minutage": "13 phrases, 7 coups, 1 pauses"}
### commandes/perso_lasker_albin_1.json
    voix générée : 595 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/lasker_albin_1.mp4 {"voix_brute_s": 45.8, "tempo": 1.0, "video_s": 47.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 112, "minutage": "17 phrases, 13 coups, 1 pauses"}
### commandes/perso_opposition_ke5_1.json
    sans voix (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/opposition_ke5_1.mp4 {"voix_brute_s": 40.5, "tempo": 1.0, "video_s": 45.1, "voice_id": "aucune", "musique": "aucune", "mots_transcrits": 101, "minutage": "22 phrases, 15 coups, 1 pauses"}
### commandes/perso_opposition_ke5_1_fr.json
    voix générée : 551 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/opposition_ke5_1_fr.mp4 {"voix_brute_s": 46.3, "tempo": 1.0, "video_s": 47.9, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 116, "minutage": "21 phrases, 15 coups, 1 pauses"}
### commandes/perso_reti_tartakower_1.json
    voix générée : 376 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/reti_tartakower_1.mp4 {"voix_brute_s": 33.5, "tempo": 1.0, "video_s": 35.2, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 72, "minutage": "12 phrases, 6 coups, 1 pauses"}
## 2026-11-09 00:18 UTC · run 42539407042
### commandes/perso_deux_cavaliers_1.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/deux_cavaliers_1.mp4 {"voix_brute_s": 37.6, "tempo": 1.0, "video_s": 41.3, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 89, "minutage": "14 phrases, 7 coups, 1 pauses"}
### commandes/perso_lasker_albin_1.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/lasker_albin_1.mp4 {"voix_brute_s": 45.8, "tempo": 1.0, "video_s": 47.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 112, "minutage": "17 phrases, 13 coups, 1 pauses"}
### commandes/perso_opposition_ke5_1_fr.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/opposition_ke5_1_fr.mp4 {"voix_brute_s": 46.3, "tempo": 1.0, "video_s": 47.9, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 116, "minutage": "21 phrases, 15 coups, 1 pauses"}
## 2026-11-10 00:05 UTC · run 42725463913
### commandes/perso_course_d6_1.json
    voix générée : 304 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/course_d6_1.mp4 {"voix_brute_s": 28.4, "tempo": 1.0, "video_s": 30.9, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 62, "minutage": "11 phrases, 5 coups, 1 pauses"}
### commandes/perso_course_d6_1_fr.json
    voix générée : 343 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/course_d6_1_fr.mp4 {"voix_brute_s": 27.0, "tempo": 1.0, "video_s": 29.7, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 73, "minutage": "11 phrases, 5 coups, 1 pauses"}
### commandes/perso_deux_pions_e6_1.json
    voix générée : 454 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/deux_pions_e6_1.mp4 {"voix_brute_s": 38.3, "tempo": 1.0, "video_s": 43.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 91, "minutage": "13 phrases, 10 coups, 1 pauses"}
### commandes/perso_deux_pions_e6_1_fr.json
    voix générée : 467 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/deux_pions_e6_1_fr.mp4 {"voix_brute_s": 35.2, "tempo": 1.0, "video_s": 37.9, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 92, "minutage": "13 phrases, 10 coups, 1 pauses"}
### commandes/perso_kasparov_topalov_1.json
    voix générée : 502 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/kasparov_topalov_1.mp4 {"voix_brute_s": 46.0, "tempo": 1.0, "video_s": 49.5, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 101, "minutage": "15 phrases, 9 coups, 1 pauses"}
### commandes/perso_krause_bxf6_1.json
    voix générée : 406 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/krause_bxf6_1.mp4 {"voix_brute_s": 35.9, "tempo": 1.0, "video_s": 37.5, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 79, "minutage": "14 phrases, 5 coups, 1 pauses"}
## 2026-11-10 00:13 UTC · run 42726477094
### commandes/perso_course_d6_1_fr.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/course_d6_1_fr.mp4 {"voix_brute_s": 27.0, "tempo": 1.0, "video_s": 29.7, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 73, "minutage": "11 phrases, 5 coups, 1 pauses"}
### commandes/perso_deux_pions_e6_1.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/deux_pions_e6_1.mp4 {"voix_brute_s": 38.3, "tempo": 1.0, "video_s": 43.0, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 91, "minutage": "13 phrases, 10 coups, 1 pauses"}
## 2026-11-10 18:28 UTC · run 42875260334
### commandes/perso_kasparov_topalov_2.json
    voix générée : 357 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/kasparov_topalov_2.mp4 {"voix_brute_s": 31.9, "tempo": 1.0, "video_s": 35.5, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 72, "minutage": "10 phrases, 9 coups, 1 pauses"}
### commandes/perso_krause_bxf6_2.json
    voix générée : 239 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/krause_bxf6_2.mp4 {"voix_brute_s": 21.2, "tempo": 1.0, "video_s": 22.9, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 46, "minutage": "9 phrases, 5 coups, 1 pauses"}
## 2026-11-11 00:07 UTC · run 42928758899
### commandes/perso_decouverte_g_1.json
    voix générée : 305 caractères
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/decouverte_g_1.mp4 {"voix_brute_s": 27.8, "tempo": 1.0, "video_s": 31.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 61, "minutage": "11 phrases, 5 coups, 1 pauses"}
### commandes/perso_levitsky_marshall_1.json
    voix générée : 410 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/levitsky_marshall_1.mp4 {"voix_brute_s": 33.5, "tempo": 1.0, "video_s": 36.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 81, "minutage": "10 phrases, 11 coups, 1 pauses"}
### commandes/perso_levitsky_marshall_1_fr.json
    voix générée : 440 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/levitsky_marshall_1_fr.mp4 {"voix_brute_s": 33.9, "tempo": 1.0, "video_s": 36.7, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 93, "minutage": "10 phrases, 11 coups, 1 pauses"}
### commandes/perso_pion_g5_1.json
    voix générée : 216 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/pion_g5_1.mp4 {"voix_brute_s": 21.2, "tempo": 1.0, "video_s": 25.8, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 46, "minutage": "10 phrases, 5 coups, 1 pauses"}
### commandes/perso_trois_pions_d7_1.json
    voix générée : 281 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/trois_pions_d7_1.mp4 {"voix_brute_s": 25.0, "tempo": 1.0, "video_s": 29.6, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 53, "minutage": "8 phrases, 6 coups, 1 pauses"}
### commandes/perso_trois_pions_d7_1_fr.json
    voix générée : 327 caractères
    OK /home/runner/work/blundercheck/blundercheck/sorties/trois_pions_d7_1_fr.mp4 {"voix_brute_s": 26.6, "tempo": 1.0, "video_s": 29.3, "voice_id": "ecxPjiGTvAfpGEams6ec", "musique": "aucune", "mots_transcrits": 63, "minutage": "8 phrases, 6 coups, 1 pauses"}
## 2026-11-11 00:17 UTC · run 42930044482
### commandes/perso_decouverte_g_1.json
    voix réutilisée (0 crédit)
    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    OK /home/runner/work/blundercheck/blundercheck/sorties/decouverte_g_1.mp4 {"voix_brute_s": 27.8, "tempo": 1.0, "video_s": 30.4, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 61, "minutage": "11 phrases, 5 coups, 1 pauses"}
### commandes/perso_levitsky_marshall_1.json
    voix réutilisée (0 crédit)
    OK /home/runner/work/blundercheck/blundercheck/sorties/levitsky_marshall_1.mp4 {"voix_brute_s": 33.5, "tempo": 1.0, "video_s": 36.1, "voice_id": "JBFqnCBsd6RMkjVDRZzb", "musique": "aucune", "mots_transcrits": 81, "minutage": "10 phrases, 11 coups, 1 pauses"}
