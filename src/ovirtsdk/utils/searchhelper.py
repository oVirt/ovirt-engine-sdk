from urllib import urlencode
import re
import fnmatch

class SearchHelper():

    @staticmethod
    def appendQuery(url, qargs={}):
        '''Appends search query to url'''

        if (qargs and len(qargs) > 0):
            for k, v in qargs.items():
                if v != None:
                    url += '?' + urlencode({k : v}) if url.find('?') is -1 \
                                                    else '&' + urlencode({k : v})
        return url

    @staticmethod
    def filterResults(result, constraints={}):
        '''Provides filtering capabilities base on custom constraint'''
        matched = [];
        compiled = []
        for attr in constraints:
            match = constraints[attr]
            if isinstance(match, str):
                match = re.compile(fnmatch.translate(match))
            compiled.append((attr.split('.'), match))
        for res in result:
            for attr, match in compiled:
                value = res
                for at in attr:
                    value = getattr(value, at, None)
                    if value is None:
                        break
                if not hasattr(match, 'match') and value != match:
                    break
                if hasattr(match, 'match') and (value is None or not match.match(str(value))):
                    break
            else:
                matched.append(res)
        return matched
