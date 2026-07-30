# Ingest pipeline

Reproducible pipeline from episode list to coach playbooks.

1. `video_ids.txt` — one YouTube video ID per line (the corpus).
2. Download captions + metadata (no video download):
   ```bash
   yt-dlp -a video_ids.txt --skip-download --no-simulate \
     --write-auto-subs --write-subs --sub-langs "en,en-US,en-orig" --sub-format vtt \
     -o "subs/%(id)s.%(ext)s" \
     --print-to-file "%(id)s\t%(title)s\t%(channel)s\t%(duration_string)s" meta/index.tsv \
     --ignore-errors
   ```
3. Clean to plain text: `python3 vtt2txt.py subs transcripts`
4. Distill playbooks into `../knowledge/` following `DISTILL_BRIEF.md` (one Claude agent per coach works well).

`subs/` and `transcripts/` are gitignored: third-party podcast transcripts are processed locally, never committed. Only the distilled playbooks with short attributed quotes live in the repo.

Known gap: GUjt0iRJ3eo (Founder Films — Melanie Perkins) hit YouTube rate limiting; re-run step 2 for it to include it.
