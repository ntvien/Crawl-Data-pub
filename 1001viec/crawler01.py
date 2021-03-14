import requests
from bs4 import BeautifulSoup
import json

def trade_spider(max_page):
    count_company=0
    page = 1
    jobs_array = {}
    jobs = []
    while page <= max_page :
        url = "https://1001vieclam.com/search-results-jobs/?searchId=1606639087.9815&action=search&page="+str(page)+"&view=list"
        source = requests.get(url)
        soup = BeautifulSoup(source.text, "html.parser")
        for links in soup.findAll('div', {'class' : 'listing-title'}):
            sub_url = process(str(links))
            jobs.append(get_item(sub_url))
            count_company += 1
        page += 1
        if count_company==2000:
            break

    jobs_array["jobs"] = jobs
    writeJSONFile(jobs_array)
    #printToConsole(jobs)

def get_item(item_url):
    source = requests.get(item_url)
    soup = BeautifulSoup(source.text, "html.parser")
    info = soup.findAll('div', {'class', 'displayFieldBlock'}) #Array info
    job_item = {}
    job_item["Tiêu đề"] = title_process(str(soup.find('div' , {'class' : 'listingInfo'})))
    job_item["Tên công ty"] = company_process(str(soup.find('div',{'class': 'comp-profile-content'})))
    mota = info[len(info)-3]
    job_item["mô tả"] = str(motaa(mota)).replace("[", "").replace("]","")
    job_item["yêu cầu"] = str(yeucau(
        info[len(info)-2])).replace("[", "").replace("]", "").replace("\\xa0", "")
    job_item["quyền lợi"] = str(
        quyenloi(info[len(info)-1])).replace("[", "").replace("]", "")
    job_item["số lượng"] = "1"
    for i in info[0:len(info) - 3]:
        data_array = data_process(str(i))
        for i in range(len(data_array)):
            job_item[data_array[0]] = str(data_array[1]).replace("[", "").replace("]", "")
    tem=filter_data(job_item)
    return tem
def motaa(mota_file):
    value =[]
    x=mota_file.findAll('li')
    for i in x:
        value.append("-"+i.text)
    y=mota_file.findAll('p')
    for i in y:
        value.append(i.text)
    if x == []:
        if y==[]:
            mota_file=str(mota_file)
            a=len(mota_file)
            mota_file=str(mota_file[84:a])
            while (mota_file.find("<br/>")!=-1):
                temp=mota_file.find("<br/>")
                value.append("-"+mota_file[0:temp])
                mota_file=mota_file[temp+4]
    
    return value
def yeucau(mota_file):
    value =[]
    x=mota_file.findAll('li')
    for i in x:
        value.append("-"+i.text)
    y=mota_file.findAll('p')
    for i in y:
        value.append(i.text)
    if x == []:
        if y==[]:
            mota_file=str(mota_file)
            a=len(mota_file)
            mota_file=str(mota_file[85:a])
            while (mota_file.find("<br/>")!=-1):
                temp=mota_file.find("<br/>")
                value.append("-"+mota_file[0:temp])
                mota_file=mota_file[temp+4]
    
    return value
def quyenloi(mota_file):
    value =[]
    x=mota_file.findAll('li')
    for i in x:
        value.append("-"+i.text)
    y=mota_file.findAll('p')
    for i in y:
        value.append(i.text)
    if x == []:
        if y==[]:
            mota_file=str(mota_file)
            a=len(mota_file)
            mota_file=str(mota_file[78:a])
            while (mota_file.find("<br/>")!=-1):
                temp=mota_file.find("<br/>")
                value.append("-"+mota_file[0:temp])
                mota_file=mota_file[temp+4]
    
    return value
def title_process(str_title):
    begin = str_title.find("<h1>") +4
    end = str_title.find("</h1>"  )
    return str_title[begin:end]
def company_process(str_company):
    begin = str_company.find("</div>")+39
    end = str_company.find("</span>")
    return str_company[begin:end]


def data_process(data):
    category = ""
    value =""
    #xx= data.find( "<ul><li>")
    yy= data.find("<!-- <pre>")
    aa= data.find("<!-- <h3>Tỉnh / Thành:</h3> -->")
    date = data.find("<!-- <h3>Ngày đăng:</h3> -->")
    nganh = data.find("<h3>Ngành:</h3>")  
    if nganh!=-1: #ngành
        begin = data.find("<h3>")+4
        middle = data.find("</h3>")
        end = data.find("</div>")
        category=data[begin:middle]
        value=data[middle+32:end]
        x=data.find("\t\t\t\t")
        if x != -1:
            value = [data[middle+32:x]]
            data =data[x+8:end]
            while(data.find("\t\t\t\t") != -1):
                temp = data.find("\t\t\t\t")
                value.append("-" + data[0:temp])
                data = data[temp + 4:]
        return[category,value]

    if yy!=-1:#lương
        begin = data.find("<h3>")+4
        middle = data.find("</h3>")
        end = yy
        category=data[begin:middle]
        value = data[middle+97:end-61]
        return[category,value]
    if aa!=-1:#nơi làm việc
        begin = data.find("<h3>")+4
        middle = data.find("</h3>")
        end = data.find("</div>")
        category=data[begin+len("Tỉnh / Thành:</h3> --><h3>")+1:middle+len("Tỉnh / Thành:</h3> --><h3>")+1]
        value=data[middle+len("Tỉnh / Thành:</h3> --><h3>")+51:end-15]
        return[category,value]

    
     
    if date!=-1:
        return[category,value]
    return[category,value]
def filter_data(dict):
    job = {}
    if "Tiêu đề" in dict:
        job['job_title'] = dict["Tiêu đề"]
    if "Tên công ty" in dict:
        job['company'] = dict['Tên công ty']
    if "Lương:" in dict:
        job['salary'] = dict['Lương:']
    if "Nơi làm việc:" in dict:
        job['location'] = dict['Nơi làm việc:']
    if "Ngành:" in dict:
        job['position'] = dict['Ngành:']
    # if "Ngành:" in dict:
    #     job['Position'] = dict['Ngành:']
    if "mô tả" in dict:
        job['job_description'] = dict['mô tả']
    if "yêu cầu" in dict:
        job['job_requirement'] = dict['yêu cầu']
    if "quyền lợi" in dict:
        job['benefit'] = dict['quyền lợi']
    if "số lượng" in dict:
        job['quantity'] = dict["số lượng"]
    return job 

def writeJSONFile(dictionary):
    # Serializing json  
    json_object = json.dumps(dictionary, indent=len(dictionary.keys()), ensure_ascii=False)

    # Writing to sample.json 
    # with open("sample.json", "a", encoding='utf8') as outfile: 
    #     outfile.write(json_object)

    with open("data1.json", "a", encoding='utf8') as outfile:
        outfile.write(json_object)

def printToConsole(dictionary):
    index = 1
    for i in dictionary:
        print(index)
        for key, value in i.items():
            print(key)
            print(value)
        print("------------------") 
        index += 1

def process(data):
    begin = data.find("href=\"")
    end = data.rfind("\">")
    return data[begin+len("href=\""):end]
trade_spider(100)
