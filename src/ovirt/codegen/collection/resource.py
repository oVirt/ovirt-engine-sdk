'''
Created on Oct 24, 2011

@author: mpastern
'''
from ovirt.codegen.utils.typeutil import TypeUtil

#============================================================
#===========================RESOURCE=========================
#============================================================

class Resource(object):
    SUB_COLLECTIONS_FIXME = "        #SUB_COLLECTIONS"

    @staticmethod
    def resource(xml_entity, sub_collections=[], KNOWN_WRAPPER_TYPES={}):
        actual_xml_entity = TypeUtil.getValueByKeyOrNone(xml_entity.lower(), KNOWN_WRAPPER_TYPES)

        resource_template_values = {'xml_entity': actual_xml_entity if actual_xml_entity is not None else xml_entity,
                                    'xml_entity_lc':xml_entity.lower(),
                                    'sub_collections':sub_collections}

        resource_template = \
        ("class %(xml_entity)s(params.%(xml_entity)s, Base):\n" + \
        "    def __init__(self, %(xml_entity_lc)s):\n" + \
        #Resource.__addSubCollectionInstances(xml_entity.lower(), sub_collections)+\
        Resource.SUB_COLLECTIONS_FIXME + "\n" + \
        "        self.superclass = %(xml_entity_lc)s\n\n" + \
        "    def __new__(cls, %(xml_entity_lc)s):\n" + \
        "        if %(xml_entity_lc)s is None: return None\n" + \
        "        obj = object.__new__(cls)\n" + \
        "        obj.__init__(%(xml_entity_lc)s)\n" + \
        "        return obj\n\n") % resource_template_values

        return resource_template

    @staticmethod
    def addSubCollectionInstances(parent, sub_collections={}):
        tmpl = "        self.%s = []\n" + \
               "        self.%s = %s(%s)\n"

        new_tmpl = ''
        for k, v in sub_collections.items():
            new_tmpl += tmpl % (k.lower(), k.lower(), v, parent)

        return new_tmpl

    @staticmethod
    def action(url, action_name, resource_name_lc, method, action_params={}):
        resource_action_template_values = {'url':url,
                                           'action_name':action_name,
                                           'method': method,
                                           'resource_name_lc':resource_name_lc.lower(),
                                           'method_params': Resource._addMethodParams(action_params.keys()),
                                           'action_params':Resource._addActionParams(action_params)}

        #FIXME: check if there are more params to put to Action
        #"      action = params.Action(vm=self.superclass)"

        resource_action_template = \
        ("    def %(action_name)s(self%(method_params)s):\n" + \
        "        url = '%(url)s'\n\n" + \
        "        action = params.Action()\n%(action_params)s" + \
        "        result = self._getProxy().request(method='%(method)s',\n" + \
        "                                          url=UrlHelper.replace(url, {'{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                          body=ParseHelper.toXml(action))\n" + \
        "        return result\n\n") % resource_action_template_values

        return resource_action_template

    @staticmethod
    def _addActionParams(kwargs={}):
        res = ''
        for k, v in kwargs.items():
            res += "        action." + k + "=" + v + "\n"
        return res

    @staticmethod
    def _addMethodParams(params=[]):
        res = ''
        for item in params:
            res += ', ' + item
        return res

    @staticmethod
    def delete(url, resource_name_lc):
        resource_delete_template_values = {'url':url,
                                           'resource_name_lc':resource_name_lc.lower()}

        resource_delete_template = \
        ("    def delete(self, force=False, grace_period=False):\n" + \
        "        url = '%(url)s'\n\n" + \
        "        if ((force or grace_period) is not False):\n" + \
        "            action = params.Action(force=force, grace_period=grace_period)\n" + \
        "            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                             body=ParseHelper.toXml(action))\n" + \
        "        else:\n" + \
        "            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                             headers={'Content-type':None})\n" + \
        "        return result\n\n") % resource_delete_template_values

        return resource_delete_template

    @staticmethod
    def update(url, resource_name, actual_self_name, KNOWN_WRAPPER_TYPES={}):

        actual_xml_entity = TypeUtil.getValueByKeyOrNone(actual_self_name.lower(), KNOWN_WRAPPER_TYPES)

        resource_update_template_values = {'url':url,
                                           'resource_name':resource_name,
                                           'resource_name_lc':resource_name.lower(),
                                           'actual_self_name':actual_xml_entity if actual_xml_entity is not None else actual_self_name}

        resource_update_template = \
        ("    def update(self):\n" + \
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().update(url=UrlHelper.replace(url, {'{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                         body=ParseHelper.toXml(self.superclass))\n" + \
        "        return %(actual_self_name)s(result)\n\n") % resource_update_template_values

        return resource_update_template
