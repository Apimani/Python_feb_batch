import pandas as pd
from ydata_profiling import ProfileReport
df = pd.read_csv(r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\Files\Employee.csv")

profile = ProfileReport(df)

#profile.to_html()


profile.to_file(r"C:\Users\A4952\Downloads\Python_feb_batch-20240218T160531Z-001\Python_feb_batch\Files\out.html")

