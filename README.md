# gdelt2py

`gdelt2py` is package to help you download the data from gdelt2 gkg data. 

## Install

`pip install gdelt2py`

## Usage

- download gkg_data.csv under your directory
- main.py
```txt
.
├── main.py
└── gkg_data.csv
```

- in `main.py`

```python
from gdelt2py import Gdelt2

t = Gdelt2()
t.required(themes=["WB_678_DIGITAL_GOVERNMENT"])
t.optional(locations=["#JA#","#CG#","#AG#","#US#"])
t.download_files()

```

- `start_date`: 
    - The beginning date, in format with '20201020'
    - optional default: '20201020'

- `end_date`: 
    - The end date, same format
    - optional default: latest date in gdelt2

- `themes`: 
    - Currently this package only supports gkg but will support another later.
    - default: 'gkg'

- `out_file`:
    - The name of the output file name like "output.csv"
    - default: 'output.csv'

- `data_dir`:
    - The data directory for your file downloads
    - default: current directory


*Note*
- 20170725 data is missing in gdelt2.



## Gdelt2 data format

[The Gdelt Global Knowledge Graph (GKG) Data format Codebook v2.1](http://data.gdeltproject.org/documentation/GDELT-Global_Knowledge_Graph_Codebook-V2.1.pdf)


- `GKGRecordId`
    - YYYYMMDDHHMMSS-X
        - Example:  The fifth GKG record generated in 3:30AM on February 3, 2015. 20150203033000-5
    - YYYYMMDDHHMMSS-TX
        - 20150203033000-T5 French-language document

- `Date`
    - YYYYMMDD (GKG2.0)
    - YYYYMMDDHHMMSS (GKG2.1)

- `SourceIdentifier`
    - 1: WEB (The document originates from the open web and the DocumentIdentifier is a fully-qualified URL that can be used to access the document on the web).
    - 2: CITATIONONLY (The document originates from a broadcast, print, or other offline source in which only a textual citation is available for the document. In this case the DocumentIdentifier contains the textual citation for the document).
    - 3: CORE (The document originates from the CORE archive and the DocumentIdentifier contains its DOI, suitable for accessing the original document through the CORE website). 
    - 4: DTIC (The document originates from the DTIC archive and the DocumentIdentifier contains its DOI, suitable for accessing the original document through the DTIC website).
    - 5: JSTOR (The document originates from the JSTOR archive and the DocumentIdentifier contains its DOI, suitable for accessing the original document through your JSTOR
subscription if your institution subscribes to it).
    - 6: NONTEXTUALSOURCE (The document originates from a textual proxy (such as closed
captioning) of a non-textual information source (such as a video) available via a URL and the DocumentIdentifier provides the URL of the non-textual original source. At present, this Collection Identifier is used for processing of the closed captioning streams of the Internet Archive Television News Archive in which each broadcast is available via a URL, but the URL offers access only to the video of the broadcast and does not provide any access to the textual closed captioning used to generate the metadata. This code is used in order to draw a distinction between URL-based textual material (Collection Identifier 1 (WEB) and URL-based non-textual material like the Television News Archive).

- `SourceCommonName`

- `DocumentIdentifier`

- `V1Counts`
    - AFFECT, ARREST, KIDNAP, KILL, PROTEST, SEIZE, or WOUND
    - Count Number
    - Object Type
    - Location Type
    - Location FullName
    - Location CountryCode
    - Location ADM1Code
    - Location Latitude
    - Location Longitude
    - Location FeatureID

- `V2Counts`

- `V1Themes`
    - [GKG V1](http://data.gdeltproject.org/documentation/GKG-MASTER-THEMELIST.TXT)
- `V2Themes` 
    - [GKG V2](http://data.gdeltproject.org/api/v2/guides/LOOKUP-GKGTHEMES.TXT)

- `V1Locations`
- `V2Locations`
- `V1Persons`
- `V2Persons`
- `V1_Organizations`
- `V2_Organizations`
- `Tone`
- `V2EnhancedDate`
- `GCAM`
- `urlImage`
- `urlImageRelated`
- `urlSocialMediaImageEmbeds`
- `urlSocialMediaVideoEmbeds`
- `quotations`
- `V2AllNames`
- `V2Amounts`
- `V2TranslationInfo`
- `xmlExtras`


