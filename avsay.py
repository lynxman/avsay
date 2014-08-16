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

configfile = "avsay.conf"

import random
import os, sys
import ConfigParser

sys.path.append(os.path.join(os.path.dirname(__file__), "birdy"))
sys.path.append(os.path.join(os.path.dirname(__file__), "requests-oauthlib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "oauthlib"))

configfile = os.path.join(os.path.dirname(__file__), "avsay.conf")

from birdy.twitter import UserClient

def twitterpost(consumer_key,consumer_secret,access_token,
                access_token_secret,message):
    """ Post Twitter message """
    client = UserClient(consumer_key,
                        consumer_secret,
                        access_token,
                        access_token_secret)

    print message
    try:
        client.api.statuses.update.post(status=message)
    except:
        print "Couldn't Post"
    else:
        print "OK!"

def avsay():
    """Random Av phrase generator"""
    random.seed()
    avstrings = [
        ['Sorry guys', 'Need to run', 'I\'m off', 'brb', 'afk for a bit',
         'Hold on', 'Back in a bit'],
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
    config = ConfigParser.ConfigParser(allow_no_value=True)
    try:
        with open(configfile):
            config.read(configfile)
    except IOError:
        print "Could not read config file %s, exiting" % configfile
        sys.exit(1)
    twitterpost(config.get('twitter','consumer_key'),
                config.get('twitter','consumer_secret'),
                config.get('twitter','access_token'),
                config.get('twitter','access_token_secret'),
                avsay())
