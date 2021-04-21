from sw_sixgill_dve_enrich import SixgillAPIRequests, SwimlaneDVEEnrichFields


class SwMain(SixgillAPIRequests):

    def __init__(self, context):
        super(SwMain, self).__init__(context)

    def execute(self):
        response = self.dve_enrich()
        parsed_response = self.parse_dve_data(response)
        return parsed_response

    def parse_dve_data(self, dve_feed):
        x_sixgill_info = dve_feed.get('x_sixgill_info', {})
        github_info = x_sixgill_info.get('github', {})
        sixgill_mentions_info = x_sixgill_info.get('mentions', {})
        nvd_info = x_sixgill_info.get('nvd', {})
        sixgill_score_info = x_sixgill_info.get('score', {})

        sixgill_attributes = x_sixgill_info.get('attributes', [])
        metasploit_attribute = self.get_attr_value(sixgill_attributes, 'Metasploit_attribute')
        trend_underground_attribute = self.get_attr_value(sixgill_attributes, 'Is_Trend_Underground_attribute')
        scanned_by_anonymous_attribute = self.get_attr_value(sixgill_attributes, 'Is_Scanned_by_Anonymous_attribute')
        trend_chinese_attribute = self.get_attr_value(sixgill_attributes, 'Is_Trend_Chinese_attribute')
        poc_exploit_attribute = self.get_attr_value(sixgill_attributes, 'Has_POC_exploit_attribute')
        exploit_kit_attribute = self.get_attr_value(sixgill_attributes, 'Has_Exploit_kit_attribute')
        trend_russian_attribute = self.get_attr_value(sixgill_attributes, 'Is_Trend_Russian_attribute')
        trend_arabic_attribute = self.get_attr_value(sixgill_attributes, 'Is_Trend_Arabic_attribute')
        trend_farsi_attribute = self.get_attr_value(sixgill_attributes, 'Is_Trend_Farsi_attribute')
        trend_github_general_attribute = self.get_attr_value(sixgill_attributes, 'Is_Trend_GitHub_General_attribute')
        trend_twitter_attribute = self.get_attr_value(sixgill_attributes, 'Is_Trend_Twitter_attribute')

        github_first_date = github_info.get('activity', {}).get('first_date', '')
        github_last_date = github_info.get('activity', {}).get('last_date', '')
        github_projects = self.list_to_dict(github_info.get('projects', []))
        github_forks = github_info.get('github_forks', '')
        github_projects_count = github_info.get('github_projects', '')
        github_watchers = github_info.get('github_watchers', '')
        sixgill_first_mention = sixgill_mentions_info.get('first_mention', '')
        sixgill_last_mention = sixgill_mentions_info.get('last_mention', '')
        sixgill_mentions_total = sixgill_mentions_info.get('mentions_total', '')
        nvd_config = nvd_info.get('configurations', {})
        nvd_link = nvd_info.get('link', '')
        nvd_modified = nvd_info.get('modified', '')
        nvd_published = nvd_info.get('published', '')
        nvd_v2 = nvd_info.get('v2', {})
        nvd_v3 = nvd_info.get('v3', {})
        sixgill_score_current = sixgill_score_info.get('current', '')
        sixgill_highest_date = sixgill_score_info.get('highest', {}).get('date', '')
        sixgill_highest_score = sixgill_score_info.get('highest', {}).get('value', '')
        sixgill_previously_exploited = sixgill_score_info.get('previouslyExploited', '')
        raw_response = SwimlaneDVEEnrichFields(created=dve_feed.get('created', ),
                                               description=dve_feed.get('description', ''),
                                               external_references=str(dve_feed.get('external_references', {})),
                                               sixgill_id=dve_feed.get('id', ''),
                                               last_activity_date=dve_feed.get('last_activity_date', ''),
                                               dve_name=dve_feed.get('name', ''),
                                               dve_type=dve_feed.get('type', ''),
                                               attribute_metasploit=metasploit_attribute,
                                               attribute_trend_underground=trend_underground_attribute,
                                               attribute_scanned_by_anonymous=scanned_by_anonymous_attribute,
                                               attribute_trend_chinese=trend_chinese_attribute,
                                               attribute_poc_exploit=poc_exploit_attribute,
                                               attribute_exploit_kit=exploit_kit_attribute,
                                               attribute_trend_russian=trend_russian_attribute,
                                               attribute_trend_arabic=trend_arabic_attribute,
                                               attribute_trend_farsi=trend_farsi_attribute,
                                               attribute_trend_github_general=trend_github_general_attribute,
                                               attribute_trend_twitter=trend_twitter_attribute,
                                               github_activity_first_date=github_first_date,
                                               github_activity_last_date=github_last_date,
                                               github_projects=github_projects,
                                               github_forks=github_forks,
                                               github_projects_count=github_projects_count,
                                               github_watchers=github_watchers,
                                               sixgill_first_mention=sixgill_first_mention,
                                               sixgill_last_mention=sixgill_last_mention,
                                               sixgill_mentions_total=sixgill_mentions_total,
                                               nvd_configurations=nvd_config,
                                               nvd_link=nvd_link,
                                               nvd_modified=nvd_modified,
                                               nvd_published=nvd_published,
                                               nvd_v2_info=nvd_v2,
                                               nvd_v3_info=nvd_v3,
                                               sixgill_current_score=sixgill_score_current,
                                               sixgill_highest_score=sixgill_highest_score,
                                               sixgill_highest_date=sixgill_highest_date,
                                               sixgill_previously_exploited=sixgill_previously_exploited).__dict__
        return raw_response

    def list_to_dict(self, obj_list):
        out_dict = {}
        for idx, each_item in enumerate(obj_list):
            out_dict[idx] = each_item
        return out_dict

    def get_attr_value(self, sixgill_attributes, attr_name):
        attrs_list = [str(attr.get('value', '')) for attr in sixgill_attributes
                      if attr.get('name', '') == attr_name]
        if len(attrs_list) != 0:
            return attrs_list[0]
        return ''


