import pandas as pd

from pandasql import sqldf

# df=pd.read_csv(r"C:\Users\A4952\PycharmProjects\pythonProject\source_files\Contact_info.csv")

# print(df.head(2))
# print(df.tail(2))
# print(df.describe())

test_data = pd.read_excel(r"C:\Users\A4952\Desktop\template_file.xlsx")

print(test_data.head())

Out = {
    "validation_Type": [],
    "Source_name": [],
    "target_name": [],
    "Number_of_source_Records": [],
    "Number_of_target_Records": [],
    "Number_of_failed_Records": [],
    "column": [],
    "Status": [],
    "source_type": [],
    "target_type": []
}

def col_cnt_check(target, exp_col_cnt):
    actColcnt = target.shape[1]
    print("actual count", actColcnt)
    exp_col_cnt=exp_col_cnt
    if actColcnt == exp_col_cnt:
        print('pas')
    else:
        print("fail")

for index,row in test_data.iterrows():
    print("*"*50)
    print("path",row['file_name'])
    path = row['file_name']
    expected_col_count  = row['expected_col_count']
    print("expected_col_count", row['expected_col_count'])
    target = pd.read_excel(path)
    print(f"file name is {path}")
    col_cnt_check(target, expected_col_count)
    print("*" * 50)



# source = pd.read_csv(r"C:\Users\A4952\PycharmProjects\pythonProject\source_files\Contact_info.csv")
# target = pd.read_csv(r"C:\Users\A4952\PycharmProjects\pythonProject\source_files\Contact_info_t.csv")





def count_val(source, target):
    src_cnt = sqldf("select count(*) count1 from source")
    src_cnt = source.shape[0]
    tgt_cnt = target.shape[0]
    tgt_cnt = sqldf("select count(*) count1 from target")
    if list(src_cnt.count1) == list(tgt_cnt.count1):
        print("matching")
    else:
        print("count validation failed", src_cnt-tgt_cnt)

def Column_value_val(source, target):
    Mismatch_S_T = sqldf("select *  from source except select *  from target")
    Mismatch_T_S = sqldf("select *  from target except select *  from source")
    print("Mismatch records between source and target")
    print(Mismatch_S_T)
    print("Mismatch records between target and source")
    print(Mismatch_T_S)
    source.compare(target)

#Column_value_val(source, target )

def duplicate(target, key_column ):
    duplicate = sqldf(f'''select {key_column}, count(*)  from target"
                       group by {key_column} having count(*)>1''')
    if duplicate.shape[0]>0:
        print("duplicates")
    else:
        print("no duplicates")
#duplicate(target,'identifier')




