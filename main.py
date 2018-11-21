import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

URL = "https://www.tutorialspoint.com/oracle_terminal_online.php"
TA = ".ace_text-input"
EXECUTE = "#execute"
TABLE = "#eastcover table"
FILE = "markdown.md"

COMMANDS = [
    "select * from emp;",
    "select ename, msal from emp where msal > 2000;",
    "select * from emp where ename like 'S%';",
    "select * from emp where ename like '%S';",
    "select * from emp where ename like '_L%';",
    "select * from emp where comm != 0;",
    "select ename \"Name\", msal \"Salary\"  from emp;"
]


def exec_sql(command):
    driver = webdriver.Chrome()
    driver.get(URL)
    elem = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, TA)))
    elem.send_keys(Keys.CONTROL, "a")
    elem.send_keys(command)
    elem = driver.find_element_by_css_selector(EXECUTE)
    elem.click()
    elem = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, TABLE)))
    return elem.get_attribute('outerHTML')


def html2md(html):
    md = ""
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select("tr")
    for i in range(0, rows.__len__()):
        elems = rows[i].select("td")
        if i == 0:
            elems = rows[i].select("th")
        for j in range(0, elems.__len__()):
            md += "|" + elems[j].text.strip(" ").strip("\n").strip(" ").strip("	")
            if j == elems.__len__() - 1:
                md += "|"
        md += "\n"
        if i == 0:
            for j in range(0, elems.__len__()):
                md += "|-"
                if j == elems.__len__() - 1:
                    md += "|"
            md += "\n"
    return md


if os.path.exists(FILE):
    os.remove(FILE)

for i in range(0, COMMANDS.__len__()):
    command = COMMANDS[i]
    data = "## %s. `%s`\n" % (str(i + 1), command) + html2md(exec_sql(command))
    open(FILE, "a").write(data)
