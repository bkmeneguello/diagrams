import os
import requests
import zipfile
import tempfile
from os import path

def resources(z):
    for f in z.namelist():
        _, ext = path.splitext(f)
        dirname, basename = path.split(f)
        _, dirname = path.split(dirname)
        if ext == ".svg":
            if basename.startswith("Arch_") and dirname in ("64", "Arch_64"):
                yield f
            if basename.startswith("Res_") and dirname == "Res_48_Light":
                yield f

def fix_name(f):
    p = f.split("/")[2:]
    p[0] = p[0].replace("Res_", "").\
        replace("Arch_", "").\
        replace("- ", "-").\
        replace("_", "-").\
        lower().\
        replace("app-integration", "integration").\
        replace("application-integration", "integration").\
        replace("ar-vr", "arvr").\
        replace("business-application", "business").\
        replace("cost-management", "cost").\
        replace("customer-enablement", "enablement").\
        replace("customer-enagagement", "engagement").\
        replace("customer-engagement", "engagement").\
        replace("developer-tools", "devtools").\
        replace("end-user-computing", "enduser").\
        replace("game-tech", "game").\
        replace("general-icons", "general").\
        replace("internet-of-things", "iot").\
        replace("lot", "iot").\
        replace("machine-learning", "ml").\
        replace("management-governance", "management").\
        replace("media-services", "media").\
        replace("migration-and-transfer", "migration").\
        replace("migration-transfer", "migration").\
        replace("networking-and-content-delivery", "network").\
        replace("networking-content", "network").\
        replace("quantum-technologies", "quantum").\
        replace("security-identity-compliance", "security").\
        replace("security-identity-and-compliance", "security")
    p[2] = p[2].replace("Res_", "").\
        replace("Arch_", "").\
        replace("_48_Light", "").\
        replace("_48_Dark", "").\
        replace("_64", "").\
        lower().\
        replace("aws-", "").\
        replace("amazon-", "").\
        replace("&", "and")
    # Underscores separate the subresources
    s = p[2].split("_")
    # Separate package names by underscores
    m = list(map(lambda s: s.replace("-", "_").replace("lambda", "_lambda"), s[:-1]))
    return path.join(p[0].replace("lambda", "_lambda"), *(m + s[-1:]))

tmpfile = path.join(tempfile.gettempdir(), 'aws-assets.zip')
if not os.path.isfile(tmpfile):
    # from https://aws.amazon.com/architecture/icons/
    url = "https://d1.awsstatic.com/webteam/architecture-icons/Q32020/AWS-Architecture-Assets-For-Light-and-Dark-BG_20200911.478ff05b80f909792f7853b1a28de8e28eac67f4.zip"
    r = requests.get(url, allow_redirects=True)
    with open(tmpfile, 'wb') as assets:
        assets.write(r.content)

with zipfile.ZipFile(tmpfile) as z:
    d = {}
    for f in resources(z):
        name = fix_name(f)
        if name in d:
            # some resource names conflicts, pick the shortest (no specific reason)
            if len(f) < len(d[name]):
                d[name] = f
        else:
            d[name] = f

    for name, filename in d.items():
        name = path.join("resources", "aws", name)
        dest = path.dirname(name)
        os.makedirs(dest, exist_ok=True)
        with open(name, 'wb') as tgt:
            tgt.write(z.read(filename))
