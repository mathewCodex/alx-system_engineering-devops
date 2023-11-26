#!/usr/bin/pup
# Install a particular version of flask 2.1.0
# using puppet
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
