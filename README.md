# Football Dashboard Webhook



# Football Data Webhook Automation

This automation script is designed to trigger a webhook whenever new matches are played in the top 5 football leagues. It uses the Football Data API to fetch match data and compares it with the previously fetched data to determine if any new matches have been played.
And sends a post call to https://fbtransfersdashboard.azurewebsites.net/refresh_dashboard to trigger updating the dashbaord.

## Installation


1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Football Data API key:

   - Obtain an API key from [Football Data API](https://www.football-data.org/)
   - Replace 'API_TOKEN'` in the `Headers` dictionary with your API key.



## Workflow Configuration

The automation script is configured using Cron job & GitHub Actions During Football Season. The workflow file `.github/workflows/run-automation-script.yml` contains the schedule configuration and the steps to run the script.

## File Descriptions

- `main.py`: Contains the main logic for triggering the webhook based on new match data.
- `ids_count.json`: Stores the count of match IDs to compare with new data.
- `README.md`: This file, containing information about the project and how to use it.
- `requirements.txt`: Contains the list of required Python packages.

## Troubleshooting

If the webhook fails to trigger or if there are issues with the script, check the following:

- Ensure that the Football Data API key is correctly configured.
- Check the log file `main.log` for any error messages.
- Verify that the GitHub Actions workflow is correctly configured and running as expected.
```

