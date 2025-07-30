# Statt ETL Pipeline

## Hey, Welcome to My Project!
This little script pulls data on proposed regulations from the California Office of Administrative Law (OAL) website[](https://oal.ca.gov/proposed-regulations/). The goal was to build a clean ETL pipeline for this assignment, but I hit a snag—the source data doesn't give me the date regulations were first proposed or the full text. I've left the date out to avoid confusion (since it'd just be a fake placeholder), and the full text is empty because it's not available. To make up for it, I added some extra details like the agency and file type to spice things up a bit!

## Getting Started
If you want to try this out on your own machine, here's how to set it up:

### Quick Start (Recommended)
1. Grab the code by cloning the repo: `git clone <repo-url>`
2. Navigate to the project directory: `cd statt_etl_pipeline`
3. Run the setup and execution script: `./run.sh`

That's it! The `run.sh` script will automatically:
- Check if Python 3 is installed
- Check if pip is available
- Create a virtual environment (if needed)
- Install all required packages from requirements.txt
- Run the main.py script

### Manual Setup (Alternative)
If you prefer to set things up manually:
1. Create a virtual environment: `python3 -m venv venv`
2. Activate it—on Mac/Linux, use `source venv/bin/activate`; on Windows, try `venv\Scripts\activate`
3. Install the needed packages: `pip install -r requirements.txt`
4. Run the script: `python3 main.py`

## Running the Script
- **Easy way**: Just run `./run.sh` and it handles everything
- **Manual way**: After manual setup, type `python3 main.py`

You'll see log messages to track progress, and it should finish without a hitch if everything's installed right.

## What You Get
After running, you'll find a file called `proposed_regulations.json` in the folder. It includes:
- **Title**: The name of the regulation (e.g., "Microstamping Performance Standards").
- **Identifier**: A unique code from the OAL (e.g., "2025-0721-01").
- **Full Text**: Left empty because the source table doesn't have it—no PDFs or text links were found.
- **Agency**: Who's behind it (e.g., "Department of Justice"), pulled as a bonus.
- **File Type**: What kind of filing it is (e.g., "File and Print Only (FP)"), another bonus.
- **Source**: Set to "California OAL" for context.
- **Scraped_at**: When I grabbed the data (e.g., "2025-07-29T15:38:25.632751").

## A Few Notes
- **Full Text Issue**: I couldn't get the actual regulation text because the OAL table doesn't link to PDFs or include it directly. This is a limitation of the data source, which fits the assignment's "hard datasets" vibe. I kept the field to show I tackled the requirement, even if it's empty.
- **Date Missing**: The proposal date isn't in the data either, so I skipped it to avoid fake dates that'd confuse things. The assignment lets us be creative with limited info, so I focused on what I could grab.
