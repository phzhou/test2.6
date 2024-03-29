# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads.adobjects.abstractobject import AbstractObject
from facebookads.adobjects.abstractcrudobject import AbstractCrudObject
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please tell us on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class Event(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isEvent = True
        super(Event, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        attending_count = 'attending_count'
        can_guests_invite = 'can_guests_invite'
        category = 'category'
        cover = 'cover'
        declined_count = 'declined_count'
        description = 'description'
        end_time = 'end_time'
        guest_list_enabled = 'guest_list_enabled'
        id = 'id'
        interested_count = 'interested_count'
        is_page_owned = 'is_page_owned'
        is_viewer_admin = 'is_viewer_admin'
        maybe_count = 'maybe_count'
        name = 'name'
        noreply_count = 'noreply_count'
        owner = 'owner'
        parent_group = 'parent_group'
        place = 'place'
        start_time = 'start_time'
        ticket_uri = 'ticket_uri'
        timezone = 'timezone'
        type = 'type'
        updated_time = 'updated_time'

    class Category:
        art_event = 'ART_EVENT'
        book_event = 'BOOK_EVENT'
        movie_event = 'MOVIE_EVENT'
        fundraiser = 'FUNDRAISER'
        volunteering = 'VOLUNTEERING'
        family_event = 'FAMILY_EVENT'
        festival_event = 'FESTIVAL_EVENT'
        neighborhood = 'NEIGHBORHOOD'
        religious_event = 'RELIGIOUS_EVENT'
        shopping = 'SHOPPING'
        comedy_event = 'COMEDY_EVENT'
        music_event = 'MUSIC_EVENT'
        dance_event = 'DANCE_EVENT'
        nightlife = 'NIGHTLIFE'
        theater_event = 'THEATER_EVENT'
        dining_event = 'DINING_EVENT'
        food_tasting = 'FOOD_TASTING'
        conference_event = 'CONFERENCE_EVENT'
        meetup = 'MEETUP'
        class_event = 'CLASS_EVENT'
        lecture = 'LECTURE'
        workshop = 'WORKSHOP'
        fitness = 'FITNESS'
        sports_event = 'SPORTS_EVENT'
        other = 'OTHER'

    class Type:
        private = 'private'
        public = 'public'
        group = 'group'
        community = 'community'
        legacy = 'legacy'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Event,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    _field_types = {
        'attending_count': 'int',
        'can_guests_invite': 'bool',
        'category': 'Category',
        'cover': 'Object',
        'declined_count': 'int',
        'description': 'string',
        'end_time': 'string',
        'guest_list_enabled': 'bool',
        'id': 'string',
        'interested_count': 'int',
        'is_page_owned': 'bool',
        'is_viewer_admin': 'bool',
        'maybe_count': 'int',
        'name': 'string',
        'noreply_count': 'int',
        'owner': 'Object',
        'parent_group': 'Object',
        'place': 'Object',
        'start_time': 'string',
        'ticket_uri': 'string',
        'timezone': 'string',
        'type': 'Type',
        'updated_time': 'datetime',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Category'] = Event.Category.__dict__.values()
        field_enum_info['Type'] = Event.Type.__dict__.values()
        return field_enum_info