config: config.d/*
	cat config.d/* > config
	i3-msg reload

install: config
	ln -s $(realpath xsession) ~/.xsession