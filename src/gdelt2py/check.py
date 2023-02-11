import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("./temp.csv",engine="pyarrow", encoding='latin1', names=[
"GKGRecordId",	
"Date",	
"SourceIdentifier",
"SourceCommonName",
"DocumentIdentifier",
"V1Counts",
"V2Counts",
"V1Themes",
"V2Themes",
"V1Locations",
"V2Locations",
"V1Persons",
"V2Persons",
"V1Organizations",
"V2Organizations",
"Tone",
"V2EnhancedDate",
"GCAM",
"urlImage",
"urlImageRelated",
"urlSocialMediaImageEmbeds",
"urlSocialMediaVideoEmbeds",
"quotations",
"V2AllNames",
"V2Amounts",
"V2TranslationInfo",
"xmlExtras"])

# Check if every row in the "locations" column contains the string "#JA#"
# result = all(df['locationsCharLoc'].str.contains("#US#"))

# Iterate over the rows of the DataFrame
count = 0
for i, row in df.iterrows():
    # Check if the "locations" column contains the string "#JA#"
    if not "#JA#" in str(row["V2Locations"]):
        print(f"Row {i} does not contain #JA# in the 'V2Locations' column.")

    if not "TAX_FNCACT_RETAILER" in str(row["V2Themes"]):
        print(f"Row {i} does not contain #JA# in the 'V2Themes' column.")
    if not "SMART" in str(row["V2Themes"]):
        print("None")
