import pychrome
import time
from bs4 import BeautifulSoup

def function():
    document = tab.call_method("DOM.getDocument")
    root_node_id = document["root"]["nodeId"]

    html_content = tab.call_method("DOM.getOuterHTML", nodeId=root_node_id)["outerHTML"]
    print("Fetching updated HTML content...")
    with open('templates/index.html', 'w', encoding='utf8') as f:
        soup = BeautifulSoup(html_content, 'html.parser')
        input_tag = soup.find('div', {'class': 'flex flex-col text-sm md:pb-9'})
        if input_tag:
            f.write(str(input_tag))
        else:
            f.write("No matching content found.")

    print("HTML content updated. Sleeping for 5 seconds...")

browser = pychrome.Browser(url="http://127.0.0.1:9222")
targets = browser.list_tab()
if not targets:
    print("No active tabs found. Please open a tab in Chrome.")
    exit()

tab = targets[0]
tab.start()

try:
    tab.call_method("DOM.enable")

    while True:
        function()
        time.sleep(5)  # Wait for 5 seconds before the next update

except pychrome.exceptions.CallMethodException as e:
    print("Error occurred:", e)
finally:
    tab.stop()
