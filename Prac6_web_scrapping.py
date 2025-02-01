# import requests
# from bs4 import BeautifulSoup
# import re
# # def webscrap(url):
    
# #     response = requests.get(url)
# #     print(response)
# #     content = response.text
# #     print(content)
    
# #     bs = BeautifulSoup(content, "html.parser")
    
# #     tags = ['h1', 'h2', 'h2', 'title']
    
# #     for tags in bs.find_all(tags):
# #         print(f"tag name: {tags.name}, tag text: {tags.text.strip()}")

# # webscrap("https://realpython.github.io/fake-jobs/")


# def webscrap(url):
#     response = requests.get(url)
#     print(response.text)
#     soup = BeautifulSoup(response.text, "html.parser")
    
#     product_element = soup.find("div", class_="product-price")
#     print(product_element)
    
#     if product_element:
#         price_text = product_element.text
#         print(price_text)
#         match = re.search(r"\d+\.\d+", price_text)
#         if match:
#             price = match.group(0)
#             print(f"Price: {price}")
#         else:
#             print("Price pattern not found")
#     else:
#         print("Product element not found")

# webscrap("https://www.amazon.in/Lamper-Zenora-Furniture-Included-Premium/dp/B0DJ69K9KK/?_encoding=UTF8&pd_rd_w=Ul8v7&content-id=amzn1.sym.f93d7a1d-c570-4a72-8d9f-cc9d645b346f&pf_rd_p=f93d7a1d-c570-4a72-8d9f-cc9d645b346f&pf_rd_r=FKQSERTEFH1K60CWM4XX&pd_rd_wg=pmzAG&pd_rd_r=5c23bbec-e45f-41f2-8fa1-b7bb70ad0136&ref_=pd_hp_d_btf_LPDEALS&th=1")




def webscrap_news(url):
    
    return
webscrap("")