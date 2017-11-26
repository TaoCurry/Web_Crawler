#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

"""
__author__ = "Curry"

from bs4 import BeautifulSoup
import requests
import time

# 网页地址
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_LIST'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'Cookie': 'TAUnique=%1%enc%3A0K2Wy69nxlE74pN4AHInefDuFfEp6RE%2BAkHI6GDglDU2jHwltRJPGQ%3D%3D; TASSK=enc%3AANRh%2Fqus59Ww2N2soFbzhIHuZS%2Bp3aWDCWqkHPdbzEMAritRoBzU5xLDoz9wd4Mx453G4WsF3m5CFQvtVmohG%2BgjCHm%2FT5eVxAxU1XnbygaBCgPF0pCTx13OfGNGumL9Mw%3D%3D; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1511697336125; ServerPool=R; SecureLogin2=3.4%3AAIPAKeezDVAYaAj6Rbw8N1JkjeInGCILs%2FG8PlEkchT%2BOBxQ405dKoU4BkAB9pS02Vc9CXdEzIo6m0ICwXuSuRfpPaEhfuM3QhprqC5Xhb9KArk4wdiQKUGdJlOYdLJOS03RtRDhFNHMPXDYbDg6Az0sQhmkjehycBWK6B324stVSt5aZ1vAAcGc5%2FyScIzqM4u%2FRGF%2BjVJmFUIk%2BZMb%2FiU%3D; TAAuth3=3%3A0cd177e036f25558de67dc0222d5e52a%3AAHxGweSMCrJw%2F0nifg2zCgC62KREWK5StYZ61FPm2G6YR0AsfvUs7cDTrN9UihOmzEgEXzoeg0BhMCBRZQ%2BIoTrjgQtVztThPjao6ui3ara4%2FzeiZUi2D4T2G0ILp0rDDtvUtwO%2FHw5%2Fw1FjinDGWD2PyQLiQ%2FsGYxUsCIFgRInt5%2BBNiIwVzyz0u23FCd9MRQ%3D%3D; CommercePopunder=SuppressAll*1511699694422; _smt_uid=5a117182.4cd4ddae; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCpmPopunder_1%2C1%2C1511786071%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C1%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; roybatty=TNI1625!AMI%2FkSVjIyEI9GH4TOWlTmyFE9Kg87MRaDRMIPAUYJx%2BfErFW2QYBbhhtUa9CqhrzDuL8vVrCutC%2FqbazlkaFFpcKT0zqlyDBFnXlwCdtoUWILCCUThFP2H3wwfRpTjQLvsbBEbv%2Bc0dtkhRo%2FfXBylF4nWTG02hSGtlj5k%2BnSbA%2C1; ki_t=1511092543477%3B1511699672395%3B1511702406563%3B3%3B20; ki_r=; TASession=%1%V2ID.0EF11D70FC513B7049AED23ECF02917E*SQ.53*LP.%2F*PR.427%7C*LS.DemandLoadAjax*GR.14*TCPAR.47*TBR.35*EXEX.99*ABTR.13*PHTB.46*FS.92*CPU.86*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8D6068079E636ED54C7CDC0288DA15C2*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.60763; TATravelInfo=V2*AY.2017*AM.12*AD.3*DY.2017*DM.12*DD.4*A.2*MG.-1*HP.2*FL.3*RVL.267031_323l32655_330l191_330l60763_330*DSM.1511702413426*RS.1; TAUD=LA-1511691625697-1*RDD-1-2017_11_26*LD-10787714-2017.12.3.2017.12.4*LG-10787716-2.1.F.'
}   # 构造header是为了伪造账户已经登陆
urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30, 1140, 30)]    # 连续爬取多个网页


def getUrl(url):
    # 使用requests进行网页请求,网页会返回一个response
    wb_data = requests.get(url, headers=header)
    time.sleep(2)   # 每隔两秒请求一次,防止封IP
    # 使网页变得可读
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a')
    imgs = soup.select('img[height="180"]')
    commits = soup.select('#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_rating > div > div > span.more > a')
    for title, img, commit in zip(titles, imgs, commits):
        data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'commit': commit.get_text().strip('\n'),
        }
        print(data)

for singel_url in urls:
    getUrl(singel_url)


