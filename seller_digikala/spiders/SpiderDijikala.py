from pathlib import Path
import json

import scrapy
from scrapy.http.cookies import CookieJar


class SpiderDijikala(scrapy.Spider):
    name = "SpiderDijikala"

    cookies = {
        "tracker_glob_new": "dVDsxXb",
        "_gid": "GA1.2.1127344745.1690297304",
        "PHPSESSID": "fl4p97jvk4it1qnphjllp4k58q",
        "_hjSessionUser_2754176": "eyJpZCI6IjZkNWZiNTI5LTdjMDQtNWE5ZC1hODQyLWE4Mjk3NDU0M2E3NSIsImNyZWF0ZWQiOjE2OTAyOTczMDM4NzUsImV4aXN0aW5nIjp0cnVlfQ==",
        "_hjSessionUser_3324387": "eyJpZCI6Ijk0ODc1NzdiLTRmOWUtNWE2MS04ZWUzLWFmNzE4ZTg5MjY3ZSIsImNyZWF0ZWQiOjE2OTAzMDAwODQ5MDAsImV4aXN0aW5nIjp0cnVlfQ==",
        "tracker_session": "dZ7mlH7",
        "_sp_ses.13cb": "*",
        "_hjSession_3324387": "eyJpZCI6ImM2NDA1NGFmLWU2NWYtNGNjNS1hNDc2LTYyYzljYzQ1ZmJmMyIsImNyZWF0ZWQiOjE2OTAzNDQ5NTk1NzksImluU2FtcGxlIjpmYWxzZX0=",
        "_hjAbsoluteSessionInProgress": "0",
        "_hjIncludedInSessionSample_2754176": "0",
        "_hjSession_2754176": "eyJpZCI6ImQwMjAxM2MzLTM1MDUtNGY1Yy05OTk4LTNiNGJmOGZmNTI3NyIsImNyZWF0ZWQiOjE2OTAzNDUxNjYzMTgsImluU2FtcGxlIjpmYWxzZX0=",
        "TS018d011a": "010231059107e732276c81459dcaac546fa150f6ce9fadf4b4814178ec09235ca7971af898f03f8aaee4431422aa603fe808db2b860023722fc80ff0875471209434ef24669a96311066d6317398a0c8174660a463b645a196daa0d6ba85e66ab9c5cc4c600eac2faa4be67432cb0b0d2330b57524c78c6fa21894117d890d5d376d8e6db2",
        "_ga_G963H4KF8M": "GS1.1.1690345163.2.1.1690345746.0.0.0",
        "_ga": "GA1.1.1867793150.1690297304",
        "_ga_337056556": "GS1.1.1690344959.2.1.1690345771.0.0.0",
        "_sp_id.13cb": "0f41c880-5887-4168-8ddc-810f11432060.1690297303.2.1690345772.1690301056.636a1aaa-17cc-490e-9358-1bd47a2ce0b4..744fb906-bc0c-432f-b5d0-3526046f5c77.1690345760094.2",
        "_ga_QWN9MHGGRZ": "GS1.1.1690344959.2.1.1690345784.0.0.0"
    }

    def set_cookies(self,response):
        obj = CookieJar(policy=None)
        jar = obj.make_cookies(response, response.request)
        for cookie in jar:
            self.cookies[cookie.name] = cookie.value
    def start_requests(self):
        url = 'https://seller.digikala.com/api/v2/login'
        body = '{"username":"soheilamohamdrezapour@gmail.com","captcha_token":"03AAYGu2SUn4nFt3iyWV9z4meuEZZw-Yw08u-UsAdPWCCFapD0eXP8rK3xY2F2RyT5jZVd_zeN7ZnDUL8OmNUnzYpw24NqhMj02bZdVPYS8WpvTHLKXHTUEeqrru4CtVSmiMYyIWnTK3Dy2W882mePQH46z9oSUrJnNPohASPF9W_QKUjmK51LwHf4gkgm0q7wJGdCqVxwlBmPjFUdid-2mlGMYo-m78UKaSu4spI5qfQXrHt2iHK4pxSj_gigO69KJY6NRWJikVUY84rpYyZrrLC6yctEHE2g9R0IU5SylIIV4NbYa0jNc8dY3r0JZH70DRnYrrCBsTqHEXnfJ3pGCt3DkuBogYxL9ZANgkwRR7zrPGHNN1uf91_l3IGPooGwuH5DeFDfK7Hyjn18Q59mmSP1LR0BkmhoP5GIsgfejFe_hFOb7sRda12DvIBPEnIGZjQT3reWXlEsSohiq19pWKgNXzN2gGjd_mqdyPONuj3ah980mKR-4_Nge0JGXkKwfaPaUF4m_D6Nq-bBZxcNX8yKlYah88s5nargWRfRPw58IXZa_2i3LLadNFCuCv5XEXpGAT0yX7z88dywDDWvFsp0bnPS4Q7diyzEBXVxePkDKRe60OQlloOZYOkEHHtyV0wlrhES0K9hTvo0gZ0Yzbwn_DIk7VnuCrYojvEn5i7yhr1VhyCXc0KOnpVXgHNNUOI8XU4zfD-7K7jP-_04iZRiwGXBNfriTphs9lclstxmZQQgHf6PO-ehY_2pzN43TG8NEFgxEknCbSpq2MSPhjXYiFM4Hp7zE5G-wiUOF4OZeE0isl1KsWeVwcSGy1CupzR3hZpuMtARjz0PeUTmGxl-Xo-eGjkh9fwBxg0L0hgdtJifa2fkrArRvfmz2GXr1ozNYQZoHsC334_9GwwMTTuP_qEQYYqV7UfhQ0992c5D7DtRnzd_5LIVhawkAkpWAvAjTByGTBmlDF-DG7ICGkOpziTCLIa31IDOcys5kapxH9kYrghQASlzRxvQTKLSkSCRSgSn82-nW3cGHwh6eRf39AZkX5-qbW3PAuGJvad2wsqZ1sxOASDYzEf_pbEcJAFoNwz-8gbJXoVIu71toNI68GwuUDlT51ToDwbVIqDjBQXrnzuoe3JZuaOb8W4tECofTwlR9kYl0BzMusXpWpfNePqMTmZijZTbIgrc57aKA5RUpe08Kdj-wg1BGo9HpyFXDofeS21YE6hwtaE4ECuSuYKjKDWe37HYJiTVzAb20QkdrIGKfHKhJS9AodjXICUk3lZv8dDdQJv7Ea8QbziW6IXXozkPKC-XIBD5gRY4XLteyt92BXYqR62z9ufAZk2OwdF8frOubJiYlYNzEOFrlLhzRpv3NmNCHlXfxjGiz7412RlHp8jU88kI6dHBsXgVVeJ4loaNMy8kTGtZ3cbmDsBUMPcVdhRfeSdSi8wAoLI2RDZ1wZn7jhDuHBGrM9MfcntVFl6q71on_DTQ55tl1iBRlWA1dPK4HLVYt0aeSfAjHNECoBk"}'
        
        yield scrapy.Request(url=url,
                            method='POST',
                            dont_filter=True,
                            body=body,
                            callback=self.sendPassword)

    def sendPassword(self, response):
        # print('+++++++++++++++++++++++ sendPassword ++++++++++++++++++++++++')
        # print(response.text)
        url = 'https://seller.digikala.com/api/v2/login/password'
        body = '{"username":"soheilamohamdrezapour@gmail.com","password":"Pishgam$1400"}'
        yield scrapy.Request(url=url,
                            method='POST',
                            dont_filter=True,
                            cookies=self.cookies,
                            body=body,
                            callback=self.parse)

        
    def parse(self, response):
        
        # print('+++++++++++++++++++++++ parse ++++++++++++++++++++++++')
        # print(response.text)
        self.set_cookies(response)
        for i in range(1, 299):
            url = f'https://seller.digikala.com/ajax/variants/search/?sortColumn=&sortOrder=desc&page={i}&items=10&'
            yield scrapy.Request(url=url,
                                method='GET',
                                dont_filter=True,
                                cookies=self.cookies,
                                callback=self.get_info)
    def get_info(self, response):
        print('+++++++++++++++++++++++ get_info ++++++++++++++++++++++++')
        # print(response.text)
        data = json.loads(response.text)

        items = data['data']['items']
        for item in items:
            title = item['product_variant_title'][::-1]
            price_list_latin = item['price_list']
            print("*" * 80)
            print(price_list_latin)
            print("*" * 50)
            print(title)
            print("+" * 80)
 
