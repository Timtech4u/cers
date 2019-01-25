from django.core.management.base import BaseCommand
from messenger.models import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Performs import of Polling Units'
    states = ['ABIA', 'ADAMAWA', 'AKWA IBOM', 'ANAMBRA', 'BAUCHI', 'BAYELSA', 'BENUE', 'BORNO', 'CROSS RIVER', 'DELTA', 'EBONYI', 'EDO', 'EKITI', 'ENUGU', 'FCT', 'GOMBE', 'IMO', 'JIGAWA', 'KADUNA', 'KANO', 'KATSINA', 'KEBBI', 'KOGI', 'KWARA', 'LAGOS', 'NASARAWA', 'NIGER', 'OGUN', 'ONDO', 'OSUN', 'OYO', 'PLATEAU', 'RIVERS', 'SOKOTO', 'TARABA', 'YOBE', 'ZAMFARA']

    def getData(self, link):
        page = urlopen(link)
        soup = BeautifulSoup(page, 'html.parser').find_all('option')
        datasets = []
        for s in soup:
            datasets.append(s.get_text())
        datasets.pop(0)
        return datasets

    def import_locations(self, id):
        state = self.states[id]
        print("Performing import for {} ......".format(state))
        lga_url = 'http://52.23.145.6/web/site/lga?state_id={}'.format(id)
        lgas = self.getData(lga_url)
        for i, l in enumerate(lgas):
            ward_url = 'http://52.23.145.6/web/site/ward?lga_id={}&state_id={}'.format(i+1, id)
            wards = self.getData(ward_url)
            for ii, w in enumerate(wards):
                unit_url = 'http://52.23.145.6/web/site/units?lga_id={}&state_id={}&ward_id={}'.format(i+1, id, ii+1)
                units = self.getData(unit_url)
                for unit in units:
                    Units.objects.get_or_create(
                        name = unit,
                        ward = w,
                        lga = l,
                        state = state
                    )
        print("Done.....")

    def handle(self, *args, **options):
        for i in range(37):
            print(i)
            self.import_locations(i)
        