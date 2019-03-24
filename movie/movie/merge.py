import os
from scrapy.conf import settings


class Merge(object):
    def __init__(self, **kwargs):
        '''
        please input EPISODE SOAP_NAME
        :param kwargs:
        '''
        for name, value in kwargs.items():
            setattr(self, name, value)

        EPISODE = self.EPISODE if hasattr(self, 'EPISODE') else settings['EPISODE']
        SOAP_NAME = self.SOAP_NAME if hasattr(self, 'SOAP_NAME') else settings['SOAP_NAME']
        SOAP_DIR = f"F:/{SOAP_NAME}"
        self.input = f"{SOAP_DIR}/{EPISODE}"
        self.output_dir = f"F:/movie/output/{SOAP_NAME}"
        self.EPISODE = EPISODE
        self.SOAP_DIR = SOAP_DIR



    def main(self):
        a = [j for i in os.walk(self.input) for j in i[2] if 'ts' in j]
        a = [(int(i.split('.')[0]), i) for i in a]
        a.sort()
        print(a)
        s = b''
        for i in a:
            with open(f'{self.input}\{i[1]}', 'rb') as f:
                print(f"It is going to merge {i[1]}")
                s += f.read()
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        with open(f"{self.output_dir}/{self.EPISODE}.ts", 'wb') as f:
            f.write(s)
        print(f"{self.SOAP_DIR} has been merged!")
        print(len(s))

if __name__ == '__main__':
    # merge = Merge(SOAP_NAME=SOAP_NAME, EPISODE=EPISODE)
    # merge.main()
    pass

