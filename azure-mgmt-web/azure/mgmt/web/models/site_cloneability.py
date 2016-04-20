# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SiteCloneability(Model):
    """
    Represents whether or not a web app is cloneable

    :param result: Name of web app. Possible values include: 'Cloneable',
     'PartiallyCloneable', 'NotCloneable'
    :type result: str
    :param blocking_features: List of features enabled on web app that
     prevent cloning
    :type blocking_features: list of :class:`SiteCloneabilityCriterion
     <azure.mgmt.web.models.SiteCloneabilityCriterion>`
    :param unsupported_features: List of features enabled on web app that are
     non-blocking but cannot be cloned. The web app can still be cloned
     but the features in this list will not be set up on cloned
     web app.
    :type unsupported_features: list of :class:`SiteCloneabilityCriterion
     <azure.mgmt.web.models.SiteCloneabilityCriterion>`
    :param blocking_characteristics: List of blocking application
     characteristics
    :type blocking_characteristics: list of :class:`SiteCloneabilityCriterion
     <azure.mgmt.web.models.SiteCloneabilityCriterion>`
    """ 

    _validation = {
        'result': {'required': True},
    }

    _attribute_map = {
        'result': {'key': 'result', 'type': 'CloneAbilityResult'},
        'blocking_features': {'key': 'blockingFeatures', 'type': '[SiteCloneabilityCriterion]'},
        'unsupported_features': {'key': 'unsupportedFeatures', 'type': '[SiteCloneabilityCriterion]'},
        'blocking_characteristics': {'key': 'blockingCharacteristics', 'type': '[SiteCloneabilityCriterion]'},
    }

    def __init__(self, result, blocking_features=None, unsupported_features=None, blocking_characteristics=None):
        self.result = result
        self.blocking_features = blocking_features
        self.unsupported_features = unsupported_features
        self.blocking_characteristics = blocking_characteristics
