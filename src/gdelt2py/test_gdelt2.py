from gdelt2 import Gdelt2

t = Gdelt2()
t.required(themes=["WB_678_DIGITAL_GOVERNMENT"])
t.optional(locations=["#JA#","#CG#","#AG#","#US#"])
t.download_files()
