import time
import datetime
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()


def connent_url(UrlPath):
    Data_List = []  # 存放获取到的数据
    df = pd.read_csv(UrlPath)

    i = 1
    for url in df:
        driver.get(url)
        time.sleep(5)
        js = 'window.scrollBy(0,10000)'
        driver.execute_script(js)
        page = 0
        flag = True
        while flag:
            try:
                btn = driver.find_element_by_class_name(
                    'css-vsuiox').find_element_by_tag_name('button')
                btn.click()
                time.sleep(1)
                page += 1
                print('Fetching data on page {}！！！'.format(page))
            except:
                flag = False
        else:
            print('The page is loaded and data is being obtained！！！')
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            lis = soup.find_all(
                'li', {'class': 'css-1l4w6pd'})

            for li in lis:
                data_list = []
                date = li.find('span', {'class': 'css-17ubb9w'})['aria-label']
                if len(date.split(' ')) < 3:
                    date = date + str(',2020')
                data_list.append(date)  # 时间
                nature = li.find('p', {'class': 'css-myxawk'}).get_text()
                data_list.append(nature)  # 新闻性质
                news_title = li.find('h4', {'class': 'css-2fgx4k'}).get_text()
                data_list.append(news_title)  # 新闻标题
                news_Abstract = li.find(
                    'div', {'class': 'css-e1lvw9'}).get_text()
                data_list.append(
                    str(news_Abstract).strip().replace('\n', ''))  # 新闻摘要
                Data_List.append(data_list)
        print('第 {} 个URL信息已获取完毕。'.format(i))
        i = i + 1

    driver.close()

    Data_List_New = []
    for data in Data_List:
        if data not in Data_List_New:
            Data_List_New.append(data)
    return Data_List_New


def Save_Data(UrlPath):
    Data_List_New = connent_url(UrlPath=UrlPath)
    print('共爬取了{}条数据。'.format(len(Data_List_New)))
    df_Sheet = pd.DataFrame(Data_List_New, columns=[
                            'date', 'nature', 'news_title', 'news_Abstract'])
    print('Get data successfully!!!')

    TIMEFORMAT = '%Y-%m-%d %H:%M:%S'
    now = datetime.datetime.now().strftime(TIMEFORMAT)
    csv_path = 'New_York_Times_Crawler/New_York_Times_Data/New_York_Times_Data(' + \
        now + ').csv'
    df_Sheet.to_csv(csv_path)

    excel_path = 'New_York_Times_Crawler/New_York_Times_Data/New_York_Times_Data(' + \
        now + ').xlsx'
    writer = pd.ExcelWriter(excel_path)
    df_Sheet.to_excel(excel_writer=writer,
                      sheet_name='New_York_Times', index=None)
    writer.save()
    print('Save - successfully!!!')
    writer.close()
    print('Close - successfully!!!')


def Run():
    Save_Data(UrlPath='New_York_Times_Crawler/news_url.txt')


if __name__ == '__main__':
    Run()
