# Netflix Data File Analyzer

A terminal-based Python tool that analyzes your personal Netflix viewing and billing data. Built as the final project for Harvard's CS50P (CS50's Introduction to Programming with Python).

## What It Does

When you request your data from Netflix, they send you a ZIP file containing your complete viewing history and payment records. This program reads that data and gives you insights like which series you've watched the most, how much you've spent, and what your cost per hour of entertainment works out to.

## Features

The program presents an interactive menu with five analysis options:

1. **Total Spent** — sums all charges from your billing history and optionally converts the total from USD to PYG (Paraguayan Guaraní) using a live exchange rate.
2. **Most Watched Series** — ranks TV series by total watch time, excluding movies and non-real views like trailers and autoplay previews.
3. **Most Watched Movies** — same as above, but only for films.
4. **Total Watch Time** — displays your total hours and minutes watched across all content.
5. **Cost Per Hour Watched** — divides your total spending by total watch time to show how much each hour of Netflix actually costs you.

Additional capabilities:

- **Profile filtering** — select a specific Netflix profile (or "All Profiles") before running any analysis, so you can see stats for just one person.
- **Smart content detection** — separates series from movies by checking for the "Episode" keyword in titles, avoiding the common pitfall of counting a movie and a series as the same thing.
- **Fake view filtering** — automatically removes trailers, hooks, and autoplay previews so they don't skew your watch time.
- **Unicode normalization** — cleans up non-standard colon characters and extra whitespace in titles so that "Stranger Things" isn't counted separately from "Stranger Things" with a weird Unicode colon.
- **Input validation** — rejects non-numeric menu selections and out-of-range choices with clear error messages.
- **Keyboard interrupt handling** — pressing Ctrl+C anywhere exits cleanly without a traceback.

## How Netflix Data Works

1. Go to your Netflix Account → **Download your personal information**.
2. Submit the request and wait for the email (usually within 24 hours).
3. Download and extract the ZIP file. You'll get a folder with a numeric name (e.g., `1343059170`) containing many subfolders.
4. This program only needs two of them:
   - `CONTENT_INTERACTION/ViewingActivity.csv` — your watch history
   - `PAYMENT_AND_BILLING/BillingHistory.csv` — your payment records

## Installation & Usage

**Requirements:** Python 3.8+, plus the libraries listed in `requirements.txt`.

```bash
# Clone the repository
git clone https://github.com/evanczm/Netflix-Data-File-Analyzer.git
cd Netflix-Data-File-Analyzer

# Install dependencies
pip install -r requirements.txt

# Run with the path to your Netflix data folder
python project.py C:\Users\evanc\Downloads\1343059170

# Or run without arguments and type the path when prompted
python project.py
```

## Files

| File | Purpose |
|------|---------|
| `project.py` | Main program — all logic lives here, from CSV loading to analysis functions to the interactive menu. |
| `test_project.py` | Pytest test suite covering the core helper functions with multiple test cases each. |
| `requirements.txt` | Lists `pandas` and `requests` as pip-installable dependencies. |

## Design Choices

**Pandas for data handling.** While the standard library's `csv` module could parse the files, pandas provides vectorized operations that make filtering, grouping, and aggregation concise and readable. A single `df.groupby().sum().sort_values()` replaces what would otherwise be 15+ lines of manual dictionary loops.

**No global variables.** All data (DataFrames, selected profile) is passed into functions as arguments. This keeps each function self-contained, testable, and free of hidden dependencies — a core CS50P requirement.

**Functions return data, not strings.** Analysis functions like `mostWatchedSeries` and `mostWatchedMovies` return pandas Series objects rather than pre-formatted strings. The formatting (hours/minutes conversion, ranking numbers) happens at the call site in `selector()`. This separation means the analysis logic can be tested independently of presentation.

**Separating series from movies.** Rather than relying on Netflix's own categorization (which isn't always present in exports), the program checks for the word "Episode" in each title. TV show titles follow the pattern `Show Name: Season X: Episode Title (Episode N)`, while movies lack "Episode" entirely. This simple heuristic works reliably across the entire Netflix catalog.

**Graceful currency conversion.** The USD-to-PYG conversion uses a free exchange rate API with a try/except block. If the request fails (no internet, API down, rate limit), the program prints a friendly message instead of crashing and still shows the original USD amount.

**Profile-first design.** The profile picker appears before the analysis menu and can be returned to at any time (option 6). This avoids the frustration of having to restart the program to switch profiles.

## Acknowledgements

- CS50P — Harvard University's Introduction to Programming with Python
- [Exchange Rate API](https://open.er-api.com/) — free currency conversion data
- Netflix — for providing downloadable personal data
