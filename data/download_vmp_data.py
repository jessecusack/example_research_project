from urllib.request import urlretrieve

url = "https://www.dropbox.com/s/hb6cy36jq6687qn/vmp_profile_SPAMEX_2014.mat?dl=1"

print(
    f"""Downloading:
{url}"""
)

urlretrieve(url, "external/vmp_profile_SPAMEX_2014.mat")
