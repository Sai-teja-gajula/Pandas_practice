#Combine all sheets into a single DataFrame.
#Add a column called "Month" with the sheet name (“Jan”, “Feb”, “Mar”) for each record.
#Check how many rows each sheet has while loading (print a message for each).
#After combining, calculate total revenue per month.
#Export the final monthly summary to a new Excel file called "Monthly_Sales_Summary.xlsx" with one sheet named "Summary".
import pandas as pd
xls= pd.ExcelFile("Store_Sales_2025.xlsx")
frames = []
for sheet in xls.sheet_names:
    df= pd.read_excel(xls,sheet)
    df["Month"]= sheet
    print (f"{sheet} has {len(df)} rows")
    frames.append(df)
all_sheets= pd.concat(frames, ignore_index=True)
final = all_sheets.groupby("Month", as_index= False)["Revenue"].sum()
final.to_excel("Monthly_sales_summary.xlsx", index= False, sheet_name="Summary")
print (final)
