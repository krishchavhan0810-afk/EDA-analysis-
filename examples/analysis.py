import pandas as pd
import sweetviz as sv
from ydata_profiling.utils.cache import cache_file  # you can reuse your cache logic if needed

if __name__ == "__main__":
    file_name = cache_file(
        "titanic.csv",
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
    )

    df = pd.read_csv(file_name)

    report = sv.analyze(df, target_feat=None)  # or set target_feat="Survived" etc
    report.show_html("titanic_sweetviz_report.html")  # writes the report to an HTML file
