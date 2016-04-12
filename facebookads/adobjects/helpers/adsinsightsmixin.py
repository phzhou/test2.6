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

class AdsInsightsMixin:

    class Increment(object):
        monthly = 'monthly'
        all_days = 'all_days'

    class Operator(object):
        all = 'all'
        any = 'any'
        contain = 'contain'
        equal = 'equal'
        greater_than = 'greater_than'
        greater_than_or_equal = 'greater_than_or_equal'
        in_ = 'in'
        in_range = 'in_range'
        less_than = 'less_than'
        less_than_or_equal = 'less_than_or_equal'
        none = 'none'
        not_contain = 'not_contain'
        not_equal = 'not_equal'
        not_in = 'not_in'
        not_in_range = 'not_in_range'
