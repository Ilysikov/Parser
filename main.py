import os
from save_file import CallSave
from manage.create_wd import CreateWd
from manage.pubs_manage import Pubs
from manage.rubs_manage import Rubs
import json


def collecting_links():
    wd = CreateWd()
    rubs = Rubs(wd)
    list_rubs = rubs.all_rubs()
    for pub in list_rubs:
        pubs = Pubs(wd, pub['href'], pub['name'])
        pubs.create_list_state()
        pub["state"] = pubs.all_pubs()
    return rubs.all_rubs()


def save_to_json(links):
    if not os.path.exists('../CSM/catalog/'):
        os.makedirs('../CSM/catalog/', exist_ok=True)
    with open(f'../CSM/catalog/list_rubs.json', 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    all_links = collecting_links()
    save_to_json(all_links)
    CallSave('html')
    CallSave('pdf')
    CallSave('page')
    CallSave('doc')
    CallSave('photo')
    CallSave('soup')
