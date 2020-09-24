import os
import re
from cseothirdparytemplate import app


def thirdpartyexcelauto(data, data_mas):
    def masrules(x):
        x = x.replace("\r\n  \r\n", "\r\n\r\n").replace("\r\n \r\n", "\r\n\r\n").replace("\r\n\r\n\r\n",
                                                                                         "\r\n\r\n").split("\r\n\r\n")
        s = ""
        for i in range(len(x)):
            if re.search(r"^MAS", x[i]):
                s = s + x[i]
            if re.search(r"^WCAG", x[i]):
                s = s + '\r\n\r\n' + x[i]
        return s

    def masrulsdel(x):
        m = masrules(x)
        return x.replace(m, "")

    data["MAS / WCAG References"] = data["Repro Steps"].map(masrules)

    def mascolumn(x):
        x = x.split("\r\n\r\n")
        s = ""
        for i in range(len(x)):
            if re.search(r"^MAS", x[i]):
                s = s + x[i]
        return s

    def wcagcolumn(x):
        x = x.split("\r\n\r\n")
        s = ""
        for i in range(len(x)):
            if re.search(r"^WCAG", x[i]):
                s = s + x[i]
        return s

    def Wcaghyperlink(x):
        x = x.split("\r\n")
        s = ""
        for i in range(len(x)):
            if re.search(r"^https:|^http:|www.", x[i]):
                s = s + x[i]
        return '=HYPERLINK("%s", "%s")' % (s, s)

    def Mashyperlink(x):
        x = x.split("\r\n")
        s = ""
        Mno = ""
        a = ""
        link = ""
        for i in range(len(x)):
            if re.search(r"\d", x[i]):
                s = s + x[i]
            if s != "":
                Mno = re.search(r"\d.\d.\d\d|\d.\d.\d|\d.\d\d|\d.\d", s).group()
                a = data_mas[data_mas['Standard'] == Mno].index[0]
                link = data_mas['link'][a]
        mas = f'=HYPERLINK("{link}", "{s}")'
        if len(mas) > 299:
            return s
        else:
            return mas

    def IDlink(x):
        s = 'https://microsoftit.visualstudio.com/OneITVSO/_workitems/edit/' + str(x)
        Id = str(x)
        return f'=HYPERLINK("{s}", "{Id}")'

    data['S.No'] = list(range(1, data.shape[0] + 1))
    data['Attachment'] = data.ID.map(lambda x: 'Please refer the attachment folder: ' + str(x))
    data["Repro Steps"] = data["Repro Steps"].map(masrulsdel)
    data["MAS Rules"] = data["MAS / WCAG References"].map(mascolumn)
    data["WCAG Rules"] = data["MAS / WCAG References"].map(wcagcolumn)
    data["WCAG Reference"] = data["WCAG Rules"].apply(lambda x: Wcaghyperlink(x))
    data["MAS Reference"] = data["MAS Rules"].apply(lambda x: Mashyperlink(x))
    data['ID'] = data['ID'].apply(lambda x: IDlink(x))

    column_titles = ['S.No', 'ID', 'Title', 'Repro Steps', 'Attachment', 'MAS / WCAG References', 'MAS Reference',
                     'WCAG Reference', 'Severity', 'State', 'Tags']
    data = data.reindex(columns=column_titles)
    path = os.path.join(app.root_path, 'static/data', 'Data_Updated.xlsx')
    data.to_excel(path, index=False)
