import xml.etree.cElementTree as et

tree = et.parse("sample.xml")

root = tree.getroot()
Job_title = []
Company_name = []
City_name = []
Category = []

for title in root.iter('job_title'):
    Job_title.append(title.text)


for company in root.iter('company_name'):
    Company_name.append(company.text)

for city in root.iter('city'):
    City_name.append(city.text)

for category in root.iter('category'):
    Category.append(category.text)

print("Job Title:", Job_title)
print("Company Name:", Company_name)
print("City:", City_name)
print("Category:", Category)