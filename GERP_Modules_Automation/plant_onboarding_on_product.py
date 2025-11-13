from Setup import *


# driver, wait, actions = setup_driver()
# domain = "https://app.release.gensomerp.com"
# login(driver, domain)


file_path = "C:\Automation\GERP\project_details.xlsx"
df = pd.read_excel(file_path, "plant")
data_list = df.to_dict(orient="records")

for item in data_list:
    project_name = item.get("project_name")


    for i in range(1, 501):  # Loop from 1 to 500
        print(f"DEMO-{project_name}-{i:03d}")
        p_id = project_name.replace(" ","")
        project_id = (f'{i:03d}{p_id}')
        print(project_id)

        # time.sleep(1)






