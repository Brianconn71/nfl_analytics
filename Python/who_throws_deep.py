import pandas as pd
import nfl_data_py as nfl

# import the play by play data
pbp_py = nfl.import_pbp_data([2021])

## need to filter the data to only include plays where the ball is thrown in the air as a pass
fliter = 'play_type == "pass" & air_yards.notnull()'

# group the returned filet data by passer id and passer of the ball before aggregating the data in a python dictionary usijng .agg()
pbp_py_p = (
    pbp_py.query(filter).groupby(["passer_id", "passer"]).agg({"air_yards": ["count", "mean"]})
)

print(pbp_py_p)
