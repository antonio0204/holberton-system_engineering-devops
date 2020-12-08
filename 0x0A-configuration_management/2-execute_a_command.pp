#Using Puppet, create a manifest that kills a process named killmenow
exec { 'killmenow':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
  onlyif   => 'pkill -f ./killmenow'
}
