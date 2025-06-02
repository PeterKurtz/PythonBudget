import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from links import *
import sqlite3

def certify():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  return creds

def getSheetValues(creds, sheetName):
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  sheetValues = []
  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=sheetName)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    for v in values:
      sheetValues.append(v)

  except HttpError as err:
    print(err)

  return sheetValues

def writeToSheet(creds, data, range_name):
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        body = {
            "values": data
        }

        result = (
            sheet.values()
            .update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=range_name,
                valueInputOption="RAW",
                body=body,
            )
            .execute()
        )
        print(f"{result.get('updatedCells')} cells updated.")
    except HttpError as err:
        print(err)

def getRegCostsValues(year, month):
  if month == 12:
    nextMonth = 1
    nextYear = year + 1
  else:
    nextMonth = month + 1
    nextYear = year

  sqlQuerry=f"""SELECT rcc.CostCatName, rc.CostDate, rc.Amount, rc.Explanation
                FROM RegularCosts rc
                INNER JOIN RegularCostCat rcc
                  ON rc.CostID = rcc.CostID
                WHERE rc.CostDate >= '{month}/1/{year}'
                  AND rc.CostDate < '{nextMonth}/1/{year}'
                ORDER BY rc.CostDate"""
  
  con = sqlite3.connect("budget.db")
  cur = con.cursor()
  result = cur.execute(sqlQuerry).fetchall()
  con.close()

  return result

values = getRegCostsValues(2025, 4)

creds = certify()

writeToSheet(creds, [("CostCatName", "CostDate", "Amount", "Explanation")], "4/2025!A1")
writeToSheet(creds, values, "4/2025!A2")