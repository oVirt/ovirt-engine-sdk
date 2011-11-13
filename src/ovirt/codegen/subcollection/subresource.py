'''
Created on Oct 24, 2011

@author: mpastern
'''
from ovirt.codegen.utils.typeutil import TypeUtil
from ovirt.codegen.collection.resource import Resource


#============================================================
#=====================SUB COLLECTION RESOURCE================
#============================================================

class SubResource(object):
    @staticmethod
    def resource(sub_res_type, encapsulating_entity, parent, KNOWN_WRAPPER_TYPES={}):
        actual_xml_entity = TypeUtil.getValueByKeyOrNone(encapsulating_entity.lower(), KNOWN_WRAPPER_TYPES)
        actual_sub_res_type = TypeUtil.getValueByKeyOrNone(sub_res_type.lower(), KNOWN_WRAPPER_TYPES)

        sub_collection_resource_template_values = {'encapsulating_entity':actual_sub_res_type if actual_sub_res_type is not None else sub_res_type,
                                                   'sub_res_type': actual_sub_res_type if actual_sub_res_type is not None else \
                                                                                       actual_xml_entity if actual_xml_entity is not None else\
                                                                                       encapsulating_entity,
                                                   'parent':parent.lower(),
                                                   'encapsulated_entity':encapsulating_entity.lower()}

        sub_resource_template = \
        ("class %(encapsulating_entity)s(params.%(sub_res_type)s, Base):\n" + \
        "    def __init__(self, %(parent)s, %(encapsulated_entity)s):\n" + \
        "        self.parentclass = %(parent)s\n" + \
        "        self.superclass  =  %(encapsulated_entity)s\n\n" + \
        "    def __new__(cls, %(parent)s, %(encapsulated_entity)s):\n" + \
        "        if %(encapsulated_entity)s is None: return None\n" + \
        "        obj = object.__new__(cls)\n" + \
        "        obj.__init__(%(parent)s, %(encapsulated_entity)s)\n" + \
        "        return obj\n\n") % sub_collection_resource_template_values

        return sub_resource_template

    @staticmethod
    def action(url, action_name, parent_resource_name_lc, resource_name_lc, method, action_params={}):
        sub_collection_resource_action_template_values = {'url':url,
                                                          'action_name':action_name,
                                                          'method': method,
                                                          'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                                          'resource_name_lc':resource_name_lc.lower(),
                                                          'add_method_params' : Resource._addMethodParams(action_params.keys()),
                                                          'add_action_parans' : Resource._addActionParams(action_params)}

        #FIXME: check if there are more params to put to Action
        #"      action = params.Action(vm=self.superclass)"



        #url = '/api/vms/{vm:id}/nics/{nic:id}/do'"
        sub_collection_resource_action_template = \
        ("    def %(action_name)s(self%(add_method_params)s):\n" + \
        "        url = '%(url)s'\n\n" + \
        "        action = params.Action()\n%(add_action_parans)s" + \
        "        result = self._getProxy().request(method='%(method)s',\n" + \
        "                                          url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
        "                                                                     '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                          body=ParseHelper.toXml(action))\n\n"
        "        return result\n\n") % sub_collection_resource_action_template_values

        return sub_collection_resource_action_template

    @staticmethod
    def update(url, parent_resource_name_lc, resource_name, actual_self_name, KNOWN_WRAPPER_TYPES):
        actual_xml_entity = TypeUtil.getValueByKeyOrNone(actual_self_name.lower(), KNOWN_WRAPPER_TYPES)

        sub_collection_resource_update_template_values = {'url':url,
                                                          'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                                          'resource_name':resource_name,
                                                          'resource_name_lc':resource_name.lower(),
                                                          'actual_self_name':actual_xml_entity if actual_xml_entity is not None else actual_self_name}

        #url = '/api/vms/{vm:id}/nics/{nic:id}'"
        sub_collection_resource_update_template = \
        ("    def update(self):\n" + \
        "        url = '%(url)s'\n\n" + \
        "        result = self._getProxy().update(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
        "                                                                     '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
        "                                         body=ParseHelper.toXml(self.superclass))\n\n" + \
        "        return %(actual_self_name)s(self.parentclass, result)\n\n") % sub_collection_resource_update_template_values

        return sub_collection_resource_update_template

    @staticmethod
    def delete(url, parent_resource_name_lc, resource_name_lc):
        sub_collection_resource_delete_template_values = {'url':url,
                                                          'parent_resource_name_lc':parent_resource_name_lc.lower(),
                                                          'resource_name_lc':resource_name_lc.lower()}

        #url = '/api/vms/{vm:id}/nics/{nic:id}'"
        sub_collection_resource_delete_template = \
        ("    def delete(self, force=False, grace_period=False):\n" + \
         "        url = '%(url)s'\n\n" + \
         "        if ((force or grace_period) is not False):\n" + \
         "            action = params.Action(force=force, grace_period=grace_period)\n" + \
         "            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
         "                                                                         '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
         "                                             body=ParseHelper.toXml(action))\n" + \
         "        else:\n" + \
         "            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{%(parent_resource_name_lc)s:id}' : self.parentclass.get_id(),\n" + \
         "                                                                         '{%(resource_name_lc)s:id}': self.get_id()}),\n" + \
         "                                             headers={'Content-type':None})\n" + \
         "        return result\n\n") % sub_collection_resource_delete_template_values

        return sub_collection_resource_delete_template
