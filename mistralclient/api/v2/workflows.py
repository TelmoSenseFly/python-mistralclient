# Copyright 2014 - Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from mistralclient.api import base


class Workflow(base.Resource):
    resource_name = 'Workflow'


class WorkflowManager(base.ResourceManager):
    resource_class = Workflow

    def create(self, name, definition, description=None, tags=None):
        self._ensure_not_empty(name=name, definition=definition)

        data = {
            'name': name,
            'definition': definition,
            'description': description,
            'tags': tags,
        }

        return self._create('/workflows', data)

    def update(self, name, definition=None, description=None, tags=None):
        self._ensure_not_empty(name=name)

        data = {
            'name': name,
            'description': description,
            'tags': tags,
        }

        if definition:
            data.update({'definition': definition})

        return self._update('/workflows/%s' % name, data)

    def list(self):
        return self._list('/workflows', response_key='workflows')

    def get(self, name):
        self._ensure_not_empty(name=name)

        return self._get('/workflows/%s' % name)

    def delete(self, name):
        self._ensure_not_empty(name=name)

        self._delete('/workflows/%s' % name)