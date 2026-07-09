# Netflix Data File Analyzer

A Python program that reads your Netflix viewing and billing data and shows you fun stats. Built for CS50P at Harvard.

## What It Does

Netflix lets you download all your data — every show you've watched, every dollar you've spent. But the files are just raw CSVs. This program makes them readable.

You pick a profile (or all of them), then choose from a menu:

1. **Total Spent** — how much you've paid since joining. Asks if you want PYG conversion too.
2. **Most Watched Series** — top 5 shows ranked by watch time.
3. **Most Watched Movies** — same thing, but for films.
4. **Total Watch Time** — all your hours combined in one number.
5. **Cost Per Hour** — total spent divided by total hours.

It automatically skips trailers, hooks, and autoplay previews so your real watch time isn't inflated.

## Getting Your Netflix Data

1. Netflix → Account → Download your personal information
2. Wait for the email (usually less than a day)
3. Download and unzip the file
4. You'll get a folder with a name like `1343059170`
5. Inside it, the program uses two folders:
      CONTENT_INTERACTION/ViewingActivity.csv
      PAYMENT_AND_BILLING/BillingHistory.csv

## How to Run

```bash
pip install -r requirements.txt
python project.py C:\Users\you\Downloads\1343059170
```

Or just python project.py and type the path when asked.

## Files

   project.py — the whole program. Menu, analysis functions, everything.
   test_project.py — tests for the main functions (to do).
   requirements.txt — the two libraries needed: pandas and requests.

