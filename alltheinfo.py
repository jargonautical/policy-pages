import requests
import requests_cache
import base_parser
from bs4 import BeautifulSoup

requests_cache.install_cache('meetings')

class SingleMeeting():
    def __init__(self, base_url, meeting_id):
        self.base_url = base_url
        self.meeting_id = meeting_id
        self.get_meeting()

    def get_meeting(self):
        url = "{}/GetMeeting?lMeetingId={}".format(
            self.base_url,
            self.meeting_id
        )
        self.soup = BeautifulSoup(requests.get(url).text, "html.parser")
        pretty print (self.soup)
        
if __name__ == "__main__":
    s = SingleMeeting("http://democracy.devon.gov.uk/mgWebService.asmx", 206)