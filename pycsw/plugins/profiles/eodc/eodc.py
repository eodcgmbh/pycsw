from pycsw.plugins.profiles import profile

class EODC(profile.Profile):
    ''' EODC class '''
    def __init__(self, model, namespaces, context):
        self.context = context

        self.namespaces = {
            # 'gmd': 'http://www.isotc211.org/2005/gmd',
            # 'gco': 'http://www.isotc211.org/2005/gco',
            'eodc': 'http://example.org/foo'
        }

        self.repository = {
            'eodc:Metadata': {
            #'gmi:MI_Metadata': {
                #'outputschema': 'http://www.isotc211.org/2005/gmd',
                'queryables': {
                    'EODCQueryables': {
                        'eodc:cloudCoverPercentage': {'xpath': 'gmd:contentInfo/gmd:MD_ImageDescription/gmd:cloudCoverPercentage/gco:Real', 'dbcol': 'cloud_coverage'}
                    }
                }
            }
        }

        profile.Profile.__init__(self,
            name='eodc',
            version='0.1.0',
            title='EODC Metadata Application Profile',
            url='http://example.org/fooprofile',
            namespace=self.namespaces['eodc'],
            typename='eodc:Metadata',
            outputschema=None,
            prefixes=['eodc'],
            model=model,
            core_namespaces=namespaces,
            added_namespaces=self.namespaces,
            repository=self.repository['eodc:Metadata'])

    def extend_core(self, model, namespaces, config):
        ''' Extend core configuration '''
        pass

    def check_parameters(self, kvp):
        '''Check for Language parameter in GetCapabilities request'''
        return None

    def get_extendedcapabilities(self):
        ''' Add child to ows:OperationsMetadata Element '''
        return None

    def get_schemacomponents(self):
        ''' Return schema components as lxml.etree.Element list '''
        return []

    def check_getdomain(self, kvp):
        '''Perform extra profile specific checks in the GetDomain request'''
        return None
