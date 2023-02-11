import pandas as pd
import os
import glob
from typing import List,Union

class Task():
    init_filter = {"V2Locations":[],"V2Themes":[]}

    def __init__(self,files=[], mode="date", filter_dict=init_filter,filter_optional = init_filter):
        self.files = files
        self.mode  =  mode
        self.filter = filter_dict
        self.filter_optional = filter_optional

    def file_list(self,files):
        self.files = files

    def filtered(self,locations : List,themes : List):
        self.filter['V2Locations'] = locations + self.filter['V2Locations']
        self.filter['V2Themes'] = themes + self.filter['V2Themes']

    def filtered_optional(self, themes: Union[None,List], locations : Union[None,List]):
        self.filter_optional['V2Themes'] = themes + self.filter_optional['V2Themes']
        self.filter_optional['V2Locations'] = locations + self.filter_optional['V2Locations']

    def to_csv(self,name):
        for i in self.files:
            df = pd.read_csv(i,engine="pyarrow",encoding="latin1",delimiter="\t", names=[

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

            count = []
            df_date = df
            # df_date = df[df['V2Themes'].isin(self.filter_optional['V2Themes']) ]

            for labels,values in self.filter.items():
                if len(values) != 0:
                    count.append(labels)

            if len(count) == 0 and len(self.filter_optional["V2Themes"]) == 0:
                print("None")
                # df_date.to_csv(f"{name}.csv")
            else:
                for label in count:
                    for j in self.filter[label]:
                        df_country = df_date[df_date[label].str.contains(j)]
                        df_country.to_csv(f"{name} {j}.csv",mode="a",header=False,index=False)
            os.remove(i)
