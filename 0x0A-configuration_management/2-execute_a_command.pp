# a command that kill a process


exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
