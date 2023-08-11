def sort_dic():
    d = {
        'Hendrix':'1942',
        'Allman':'1946',
        'King':'1925',
        'Clapton':'1945',
        'Johnson':'1911',
        'Berry':'1926',
        'Vaughan':'1954',
        'Cooder':'1947',
        'Page':'1944',
        'Elisa':'2000',
        'Hammett':'1962',
        'Cobain':'1967',
        'Garcia':'1942',
        'Beck':'1944',
        'Santana':'1947',
        'Ramone':'1948',
        'White':'1975',
        'Frusciante':'1970',
        'Thompson':'1949',
        'Burton':'1939',
    }
    # usa o lambda para primeiro orderna pelo value (d[k]) e depois pela key(k)
    myKeys = sorted(d, key=lambda k: (d[k], k))

    print(myKeys)

if __name__ == '__main__':
    sort_dic()