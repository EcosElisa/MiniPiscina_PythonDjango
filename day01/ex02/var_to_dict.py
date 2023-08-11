def my_dictionary():
    d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')
    ]

    dic = {}
    for musician, year in d:
        if year in dic:
            dic[year] += " " + musician
        else:
            dic[year] = musician

    for item in dic:
        print(f"{item} : {dic[item]}")

if __name__ == '__main__':
    my_dictionary()
