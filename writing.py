import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from links import *

def update_values(spreadsheet_id, range_name, value_input_option, _values):
  
  creds, _ = google.auth.default()
  # pylint: disable=maybe-no-member
  try:
    service = build("sheets", "v4", credentials=creds)
    values = [
        [
            # Cell values ...
        ],
        # Additional rows ...
    ]
    body = {"values": values}
    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body=body,
        )
        .execute()
    )
    print(f"{result.get('updatedCells')} cells updated.")
    return result
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error


if __name__ == "__main__":
  # Pass: spreadsheet_id,  range_name, value_input_option and  _values
  update_values(
      SAMPLE_SPREADSHEET_ID,
      "A1:C2",
      "USER_ENTERED",
      [["A", "B"], ["C", "D"]],
  )