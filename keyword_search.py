# what do we need to import?
from bs4 import BeautifulSoup
import requests
#import requests_cache

#requests_cache.install_cache('meetings')

# pick a keyword
keyword = input("> Keyword ... ? ")

# find meetings where the keyword is mentioned in the minutes

# get the meeting details
# committee name, meeting number, meeting date
# get the minute item name
# get the url for the minutes

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
        return self.soup
        
if __name__ == "__main__":
    s = SingleMeeting("http://democracy.devon.gov.uk/mgWebService.asmx", 206)
    for topic in s.soup.findAll('agendaitem'):
        item = topic.get_text()
        if keyword in item:
            print (("ITEMS CONTAINING %s" % keyword), item.strip())


