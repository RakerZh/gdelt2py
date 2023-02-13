import pandas as pd
import copy
import os

# https://stackoverflow.com/a/74115867
def find_all_words(data, list_of_words,column_name):
    function = lambda row: all(word in row for word in list_of_words)

    return data.loc[data[column_name].apply(function)]

def find_any_words(data, list_of_words,column_name):
    function = lambda row: any(word in row for word in list_of_words)

    # add flags to the dataframe
    if column_name == "V2Themes":
        data_flags = data.loc[data[column_name].apply(function)].copy()
        flags = [ i+"_flag" for i in list_of_words]
        for word, flag in zip(list_of_words, flags):
            data_flags[flag] = data_flags[column_name].str.contains(word)
        return data_flags

    return data.loc[data[column_name].apply(function)]

def find_one_word(data, word,column_name):
    function = lambda row: (word in row)

    return data.loc[data[column_name].apply(function)]

class Task():
    init_filter = {"V2Locations":[[],[]],"V2Themes":[[],[]]}

    def __init__(self,files=[], mode="default", filter_dict=init_filter):
        self.files = files
        self.filter = filter_dict
        if mode not in ["default", "themes", "locations", "both"]:
            raise ValueError("Invalid mode. Only accept 'all', 'themes', 'locations', 'both'")
        self.mode  =  mode
        self.themes_check = False
        self.locations_check = False

    def file_list(self,files):
        self.files = files

    # TODO: Implement optional parameter

    def filtered(self,themes=[],locations=[],optional=False):
        index = 0

        if optional:
            index = 1

        if locations != []:
            self.filter['V2Locations'][index] = locations + self.filter['V2Locations'][index]
            self.locations_check = True
        if themes != []:
            self.filter['V2Themes'][index] = themes + self.filter['V2Themes'][index]
            self.themes_check = True

        if self.themes_check and self.locations_check:
            self.mode = "both"
        elif self.themes_check:
            self.mode = "themes"
        elif self.locations_check:
            self.mode = "locations"
        else:
            self.mode = "default"

    def copy(self):
        return copy.copy(self)

    def to_csv(self,name):
        pd.options.mode.chained_assignment = None
        for i in self.files:
            df = pd.read_csv(i,encoding="latin1",delimiter="\t", names=[
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
            df_out = df

            if self.mode == "default":
                df_out.to_csv(f"{name}.csv",mode="a",header=False,index=False)

            if self.mode == "themes" or self.mode == "both":
                df_out["V2Themes"] = df_out["V2Themes"].astype(str)

                if self.filter['V2Themes'][0] != []:
                    df_out = find_all_words(df_out,self.filter["V2Themes"][0],"V2Themes")

                if self.filter['V2Themes'][1] != []:
                    df_out = find_any_words(df_out,self.filter["V2Themes"][1],"V2Themes")

                if self.mode == "themes":
                    df_out.to_csv(f"{name}.csv",mode="a",header=False,index=False)

            if self.mode == "locations" or self.mode == "both":
                df_out["V2Locations"] = df_out["V2Locations"].astype(str)


                if self.filter['V2Locations'][0] != []:
                    df_out = find_all_words(df_out,self.filter["V2Locations"][0],"V2Locations")

                if self.filter['V2Locations'][1] != []:
                    for location in self.filter['V2Locations'][1]:
                        df_country = find_one_word(df_out,location,"V2Locations")
                        df_country.to_csv(f"{name} {location}.csv",mode="a",header=False,index=False)
                else:
                    df_out.to_csv(f"{name}.csv",mode="a",header=False,index=False)

            os.remove(i)
