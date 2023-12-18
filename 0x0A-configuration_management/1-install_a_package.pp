# A puppet manifest installing flask v2.1.0 which is a package from pip3.
# Install a particular version of flask 2.1.0
# using puppet
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
