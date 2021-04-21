from sixgill.sixgill_enrich_client import SixgillEnrichClient
from sixgill.sixgill_feed_client import SixgillBaseClient
import requests


class SixgillDveEnrichBaseClass(object):
    def __init__(self, context):
        self.client_id = context.asset.get('client_id', '')
        self.client_secret = context.asset.get('client_secret', '')
        self.verify = context.asset.get('verify_ssl', False)
        http_proxy = context.asset.get('http_proxy')
        self.dve_id = context.inputs.get('dve_id', '')
        session = requests.Session()
        session.proxies = {} if not http_proxy else http_proxy
        self.proxy = session
        self.channel_id = '9edd89168582842d84430bac51a06eb3'

    def auth_test(self):
        """checks to see if asset inputs are valid."""
        access_token = SixgillBaseClient(self.client_id, self.client_secret, self.channel_id, session=self.proxy,
                                         verify=self.verify).get_access_token()
        return access_token


class SixgillAPIRequests(SixgillDveEnrichBaseClass):

    def __init__(self, context):
        super(SixgillAPIRequests, self).__init__(context)
        self.sixgill_enrich_client = SixgillEnrichClient(client_id=self.client_id, client_secret=self.client_secret,
                                                         channel_id=self.channel_id, verify=self.verify,
                                                         session=self.proxy)

    def dve_enrich(self):
        raw_response = self.sixgill_enrich_client.enrich_dve(self.dve_id)
        return raw_response


class SwimlaneDVEEnrichFields:

    def __init__(self, created, description, external_references, sixgill_id, last_activity_date, dve_name, dve_type,
                 attribute_metasploit, attribute_trend_underground, attribute_scanned_by_anonymous,
                 attribute_trend_chinese, attribute_poc_exploit, attribute_exploit_kit, attribute_trend_russian,
                 attribute_trend_arabic, attribute_trend_farsi, attribute_trend_github_general, attribute_trend_twitter,
                 github_activity_first_date, github_activity_last_date, github_projects,
                 github_forks, github_projects_count, github_watchers, sixgill_first_mention, sixgill_last_mention,
                 sixgill_mentions_total, nvd_configurations, nvd_link, nvd_modified, nvd_published, nvd_v2_info,
                 nvd_v3_info, sixgill_current_score, sixgill_highest_score, sixgill_highest_date,
                 sixgill_previously_exploited
                 ):
        self.created = created
        self.description = description
        self.external_references = external_references
        self.sixgill_id = sixgill_id
        self.last_activity_date = last_activity_date
        self.dve_name = dve_name
        self.dve_type = dve_type
        self.attribute_metasploit = attribute_metasploit
        self.attribute_trend_underground = attribute_trend_underground
        self.attribute_scanned_by_anonymous = attribute_scanned_by_anonymous
        self.attribute_trend_chinese = attribute_trend_chinese
        self.attribute_poc_exploit = attribute_poc_exploit
        self.attribute_exploit_kit = attribute_exploit_kit
        self.attribute_trend_russian = attribute_trend_russian
        self.attribute_trend_arabic = attribute_trend_arabic
        self.attribute_trend_farsi = attribute_trend_farsi
        self.attribute_trend_github_general = attribute_trend_github_general
        self.attribute_trend_twitter = attribute_trend_twitter
        self.github_activity_first_date = github_activity_first_date
        self.github_activity_last_date = github_activity_last_date
        self.github_projects = github_projects
        self.github_forks = github_forks
        self.github_projects_count = github_projects_count
        self.github_watchers = github_watchers
        self.sixgill_first_mention = sixgill_first_mention
        self.sixgill_last_mention = sixgill_last_mention
        self.sixgill_mentions_total = sixgill_mentions_total
        self.nvd_configurations = nvd_configurations
        self.nvd_link = nvd_link
        self.nvd_modified = nvd_modified
        self.nvd_published = nvd_published
        self.nvd_v2_info = nvd_v2_info
        self.nvd_v3_info = nvd_v3_info
        self.sixgill_current_score = sixgill_current_score
        self.sixgill_highest_score = sixgill_highest_score
        self.sixgill_highest_date = sixgill_highest_date
        self.sixgill_previously_exploited = sixgill_previously_exploited
