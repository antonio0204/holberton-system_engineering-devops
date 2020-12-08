exec { 'killmenow':
path   => '/usr/bin:/usr/sbin:/bin',
provider   => 'shell',
onlyif => 'pkill -f ./killmenow'
}
