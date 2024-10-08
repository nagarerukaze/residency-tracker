import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class googleSheetsHandler:
    def __init__(self, spreadsheet_id, range_name):
        # If modifying these scopes, delete the file token.json.
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

        # The ID and range of a sample spreadsheet.
        self.SPREADSHEET_ID = spreadsheet_id
        self.RANGE_NAME = range_name
        
        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self.SCOPES
                )
                self.creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open("token.json", "w") as token:
                    token.write(self.creds.to_json())

        try:
            service = build("sheets", "v4", credentials=self.creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = (
                sheet.values()
                .get(spreadsheetId=self.SPREADSHEET_ID, range=self.RANGE_NAME)
                .execute()
            )
            values = result.get("values", [])

            if not values:
                print("No data found.")
            return
        except HttpError as err:
            print(err)

    def editTems(self, rows):
        try:
            service = build("sheets", "v4", credentials=self.creds)

            # Call the Sheets API
            sheet = service.spreadsheets()

            #!!!! SHEETS OPERATIONS HERE!!!!
            values = []
            values.append(rows)
            body = {'values': values}

            result = (
                sheet.values()
                .append(
                        spreadsheetId=self.SPREADSHEET_ID,
                        range=self.RANGE_NAME,
                        valueInputOption="USER_ENTERED",
                        body=body)
                .execute()
            )

            print("Rows Updated: ", result['updates']['updatedRows'])
        except HttpError as err:
            print(err)
            
    def insertRows(self, rows):
        try:
            service = build("sheets", "v4", credentials=self.creds)

            # Call the Sheets API
            sheet = service.spreadsheets()

            #!!!! SHEETS OPERATIONS HERE!!!!
            values = []
            values.append(rows)
            body = {'values': rows}

            # Build the service
            service = build('sheets', 'v4', credentials=self.creds)

            # Use the Sheets API to append the data
            request = service.spreadsheets().values().append(
                spreadsheetId=self.SPREADSHEET_ID,
                range=self.RANGE_NAME,
                valueInputOption='RAW',  # Options: 'RAW' or 'USER_ENTERED'
                insertDataOption='INSERT_ROWS',  # To append data
                body=body
            )
            response = request.execute()

            print("Rows Updated: ", response)
        except HttpError as err:
            print(err)
