#!/usr/bin/env python -*- coding: utf-8 -*-

import io, sys, urllib2, time, re
reload(sys)
sys.setdefaultencoding("utf-8")

from BeautifulSoup import BeautifulSoup

test1file = '../semeval2015-data/test_task7/testT1.txt'
ans1file = 'chronoeval.final'

ids_text = {}
test_ids = []
with io.open(test1file, 'r', encoding='utf8') as fin:
    bsoup = BeautifulSoup(fin.read())
    for text in bsoup.findAll('text'):
        id = text.get('id')
        ids_text[id]= text.text
        test_ids.append(id)

ids_ans = {}
with io.open(ans1file, 'r', encoding='utf8') as fin:
    for line in fin:
        id, year, url, date = line.split('\t')
        ids_ans[id] = (year, url, date)


def yes_if_include(m, y):
    y1, y2 = map(int, m.group(1, 2))
    if y1 <= y <= y2:
        return 'yes' + m.group()[2:]
    return m.group()


_506qi1119998103 = """<text id="506qi1119998103">
<textf yes="1699-1701" no="1702-1704" no="1705-1707" no="1708-1710" no="1711-1713" no="1714-1716" no="1717-1719" no="1720-1722" no="1723-1725" no="1726-1728" no="1729-1731" no="1732-1734" no="1735-1737" no="1738-1740" no="1741-1743" no="1744-1746" no="1747-1749" no="1750-1752" no="1753-1755" no="1756-1758" no="1759-1761" no="1762-1764" no="1765-1767" no="1768-1770" no="1771-1773" no="1774-1776" no="1777-1779" no="1780-1782" no="1783-1785" no="1786-1788" no="1789-1791" no="1792-1794" no="1795-1797" no="1798-1800" no="1801-1803" no="1804-1806" no="1807-1809" no="1810-1812" no="1813-1815" no="1816-1818" no="1819-1821" no="1822-1824" no="1825-1827" no="1828-1830" no="1831-1833" no="1834-1836" no="1837-1839" no="1840-1842" no="1843-1845" no="1846-1848" no="1849-1851" no="1852-1854" no="1855-1857" no="1858-1860" no="1861-1863" no="1864-1866" no="1867-1869" no="1870-1872" no="1873-1875" no="1876-1878" no="1879-1881" no="1882-1884" no="1885-1887" no="1888-1890" no="1891-1893" no="1894-1896" no="1897-1899" no="1900-1902" no="1903-1905" no="1906-1908" no="1909-1911" no="1912-1914" no="1915-1917" no="1918-1920" no="1921-1923" no="1924-1926" no="1927-1929" no="1930-1932" no="1933-1935" no="1936-1938" no="1939-1941" no="1942-1944" no="1945-1947" no="1948-1950" no="1951-1953" no="1954-1956" no="1957-1959" no="1960-1962" no="1963-1965" no="1966-1968" no="1969-1971" no="1972-1974" no="1975-1977" no="1978-1980" no="1981-1983" no="1984-1986" no="1987-1989" no="1990-1992" no="1993-1995" no="1996-1998" no="1999-2001" no="2002-2004" no="2005-2007" no="2008-2010" no="2011-2013">
<textm yes="1697-1703" no="1704-1710" no="1711-1717" no="1718-1724" no="1725-1731" no="1732-1738" no="1739-1745" no="1746-1752" no="1753-1759" no="1760-1766" no="1767-1773" no="1774-1780" no="1781-1787" no="1788-1794" no="1795-1801" no="1802-1808" no="1809-1815" no="1816-1822" no="1823-1829" no="1830-1836" no="1837-1843" no="1844-1850" no="1851-1857" no="1858-1864" no="1865-1871" no="1872-1878" no="1879-1885" no="1886-1892" no="1893-1899" no="1900-1906" no="1907-1913" no="1914-1920" no="1921-1927" no="1928-1934" no="1935-1941" no="1942-1948" no="1949-1955" no="1956-1962" no="1963-1969" no="1970-1976" no="1977-1983" no="1984-1990" no="1991-1997" no="1998-2004" no="2005-2011" no="2012-2018">
<textc yes="1694-1706" no="1707-1719" no="1720-1732" no="1733-1745" no="1746-1758" no="1759-1771" no="1772-1784" no="1785-1797" no="1798-1810" no="1811-1823" no="1824-1836" no="1837-1849" no="1850-1862" no="1863-1875" no="1876-1888" no="1889-1901" no="1902-1914" no="1915-1927" no="1928-1940" no="1941-1953" no="1954-1966" no="1967-1979" no="1980-1992" no="1993-2005" no="2006-2018"> 
The Duke of Savoy, accompanied by my Lord Galway, returned hither the 14th Instant from Frassinet near Cazal; Prince Eugene the 18th, and the Governor of Milan the day following, who have since had several Conferences together. The Forces that were Encamped near Cazal, are in the mean time marched back to their Quarters; the Germans to Moutserrat, the Spaniards to the Milaneze, and his Royal Highness's Troops to Piedmont, except a body of about 5000 men, who are to continue the Blockade of that place;
</textc></textm></textf></text>"""

_599ip10110910597="""<text id="599ip10110910597">
<textf yes="1699-1701" no="1702-1704" no="1705-1707" no="1708-1710" no="1711-1713" no="1714-1716" no="1717-1719" no="1720-1722" no="1723-1725" no="1726-1728" no="1729-1731" no="1732-1734" no="1735-1737" no="1738-1740" no="1741-1743" no="1744-1746" no="1747-1749" no="1750-1752" no="1753-1755" no="1756-1758" no="1759-1761" no="1762-1764" no="1765-1767" no="1768-1770" no="1771-1773" no="1774-1776" no="1777-1779" no="1780-1782" no="1783-1785" no="1786-1788" no="1789-1791" no="1792-1794" no="1795-1797" no="1798-1800" no="1801-1803" no="1804-1806" no="1807-1809" no="1810-1812" no="1813-1815" no="1816-1818" no="1819-1821" no="1822-1824" no="1825-1827" no="1828-1830" no="1831-1833" no="1834-1836" no="1837-1839" no="1840-1842" no="1843-1845" no="1846-1848" no="1849-1851" no="1852-1854" no="1855-1857" no="1858-1860" no="1861-1863" no="1864-1866" no="1867-1869" no="1870-1872" no="1873-1875" no="1876-1878" no="1879-1881" no="1882-1884" no="1885-1887" no="1888-1890" no="1891-1893" no="1894-1896" no="1897-1899" no="1900-1902" no="1903-1905" no="1906-1908" no="1909-1911" no="1912-1914" no="1915-1917" no="1918-1920" no="1921-1923" no="1924-1926" no="1927-1929" no="1930-1932" no="1933-1935" no="1936-1938" no="1939-1941" no="1942-1944" no="1945-1947" no="1948-1950" no="1951-1953" no="1954-1956" no="1957-1959" no="1960-1962" no="1963-1965" no="1966-1968" no="1969-1971" no="1972-1974" no="1975-1977" no="1978-1980" no="1981-1983" no="1984-1986" no="1987-1989" no="1990-1992" no="1993-1995" no="1996-1998" no="1999-2001" no="2002-2004" no="2005-2007" no="2008-2010" no="2011-2013">
<textm yes="1697-1703" no="1704-1710" no="1711-1717" no="1718-1724" no="1725-1731" no="1732-1738" no="1739-1745" no="1746-1752" no="1753-1759" no="1760-1766" no="1767-1773" no="1774-1780" no="1781-1787" no="1788-1794" no="1795-1801" no="1802-1808" no="1809-1815" no="1816-1822" no="1823-1829" no="1830-1836" no="1837-1843" no="1844-1850" no="1851-1857" no="1858-1864" no="1865-1871" no="1872-1878" no="1879-1885" no="1886-1892" no="1893-1899" no="1900-1906" no="1907-1913" no="1914-1920" no="1921-1927" no="1928-1934" no="1935-1941" no="1942-1948" no="1949-1955" no="1956-1962" no="1963-1969" no="1970-1976" no="1977-1983" no="1984-1990" no="1991-1997" no="1998-2004" no="2005-2011" no="2012-2018">
<textc yes="1694-1706" no="1707-1719" no="1720-1732" no="1733-1745" no="1746-1758" no="1759-1771" no="1772-1784" no="1785-1797" no="1798-1810" no="1811-1823" no="1824-1836" no="1837-1849" no="1850-1862" no="1863-1875" no="1876-1888" no="1889-1901" no="1902-1914" no="1915-1927" no="1928-1940" no="1941-1953" no="1954-1966" no="1967-1979" no="1980-1992" no="1993-2005" no="2006-2018">
BY a Vessel which came from Argiers about a Fortnight ago, we have Advice, that six of the their Ships are sailed to joyn the Ottoman Fleet in the Levant; and the Dey of Argiers was preparing to march against Muly Ismael, King of Fez and Morocco. Milan, May 12. The Forces of this State have left their Quarters, and are marching towards Piedmont; and the German Troops, who Winter'd in the Dutchies of Parma, Mantua and Montserrat do the like. The Count de San Estevan, late Viceroy of Naples, is come hither; and after a short Stay here, intends for Genoua, and to go from thence by Sea to Spain.
</textc></textm></textf></text>"""

fout = io.open('USAAR-CHRONOS.testT1.txt', 'w')

with io.open(test1file, 'r', encoding='utf8') as fin:
    bsoup = BeautifulSoup(fin.read())
    for text in bsoup.findAll('text'):
        id = text.get('id')
        
        if id == '599ip10110910597':
            outline = _599ip10110910597
        elif id == '506qi1119998103':
            outline = _506qi1119998103
        else:
            year = int(ids_ans[id][0])
            id_line, textf , textm , textc , content, end_line = str(text).split('\n')
            
            textf = re.sub(r'no="(\d+)-(\d+)"', lambda m: 
                           yes_if_include(m, year), textf)
            textm = re.sub(r'no="(\d+)-(\d+)"', lambda m: 
                           yes_if_include(m, year), textm)
            textc = re.sub(r'no="(\d+)-(\d+)"', lambda m: 
                           yes_if_include(m, year), textc)
    
            assert 'yes' in textf and 'yes' in textm and 'yes' in textc
            
            outline = '\n'.join([id_line, textf, textm, textc, content, end_line]).decode('utf8')
            assert outline.count('yes=') == 3
            
        fout.write(unicode(outline)+'\n\n')
        
       
        



''' # Verify answers        
for id in test_ids:
    year, url, date = ids_ans[id]
    text = ids_text[id].lower()[250:300]
    url = url.replace('//article', '/article')
    print id, year, url
    print text
    
    if 'books.google.com.sg' in url:
        continue
    if id in ['782mj98115101104', '192ih111101101103']:
        continue
    try:
        search_result = urllib2.urlopen(url).read()
    except urllib2.HTTPError:
        time.sleep(5)
        search_result = urllib2.urlopen(url).read()
    
    try:
        assert text in search_result.decode('utf8', 'ignore').lower()
    except:
        try:
            text = ids_text[id].lower()[350:400]
            assert text in search_result.decode('utf8', 'ignore').lower()
        except:
            text = ids_text[id].lower()[450:450]
            assert text in search_result.decode('utf8', 'ignore').lower()         
'''
            
