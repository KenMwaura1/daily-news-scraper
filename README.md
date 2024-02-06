# Daily-news-scraper

Ths is a simple web scraper utilizing [newspaper3k](https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#) to scrape news articles and send them via text.
Currently, it scrapes 2 sources: [Business Daily](https://www.businessdailyafrica.com/) and [Standard media](https://www.standardmedia.co.ke/)

The Script then sends top 3 headlines with links to the specified `mobile_number` in the `.env

## Prerequisites

This project also uses an .env file to store the API key, username and mobile number
Both can be obtained by [signing up/logging into Africas Talking](https://www.account.africastalking.com/)
An env example is provided for reference.

## Step 1

Clone this repo to a suitable location.

`git clone https://github.com/KenMwaura1/daily-news-scraper`

OR

Download the zip and extract it.

## Step 2

Change into the directory.

`cd daily-news-scraper`

## Step 3

Create a virtual environment (venv) to hold all of the required dependecies.Here we use
the built-in venv module.
  
`python -m venv env`

Activate the virtual environment

`source env/bin/activate`

Alternatively if you are using [pyenv](https://github.com/pyenv/pyenv)

```shell
pyenv virtualenv daily-news-scraper
pyenv activate daily-news-scraper
   ```

## Step 4

Install the required dependencies:

`pip install -r requirements`  

## Step 5

Create `.env` file and add your credentials as specified.

`touch .env`

OR

Copy the provided  example and edit as required:

`cp .env-example env`

## Step 6

Run the script

`python news_scraper.py`
