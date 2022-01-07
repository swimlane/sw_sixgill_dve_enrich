from sixgill.sixgill_enrich_client import SixgillEnrichClient
from sixgill.sixgill_feed_client import SixgillBaseClient
import requests


class SixgillDveEnrichBaseClass:
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

    def __init__(self, cve_name, cve_type, created, last_activity_date, description, cybersixgill_current_score,
                 cybersixgill_highest_score, cybersixgill_highest_date, cybersixgill_previously_exploited,
                 cybersixgill_first_mention, cybersixgill_last_mention, cybersixgill_mentions_total,
                 attribute_metasploit, attribute_trend_underground, attribute_scanned_by_anonymous,
                 attribute_trend_chinese, attribute_poc_exploit, attribute_exploit_kit,
                 attribute_trend_russian, attribute_trend_arabic, attribute_trend_farsi, attribute_trend_github_general,
                 attribute_trend_twitter, github_activity_first_date, github_activity_last_date, github_projects_count,
                 github_forks, github_watchers, github_projects, nvd_configurations, nvd_link, nvd_modified,
                 nvd_published, nvd_v2_info, nvd_v3_info, external_references_source_name):
        self.cve_name = cve_name
        self.cve_type = cve_type
        self.created = created
        self.last_activity_date = last_activity_date
        self.description = description
        self.cybersixgill_current_score = cybersixgill_current_score
        self.cybersixgill_highest_score = cybersixgill_highest_score
        self.cybersixgill_highest_date = cybersixgill_highest_date
        self.cybersixgill_previously_exploited = cybersixgill_previously_exploited
        self.cybersixgill_first_mention = cybersixgill_first_mention
        self.cybersixgill_last_mention = cybersixgill_last_mention
        self.cybersixgill_mentions_total = cybersixgill_mentions_total
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
        self.github_projects_count = github_projects_count
        self.github_forks = github_forks
        self.github_watchers = github_watchers
        self.github_projects = github_projects
        self.nvd_configurations = nvd_configurations
        self.nvd_link = nvd_link
        self.nvd_modified = nvd_modified
        self.nvd_published = nvd_published
        self.nvd_v2_info = nvd_v2_info
        self.nvd_v3_info = nvd_v3_info
        self.external_references_source_name = external_references_source_name