# Daily email

Email contains
- Today's weather and temperature
- Joke of the day
- Quote of the day
- more?

## Local project setup

- Create a virtual environment with Python 3.8 and activate it
- `pip install -r requirements.txt`
- Create a copy of `.env-sample` and rename it to `.env`
- Update values in `.env` for your email/password and coordinates
  - Put data in this file that you don't want to make public. Don't commit it to git.

### Run the code
`python daily_email/main.py {your_name}`

## Python Anywhere setup

### Get the code
1. From the homepage, go to **Consoles**  and open a new **Bash Console**
2. In the terminal, clone this repository `git clone <repo_url>`
3. Navigate into the project folder `cd daily_email_project`

### Install project requirements
4. Install the requirements `pip3.8 install --user -r requirements.txt`
   - You must use the `--user` flag to install your own modules in PythonAnywhere

### Set your secret variables
5. From the homepage, go to the **Files**
6. Open up the `daily_email_project` directory
7. Open the `.env-sample` file
8. Click **Save as...** and rename to `.env`
9. Fill in your info and save

### Create a scheduled task
10. From the homepage, go to **Tasks**
11. Create a new task with details:
    - *Frequency*: Daily
    - *Time*: Current server time + 1 minute
    - *Command*: python3.8 /home/<your_username>/daily_email_project/daily_email/main.py <Your name>
    - *Description*: Daily email
12. Save the task
13. See the console logs for print messages or errors
14. Once errors are resolved, set the task time for the morning and you're done!

## Troubleshooting

### SMTPAuthenticationError

<pre style="color: #EE3344; background-color:#F1F3F5FF; padding: 8px; font-size: 14px;">
smtplib.SMTPAuthenticationError:
Please log in via your web browser and then try again.
Learn more at https://support.google.com/mail/answer/78754
</pre>

You must create a Google app password to log into your Gmail account.

1. [Turn on 2-Step verification](https://support.google.com/accounts/answer/185839)
2. [Create an app password](https://support.google.com/accounts/answer/185833)
3. Use that password as the `GMAIL_PASSWORD` in your `.env` file

### ProxyError or OSError

<pre style="color: #EE3344; background-color:#F1F3F5FF; padding: 8px; font-size: 14px;">
requests.exceptions.ProxyError: HTTPSConnectionPool(host='api.jokes.one', port=443):
Max retries exceeded with url: /jod 
(Caused by ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 403 Forbidden')))
</pre>

The API you are requesting isn't on Python Anywhere's [list of allowed URLs](https://www.pythonanywhere.com/whitelist/).

[Read more about their policy](https://help.pythonanywhere.com/pages/RequestingWhitelistAdditions/).

To request that your API be added to the list of allowed URLs:
1. Send a message through the "Send feedback" button in the header
2. Send an email to info@pythonanywhere.com

Make sure to include:
- a link to the API documentation. Particularly to documentation that states the domain where the API is published.
  - e.g. https://jokes.one/api/joke/
- the domain or domains (including subdomains) that the API is served from.
  - e.g. https://api.jokes.one/

You will probably want to wrap each API call in a `try` block 
so that successful calls get sent in an email and unsuccessful ones get printed to the console.

## License

This project has no license. See the [LICENSE](LICENSE.txt) file for more details.

You can choose a license from https://choosealicense.com/.
Replace contents of [LICENSE](LICENSE.txt) with the license content.
