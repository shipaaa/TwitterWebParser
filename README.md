# TwitterWebParser

#### Service that searches for tweets by phrase or phrases

### Stack

- [Python](https://www.python.org/downloads/)
- [Tweepy](https://www.tweepy.org)

## Description
Current service has 2 variations

`1. Global search.` — This method looks through all profiles for the last few hours* and searches for tweets that contain phrases that you have specified.\
*You can specify for what specific time you need to find tweets

`2. Search by specific profiles` — This option applies only to certain profiles, you specify the profile username in the code itself, and then the program searches for tweets containing a specific phrase

*Final result of the program outputs information to the telegram chat, namely*
* Time and date of creation of the tweet
* Text of the tweet itself
* Link to the tweet

## Getting Started

1. Clone this repo.

   ```
   git clone https://github.com/shipaaa/TwitterWebParser.git
   ```

2. Create and activate a new virtual environment.

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install packages.

   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Copy .env.example to .env and edit .env file by filling in all environment variables in it.

   ```
   cp code/.env.example code/.env
   ```
