# Random_Keys_Generator_LF

## Technologies Used
* Django
* SQLite3
* Redis
* Celery

## Database Partitions
* RandomKey - Containing all generated API Keys
* AvailableKey - Containing API Keys available to serve

## API Endpoints
* /api/generate (GET) - Generating new random API Key
* /api/serve (GET) - Serving avaiable API Key
* /api/unblock (POST) - Unblocking an API Key
* /api/delete (POST) - Deleting(Purging) an API Key
* /api/keep_alive (POST) - Reclocking existing API Key so it doesn't get deleted

## Periodic Tasks
* check_last_alive() - Runs every 1 minute on a separate thread to delete(permanently)
API Keys who has not received a keep alive in the last 5 minutes
* I haven't implemented Rule 1 due to the following doubt,
"It says that a user should revert back every 5 minutes to keep a Key intact (or
to keep it blocked so it is not reassigned). But Rule 1 asks to release blocked keys
within 60 secs. Isn't it contradicting; I mean if blocked keys are released within 60 secs,
it doesn't give the user a chance at calling endpoint R5 to keep the Key intact."

## Screenshots
* Generating API Key
  ![](/screenshots/generate.PNG)
* Serving API Key
  ![](/screenshots/serve.PNG)
* Unblocking API Key
  ![](/screenshots/unblock.PNG)
* Deleting API Key
  ![](/screenshots/delete.PNG)
* Reclocking existing API Key
  ![](/screenshots/keep_alive.PNG)
