#!/usr/bin/env python
"""
 (C) Copyright 2011 Marc Cluet

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

 Contributors:
  Marc Cluet <lynxman@devroot.org>
"""

__author__ = 'Marc Cluet (lynxman@devroot.org)'
__copyright__ = 'Copyright (c) 2011 Marc Cluet'
__license__ = 'Apache 2.0'
__vcs_id__ = '$Id$'
__version__ = '0.0.1'

import random

def avsay():
    """Random Av phrase generator"""
    random.seed()
    avstrings = [
        ['Sorry guys', 'Need to run', 'I\'m off', 'brb', 'afk for a bit',
         'hold on', 'back in a bit'],
        ['need to', 'going to', 'have to'],
        ['go to shops', 'let dogs out', 'wipe jam off my knees',
         'bail out the basement', 'clean up', 'drain the pool', 'cook dinner',
         'miss my flight', 'do a release', 'go to Patrick\'s', 'cook lunch',
         'feed the dogs', 'feed the cats', 'feed the ferrets', 'mow the lawn',
         'restart skype', 'reboot my laptop', 'restart db04', 'roll the app',
         'offline the site', 'call Patrick', 'wake Marc up', 'shower',
         'find an intern', 'wait for George', 'get Jan to Marcs'],
        ['because'],
        ['my son', 'my wife', 'stokols', 'Patrick', 'the database',
         'the web server', 'my jam', 'my ferret', 'my car', 'Mike', 'Frank',
         'Otu', 'Matt', 'Marc', 'Nic', 'my internet connection', 'my daughter'],
        ['destroyed', 'eaten', 'broken', 'spread jam on', 'hidden',
         'disconnected', 'unplugged', 'throttled', 'trolled', 'mislaid',
         'reset', 'melted', 'dropped', 'wet', 'burnt'],
        ['car', 'passport', 'jam', 'dog', 'cat', 'kitchen', 'laptop', 'phone',
         'cable tv', 'headphones', 'ferrets', 'site stats', 'user experience',
         'bandwidth', 'tv', 'car', 'lawn', 'tires', 'coax', 'token ring',
         'jabber', 'skype', 'soap', 'tacos', 'porn collection']]
    choices = tuple(random.choice(avstr) for avstr in avstrings)
    quote = '%s, %s %s %s %s has %s my %s.' % choices
    return quote

if __name__ == "__main__":
    print avsay()
