from reykunyu_py import reykunyu
import requests

response = reykunyu.request("oel ngati kameie")

# all = requests.get("https://reykunyu.wimiso.nl/api/frau").json()
# for entry in all:
#     try:
#         if len(all.get(entry).get("pronunciation")) > 1:
#             print(entry)
#     except TypeError:
#         pass

for entry in response.entries():
    print(entry.best_answer().best_pronunciation().get())
