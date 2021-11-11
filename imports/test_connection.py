from sw_cybersixgill_dve_enrich import SixgillDveEnrichBaseClass


class SwMain(SixgillDveEnrichBaseClass):

    def execute(self):
        try:
            self.auth_test()
        except Exception as e:
            return {'successful': False, 'errorMessage': str(e)}
        return {'successful': True}
