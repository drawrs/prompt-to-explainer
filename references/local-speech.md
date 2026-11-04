# Local speech and measured boundaries

On macOS synthesize a short paragraph at a time with the built-in voice:

    say -v Samantha -f paragraph.txt -o paragraph.aiff
    ffmpeg -v error -i paragraph.aiff -ar 16000 -ac 1 paragraph.wav

For word intervals, install whisperx in an isolated Python environment. The first alignment for a language downloads its acoustic model. Align the known text to its own paragraph recording on CPU. For English:

    import whisperx
    from pathlib import Path
    audio = whisperx.load_audio("paragraph.wav")
    transcript = Path("paragraph.txt").read_text().strip()
    model, metadata = whisperx.load_align_model(language_code="en", device="cpu")
    segment = {"start": 0, "end": len(audio) / 16000, "text": transcript}
    result = whisperx.align([segment], model, metadata, audio, "cpu")
    words = result["word_segments"]

Keep the word/start/end fields. Spell numbers and symbols as spoken in the input text. Check for missing timestamps and inspect alignment against playback. Re-align shorter segments when necessary. After concatenating PCM paragraphs, offset each word by the exact preceding sample count divided by the sample rate, including inserted pauses. Write the combined array to words.json and run the timeline helper. Use the final audio sample clock if resampling or speed changes occur.

Alignment estimates phonetic boundaries; animation is frame-accurate to the accepted alignment. See the [WhisperX alignment implementation](https://github.com/m-bain/whisperX/blob/main/whisperx/alignment.py).
